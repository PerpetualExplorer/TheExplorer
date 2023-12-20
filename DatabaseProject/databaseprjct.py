import pymysql.cursors
connection=pymysql.connect(host='localhost',user='root',password='root',database='minedb',cursorclass=pymysql.cursors.DictCursor)

def insert(Ename,Exp,Company,Country):
    user = connection.cursor()
    job = "insert into table1 ( Ename, Exp, Company, Country) values (%s, %s, %s, %s)"
    ips = (Ename,Exp,Company,Country)
    user.execute(job,ips)
    connection.commit()
    print("New Row is created successfully...")
def update(Company,Ename):
    user=connection.cursor()
    job = "update table1 set Company=%s where Ename=%s"
    ips=(Company,Ename)
    user.execute(job,ips)
    connection.commit()
    print("Successfully updated...")
def read():
    user=connection.cursor()
    job="select *from table1"

    user.execute(job)
    x=user.fetchall()
    print("The table as follows:")
    for y in x:
        print(y)
    connection.commit()
def delete(Exp):
    user=connection.cursor()
    job="delete from table1 where Exp=%s"
    ips=(Exp,)
    user.execute(job,ips)
    connection.commit()
    print("Deleted Successfully...")
while(True):
    print("1.Insert Data")
    print("2.Update data")
    print("3.Read data")
    print("4.Delete data")
    print("5.Exit")

    E=int(input("Enter your Choice:"))
    if (E==1):
      Ename=input("Enter the name of the Employee:")
      Exp=int(input("Enter his Experience in yrs:"))
      Company=input("Enter the company name:")
      Country=input("Enter his country name:")
      insert(Ename,Exp,Company,Country)
    elif(E==2):
      Company=input("Enter the company name to be changed to:")
      Ename=input("Enter the name of the Employee whose company to be updated:")
      update(Company,Ename)
    elif(E==4):
      Exp=int(input("Enter The Experience of the Employee to be deleted:"))
      delete(Exp)
    elif(E==3):
      read()
    elif(E==5):
      quit()
    else:
      print("Invalid Data\n")





