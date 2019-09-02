import serial

USB_Line = '/dev/ttyUSB0'  # CAUTION: may change due to USB port contention
ser = serial.Serial(USB_Line, 9600)
while True: 
    if(ser.in_waiting > 0):
        line = ser.readline()
        print(line)
        print (type(line))
        lineString = str(line)
        print (lineString[0:1])
        print (type(lineString))
        print()
