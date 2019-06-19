# Temperature Sensor Single Read Project for  TMP36
# Created by Rich Park 2019-04-19

import serial
import matplotlib.pyplot as plot

# The USB serial port will vary by device This particular port

USB_Line = '/dev/ttyUSB0'  # CAUTION: may change due to USB port contention
ser = serial.Serial(USB_Line, 9600) # RBP Raspberry Pi3-B+

def getTemps(size):
    tempsList = []
    for item in range (size):
        line = str(ser.readline())
        print()

        if (line[0:1]) != "b": # The first character is generally a 'b'.
            print('Bad Data. Line =', line)
        else:
            print('Good Data. First character =', line[0:1])
        
        print('Raw record from the Arduino USB port. =', line) # Raw input from the serial port
        getSerial = (line[2:7]) # After slicing the string
        print('Temperature stripped from the raw record. =', getSerial)
        tempsList.append(float(getSerial[0:7]))
        print ('Build the list for plotting. =', tempsList, '\n') # Show the plot list being constructed
    return tempsList


def plot_it(mytemps):
    plot.bar(range(len(mytemps)), mytemps, align='center', alpha=0.5)
    plot.xticks(range(len(mytemps)))
    plot.ylabel('Arduino TMP36 Fahrenheit')
    plot.title('Temperature Plots')
    plot.show()

# Main Program Loop
values = (input("Enter the number of temperature readings to plot [5-25] -> "))
myTemps = getTemps(int(values))
plot_it(myTemps)
