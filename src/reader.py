'''
    @file       reader.py
    @brief      communicates user input to microcontroller using serial port
    @details    The gain value and set point are entered in as bytes through
                the serial port where the microcontroller takes these numbers
                for the ClosedLoop class. After a second of data collection,
                the program will print the time and motor position, then it 
                will stop with an intentional keyboard interrupt.
                
    @author     Jeremy Baechler
    @author     Kendall Chappell
    @author     Matthew Wimberley
    @date       31-Jan-2022

'''

import serial, time

with serial.Serial ('COM3', 115200) as s_port:
    '''@brief   communicates gain and set point values to microcontroller
       @param   'COM3'  right USB port on computer
       @param   baud    the communication speed for data transfer
       '''
       
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

