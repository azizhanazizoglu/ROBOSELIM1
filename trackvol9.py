from __future__ import division
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import Robot
import numpy as np
#import picam
import time
import arama
#import vol5
#import vol5tiltv1
#import vol5panv1


import panvetiltv1


import dckontrol


import cv2

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

redLower = np.array([0, 41, 172], dtype = "uint8")
redUpper = np.array([36, 156, 255], dtype = "uint8")

#pwm ekleyip servo kontrol yapacağız
#pwm = Adafruit_PCA9685.PCA9685()
#pixel = 640
#xdeg=int(input("1.bolgedeki konum giriniz -x ekseni :"))




#vidyoyu yüklüyoruz
#burası direk olarak terminalden gelen
#picamerayı belirtilen boyutlarda görüntüleyecektir.
#vol1'de 460x460 örneği belirlenmiştir
#video= picam.camera()
#burada kendimize picam dan referans alabilceğimiz bir obje seçiyoruz
#buna camera simini veriyoruz
#kare hızını ve çözünürlüğünü ayarlıyoruz

camera = PiCamera()
#gündüz
camera.contrast = 20
camera.brightness = 55
#gece
#camera.brightness = 80
#camera.contrast = 70
camera.resolution = (640 , 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        #read() komutu sıradaki kameradan gelen
        #kareyi alır ve bu vidyolar çok gruplu verilere
        #aktarılır. boelen (mantıksal) indirgemeye tutulur
        #bu indirgemenin amacı vidyodan kareler düzgün okundu mu?
        #ikinci olan frame komutu karelerin ta kendisi
##        (grabbed, frame) = video .read()
        #time.sleep(0.025)
        #frame=camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
        #camera.capture(rawCapture,format="bgr")      
        image = frame.array
        #cv2.imshow("Image", image)
        #key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        #Eğer vidyodaki datalar okunmadı ise
        #pi den alınan kamera görüntüsünü durdurur.
        #if not grabbed:
         #    break

                
        #Mavinin tonlarını bulmak için aşağıdaki range komutlarını kullanacağız
        #bu fonksiyon 3 tane parametre gereklidir.
        #1.sis frame ler düzgün mü değilmi kontrolü
        #en düşük trashold değereri
        #ve en son olarak en yüksek treshold
        #sonuç olarak blue adında tresholded (sınırlanan)
        #bir resim, belirli sınırlarda beyazdan siyaha değişen binarry formuna dönüşür
                
        red = cv2.inRange(image, redLower, redUpper)
        #sonunda resimimizi bulanıklaştırıp contoursları bulmaya çalışacağız
        #gussian blur
        #contours köşleri belirlenen bir binary karesinin
        #i(önce binaryde çerçeve oluşturur)
        #üzerine gerçek resim konularak tam olarak sınırları çizilmiş olunur.
        red = cv2.GaussianBlur(red, (3, 3), 0)
           
        #sırada contourları bulmaya geldi
        #şimid elimizde sınırlandırılmış resimler var
        #aralarında takip etmek için en büyüğü bulacağız
        #cvwfind tresholded (sınırlandırılan resmin contuarlarını bulucak
        #copy kullanmamız lazım
        #çünkü orjinalini alırsak numpy kütüphaensini patlatabiliriz.
        #burada retr diktörgen olarak alınmış

        # find contours in the image
        (_, cnts, _) = cv2.findContours(red.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)

        #contuarların gerçekten bulunup bulunadığını kontrol edeceğiz
        #bunun için if komutunu kullanıyoruz
        #eğer bölgeler toplamı sıfır ise mavi bir cisim bulunmamıştır demektir
        if len(cnts) > 0:
                        
                #artık bulduğumuz contourlarda takib edebilmek için
                #en büyük olanını alıyoruz.
                #bunu cv.countourArena fonksiyonu ile sağlıyoruz
                #bunu yaparken bu formul dikdörtgenlerin içini alanını hesaplamaktadır.
                #böylelikle birsürü mavi küçük karelerden sadece en büyük bir taneyi almış oluyoruz
                #hem data yükümüz haffliyor hem de birden fazla center point bulmamış olacağız
                #artık doğru contuara sahib objeye sahipiz
                #şimdi gerekli işlemler yapmak için bir kutu içine almamız gereki,yor
                        
                cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                alan = round(cv2.contourArea(cnt))
                
                print('alanııııııııııı', alan)
                
                #33000 den büyükse stop etmesi lazım
                
                if alan > 25000:
                    (merkezx,merkezy), radius = cv2.minEnclosingCircle(cnt)
                    center = (int(merkezx),int(merkezy))
                    radius = int(radius)
                    cv2.circle(image,center,radius,(0,255,0),2)
                    
                    mx = round(merkezx)
                    my = round(merkezy)
                    cv2.line(image, (mx, my), (mx, my), (0,255,0), 5)
                    
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    text_writeX = str(mx)
                    text_writeY = str(my)
                    cv2.putText(image, text_writeX, (100, 200), font, 1, (0, 255, 0),2)
                    cv2.putText(image, text_writeY, (100, 250), font, 1, (0, 255, 0),2)
                
                else:

                    
                    #merkez bulma
                    #M = cv2.moments(cnt)
                    #cx = int(M['m10']/M['m00'])
                    #cy = int(M['m01']/M['m00'])
                    #print(cx)
                    #print(cy)
                    
                    #çevreyi dairesel sarma deneme
                    (merkezx,merkezy), radius = cv2.minEnclosingCircle(cnt)
                    center = (int(merkezx),int(merkezy))
                    radius = int(radius)
                    cv2.circle(image,center,radius,(0,255,0),2)
                    #print(merkezx,'x ekseni')
                    #print(merkezy, 'y ekseni')
                    
                    #yuvarlama işlemi yaparsak
                    mx = round(merkezx)
                    my = round(merkezy)
                    #print(mx, 'x ekseni')
                    #print(my, 'y ekseni')
                    
                    
                    #merekz noktası koyma denemeleri
                    #normalde merkezx,merkezy ile yapmaya çalışıldı ama float olduğu için yapılamadı.
                    #int gibi bir fonksiyon bulunup rakamsal fonksiyona çevirilmnesi gerekmektedir.
                    cv2.line(image, (mx, my), (mx, my), (0,255,0), 5)
                    
                    #kutu içine alabilmek için minimum sınırları içerisine
                    #alması için gereken boyutu bilmemiz gerekiyor
                    #cv2.boxPoints fonksiyonu bu sınır kutularını yeniden şekillendirir.
                            
                    # rectengular olarak bu sınır  kutularını kayıt ediyoruz
                    # daha sonra önceden gördüğümüz dikdörtgen çizimini yapıyoruz
                    #yeşil renk içine alıyoruz
                    
                    #dikdörtgen çevresine alma
                    #rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
                    #cv2.drawContours(image, [rect], -1, (0, 255, 0), 2)
                    #cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
                    #bu tam tamalamıyor

                    #daha sonra takip ettiğimiz kareleri
                    #sınırları belirlenen(sonuç) olan resmi gösteririz
                    #istersek ilkini açmayıp sisteme gerksiz yüklenmeyiz
                    
                    #text koyma denemeleri
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    #float.merkez_yeni = (merkezx, merkezy)
                    #text_write = format("merkez noktasi =", merkez_yeni)
                    
                    text_writeX = str(mx)
                    text_writeY = str(my)
                    #sadece x eksenindeki koordinatı yazar
                    #str farklı veri tiplerini karakter dizisine çevirmek için
                
                    
                    cv2.putText(image, text_writeX, (100, 200), font, 1, (0, 255, 0),2)
                    cv2.putText(image, text_writeY, (100, 250), font, 1, (0, 255, 0),2)
                    #cv2.putText(image, ('merkezx, merkezy'), (100, 200), font, 1, (0, 255, 0),2)
                    #cv2.putText(image, (mx, my), (100, 200), font, 1, (0, 255, 0),2)
                    
                    
                    #servo uygulamaları denemeleri
                    #pixel = 640
                    #xdeg = mx
                    
                    #vol5.mapServoPosition (mx)
                    #print('sinyal kontrol track vol9 dc track sisteme giriş yapıyor')
                    #panvetilt.mapServoPosition (mx, my)
                    
                    #print('sinyal kontrol track vol9 dc')
                    #print(pwmgirdisi, 'pwmgirisinin trackvol9.py üzerinde gözükmesi bu gözküşse iş bitmiştir')
                    
                    
                    panvetiltv1.mapServoPosition (mx, my, aaa)
                    pwmout = panvetiltv1.pwmout (mx, aaa) 
            
                    int(pwmout)
        
                    dckontrol.pwmdckontrol (pwmgirdisi)
                    #olmadı şu en son yazdığım.pwmgirdisini dc nin altına yaz
                    
    ##                int(pwmgirdisi)
    ##                dckontrol.pwmdckontrol (pwmgirdisi)
    ##                print('sinyal kontrol track vol9 sinyal çıktı dc')
    ##                #burdan aynı loop içerisinde servolar haraket etsin
                    #herkez kendi işini yapıcak
                    #sıkıntı şu ki burdaki yenilenme hızını
                    #tekerlerede uydurmak lazım
                    #ikinci bir seçenek olarak tekerler bu loopdan ayrı çalışabilir
                    #ilk olarak ayrı çalışmayacağı şekilde tasarlayacağım
                    
                    
                    
                    #from panvetilt import apwm
                    #import panvetilt 
                    #dcdenvol1.mapdc (apwm)
                
        else:
               
                aaa = arama.cisimarama ()
                int(aaa)
                print('panAnglecıktısı', aaa)
                #if aaa > 450 :

            
                
        cv2.imshow("Tracking", image)
        #cv2.imshow("Binary", red)

                #cıhaz hızımıza göre kare alma hızımızı ayarlıyoruz
                #biz burada çoğu cihazda çalışabi,lecek olan 32 kare saniyede aldık
            
        at = int(1 // 64)
        time.sleep(at)

                #klavyeden 1 ya basınca dur
                #bu sadece görüntü işlemi için olan bunu koymayacağız sistem buradan birleşicek
               
                
        if cv2.waitKey(1) & 0xFF == ord("q"):
                break

# kamerayı ve pencereleri kapatmak iç
#birleştirince bu iki komutu en sona koyuycaz
#camera.release()
#cv2.destroyAllWindows()



