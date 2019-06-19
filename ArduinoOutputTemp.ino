/*  Temperature Sensor Project for  TMP36
 *  This original sketch was written for Arduino Step by Step course by Peter Dalmaris.
 *  Modified by Rich Park as an Arduino analog temperature sensor for streaming
 *   information to the Tech Explorations Raspberry Pi FS Raspbian environment
 *    
 *     Lesson: Wiring the TMP36 and a demonstration sketch
 * 
 *  This sketch reads the the voltage of the TMP36 sensor output pin.
 *  It then does a calculation to convert this raw reading into a temperature (fahrenheit.)
 * 
 * 
 * Components
 * ----------
 *  - Arduino Uno
 *  - TMP36 temperature sensor
 *  
 *  Libraries
 *  ---------
 *  NONE
 *
 * Connections
 * -----------
 * 
 * As you look at the sensor with the label facing you, the left most pin is #1
 * 
 *  Break out    |    Arduino Uno
 *  -----------------------------
 *      1        |         5V   (Red wire)
 *      2        |         A0   (Yellow wire)
 *      3        |         GND  (Black wire)
 *      
 * 
 * Other information
 * -----------------
 * 
 * Datasheet: http://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf
 * 
 *  Original creation on October 8 2016 by Peter Dalmaris
 *  Adapted by Rich Park 2019-05-11
 * 
 */

 
float temp;

 // Ambient temp triggers LED when exceeded by temp
float ambientTemp = 76;

int tempPin = A0; // The reading is obtained from analog pin 0 (A0)
int ledPin = 13; // Used as output to show temperature exceeding a threshold

void setup()
{
  pinMode(ledPin, OUTPUT); // Assign LED pin as an output
  Serial.begin(9600);  // Start the serial connection with the computer
                       // to view the result open the serial monitor 
}

void loop()
{
temp = analogRead(tempPin);

// Adjust TMP36 output for fahrenheit
temp = temp * 0.48828125;

// Output only the temp value
Serial.println(temp);
delay(1000);

  // If temp exceeds the ambientTemp setting then
  //  trigger the LED when the TMP36 is pinched to raise
  //   temperature.
  if (temp >= ambientTemp){
  digitalWrite(ledPin, HIGH);
  }
  
  if (temp < ambientTemp) {
  digitalWrite(ledPin, LOW);
  }
}

