''' @file controlloop.py
    @author Jeremy Baechler
    @author Kendall Chappell
    @author Matthew Wimberley

'''
from ulab import numpy as np
import utime

class ClosedLoop:
    
    def __init__(self, Kp, ref):
        self.Kp = Kp
        self.ref = ref
        self.listpos = []
        self.time = []
        self.start_time = utime.ticks_ms()
    
    def run(self, pos):
        self.pos = pos
        self.error = self.ref-self.pos
        print('Position', self.pos, 'Error:', self.error)
        duty = self.error * self.Kp
        return duty
        
    
    def set_ref(self, ref):
        self.ref = ref
    
    def set_Kp(self, Kp):
        self.Kp = Kp
    
    def add_data(self):
        self.current_time = utime.ticks_ms()
        time = utime.ticks_diff(self.current_time, self.start_time)
        self.time.append(time)
        self.listpos.append(self.pos)
    
    

if __name__ == '__main__':
    controller = ClosedLoop(.15, 10)
    print(controller.run(5))