'''
    @file reader.py
    @author Jeremy Baechler
    @author Kendall Chappell
    @author Matthew Wimberley

'''

import serial

with serial.Serial ('COM3', 115200) as s_port:
#     Kp = float(input('Please type in a proportional gain constant!: '))
#     setpoint = float(input('Please type in a position setpoint!: '))
    s_port.write (b'0.15')   # Write bytes, not a string
    s_port.write(b'13000')
    
    print (s_port.readline ().split (b','))

