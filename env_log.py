############################################
#  env_log.py                              #
#   Rich Park May 10, 2019 (rev 6/17/19)   #
#    A program to query the temperature    #
#     of a TMP36 Analog Temperature sensor #
############################################

import sqlite3
import sys
import serial

def getTemp(): # Slice the temperature reading from Arduino serial output

    USB_Line = '/dev/ttyUSB0' # CAUTION: may change due to USB port contention
    ser = serial.Serial(USB_Line, 9600) # RBP Raspberry Pi3-B+
    line = str(ser.readline())
    
    if (line[0:1]) != "b": # The first character is generally a 'b'.
        print('Bad Data. Line =', line)

    lineString = line
    return (float(lineString[2:7]))


def log_values(temp):
    # It is important to provide an absolute path to the database
    #  file, otherwise Cron won't be able to find it!
    conn=sqlite3.connect('/home/pi/TMP36_Project/tmp36.db')

    curs=conn.cursor()

    # Note the added comma after "temp" below (temp,)):
    # The reason this happens is that (temp) is an float but (temp,)
    #  is a tuple of length one containing temp/
    # This is necessary!
    curs.execute("INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?))", (temp,))
    conn.commit()
    conn.close()

# Get a temperature reading from the Arduino serial stream
#  timestamp it then, log it into a the SQLite3 'tmp36.db
# temperature = (mymod.getTemp())
temperature = (getTemp())
log_values(temperature)

