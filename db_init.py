import sqlite3
import json

# Mockup JSON data
data = json.loads('''
[
    {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2015, "price": 12000},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2016, "price": 13500},
    {"id": 3, "make": "Ford", "model": "Focus", "year": 2017, "price": 14000},
    {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2018, "price": 15000},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2015, "price": 12500},
    {"id": 6, "make": "BMW", "model": "3 Series", "year": 2019, "price": 27000},
    {"id": 7, "make": "Audi", "model": "A4", "year": 2020, "price": 32000},
    {"id": 8, "make": "Mercedes-Benz", "model": "C-Class", "year": 2017, "price": 24000},
    {"id": 9, "make": "Hyundai", "model": "Elantra", "year": 2018, "price": 14000},
    {"id": 10, "make": "Volkswagen", "model": "Passat", "year": 2016, "price": 16000},
    {"id": 11, "make": "Subaru", "model": "Impreza", "year": 2019, "price": 18000},
    {"id": 12, "make": "Mazda", "model": "Mazda3", "year": 2017, "price": 13500},
    {"id": 13, "make": "Kia", "model": "Optima", "year": 2020, "price": 22000},
    {"id": 14, "make": "Tesla", "model": "Model 3", "year": 2021, "price": 35000},
    {"id": 15, "make": "Volvo", "model": "S60", "year": 2019, "price": 28000},
    {"id": 16, "make": "Jaguar", "model": "XE", "year": 2018, "price": 30000},
    {"id": 17, "make": "Lexus", "model": "IS", "year": 2020, "price": 33000},
    {"id": 18, "make": "Acura", "model": "TLX", "year": 2021, "price": 34000},
    {"id": 19, "make": "Cadillac", "model": "ATS", "year": 2017, "price": 29000},
    {"id": 20, "make": "Infiniti", "model": "Q50", "year": 2020, "price": 32000}
]
''')

# Function to initialize the database and table
def initialize_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INT NOT NULL,              
            price REAL NOT NULL
        )
    ''')

    # Insert mockup data into the table
    cursor.executemany('''
        INSERT INTO cars (id, make, model, year, price)
        VALUES (:id, :make, :model, :year, :price)
    ''', data)

    conn.commit()
    conn.close()

# Run the function
if __name__ == '__main__':
    initialize_db()
    print("Database and table initialized with mockup data.")







# import sqlite3
# import json

# # Mockup JSON data
# data = json.loads('''
# [
#     {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2015, "price": 12000},
#     {"id": 2, "make": "Honda", "model": "Civic", "year": 2016, "price": 13500},
#     {"id": 3, "make": "Ford", "model": "Focus", "year": 2017, "price": 14000},
#     {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2018, "price": 15000},
#     {"id": 5, "make": "Nissan", "model": "Altima", "year": 2015, "price": 12500},
#     {"id": 6, "make": "BMW", "model": "3 Series", "year": 2019, "price": 27000},
#     {"id": 7, "make": "Audi", "model": "A4", "year": 2020, "price": 32000},
#     {"id": 8, "make": "Mercedes-Benz", "model": "C-Class", "year": 2017, "price": 24000},
#     {"id": 9, "make": "Hyundai", "model": "Elantra", "year": 2018, "price": 14000},
#     {"id": 10, "make": "Volkswagen", "model": "Passat", "year": 2016, "price": 16000},
#     {"id": 11, "make": "Subaru", "model": "Impreza", "year": 2019, "price": 18000},
#     {"id": 12, "make": "Mazda", "model": "Mazda3", "year": 2017, "price": 13500},
#     {"id": 13, "make": "Kia", "model": "Optima", "year": 2020, "price": 22000},
#     {"id": 14, "make": "Tesla", "model": "Model 3", "year": 2021, "price": 35000},
#     {"id": 15, "make": "Volvo", "model": "S60", "year": 2019, "price": 28000},
#     {"id": 16, "make": "Jaguar", "model": "XE", "year": 2018, "price": 30000},
#     {"id": 17, "make": "Lexus", "model": "IS", "year": 2020, "price": 33000},
#     {"id": 18, "make": "Acura", "model": "TLX", "year": 2021, "price": 34000},
#     {"id": 19, "make": "Cadillac", "model": "ATS", "year": 2017, "price": 29000},
#     {"id": 20, "make": "Infiniti", "model": "Q50", "year": 2020, "price": 32000}
# ]
# ''')

# # Function to initialize the database and table
# def initialize_db():
#     conn = sqlite3.connect('data.db')
#     cursor = conn.cursor()

#     # Create table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS items (
#             id INTEGER PRIMARY KEY,
#             make TEXT NOT NULL,
#             model TEXT NOT NULL,
#             year INT NOT NULL,              
#             price REAL NOT NULL
#         )
#     ''')

#     # Insert mockup data into the table
#     cursor.executemany('''
#         INSERT INTO items (id, name, price)
#         VALUES (:id, :name, :price)
#     ''', data)

#     conn.commit()
#     conn.close()

# # Run the function
# if __name__ == '__main__':
#     initialize_db()
#     print("Database and table initialized with mockup data.")
