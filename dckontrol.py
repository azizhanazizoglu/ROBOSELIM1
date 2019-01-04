from __future__ import division

import panvetiltv1

import time
import Adafruit_PCA9685
from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit
import Robot



def pwmdckontrol (pwmout) :
    #print('sinyal kontrol track vol9 dc, sinya içerde')
    int(pwmout)
    #print(pwmgirdisi, 'pwmgirdisi dc içerideee')
    #global pwmgirdisi
    if (pwmout < 420 ):
        #print("kafa sagda")
                #time.sleep(0.5)
                
                
        LEFT_TRIM   = 0
        RIGHT_TRIM  = 0
        robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
        robot.right(255, 0.05)
        #robot.forward(70, 0.02)
            
    elif (pwmout  > 460 ) :
        #print("kafa solda")
                #time.sleep(0.5)
                
        LEFT_TRIM   = 0
        RIGHT_TRIM  = 0
        robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
        robot.left(255, 0.05)
        #robot.forward(70, 0.2)


    else :
        LEFT_TRIM   = 0
        RIGHT_TRIM  = 0
        robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
        #print('kafa tam ortada düz gidicek')
        robot.forward(255, 0.1)