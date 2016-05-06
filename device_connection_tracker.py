# ------------------------------------------
#	This tread will track connection disconnection of devices.
#-------------------------------------------


import utils
import my_logger
import threading
import my_logger
import db_ops as db

connection_status_array
class DeviceTracker:
    ''' will check the device state every afer few secods'''
    
    
    def __init__(self):
                
        #self.lastConnectionSatus       =   utils.DISCONNECTED
        self.lastConnectedDeviceId      =   None;
        self.currentConnectedDeviceId   =   None;
        #self.lastCheckTime          =   None;
        self.logger                 =   my_logger.getLogger();        
        
    def checkAndUpdate(self, dType=utils.TYPE_REFERENCE_DEVICE):
        '''  This function will keep checking the device state, and if changed for it will call db thread to update
        accordingly'''
        
        #initialize state
        firstConnectionTime =   0   # the time when the ID dev connected first
        lastSeenTime        =   utils.getTime()   # the last time, dev seen without waiting for maxTimeToChangeStatus 
        
        lastDeviceState     =   utils.DISCONNECTED
        currentDeviceState  =   utils.DISCONNECTED
        
        timeSinceDisconnected    =   0
        
        self.lastConnectedDeviceId      =   utils.getConnectedDeviceId(dType);
        self.currentConnectedDeviceId   =   utils.getConnectedDeviceId(dType);
        
        #This flag is to set whe
        addedDbEntryFlag                =   False
        #always running loop after every utils.getMaxWaitBetweenDeviceConnectionCheck()
        while(True):
                        
            currentDeviceState              =   utils.getDeviceConnectioState(dType);
            self.currentConnectedDeviceId   =   utils.getConnectedDeviceId();
            currentTime                     =   utils.getTime();
            
            self.logger.debug("currentDeviceState = " + str(currentDeviceState) + "Device Id : " + str(self.currentConnectedDeviceId))
            
            
            #device state changed from previous state   to disconnected  
            if( ( currentDeviceState   != lastDeviceState ) and ( currentDeviceState == utils.DISCONNECTED )):
                
                self.logger.debug("Device state changed to Disconnect")
                if(lastSeenTime ==  0):
                    lastSeenTime                =   utils.getTime() - utils.getMaxWaitBetweenDeviceConnectionCheck()
                    
                timeSinceDisconnected       =   timeSinceDisconnected + utils.getMaxWaitBetweenDeviceConnectionCheck();
                   
                if(timeSinceDisconnected    <=  utils.getMaxTimeToChangeStatus()):
                    timeSinceDisconnected    =   timeSinceDisconnected +  utils.getMaxWaitBetweenDeviceConnectionCheck();
                    self.logger.debug("Device ID : " + str(self.lastConnectedDeviceId) +   "Total time disconnected " + str(timeSinceDisconnected))
                
                #Device disconnected for long time and need to record into db    
                else:
                    db.addSDevDisconnectedDBEntry(dType, devStatus=utils.DISCONNECTED, firstConTime=firstConnectionTime , disConTime lastSeenTime)
                    
            #disconnected device connected        
            elif ( ( currentDeviceState   != lastDeviceState ) and ( currentDeviceState == utils.CONNECTED )):
                
                
                #if different device connected and currentConnectedDeviceId not equal to DISCONNECTED 
                if((self.currentConnectedDeviceId    !=  self.lastConnectedDeviceId) and ( self.currentConnectedDeviceId != utils.DISCONNECTED) ):
                    #found new device adding rec to db
                    disconnectedProbaleTime =  currentTime  -  int(utils.getMaxWaitBetweenDeviceConnectionCheck() / 2)  
                    if(db.addDevConnectedEntry(dType, utils.CONNECTED,disconnectedProbaleTime ) == True ):
                        #db entry successfull
                        self.logger.debug("Added new device connection entry to db " + str(currentConnectedDeviceId) + " , connection Time  " + str( disconnectedProbaleTime))
                        
                        self.lastConnectedDeviceId  =   self.currentConnectedDeviceId
                       
                        firstConnectionTime         =   disconnectedProbaleTime + 2 
                        
                        currentDeviceState          =   utils.CONNECTED
                        lastDeviceState             =   utils.CONNECTED
                
                #if same device is connected
                else:
                    #check if disconnected time is big enough to consider a separate entry.
                    
                    
               
                        
                        
                    
                                                                                    
                                           
                           
                    
                
                
                            
                
            
            
            
            
        
    