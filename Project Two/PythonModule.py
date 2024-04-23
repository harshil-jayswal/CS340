from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, USER, PASS):
        # Connection Variables
       # Connection Variables
       # USER = 'aacuser'
       # PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32034
        DB = 'AAC'
        COL = 'animals'
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

        # print("Connection Successful")

    def create(self, data):
        """Inserting a document into the MongoDB database."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True  # Return True if insert is successful
            except Exception as e:
                print(f"An error occurred: {e}")
                return False  # Return False if insert fails
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, readData=None):
        """Querying documents from the MongoDB database."""
        if readData is None:
            readData = {}  # If no readData is given, set it to an empty dictionary

        try:
            documents = self.collection.find(readData)
            
            return list(documents)  # Convert cursor to list and return
        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list if query fails
        
    def update(self, query, update_values):
        """ Updating documents in the MongoDB database."""
        if query is None or update_values is None:
            raise ValueError("Query and update data cannot be null")
        try:
            result = self.collection.update_many(query, {'$set': update_values})
            return result.modified_count  # Return the count of modified documents
        except Exception as e:
            print(f"An error occurred during update: {e}")
            return 0  # Return 0 if update fails

    def delete(self, query):
        """ Deleting documents from the MongoDB database. """
        if query is None:
            raise ValueError("Query cannot be Null")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count  # Return the count of deleted documents
        except Exception as e:
            print(f"An error occurred during delete: {e}")
            return 0  # Return 0 if delete fails