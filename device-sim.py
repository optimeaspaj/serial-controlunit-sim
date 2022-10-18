#!/usr/bin/env python3
import serial
import time

COM_PORT = '/dev/ttymxc2'

def getData():
    data = f'data:{time.time()}'
    return data.encode()

def main():
    com = serial.Serial(COM_PORT,baudrate=9600)
    
    while(True):
        character = com.read(1)
        if character == b'h':
            for i in range(5):
                com.write(getData())
                time.sleep(2)
            com.flush()
            com.read_all()        

if __name__ == '__main__':
    main()