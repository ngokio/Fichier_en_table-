import psycopg2
import csv
from sql_queries import QUERY_CREATE_TABLE, QUERY_DROP_TABLE, QUERY_INSERT

class DataLoader:
    def __init__(self, db_config, csv_file):
        self.db_config = db_config
        self.csv_file = csv_file

    def load_data(self):
        try:
            with psycopg2.connect(**self.db_config) as conn:
                with conn.cursor() as cur:
                    cur.execute(QUERY_DROP_TABLE)
                    cur.execute(QUERY_CREATE_TABLE)

                    with open(self.csv_file, newline='', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        next(reader)  # skip header

                        for row in reader:
                            cleaned_row = tuple(None if val == 'NONE' else val for val in row)
                            cur.execute(QUERY_INSERT, cleaned_row)

                conn.commit()
            print("✅ Import terminé avec succès.")

        except Exception as e:
            print(f"❌ Erreur : {e}")
