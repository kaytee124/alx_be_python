from mysql.connector import connect, Error

mydb = connect(
    host="localhost",
    user="root",
    passwd="Vicky@2017",
    database="nouella")


mycursor = mydb.cursor()
mycursor.execute("select * from categories")
result = mycursor.fetchall()
print(result)

mydb.close()
mycursor.close()