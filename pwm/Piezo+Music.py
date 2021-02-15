from machine import Pin, PWM
import utime
import time

tempo = 5
tones = {
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
}
beeper = PWM(Pin(0)) #, freq=440, duty=512)
sensor_1 = machine.ADC(26)
sensor_2 = machine.ADC(27)
sensor_3 = machine.ADC(28)

while True:
    reading_1 = sensor_1.read_u16()
    reading_2 = sensor_2.read_u16()
    reading_3 = sensor_3.read_u16() 
   
    beeper.freq(1000)
       
    if reading_1 > 10000:
        beeper.freq(tones['C7'])
        #tempDuty=int((1/tones['a'])/2)
        #print(tempDuty)
        beeper.duty_u16(6000)
        time.sleep(0.25)
        #print(reading_1)
        #print("C7")
        reading_2 = 0
        reading_3 = 0
        
    if reading_2 > 10000:
        beeper.freq(tones['D7'])
        #tempDuty=int((1/tones['b'])/2)
        beeper.duty_u16(6000)
        time.sleep(0.25)
        #print(reading_2)
        #print("D7")
        reading_1 = 0
        reading_3 = 0
        
    if reading_3 > 10000:
        beeper.freq(tones['E7'])
        #tempDuty=int((1/tones['c'])/2)
        beeper.duty_u16(6000)
        time.sleep(0.25)
        #print(reading_3)
        #print("E7")
        reading_1 = 0
        reading_2 = 0
        
    beeper.duty_u16(0)
    beeper.deinit()  
    time.sleep(0.025)
    
