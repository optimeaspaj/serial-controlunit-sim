#!/usr/bin/env python3
import serial
import time

COM_PORT = '/dev/ttymxc2'
SEND_AMOUNT = 5
SEND_INTERVAL = 2
COMMAND_STRING = b'h'
BAUDRATE = 9600

def getData():
    data = f'data:{time.time()}'
    return data.encode()

def main():
    com = serial.Serial(COM_PORT,baudrate=BAUDRATE)
    
    while(True):
        character = com.read(1)
        if character == COMMAND_STRING:
            for i in range(SEND_AMOUNT):
                com.write(getData())
                time.sleep(SEND_INTERVAL)
            com.flush()
            com.read_all()        

if __name__ == '__main__':
    main()