def main(port1,port2):
    try:
        portA = serial.Serial(port1,timeout=1)
        portB = serial.Serial(port2,timeout=1)
    except serial.serialutil.SerialException as e:
        print e
        return
        
    print "Connected to {0} and {1}.".format(portA.portstr,portB.portstr)
    
    while(1):
        try:
            xA = portA.readlines()
            if xA != []:
                portB.writelines(xA)
            xB = portB.readlines()
            if xB != []:
                portA.writelines(xB)
        except:
            break
            
    portA.close()
    portB.close()
        
if __name__ == "__main__":
    import serial,sys
    try:
        portA = int(sys.argv[1])
        portB = int(sys.argv[2])
    except ValueError:
        portA = sys.argv[1]
        portB = sys.argv[2]
    except IndexError:
        print "Arguments missing. Requires two COM ports to connect to."
        sys.exit()
    
    main(portA, portB)