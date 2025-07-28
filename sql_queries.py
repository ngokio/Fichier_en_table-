# sql_queries.py

QUERY_DROP_TABLE = "DROP TABLE IF EXISTS Electric_Vehicle_Charging_Stations"

QUERY_CREATE_TABLE = """
CREATE TABLE Electric_Vehicle_Charging_Stations(
    Station_Name VARCHAR(255),
    Street_Address VARCHAR(255), 
    City VARCHAR(255), 
    Access_Days_Time VARCHAR(255), 
    EV_Level1_EVSE VARCHAR(255), 
    EV_Level2_EVSE VARCHAR(255),
    EV_DC_Fast_Count VARCHAR(255), 
    EV_Other_Info VARCHAR(255), 
    New_Georeferenced VARCHAR(255)
)
"""

QUERY_INSERT_INTO = """
INSERT INTO Electric_Vehicle_Charging_Stations(
    Station_Name, Street_Address, City, Access_Days_Time, 
    EV_Level1_EVSE, EV_Level2_EVSE, 
    EV_DC_Fast_Count, EV_Other_Info, New_Georeferenced
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
