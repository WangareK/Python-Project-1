#User input
a=input("Enter flight number:")
b= input("Enter departure city:")
c= input("Enter coordinates of departure city:")
d= input("Enter arrival city:")
e=input("Enter coordinates of destination:")
f=input("Enter time of departure:")
 



#Departure and arrival times
import datetime
from datetime import timedelta
x=datetime.datetime.now() #current time
y=timedelta(hours=3) #derived arrival time


Ticket=(a,b,c, x,x+y)

print(f"Flight number:",Ticket [0],
      "\nDeparting from:", Ticket[1],"at", Ticket[3],
      "\nArriving at:", Ticket[2], "at", Ticket[4])

#Unpacking the tuple
Ticket_Number, Departure_city, Arrival_city, Departure_time, Arrival_time=Ticket
print("Passenger's ticket number:", Ticket_Number)
print("Passenger's City of origin:", Departure_city)
print("Passenger's time and date of departure:", Departure_time)
print("Passenger's destination:", Arrival_city)
print("Passenger's time and date of arrival:", Arrival_time)


