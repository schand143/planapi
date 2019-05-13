from click._compat import raw_input
from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.planapi


def main():
    while (1):
        # chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            print
            'delete'
            delete()
        else:
            print
            '\n INVALID SELECTION \n'


# Function to insert data into mongo db
def insert():
    try:
        planId = raw_input('Enter Plan id :')
        planName = raw_input('Enter Plan Name :')
        planPrice = raw_input('Enter price :')
        planAmount = raw_input('Enter Amount :')
        currency = raw_input('Enter currency')

        db.plans.insert_one(
            {
                "id": planId,
                "name": planName,
                "price": planPrice,
                "amount": planAmount,
                "currency": currency
            })
        print
        '\nInserted data successfully\n'

    except Exception as e:
        print
        str(e)


# Function to update record to mongo db
def update():
    try:
        criteria = raw_input('\nEnter id to update\n')
        name = raw_input('\nEnter name to update\n')
        price = raw_input('\nEnter age to update\n')
        amount = raw_input('\nEnter country to update\n')
        currency = raw_input('\n Enter currency')

        db.Employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name": name,
                    "price": price,
                    "amount": amount,
                    "currency": currency
                }
            }
        )
        print
        "\nRecords updated successfully\n"

    except Exception as e:
        print
        str(e)


# function to read records from mongo db
def read():
    try:
        plnCol = db.Plans.find()
        print
        '\n All data from Plans Database \n'
        for pln in plnCol:
            print
            pln

    except Exception as e:
        print
        str(e)


# Function to delete record from mongo db
def delete():
    try:
        criteria = raw_input('\nEnter employee id to delete\n')
        db.Plans.delete_many({"id": criteria})
        print
        '\nDeletion successful\n'
    except Exception as e:
        print
        str(e)


main()