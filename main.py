import mysql.connector
from tabulate import tabulate

connect = mysql.connector.connect(host="localhost", user="root", password="Mukunthan@2004", database="dummy")


def insert(name, age, city):
    res = connect.cursor()
    sql = "INSERT INTO users(Name,Age,City) values(%s,%s,%s)"
    user = (name,age,city)
    res.execute(sql,user)
    print("Data Inserted Successfully")
    connect.commit()


def update(name, age, city,id):
    res = connect.cursor()
    sql = "UPDATE users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    print("Data Updated Successfully")
    connect.commit()

def select():
    res = connect.cursor()
    query = "SELECT * FROM USERS"
    res.execute(query)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "Name", "Age", "City"]))


def delete(id):
    res = connect.cursor()
    query = "DELETE FROM USERS WHERE id = %s"
    users = (id,)
    res.execute(query,users)
    print("Data Deleted Successfully")


while True:
    print("1.INSERT")
    print("2.UPDATE")
    print("3.SELECT")
    print("4.DELETE")
    print("5.EXIT")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        city = input("Enter City")
        insert(name,age,city)
    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        city = input("Enter City: ")
        id = int(input("Enter the ID: "))
        update(name,age,city,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = int(input("Enter id: "))
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Choice! Please try again later.")
