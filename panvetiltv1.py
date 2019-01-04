from __future__ import division

import time
import Adafruit_PCA9685
from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit
#import maru1
import Robot

pwm = Adafruit_PCA9685.PCA9685()
#mh = Adafruit_MotorHAT(addr=0x60)



#pwm.set_pwm(0, 0, 450)
#panAngle = 90
pwm.set_pwm(1, 0, 400)
tiltAngle = 100
#300 < mx < 340

#220 < my < 260



def mapServoPosition (mx, my, aaa):
    int(my) 
    #print(mx , "sonmx")
    global tiltAngle
    if (my > 220 ):
        #print(' cisim yukarıda ')
        #time.sleep(0.5)
        tiltAngle -= 5
        #print(tiltAngle, 'tiltangleyukarı')
        acideg = 2.6
        ay = int(tiltAngle * acideg)
        pwmgirdisiy = int(660 - ay)
        #print(pwmgirdisiy, 'pwmgirdisiyukarı')
        pwm.set_pwm(1, 0, pwmgirdisiy)
        if tiltAngle < 80 :
            tiltAngle = 80
            #print(tiltAngle, 'tiltanglesınır')
            acideg = 2.6
            ay = int(tiltAngle * acideg)
            pwmgirdisiy = int(660 - ay)
            pwm.set_pwm(1, 0, pwmgirdisiy)
    if (my < 260 ) :
        #print('cisim asagida')
        #time.sleep(0.5)
        tiltAngle += 5
        #print(tiltAngle, 'tiltangleasagı')
        acideg = 2.6
        ay= int(tiltAngle * acideg)
        pwmgirdisiy = int(660 - ay)
        #print(pwmgirdisiy, 'pwmgirdisiasagı')
        pwm.set_pwm(1, 0, pwmgirdisiy)
        if tiltAngle > 150 :
            tiltAngle = 150
            acideg = 2.6
            ay = int(tiltAngle * acideg)
            pwmgirdisi = int(660 - ay)
            pwm.set_pwm(1, 0, pwmgirdisi)
    
    
     
    
    
    
    int(mx) 
    #print(mx , "sonmx")
    panAngle = aaa
    if (mx < 320 ):
        #print(' cisim solda ')
        #time.sleep(0.5)
        panAngle -= 5
        #print(panAngle, 'pananglesol')
        acideg = 2.6
        az = int(panAngle * acideg)
        pwmgirdisi = int(660 - az)
        print(pwmgirdisi, 'pwmgirdisisol111111')
        pwm.set_pwm(0, 0, pwmgirdisi)
        if panAngle < 20 :
            panAngle = 20
            #print(panAngle, 'panangle2')
            acideg = 2.6
            az = int(panAngle * acideg)
            pwmgirdisi = int(660 - az)
            pwm.set_pwm(0, 0, pwmgirdisi)
            print(pwmgirdisi,"pwmgirdisidownnnnnnn111")
    if (mx > 320 ) :
        #print('cisim sagda')
        #time.sleep(0.5)
        panAngle += 5
        print('cisimdesagdapekipananglenedenortada', panAngle)
        #print(panAngle, 'pananglesag')
        acideg = 2.6
        az = int(panAngle * acideg)
        pwmgirdisi = int(660 - az)
        print(pwmgirdisi, 'pwmgirdisisag1111111111')
        pwm.set_pwm(0, 0, pwmgirdisi)
        if panAngle > 180 :
            panAngle = 180
            acideg = 2.6
            ay = int(panAngle * acideg)
            pwmgirdisi = int(660 - ay)
            pwm.set_pwm(0, 0, pwmgirdisi)
            print(pwmgirdisi,"pwmgirdisixtopppppp111")
            
def pwmgirdisi (mx, aaa):
    
    int(mx) 
    panAngle = aaa
    if (mx < 300 ):
        print(' cisim solda ')
        #time.sleep(0.5)
        panAngle -= 5
        #print(panAngle, 'pananglesol')
        acideg = 2.6
        az = int(panAngle * acideg)
        return 660 - az
        #print(pwmgirdisi, 'pwmgirdisisol')
        #pwm.set_pwm(0, 0, pwmgirdisi)
        if panAngle < 20 :
            panAngle = 20
            #print(panAngle, 'panangle2')
            acideg = 2.6
            az = int(panAngle * acideg)
            return 660 - az
            #pwm.set_pwm(0, 0, pwmgirdisi)
    elif (mx > 340 ) :
        print('cisim sagda')
        #time.sleep(0.5)
        panAngle += 5
        #print(panAngle, 'pananglesag')
        acideg = 2.6
        az = int(panAngle * acideg)
        return  660 - az
        #print(pwmgirdisi, 'pwmgirdisisag')
        #pwm.set_pwm(0, 0, pwmgirdisi)
        if panAngle > 180 :
            panAngle = 180
            acideg = 2.6
            ay = int(panAngle * acideg)
            return 660 - ay
            #pwm.set_pwm(0, 0, pwmgirdisi)
            #print(pwmgirdisi,"pwmgirdisix")
    
    #return pwmgirdisi
        
    else :
        return 430
