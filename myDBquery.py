#######################################################
# myDBquery.py                                        #
#   Rich Park February 09, 2019                       #
#   A program to query the temperature and humidities #
#   from the RPiFSv2 Database                         #
#######################################################

import sqlite3
import os # Allow for calls to the shell

#os.system('clear') # Clears the screen when using a terminal. Useful for avoiding testing clutter.

conn=sqlite3.connect('/var/www/lab_app/lab_app.db')
curs=conn.cursor()
curs.execute("SELECT * FROM temperatures")
temperatures = curs.fetchall()
conn.close()

# Get the 20 most recent temperature and humidity readings
for item in range ((len(temperatures) - 20), len(temperatures)):
        # Do a bit of formatting to make the output more readable.
        # NOTE: The u"\u2103" entry displays the 'degrees centigrade' symbol.
        #       The u"\u2109" entry displays the 'degrees fahrenheit' symbol.
    print (item," Temperature -> ", str(("{:.2f}".format)(temperatures \
                [item] [1])),u"\u2109","  ", (temperatures[item][0]), sep='')

