from config import DB_CONFIG
from db_loader import DataLoader

CSV_PATH = "Electric_Vehicle_Charging_Stations.csv"

if __name__ == "__main__":
    loader = DataLoader(DB_CONFIG, CSV_PATH)
    loader.load_data()
