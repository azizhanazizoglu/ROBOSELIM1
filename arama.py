from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()


pwm.set_pwm(0, 0, 190)
panAngle = 190
#pwm.set_pwm(1, 0, 400)
#tiltAngle = 100
#300 < mx < 340

#220 < my < 260


def cisimarama():
        pwm.set_pwm(1, 0, 390)
        global panAngle
        if panAngle > -10:
        #time.sleep(0.5)
            panAngle -= 5
            print('eksi pan angle', panAngle)
        
            acideg = 2.6
            az = int(panAngle * acideg)
            pwmgirdisi1 = int(660 - az)
        
            pwm.set_pwm(0, 0, pwmgirdisi1)
            #print('pwmgirdisi1' ,pwmgirdisi1)
            
            
        
        else:
            panAngle += 5
            print('artıpanangle',panAngle)
            acideg = 2.6
            az = int(panAngle * acideg)
            pwmgirdisi1 = int(660 - az)
            pwm.set_pwm(0, 0, pwmgirdisi1)
##        return pwmgirdisi1
        if pwmgirdisi1 > 660:
            #print('aaaaaa')
            panAngle =200
            #pwmgirdisi1 = 190
        
        
        return panAngle
        
  
def kafareset ():
        #int(aaa)
        #global aaa
        #print('aaaa', aaa)
        print('hdur')
       # if aaa > 500 :
        pwm.set_pwm(0, 0, 190)
        pwmgirdisi1 = 0
        
        return
            
       
        

    
        

