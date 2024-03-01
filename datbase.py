import pymysql

# Connect to MySQL database server
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='plmokn@12'
)

# Create database
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS password_manager")
cursor.execute("USE password_manager")

# Create passwords table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        password_reason VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# Close connection
conn.close()
