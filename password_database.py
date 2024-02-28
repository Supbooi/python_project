import pymysql

# Function to create the passwords table if it doesn't exist
def create_passwords_table():
    try:
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='plmokn@12',
        )
        mycursor=connection.cursor()
        query = "CREATE DATABASE IF NOT EXISTS password"
        mycursor.execute(query)
        query = 'USE password'
        mycursor.execute(query)
        query = 'CREATE TABLE IF NOT EXISTS data(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, username VARCHAR(100), password VARCHAR(20))'
        mycursor.execute(query)
        with connection.cursor() as cursor:
            # SQL statement to create the passwords table
            sql = """
            CREATE TABLE IF NOT EXISTS passwords (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """
            cursor.execute(sql)
            connection.commit()
            print("Table 'passwords' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if connection:
            connection.close()

# Call the function to create the passwords table
create_passwords_table()
