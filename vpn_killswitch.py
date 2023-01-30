import os
import netifaces

iface = "{AC7E5E45-4129-442F-AFD1-4CE0642707CB}" # interface of the VPN

if 2 in netifaces.ifaddresses(iface).keys():
	print "[+] VPN Connected."
else:
	print "[-] VPN Disconnected."
	print "[!] Disconnecting internet..."
	os.system('wmic path win32_networkadapter where index=2 call disable')
	