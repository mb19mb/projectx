#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time
import threading
import random

class Relais(threading.Thread):
    pin1 = 17
    pin2 = 22
    delay = 5
    isConnectedThrough = False
    hasError = False
    type = "open"

    def __init__(self, pin1, pin2, lock, type = "open", delay = 2):
        print lock
        self.lock = lock
        threading.Thread.__init__(self)
        self.type = type

        if pin1 is None or pin2 is None:
            raise Exception('Pin required')

        self.pin1 = pin1
        self.pin2 = pin2
        self.delay = delay
        self.initGPIO()

    def initGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.output(self.pin1, False)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.output(self.pin2, False)

    def run(self):
        print "Starte %s" % self.name
        #if (self.i * random.randint(0,100))  % 2 == 1:
        if self.type == "open":
            self.switch(self.pin1)
        else:
            self.switch(self.pin2)

        print "     Beende %s" % self.name

    def switch(self, p):
        try:
            self.lock.acquire()
            #self.stopAll()

            GPIO.output(self.pin1, False) # stop all
            GPIO.output(self.pin2, False) # stop all

            GPIO.output(p, True)  # connect through
            time.sleep(self.delay)  # wait n seconds
            GPIO.output(p, False)  # stop circuit connection
            self.lock.release()
        except KeyboardInterrupt:
            raise
        except:
            GPIO.output(p, False)

        GPIO.output(p, False)


    def stopAll(self):
        try:
            # stop circuit connection
            GPIO.output(self.pin1, False)
            GPIO.output(self.pin2, False)
            #time.sleep(self.delay/100)
        except:
            import sys
            sys.exit(1)

if __name__ == '__main__':

    import sys

    print 'Argument List:', str(sys.argv)
    if len(sys.argv) < 2:
        print "cmd line arguments missed"
        sys.exit(1)

    arg1 = sys.argv[1]

    lock = threading.Lock()

    r = Relais(17, 22, lock, arg1)
    r.start()
    """
    l =[]
    for i in range(1,11):
        l.append(Relais(17, 22, lock,  i))

    for r in l:
        r.start()
    """