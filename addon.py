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

global var
var=1			# At closing, var0
#
def dumpcan(): # Can berichten scannen + omzetten naar kodi / python acties
	global var
	select=0
	press=0
	retrn=0
	menu=0
	windowid=0
	left=0
	right=0
	up=0
	down=0
	for message in Bus(can_interface):
		if var==1:
			msg = unicode(message).encode('utf-8')
			canid = msg[26:29]
			msg = msg[45:99]
			if canid == ("464"): # Canid 464 is used for the use of RNS-D buttons.
#If by pressing one button (example up), the code can be changed:
# can0 464 15 20 02 02 00
# can0 464 16 20 02 02 00
# can0 464 17 20 02 02 00
#it is necessary in the lines if msg == ("15 20 02 02 00"):
#it is necessary to bring the lines to this form if msg[2:] == (" 20 02 02 00"):

#### Left Side ####
				if msg[2:] == (" 20 02 02 00"): #Up 
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg[2:] == (" 20 02 20 00"): #Down
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
				if msg[2:] == (" 20 02 01 00"): #Left
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Left","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Left","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Left","id":1}')
				if msg[2:] == (" 20 02 03 00"): #Right
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Right","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Right","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Right","id":1}')
				if msg[2:] == (" 20 02 04 00"): #OK (Key "AS")
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
#### Right Side #### 
				if msg[2:] == (" 20 02 00 50"): #Return
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Back","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Back","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Back","id":1}')
				if msg[2:] == (" 20 02 00 03"): #Context menu(Mode)
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Stop","params":{"playerid":0},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Stop","params":{"playerid":1},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ContextMenu","id":1}')
				if msg[2:] == (" 20 02 00 05"): #OSD Menu  (Key "encoder push")
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ShowOSD","id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ShowOSD","id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Select","id":1}')
				if msg[2:] == (" 20 02 00 20"): #Up (Key "-")
					windowid = xbmcgui.getCurrentWindowId()
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":0,"value":"bigforward"},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":1,"value":"bigforward"},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Up","id":1}')
				if msg[2:] == (" 20 02 00 01"): #Down (key "+")
					if (windowid == 12006): # MusicVisualisation.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":0,"value":"bigbackward"},"id":1}')
					elif (windowid == 12005): # VideoFullScreen.xml
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Player.Seek","params":{"playerid":1,"value":"bigbackward"},"id":1}')
					else:
						xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
# CALL BELOW (TO BE PERFORMED AT THE SAME TIME)
# __________________________________________
dumpcan()
