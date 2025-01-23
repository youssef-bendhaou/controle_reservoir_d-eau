from machine import Pin
import time

relayOUT = Pin(16, Pin.OUT)
relayIN = Pin(12, Pin.OUT)
trig = Pin(32, Pin.OUT)
echo = Pin(33, Pin.IN)
T_on = Toff = t = distance = 0
while 1:
    trig.on()
    time.sleep_us(10)
    trig.off()
    time.sleep_us(2)
    while echo.value() == 0:
        Toff = time.ticks_us()
    while echo.value() == 1:
        T_on = time.ticks_us()

    t = (T_on - Toff) / 2
    distance = t * 0.034
    water = 400 - distance
    if 100 < water < 300:
        print(water)
        print("moyenne")
        relayIN.on()
        relayOUT.on()
    elif water > 300:
        print(water)
        print("niveau haut")
        relayOUT.on()
        relayIN.off()
    else:
        print(water)
        print("niveau insuffisant")
        relayIN.on()
        relayOUT.off()

    time.sleep_ms(20)
