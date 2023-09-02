#!/bin/bash

sudo mount -t cifs -o user=yann,password="PWD",rw,file_mode=0777,dir_mode=0777 //192.168.2.200/homes/Yann /mnt/nas
#nohup python /home/pi/mqtt.py >/dev/null 2>&1 &
