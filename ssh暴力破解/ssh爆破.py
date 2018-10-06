#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import threading
from nmap import nmap

nmScan=nmap.PortScanner()
def scan(tgtport):
    nmScan.scan(tgthost, str(tgtport))
    state = nmScan[tgthost]['tcp'][tgtport]['state']
    print('port: %d state: %s' % (tgtport, state))

tgthost=input('host: ')
tgtports=range(8200,8400)


print('start scan')

for tgtport in tgtports:
    thread=threading.Thread(target=scan,args=(tgtport,))
    thread.start()






