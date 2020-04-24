#!/usr/bin/env python
# coding: utf-8
#pip install python-can==1.4.3
from __future__ import print_function
import time
import os
import sys
import threading
import can
can.rc['interface'] = 'socketcan_ctypes'
from threading import Thread, Timer
from can.interfaces.interface import Bus
can_interface = 'can0'
#
global var
var=1
#
def dumpcan():
    global var
    for message in Bus(can_interface):
        if var==1:
            msg = unicode(message).encode('utf +8')
            canid = msg[26:29]
            msg = msg[45:69]
            if canid == ("464"):
#### Aktivate tv-tuner #############
                if msg == ("e0 01 00"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xa0, 0x01, 0x00], extended_id=False)
                    bus.send(msg)
                if msg == ("a1 01"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x10, 0x15, 0x01, 0x00, 0x02, 0x00, 0x00], extended_id=False)
                    bus.send(msg)
                if msg == ("b1"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x11, 0x01, 0x01], extended_id=False)
                    bus.send(msg)
                if msg == ("b2"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x12, 0x27, 0x02, 0x00], extended_id=False)
                    bus.send(msg)
                if msg == ("b3"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x92], extended_id=False)
                    bus.send(msg)
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x13, 0x09, 0x01, 0x42, 0x50, 0x02, 0x0B], extended_id=False)
                    bus.send(msg)
                if msg == ("b4"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x14, 0x23, 00], extended_id=False)
                    bus.send(msg)
                if msg == ("b5"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x15, 0x27, 0x02, 0x00], extended_id=False)
                    bus.send(msg)
                if msg == ("b6"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0x16, 0x51, 00], extended_id=False)
                    bus.send(msg)
                if msg == ("b7"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xA1, 0x01], extended_id=False)
                    bus.send(msg)
                if msg == ("a3 00"):
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xA1, 0x01], extended_id=False)
                    bus.send(msg)
#### Button Up #### 10 20 01 02 00
                if msg == ("10 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 02 00"): #Up 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Up #### 10 20 02 02 00
                if msg == ("10 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 02 00"): #Up 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 02 00"): #Up
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Down #### 20 01 20 00
                if msg == ("10 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 20 00"): #Down 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Down #### 20 02 20 00
                if msg == ("10 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 20 00"): #Down 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 20 00"): #Down
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Left #### 10 20 01 01 00
                if msg == ("10 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 01 00"): #Left 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Left #### 10 20 02 01 0
                if msg == ("10 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 01 00"): #Left 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 01 00"): #Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Right #### 20 01 03 00
                if msg == ("10 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 03 00"): #Right 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Right #### 10 20 02 03 00
                if msg == ("10 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 03 00"): #Right 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 03 00"): #Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button AS #### 10 20 01 04 00
                if msg == ("10 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 04 00"): #AS 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button AS #### 10 20 02 04 00
                if msg == ("10 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 04 00"): #AS 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 04 00"): #AS
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button  + #### 10 20 01 00 20
                if msg == ("10 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 20"): # + 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button  + #### 10 20 01 00 20
                if msg == ("10 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 20"): # + 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
################ Button  + #### 10 20 02 00 20
                if msg == ("10 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 00 20"): # + 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 00 20"): # +
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button  - #### 10 20 01 00 01
                if msg == ("10 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 01"): # - 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button  - #### 10 20 02 00 01
                if msg == ("10 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 00 01"): # - 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 00 01"): # -
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Mode #### 10 20 01 00 03
                if msg == ("10 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 03"): #Mode 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Mode #### 10 20 02 00 03
                if msg == ("10 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 00 03"): #Mode 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 00 03"): #Mode
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Return #### 10 20 01 00 50
                if msg == ("10 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 50"): #Return 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Button Return #### 10 20 02 00 50
                if msg == ("10 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 00 50"): #Return 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 00 50"): #Return
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Encoder Button Pressed #### 10 20 01 00 05
                if msg == ("10 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 00"): #Encoder Button Pressed 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Encoder Button Pressed #### 10 20 02 00 05
                if msg == ("10 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 00"): #Encoder Button Pressed 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 00 05"): #Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Right Encoder Rotation to Left #### 10 20 01 00 ff
                if msg == ("10 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 00 ff"): #Right Encoder Rotation to Left 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Right Encoder Rotation to Right #### 10 20 01 01 ff
                if msg == ("10 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 01 01 ff"): #Right Encoder Rotation to Right 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 01 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Right Encoder Rotation to Left #### 10 20 02 00 ff
                if msg == ("10 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 00 ff"): #Right Encoder Rotation to Left 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 00 ff"): #Right Encoder Rotation to Left
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Right Encoder Rotation to Right #### 10 20 02 01 ff
                if msg == ("10 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 20 02 01 ff"): #Right Encoder Rotation to Right 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 20 02 01 ff"): #Right Encoder Rotation to Right
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Left Encoder Button Pressed #### 15 00 01 ## ON
                if msg == ("10 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 00 01"): #Left Encoder Button Pressed 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 00 01"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
#### Left Encoder Button Pressed #### 15 00 02 ## OFF
                if msg == ("10 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB1], extended_id=False)
                    bus.send(msg)
                if msg == ("11 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB2], extended_id=False)
                    bus.send(msg)
                if msg == ("12 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB3], extended_id=False)
                    bus.send(msg)
                if msg == ("13 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB4], extended_id=False)
                    bus.send(msg)
                if msg == ("14 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB5], extended_id=False)
                    bus.send(msg)
                if msg == ("15 00 02"): #Left Encoder Button Pressed 
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB6], extended_id=False)
                    bus.send(msg)
                if msg == ("16 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB7], extended_id=False)
                    bus.send(msg)
                if msg == ("17 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB8], extended_id=False)
                    bus.send(msg)
                if msg == ("18 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB9], extended_id=False)
                    bus.send(msg)
                if msg == ("19 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBA], extended_id=False)
                    bus.send(msg)
                if msg == ("1a 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBB], extended_id=False)
                    bus.send(msg)
                if msg == ("1b 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBC], extended_id=False)
                    bus.send(msg)
                if msg == ("1c 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBD], extended_id=False)
                    bus.send(msg)
                if msg == ("1d 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBE], extended_id=False)
                    bus.send(msg)
                if msg == ("1e 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xBF], extended_id=False)
                    bus.send(msg)
                if msg == ("1f 00 02"): #Left Encoder Button Pressed
                    bus = can.interface.Bus()
                    msg = can.Message(arbitration_id=0x264, data=[0xB0], extended_id=False)
                    bus.send(msg)
            if canid == ("35e"): #POWER OFF
                if msg == ("00 01 12 a0"):  #radio
                    os.system("sudo shutdown -h now")
                if msg == ("00 01 12 38"): # cd-changer
                    os.system("sudo shutdown -h now")
                if msg == ("00 01 12 2c"): #tvtuner
                    os.system("sudo shutdown -h now")
             if canid == ("218"): #key disable
                if msg == ("1e 01 02"):
                    os.system("sudo shutdown -h now")
dumpcan()
