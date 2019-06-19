'''
FILE NAME
lab_app.py
Version 4

1. WHAT IT DOES
Implements the first version of the project's Flask application.
This version contains adds a page that displays sensor readings from the database.
 
2. REQUIRES
* Any Raspberry Pi

3. ORIGINAL WORK
Raspberry Full Stack 2018, Peter Dalmaris
Modified 2019 to incorporate the TMP36 with 
Arduino and Rasperberry Pi, Richard Park 

4. HARDWARE
* Any Raspberry Pi
* Arduino UNO or Compatible Spark Fun Redboard
* TMP36 Analog Temperature Sensor

5. SOFTWARE
Command line terminal
Simple text editor
Libraries:
from flask import Flask, request, render_template, sqlite3, time,
 datetime, serial

6. WARNING!
None

7. CREATED 

8. TYPICAL OUTPUT
A simple web page served by this flask application in the user's browser.
The page contains the current temperature.
A second page that displays historical environment data from the SQLite3 database.

 // 9. COMMENTS
--
 // 10. END
'''

from flask import Flask, request, render_template
import time
import datetime
import sys
import serial
import sqlite3

app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

## RBP 2018-09-13
## Adding the following line outputs the value
## of '__name__' on the command line.
print()
print("Value of '__name__' = ", __name__)
print ()

@app.route("/")
def hello():
    return render_template('hello.html', 
    message1 = "Hello World!",
    message2 = "Hello World!")


@app.route("/lab_temp")
def lab_temp(): 
    USB_Line = 'dev/ttyUSB0'
    ser = serial.Serial(USB_Line, 9600)
    lineString = str(ser.readline())
    verifyTemp = (lineString[0:1])
    temperature = (float(lineString[2:7]))

    if  verifyTemp != "b":
        temperature = 999.99
        return render_template("lab_temp.html", temp=temperature)
    else:
        return render_template("lab_temp.html",temp=temperature)


@app.route("/lab_env_db1")
def lab_env_db1():
    conn=sqlite3.connect('/var/www/lab_app/lab_app.db')
    curs=conn.cursor()
    curs.execute("SELECT * FROM temperatures")
    temperatures = curs.fetchall()
    conn.close()
    return render_template("lab_env_db.html",temp=temperatures)
    

@app.route("/lab_env_db", methods=['GET']) 
def lab_env_db():
    temperatures, from_date_str, to_date_str = get_records()
    return render_template("lab_env_db.html",temp=temperatures)

def get_records():
    from_date_str = request.args.get('from',time.strftime("%Y-%m-%d 00:00")) #Get the from date value from the URL
    to_date_str = request.args.get('to',time.strftime("%Y-%m-%d %H:%M"))   #Get the to date value from the URL
    range_h_form = request.args.get('range_h','');  #This will return a string, if field range_h exists in the request

    range_h_int = "nan"  #initialise this variable with not a number

    try: 
        range_h_int = int(range_h_form)
    except:
        print ("range_h_form not a number")

    if not validate_date(from_date_str):  # Validate date before sending it to the DB
        from_date_str = time.strftime("%Y-%m-%d 00:00")
    if not validate_date(to_date_str):
        to_date_str = time.strftime("%Y-%m-%d %H:%M")  # Validate date before sending it to the DB

    # If range_h is defined, we don't need the from and to times
    if isinstance(range_h_int,int):	
        time_now = datetime.datetime.now()
        time_from = time_now - datetime.timedelta(hours = range_h_int)
        time_to = time_now
        from_date_str = time_from.strftime("%Y-%m-%d %H:%M")
        to_date_str = time_to.strftime("%Y-%m-%d %H:%M")

    conn=sqlite3.connect('/var/www/lab_app/lab_app.db')
    curs=conn.cursor()
    curs.execute("SELECT * FROM temperatures WHERE rDateTime BETWEEN ? AND ?", (from_date_str, to_date_str))
    temperatures = curs.fetchall()
    conn.close()
    return [temperatures, from_date_str, to_date_str]

def validate_date(d):
    try:
        datetime.datetime.strptime(d, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False
  
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
