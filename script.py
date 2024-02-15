import mysql.connector

# Replace 'your_database', 'your_user', 'your_password' with your actual MySQL database credentials
conn = mysql.connector.connect(
    host="host", # if docker compose db '''docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_id'''
    user="user",
    password="password",
    database="database"
)

cursor = conn.cursor()

floor_names = ['Floor 1', 'Floor 2', 'Floor 3', 'Floor 4']

# Insert data into the 'floors' table using a for loop, the only column for this table is 'name'
for name in floor_names:
    cursor.execute('INSERT INTO floors (name) VALUES (%s)', (name,))

# Commit the changes and close the connection
conn.commit()
conn.close()
