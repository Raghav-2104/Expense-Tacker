import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Raghav@2104",
  database="expensetracker"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM registration")

myresult = mycursor.fetchone()

print(myresult)



