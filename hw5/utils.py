import psycopg

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

class Interface:
    def __init__(self, db: Database):
        self.db = db
        pass

    def start(self):
        self.menu()
    
    def menu(self):
        while True:    
            print('Menu')
            print('1. Get PCs of a certain speed or better')
            print('2. Get model number and type of all products of a certain manufacturer')
            choice = input('Enter choice or anything else to quit: ')
            if choice == '1':
                self.speed()

            elif choice == '2':
                self.manufacturer()
                pass
            
            else:
                return
            pass

    def speed(self):
        # Get speed
        while True:
            uin = input('Enter speed: ')
            try:
                uin = float(uin)
                break
            except:
                print('Invalid, try again')

        # Query what PC models have a speed of at least that speed
        self.db.cur.execute(
            '''
            SELECT model FROM pc
            WHERE speed >= %s
            ''',
            (uin,)
        )
        # Display result
        result = self.db.cur.fetchall()
        # Display headers
        print([desc[0] for desc in self.db.cur.description])
        # Display rows
        for row in result:
            print(row)

        input('Enter anything to continue: ')
        pass

    def manufacturer(self):
        # Get manufacturer
        while True:
            uin = input('Enter manufacturer: ').upper()
            try:
                uin = str(uin)
                if len(uin) > 1:
                    raise ValueError
                break
            except:
                print('Invalid, try again')

        # Query model and type of all products under a manuf
        self.db.cur.execute(
            '''
            SELECT model, type FROM product
            WHERE maker = %s
            ''',
            (uin,)
        )
        # Display result
        result = self.db.cur.fetchall()
        # Display headers
        print([desc[0] for desc in self.db.cur.description])
        # Display rows
        for row in result:
            print(row)
        
        # Get input
        while True:
            uin = input('Enter model number to view price: ')
            try:
                uin = int(uin)
                break
            except:
                print('Invalid, try again')

        # Query model price
        self.db.cur.execute(
            '''
            SELECT price FROM product JOIN
            (
            	(SELECT model, price FROM pc)
            	UNION
            	(SELECT model, price FROM laptop)
            	UNION
            	(SELECT model, price FROM printer)
            ) as products
            ON product.model = products.model
            WHERE product.model = %s
            ''',
            (uin,)
        )

        # Display result
        result = self.db.cur.fetchall()
        # Display headers
        print([desc[0] for desc in self.db.cur.description])
        # Display rows
        for row in result:
            print(row)

        input('Enter anything to continue: ')
        pass
    pass


    


    