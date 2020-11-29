import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ginger94090"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")