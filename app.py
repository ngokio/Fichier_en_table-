import psycopg2
import csv
from config import DB_CONFIG
from sql_queries import QUERY_DROP_TABLE, QUERY_CREATE_TABLE, QUERY_INSERT_INTO

FILE_CSV = "Electric_Vehicle_Charging_Stations.csv"

try:
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(QUERY_DROP_TABLE)
            cur.execute(QUERY_CREATE_TABLE)

            with open(FILE_CSV, "r", newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cleaned_row = tuple(None if val == "NONE" else val for val in row)
                    cur.execute(QUERY_INSERT_INTO, cleaned_row)

    print("CREATE AND INSERT SUCCESSFUL")

except Exception as e:
    print(f"Erreur : {e}")
