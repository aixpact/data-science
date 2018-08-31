#!/usr/bin/env python

# add PATH to environment
# scapy in /usr/local/lib/python3.6/site-packages (2.4.0)
import sys, os
# print(os.sys.path) 
os.sys.path.append('/usr/local/lib/python3.6/site-packages')

from scapy.all import *

set =()

def packetHandler(pkt):
    if pkt.haslayer (Dot11) :
        if pkt.type == 0 and pkt.subtype == 8 :
            print("Available SSID: {} wlan: {}".format(pkt.info, pkt.addr2))
            
def packetHandler2(pkt):
    if pkt.haslayer(Dot11):
        dot11_layer = pkt.getlayer(Dot11)
        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
            devices.add(dot11_layer)
            print("Available SSID: {} wlan: {}".format(pkt.info, pkt.addr2))

def pktIdentifier(pkt):
    if pkt.haslayer(Dot11Beacon):
        print("[+] Detected 802.11 Beacon Frame")
    elif pkt.haslayer(Dot11ProbeReq):
        print("[+] Detected 802.11 Probe Frame")

def wifiPrint(pkt):
    if pkt.haslayer(Dot11):
        wifiMAC = pkt.getlayer(Dot11).addr2
        print(wifiMAC)
    
conf.iface = 'en0'
sniff(prn=wifiPrint)
            
# sniff(iface='en0', prn=pktIdentifier)


# chmod a+x sniff.py
# sudo ./sniff.py
