from machine import Pin
import network
import usocket
import utime
import picoweb
import ulogging
import ujson

import gc
gc.collect()

ssid = 'Modena_100FX'
password = 'fxbio_L0r&nz0'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
station.ifconfig(('192.168.1.193', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

eLock=Pin(27,Pin.OUT,value=0)
rack1=Pin(25,Pin.IN)
rack2=Pin(26,Pin.IN)
rack3=Pin(32,Pin.IN)
rack4=Pin(33,Pin.IN)

racks=[rack1,rack2,rack3,rack4]