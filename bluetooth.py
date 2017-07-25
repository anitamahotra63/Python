import time
import serial
port=serial.Serial("/dev/ttyAMA0",9600,timeout=3.0)

def abc():
	
	port.flushInput()
	port.flushOutput()
			
	time.sleep(2)
	rcv=port.read(8)
			
	if rcv:
		print "received string from 8051: "+ rcv
	        time.sleep(2)
		temp=rcv[0]+rcv[1]
	        humidity=rcv[2]+rcv[3]
	        if rcv[4]=='Y':
	        	soil="Moist soil"
	        else:
	        	soil="Dry soil"
	        if rcv[5]=="Y":
	        	light="Bright light condition"
	        else:
	        	light="Dim light condition"
	        distance=rcv[6]+rcv[7]
	        print temp
	        print humidity
	        print soil
	        print light
	        print distance
	        
	        
	else:
		print "not recieving"
	 
	return temp,humidity,soil,light,distance

abc()