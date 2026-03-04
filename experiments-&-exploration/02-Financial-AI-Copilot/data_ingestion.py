import json  
from pymongo import MongoClient  
from dotenv import load_dotenv
import os

# Load the variables from .env into the system environment
load_dotenv("/Users/ashutosh.bajpai/Desktop/PoC/datacamp/Fin_AI_Copilot/credential.env")  

def ingest_data(connection_string, database_name, collection_data_mapping):  
    """  
    Ingest data into MongoDB collections.  
  
    :param connection_string: MongoDB connection string.  
    :param database_name: Name of the database to use.  
    :param collection_data_mapping: Dictionary containing collection names and corresponding JSON file paths.  
    """  
    try:  
        # Connect to MongoDB  
        client = MongoClient(connection_string)  
        db = client[database_name]  
        print(f"Connected to MongoDB at {connection_string}. Using database: {database_name}")  
  
        for collection_name, file_path in collection_data_mapping.items():  
            # Read JSON file  
            with open(file_path, 'r') as file:  
                data = json.load(file)  
              
            # Get the collection  
            collection = db[collection_name]  
              
            # Insert data into the collection  
            result = collection.insert_many(data)  
            print(f"{len(result.inserted_ids)} documents inserted into collection '{collection_name}'.")  
  
        print("Data ingestion completed successfully!")  
    except Exception as e:  
        print(f"An error occurred during data ingestion: {e}")  
    finally:  
        # Close the connection  
        client.close()  
  
# Parameters for the ingestion
connection_string = os.getenv("MONGO_URL")
database_name = "stocks_database"  # Name of the database  
  
# JSON files for collections  
# Update paths here to match your JSON file locations  
collection_data_mapping = {  
    "stocks": "/Users/ashutosh.bajpai/Desktop/PoC/datacamp/Fin_AI_Copilot/data/data.json",  # Path to the JSON file with data for Collection 1  
    "stocks_metadata": "/Users/ashutosh.bajpai/Desktop/PoC/datacamp/Fin_AI_Copilot/data/metadata.json"   # Path to the JSON file with data for Collection 2  
}  
  
# Run the ingest function  
ingest_data(connection_string, database_name, collection_data_mapping)  
