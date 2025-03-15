import pandas as pd
import psycopg2
from psycopg2 import sql

try:
    # Establishing the connection to the database
    conn = psycopg2.connect(
        dbname="bible_plan_db",
        user="postgres",
        password="postgres",  # Replace with your actual password
        host="localhost",     # Assumes running inside the container
        port="5432"
    )
    cursor = conn.cursor()
    print("Connection to database established successfully.")

    # Read the CSV file
    df = pd.read_csv('/reformatted_bible_readings.csv')
    print("CSV file read successfully.")

    # Create the insert query
    insert_query = sql.SQL("""
    INSERT INTO bible_readings (date, book, chapter, type)
    VALUES (%s, %s, %s, %s)
    """)

    # Insert each row from the DataFrame into the database
    for index, row in df.iterrows():
        cursor.execute(insert_query, (row['date'], row['book'], row['chapter'], row['type']))

    # Commit the changes
    conn.commit()
    print("Data inserted successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection only if it was established
    if 'conn' in locals() and conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")




# import pandas as pd
# import psycopg2

# # Step 1: Load the reformatted CSV file into a DataFrame
# df = pd.read_csv('reformatted_bible_readings.csv')

# # Step 2: Connect to the PostgreSQL database
# try:
#     conn = psycopg2.connect(
#         dbname="bible_plan_db",  # Replace with your database name
#         user="postgres",       # Replace with your PostgreSQL username
#         password="postgres",   # Replace with your PostgreSQL password
#         host="host.docker.internal",           # Adjust if your database is remote
#         port="5432"                 # Default PostgreSQL port
#     )
#     cursor = conn.cursor()
#     print("Connected to PostgreSQL successfully.")

#     # Step 3: Insert each row from the DataFrame into the database
#     for _, row in df.iterrows():
#         cursor.execute(
#             """
#             INSERT INTO bible_readings (date, book, chapter, type)
#             VALUES (%s, %s, %s, %s);
#             """,
#             (row['Date'], row['Book'], row['Chapter'], row['Type'])
#         )
    
#     # Commit the transaction
#     conn.commit()
#     print("Data inserted successfully!")

# except Exception as e:
#     print("An error occurred:", e)

# finally:
#     # Close the connection
#     if conn:
#         cursor.close()
#         conn.close()
#         print("PostgreSQL connection closed.")
