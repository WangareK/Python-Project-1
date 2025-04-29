# Passenger flight details
# Using tuples to represent flight details

#Using Python module to show current date and time
import datetime
from datetime import timedelta
x=datetime.datetime.now()
y=timedelta(hours=3)

#Creating a python tuple (with a nested tuple)
Ticket=("A01",("Nairobi", ("37E","3S")),
        ("Kigali",("34E","1S")),x ,x +y)
print(f"Flight number:",Ticket [0],
      "\nDeparting from:", Ticket[1],"at", Ticket[3],
      "\nArriving at:", Ticket[2], "at", Ticket[4])

#Unpacking the tuple
Ticket_Number, Departure_city, Arrival_city, Departure_time, Arrival_time=Ticket
print("Passenger's ticket number:", Ticket_Number)
print("Passenger's City of origin and coordinates:", Departure_city)
print("Passenger's time and date of departure:", Departure_time)
print("Passenger's destination and coordinates:", Arrival_city)
print("Passenger's time and date of arrival:", Arrival_time)


