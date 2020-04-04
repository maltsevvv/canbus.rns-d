import os
#os.system("sudo ip link set can0 up type can bitrate 100000 restart-ms 100 loopback on") (FOR TESTING ONLY)
os.system("ip link set can0 up type can bitrate 100000 restart-ms 100")
