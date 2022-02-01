'''
    @file       main.py
    @brief      instantiates all necessary objects for motor control
    @details    This main file sets up our pins, timer, and enabler objects 
                to run the motor. As well, the motor, encoder, and controller
                are all run as objects of their respective class. With these
                instantiated, we can control the motor output with feedback 
                from the encoder position.
                
    @author     Jeremy Baechler
    @author     Kendall Chappell
    @author     Matthew Wimberley
    @date       31-Jan-2022
'''

#Pull encoder data
#Run control loop with new data
#Take returned PWM duty and send that to the motor
#Store data in controller
#Print Data to serial port

#Input Kp, setpoint

'''VERY IMPORTANT DO NOT FORGET ABOUT ME!

    In order to get the encoder values to read properly, we need to have the blue wire plugged
    into B7 and the yellow wire plugged into B6. If this is not done, the encoder and motor
    configurations will not match, leading to increasing controller error.
'''

import EncoderReader, controlloop, pyb, utime
import motor_baechler_chappell_wimberley as motor_drv

ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
IN1 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
IN2 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP) #motor port A pins
tim3 = pyb.Timer (3, freq=20000)


Kp = float(input())
setpoint = float(input()) #blocking code

mot1 = motor_drv.MotorDriver(ENA, IN1, IN2, tim3)
enc1 = EncoderReader.EncoderReader(1)
controller = controlloop.ClosedLoop(Kp, setpoint)

while True:
    try:
        PWM = controller.run(enc1.read())
        controller.add_data()
        mot1.set_duty(PWM)
        utime.sleep_ms(10)
#         print('Sending data!')
    except KeyboardInterrupt:
        mot1.set_duty(0)
        for i in range(len(controller.time)):
            print(controller.time[i], controller.listpos[i])
        print('Stop Transmission')
        break
        
    


