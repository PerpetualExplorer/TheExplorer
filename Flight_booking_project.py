import pymysql.cursors

connection = pymysql.connect(host='localhost',user='root',password='root',database='Airline_Bookings',cursorclass=pymysql.cursors.DictCursor)


def display():
    print("\nCheck Your Details Here...")
    print(f"Name:{Passenger_Name}")
    print(f"Age:{Age}")
    print(f"Location of Departure:{Departure}")
    print(f"Location of Arrival:{Arrival}")
    print(f"Flight Number:{Flight_No}")
    print(f"No. Of Tickets:{No_of_Tickets}")
    print(f"E-Mail Id:{E_mail_Id}")
    print(f"Phone Number:{Phone_No}")


def flight_data(Departure,Arrival):
    user = connection.cursor()
    job = "select Flight_No from Flights where Departure= %s AND Arrival= %s"
    ips = (Departure,Arrival)
    user.execute(job,ips)
    print("Available Flights:")
    for x in user:
      print(x)

    connection.commit()

def booking(Passenger_Name,Age,Departure,Arrival,Flight_No,No_of_Tickets,E_mail_Id,Phone_No):
    user=connection.cursor()
    job= "insert into Passengers_Details (Passenger_Name,Age,Departure,Arrival,Flight_No,No_of_Tickets,E_mail_Id,Phone_No) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    ips=(Passenger_Name,Age,Departure,Arrival,Flight_No,No_of_Tickets,E_mail_Id,Phone_No)
    user.execute(job,ips)
    connection.commit()
    print("Booked Successfully...")
    display()
    Flight_details(Flight_No)

def Flight_details(Flight_No):
    user = connection.cursor()
    job = "select * from Flights where Flight_No='{}'".format(Flight_No)

    user.execute(job)
    x=user.fetchall()
    print("Flight Details:")
    print(x)
    connection.commit()











while(True):
    print("\nBook my Tickets?:Y/N")
    print("If 'Yes' select '1'")
    print("If 'No'  select '2'")
    print("To Exit  select '3'")

    e=int(input("Enter your choice:"))
    if e==1:
        Passenger_Name=input("Enter your name:")
        Age=int(input("Enter your Age:"))
        Departure=input("Departure :")
        Arrival= input("Destination :")
        No_of_Tickets=int(input("No. of tickets you want to book:"))
        E_mail_Id=input("Your E-mail ID:")
        Phone_No=input("Your Phone no.:")
        otp=input("Type the OTP sent to your Phone no. or E-mail ID:")
        print("Login Successfully....")
        flight_data(Departure,Arrival)
        Flight_No=input("Choose Your Flight:")
        booking(Passenger_Name,Age,Departure,Arrival,Flight_No,No_of_Tickets,E_mail_Id,Phone_No)
    elif e==2:
        print("\n""Thanks for visiting us""\n""Catch You Later...\n")
    elif e==3:
        quit()
    else:
        print("Invalid\n")



