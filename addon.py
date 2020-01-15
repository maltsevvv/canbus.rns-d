#!/usr/bin/env python
#
from __future__ import print_function
import xbmc
import xbmcgui
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
	windowid=0
	for message in Bus(can_interface):
		if var==1:
			msg = unicode(message).encode('utf-8')
			canid = msg[26:29]
			msg = msg[45:99]
			if canid == ("464"):
#
				if msg[3:] == ("20 02 02 00"): #Up 
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg[3:] == ("20 02 20 00"): #Down
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
				if msg[3:] == ("20 02 01 00"): #Left
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Left","id":1}')
				if msg[3:] == ("20 02 03 00"): #Right
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Right","id":1}')
				if msg[3:] == ("20 02 04 00"): #OK (Key "AS")
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
#### Right Side 
				if msg[3:] == ("20 02 00 20"): #Up (Key "-")
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":0,"value":"bigforward"},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":1,"value":"bigforward"},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg[3:] == ("20 02 00 01"): #Down (key "+")
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":0,"value":"bigbackward"},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":1,"value":"bigbackward"},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
				if msg[3:] == ("20 02 00 50"): #Return
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Back","id":1}')
				if msg[3:] == ("20 02 00 03"): #Context menu(Mode)
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Stop","params":{"playerid":0},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Stop","params":{"playerid":1},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ContextMenu","id":1}')
				if msg[3:] == ("20 02 00 05"): #OSD Menu  (Key "encoder push")
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ShowOSD","id":1}')
				if msg[3:] == ("20 01 00 ff"): #Encoder Up
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg[3:] == ("20 01 01 ff"): #Down
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
#
dumpcan()
