#用于在不中断电路的情况下，改变电路中电阻的装置。
#实验：PCF8591用于读取电位计的模拟值，并将值输出到LED。
import pcf8591 as ADC
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)

def loop(): 
    status = 1
    while True:
        value = ADC.read(0)
        print('Value:', value)
        ADC.write(value)
        time.sleep(0.2)

if __name__ == '__main__':
    try:    
        setup() 
        loop()  
    except KeyboardInterrupt: 
        pass    
