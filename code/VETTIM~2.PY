#Ovija Vettimayilnathan (Student B)
#CIP02 F23 Projekt
#Gruppe 16
#Galaxus Load MariaDB

# Module Imports
import mariadb
import sys
import os
import pandas as pd

def get_files():

    # stage 3 holen
    file_path1 = os.path.join(os.getcwd(), '..','Vettimayilnathan_Ovija_studentB_Data/Vettimayilnathan_Ovija_studentB_Data_stage3.csv')
    # File lesen/laden
    df_Galaxus = pd.read_csv(file_path1,encoding='UTF-8')

    # merge holen
    file_path2 = os.path.join(os.getcwd(), '..','Vettimayilnathan_Ovija_studentB_Data/Vettimayilnathan_Ovija_studentB_Data_merged.csv')
    # File lesen/laden
    df_Merged = pd.read_csv(file_path2, encoding='UTF-8')

    return df_Galaxus, df_Merged

def connect_mariadb():

    try:
        conn = mariadb.connect(
            user="cip_user",
            password="cip_pw",
            host="127.0.0.1",
            port=3306,
            database="CIP"
        )
        print("Connected to MariaDB!")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()

    return cur, conn

def upload_stage3(df_Galaxus, cur, conn):

    # Tabelle: stage 3
    table_name = 'Smartphone_Data_Galaxus_stage3'
    column_names = ', '.join(list(df_Galaxus.columns))
    query_drop = f"DROP TABLE IF EXISTS {table_name}"
    query_create = f"CREATE TABLE {table_name} (Preis FLOAT, Marke VARCHAR(255), Modell VARCHAR(255), Speicher INT, Farbe VARCHAR(255), Display FLOAT, Kamera VARCHAR(255), Mobilfunk VARCHAR(255), Produkt VARCHAR(255), Marke_Prozent FLOAT, Funk_Prozent FLOAT);"

    try:
        cur.execute(query_drop)
        cur.execute(query_create)
        print("Table created in MariaDB")
    except mariadb.Error as e:
        print(f"Error: {e}")
        cur.close()
        conn.close()

    # Daten in die Tabelle eintragen
    for index, row in df_Galaxus.iterrows():
        values = tuple(row.values)
        query_insert = f"INSERT INTO {table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cur.execute(query_insert, values)
            conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")
            conn.close()
            exit(1)
    return

def upload_merged(df_Merged, cur, conn):

    # Tabelle: stage 3
    table_name = 'Smartphone_Data_merged_stage'
    column_names = ', '.join(list(df_Merged.columns))
    query_drop = f"DROP TABLE IF EXISTS {table_name}"
    query_create = f"CREATE TABLE {table_name} (Marke VARCHAR(255), Modell VARCHAR(255), Farbe VARCHAR(255), Speicher FLOAT, Display_Inches FLOAT, Display_CM FLOAT, Mobilfunk VARCHAR(255), Rueckkamera VARCHAR(255), Frontkamera FLOAT, Modelljahr INT, Gesichtserkennung FLOAT, Produkt VARCHAR(255), Kategorie_Farbe VARCHAR(255), Med_Preis FLOAT, Gal_Preis FLOAT, Med_Gesamtkundenbewertung FLOAT, Med_Anzahl_Kundenbewertung FLOAT, Gal_Markenanteil FLOAT, Gal_Mobilfunkanteil FLOAT, Preisdifferenz FLOAT);"

    try:
        cur.execute(query_drop)
        cur.execute(query_create)
        print("Table created in MariaDB")
    except mariadb.Error as e:
        print(f"Error: {e}")
        cur.close()
        conn.close()

    # Daten in die Tabelle eintragen
    for index, row in df_Merged.iterrows():
        values = tuple(row.values)
        query_insert = f"INSERT INTO {table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cur.execute(query_insert, values)
            conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")
            conn.close()
            exit(1)
    return

def main():
    print("Get the files.")
    df_Galaxus, df_Merged = get_files()
    print("Files loaded.")

    print("Connecting to MariaDB")
    cur, conn = connect_mariadb()
    print("Successfully connected!")

    print("Upload stage3 File started!")
    upload_stage3(df_Galaxus, cur, conn)
    print("Upload stage3 successful!")

    print("Upload merged File started!")
    upload_merged(df_Merged, cur, conn)
    print("Upload merged File successful!")
    conn.close()

if __name__=="__main__":
    main()