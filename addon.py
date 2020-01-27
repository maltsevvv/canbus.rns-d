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
			msg = msg[48:99]
			if canid == ("464"):
				if msg == ("20 02 02 00"): #Button Up - KODI Up 
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg == ("20 02 20 00"): #Button Down - KODI Down
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
				if msg == ("20 02 01 00"): #Button Left - KODI Left
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Left","id":1}')
				if msg == ("20 02 03 00"): #Button Right - KODI Right
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Right","id":1}')
				if msg == ("20 02 04 00"): #Button AS - KODI OK
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
 				if msg == ("20 02 00 50"): #Button Return - KODI Back
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Back","id":1}')
				if msg == ("20 02 00 05"): #Encoder Button Pressed - KODI OK
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
				if msg == ("20 01 00 ff"): #Right Encoder Rotation to Left - KODI UP
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg == ("20 01 01 ff"): #Right Encoder Rotation to Left - KODI Down
					xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
				if msg == ("20 02 00 20"): #Button - Kodi Up
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":0,"value":"bigforward"},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":1,"value":"bigforward"},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg == ("20 02 00 01"): #Button + KODI - 
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":0,"value":"bigbackward"},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":1,"value":"bigbackward"},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
				if msg == ("20 02 00 03"): #Button Mode - KODI Context menu
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ShowOSD","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ShowOSD","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ContextMenu","id":1}')
				if msg == ("00 02"): #Stop Player if power OFF
                                        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Stop","params":{"playerid":1},"id":1}')
dumpcan()
