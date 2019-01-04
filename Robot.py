
import time
import atexit

from Adafruit_MotorHAT import Adafruit_MotorHAT


class Robot(object):
    def __init__(self, addr=0x60, left_trim=0, right_trim=0,
                 stop_at_exit=True):

        self._mh = Adafruit_MotorHAT(addr)
        self._left1 = self._mh.getMotor(4)
        self._left2 = self._mh.getMotor(3)
        self._right1 = self._mh.getMotor(1)
        self._right2 = self._mh.getMotor(2)
        self._left_trim = left_trim
        self._right_trim = right_trim
     
        self._left1.run(Adafruit_MotorHAT.RELEASE)
        self._left2.run(Adafruit_MotorHAT.RELEASE)
        self._right1.run(Adafruit_MotorHAT.RELEASE)
        self._right2.run(Adafruit_MotorHAT.RELEASE)
       
        if stop_at_exit:
            atexit.register(self.stop)

    def _left1_speed(self, speed):
       '
        speed += self._left_trim
        speed = max(0, min(255, speed))  
        self._left1.setSpeed(speed)
        
        
    def _left2_speed(self, speed):
        
        assert 0 <= speed <= 255, 
        speed += self._left_trim
        speed = max(0, min(255, speed)) 
        self._left2.setSpeed(speed)

    def _right1_speed(self, speed):
       
        assert 0 <= speed <= 255, 
        speed += self._right_trim
        speed = max(0, min(255, speed))  
        self._right1.setSpeed(speed)
        
    def _right2_speed(self, speed):
       
        speed += self._right_trim
        speed = max(0, min(255, speed))  .
        self._right2.setSpeed(speed)

    def stop(self):
        
        self._left1.run(Adafruit_MotorHAT.RELEASE)
        self._right1.run(Adafruit_MotorHAT.RELEASE)
        self._left2.run(Adafruit_MotorHAT.RELEASE)
        self._right2.run(Adafruit_MotorHAT.RELEASE)

    def forward(self, speed, seconds=None):
       
        self._left1_speed(speed)
        self._right1_speed(speed)
        self._left1.run(Adafruit_MotorHAT.FORWARD)
        self._right1.run(Adafruit_MotorHAT.BACKWARD)
        self._left2_speed(speed)
        self._right2_speed(speed)
        self._left2.run(Adafruit_MotorHAT.BACKWARD)
        self._right2.run(Adafruit_MotorHAT.FORWARD)
      
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def backward(self, speed, seconds=None):
      
   
        self._left1_speed(speed)
        self._right1_speed(speed)
        self._left1.run(Adafruit_MotorHAT.BACKWARD)
        self._right1.run(Adafruit_MotorHAT.FORWARD)
        self._left2_speed(speed)
        self._right2_speed(speed)
        self._left2.run(Adafruit_MotorHAT.FORWARD)
        self._right2.run(Adafruit_MotorHAT.BACKWARD)
       
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def right(self, speed, seconds=None):
      
        self._left1_speed(speed)
        self._right1_speed(speed)
        self._left1.run(Adafruit_MotorHAT.FORWARD)
        self._right1.run(Adafruit_MotorHAT.FORWARD)
        
        self._left2_speed(speed)
        self._right2_speed(speed)
        self._left2.run(Adafruit_MotorHAT.BACKWARD)
        self._right2.run(Adafruit_MotorHAT.BACKWARD)
     
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def left(self, speed, seconds=None):
     
    
        self._left1_speed(speed)
        self._right1_speed(speed)
        self._left1.run(Adafruit_MotorHAT.BACKWARD)
        self._right1.run(Adafruit_MotorHAT.BACKWARD)
        
        self._left2_speed(speed)
        self._right2_speed(speed)
        self._left2.run(Adafruit_MotorHAT.FORWARD)
        self._right2.run(Adafruit_MotorHAT.FORWARD)
        
       
        if seconds is not None:
            time.sleep(seconds)
            self.stop()
