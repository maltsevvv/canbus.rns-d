#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import can
def send_one():
    bus = can.interface.Bus()
    msg = can.Message(arbitration_id=0x464, data=[0xa3, 0x00], extended_id=False)
    bus.send(msg)
send_one()
