import psycopg

# Connect to database
with psycopg.connect(
    'dbname=postgres user=postgres password=jdfk host=localhost port=5433'
) as conn:
    with conn.cursor() as cur:
        cur.execute('''
            SELECT * FROM product
        ''')
        result = cur.fetchall()

for row in result:
    print(row)