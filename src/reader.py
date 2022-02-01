'''
    @file reader.py
    @author Jeremy Baechler
    @author Kendall Chappell
    @author Matthew Wimberley

'''

import serial, time

with serial.Serial ('COM3', 115200) as s_port:
#     Kp = float(input('Please type in a proportional gain constant!: '))
#     setpoint = float(input('Please type in a position setpoint!: '))
    s_port.write (b'0.05\r\n')   # Write bytes, not a string
    s_port.write(b'13000\r\n')
    time.sleep(1)
    
    s_port.write(b'\x03')
    
    while True:
        try:
            data_line = s_port.readline().strip().decode()
            print (data_line)
            if data_line == 'Stop Transmission':
#                 print('Interrupt has been seen')
                raise KeyboardInterrupt
        except:
            print('Program Terminated')
            break

