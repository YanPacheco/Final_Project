
# %%
#!/usr/bin/python
import pandas as pd
import csv

from IPython.display import clear_output
columns=['ORIGIN', 'DEST','ARR_DEL15','CANCELLED']
FlightData = pd.read_csv('c:/Users/yanky/Documents/flights.May2017-Apr2018.csv', usecols=columns)

print(FlightData.DEST.unique())
contin=''

while contin != 'quit':
    contin=input("Type quit if you would like to quit or else type enter: ")
    if contin == 'quit':
        break
    else:
        airportcode=input("Enter 3 letter airport code from list above that would like to get data on: ")

        choice =input("Enter 1 for looking at total delays to that airport or 2 for total number of cancelled flights: ")

        def CountDelays(airportcode,FlightData):
            cnt1=len(FlightData[(FlightData['DEST']== airportcode) & (FlightData['ARR_DEL15']==1)])
            print(cnt1)

        def CountCancelled(airportcode,FlightData):
            cnt2=len(FlightData[(FlightData['DEST']== airportcode) & (FlightData['CANCELLED'] == 1)])
            print(cnt2)

        if choice == '1':
            CountDelays(airportcode, FlightData)
        elif choice == '2':
            CountCancelled(airportcode, FlightData)
        with open('Data2.csv', 'w') as csvfile:
            filewriter=csv.writer(csvfile,delimiter=',')
            filewriter.writerow(['Airport_Code', 'Delay', 'Cancelled'])
            filewriter.writerow([airportcode,cnt1,cnt2])    


# %%
cnt=len(FlightData[(FlightData['DEST']== airportcode) & (FlightData['ARR_DEL15']==1)])
cnt1=int(cnt)


# %%


