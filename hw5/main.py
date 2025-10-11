import psycopg
from utils import Interface, Database

db = Database('postgres','postgres','jdfk','localhost',5433)
app = Interface(db)
app.start()


# User interface
    # Get user input on speed
        # Query what PC models have a speed of at least that speed (query)
        # Show table
    # Get user input on manufacturer
        # Query model number and type of all products made by that manufacturer (query)
        # Show table
        # Give option to select model from list of products
        # Show table/price

    # Quit