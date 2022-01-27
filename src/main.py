'''
    @file main.py
    @author Jeremy Baechler
    @author Kendall Chappell
    @author Matthew Wimberley

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


Kp = float(input('Please type in a proportional gain constant!: '))
setpoint = float(input('Please type in a position setpoint!: '))

mot1 = motor_drv.MotorDriver(ENA, IN1, IN2, tim3)
enc1 = EncoderReader.EncoderReader(1)
controller = controlloop.ClosedLoop(Kp, setpoint)

while True:
    try:
        PWM = controller.run(enc1.read())
        controller.add_data()
        mot1.set_duty(PWM)
        utime.sleep_ms(10)
    except KeyboardInterrupt:
        mot1.set_duty(0)
        for i in range(len(controller.time)):
            print(controller.time[i], controller.listpos[i])
        
        
    


