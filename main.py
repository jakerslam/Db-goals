
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initialize_firestore():


    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "key.json"

    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'user-goals',
    })

    db = firestore.client()
    return db

def add_new_goal(db):
    '''
    Prompt the user for a new item to goal to the goal database.  The
    goal name must be unique (firestore document id).  
    '''
    goal = input("Goal Name: ")
    goalDate = input("Goal date: ")

# The document ID must be unique in Firestore.
    result = db.collection("users").document(goal).get()
    if result.exists:
        print("Goal already exists.")
        return

    # Build a dictionary to hold the contents of the firestore document.
    data = {"Goal" : goal, 
            "Goal date" : goalDate}
    db.collection("Goal").document(goal).set(data)


    # Save this in the log collection in Firestore      
    #log_transaction(db, f"Added {goal} with initial quantity {qty}")

def main():
    db = initialize_firestore()
    add_new_goal(db)
    '''
    register_out_of_stock(db)
    choice = None
    while choice != "0":
        print()
        print("0) Exit")
        print("1) Add New Item")
        print("2) Add Quantity")
        print("3) Use Quantity")
        print("4) Search Inventory")
        choice = input(f"> ")
        print()
        if choice == "1":
            add_new_item(db)
        elif choice == "2":
            add_inventory(db)
        elif choice == "3":
            use_inventory(db)
        elif choice == "4":
            search_inventory(db)                        

    '''
if __name__ == "__main__":
    main()