
import utils
import my_logger
import constants
#-----------------
#   this class will hold data of device connection and provide 
#   utility to get all info about connection and disconnection
#---------------------------

class StatusHolder:
    
    def __init__(self):
        
        self.connectedDevId=[] ;
        #This list will content the adb devices, id 
        
        self.connectionStatus=[];
        #This list will content equilvalen status as connection time.
        
        self.connectedTime=[]
        #This is the time bet last connection ans previous one
        
        self.count  =   -1;
        self.prevTime = 0;
        
        self.logger =   my_logger.getLooger(__name__);
        
        self.lastConnectedDeviceId  =   None     
    #--------------------------------
    #   time in seonds from epoch, tie.time()
    #   status as connected or disconnected
    #-----------------------------------
    def setConnected(deviceId, time , status): 
        
        #if new device connected, add it into list
        
        if ( lastConnectedDeviceId is not deviceId ):
            logger.debug("New Device %s Connected %s " , deviceId , time )
            
            count+=1;
            connectedDevId.insert(count, deviceId);
            connectionStatus.insert(count, status);
            connectedTime.insert(count, time)
            lastConnectedDeviceId   =   deviceId;
            prevTime                =   time;
         
            return True;
        
        # if connected device is same as last
        if( lastConnectedDeviceId == deviceId ):
            
                
        
        
        
            
    
    #--------------------------------
    #   time in seonds from epoch, tie.time()
    #   status as connected or disconnected
    #-----------------------------------
    
    
                 
        
'''
count+=1;
        connectedDevId.insert(count, deviceId);
        connectionStatus.insert(count, status)
           
        timeBetweenConnection.insert(count, time - prevTime );
        logger.debug("device connecte, time between connection = %s ", time - prevTime )
        logger.info("Device connected : %s , %s,  %s ", deviceId, time, status )
        
'''