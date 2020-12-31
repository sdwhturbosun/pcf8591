import pcf8591 as ADC  
import time
#摇杆                          pcf8591
#X------------------------------AIN0----read(0)
#Y------------------------------AIN1----read(1)
#B------------------------------AIN2----read(2)
#实验的时候大家一边摆动摇杆，一边观察输出数据，想一想如何判断是左拉、又拉、上啦、下拉还是按下了
def setup():
    ADC.setup(0x48)                    # Setup PCF8591 
    global state  #全局变量，函数内外都可以用

def direction():    #根据数据输出摇杆摆动方向
    state = ['home', 'left', 'right', 'up', 'down', 'pressed']
    i = 0   

    if ADC.read(0) < 40:
        i = 1        #left
    if ADC.read(0) > 200: 
        i = 2        #right

    if ADC.read(1) < 20: 
        i = 3        #up
    if ADC.read(1) >235:
        i = 4        #down

    if ADC.read(2) == 255:
        i = 5        # Button pressed 

    else:
        i = 0
    
    return state[i]

def loop(): #不断检测摆动数据
    status = ''
    while True:
            print(ADC.read(0), ADC.read(1), ADC.read(2))#输出数据
            time.sleep(0.1)#等待0.1秒再读取下一次数据


if __name__ == '__main__':        # Program start from here
    setup() 

    loop()

