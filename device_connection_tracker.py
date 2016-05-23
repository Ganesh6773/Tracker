# ------------------------------------------
#	This tread will track connection disconnection of devices.
#-------------------------------------------

import threading
import time

import utils
import my_logger
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
        firstConnectionTime =   -1   # the time when the ID dev connected first
        lastSeenTime        =   -1   # the last time, dev seen without waiting for maxTimeToChangeStatus 
        
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
            #will loop until first device connection not found
            if((currentDeviceState   ==  utils.DISCONNECTED) and (firstConnectionTime == -1) ):
                self.logger.debug("No Device connected yet, will check again after " + str(utils.getMaxWaitBetweenDeviceConnectionCheck()) + "seconds")
                time.sleep(utils.getMaxWaitBetweenDeviceConnectionCheck)
                continue;
                
            self.currentConnectedDeviceId   =   utils.getConnectedDeviceId();
            
            if(lastSeenTime == -1):
                self.logger.debug("First Connection of device, setting last seen time to current : " + str(currentTime) + "Device Id " + str(self.currentConnectedDeviceId));
                #means first iteration
                lastSeenTime            =   utils.getTime()
                firstConnectionTime     =   lastSeenTime
                timeSinceDisconnected   =   0
                self.logger.debug("First Device Connection since pc boot")
                   
            self.logger.debug("currentDeviceState = " + str(currentDeviceState) + "Device Id : " + str(self.currentConnectedDeviceId))
            
            
            #device state changed from previous state   to disconnected  
            if(lastDeviceState != currentDeviceState):
                #disconnected --> connected
                if(currentDeviceState   == utils.CONNECTED):
                    self.logger.debug("Device state changed from disconnected to connected")
                    
                    #if same device is connected back
                    if( self.lastConnectedDeviceId   == self.currentConnectedDeviceId ):
                        lastSeenTime    =   utils.getTime()
                        timeSinceDisconnected   =   0
                        
                        
                    #got different device connected
                    elif(self.lastConnectedDeviceId != self.currentConnectedDeviceId ):
                        self.logger.debug("Different device connected, previous : " + str(self.lastConnectedDeviceId) + "current " + str(self.currentConnectedDeviceId))
                        lastSeenTime    = utils.getMeanTime(utils.getTime() , utils.getTime() - utils.getMaxWaitBetweenDeviceConnectionCheck())
                        
                        dbOpResult  =   db.addSDevDisconnectedDBEntry(utils.TYPE_REFERENCE_DEVICE, utils.DISCONNECTED, self.lastConnectedDeviceId, firstConTime, lastSeenTime)
                        
                        if(dbOpResult):
                            self.logger.error("Added Disconnected Entry for dev : " + str(self.lastConnectedDeviceId) + "Successfully")
                        else:
                            self.logger.error("Failed to add Device Disconnected Entry into db  for device Id : " + str(self.lastConnectedDeviceId) )
                        #if end
                        
                        lastSeenTime    =   lastSeenTime +=2 ;
                        self.lastConnectedDeviceId   =   self.currentConnectedDeviceId
                        timeSinceDisconnected   =   0
                        firstConnectionTime     =   lastSeenTime
                       
                        self.lastConnectedDeviceId      =   self.currentConnectedDeviceId
                    #if end
                
                # connected ---> Disconnected    
                elif (currentDeviceState    ==  utils.DISCONNECTED):
                    self.logger.debug("Device State Changed from Connected To Disconnected");
                    
                    #since it was previously connected and now disconnected, we are setting timeout for waiting reconnection to 0
                    lastDeviceState         =   utils.DISCONNECTED
                    probableDisconnectTime  =   utils.getMeanTime() -2
                    timeSinceDisconnected   =   utils.diffBetTime(utils.getTime() - probableDisconnectTime )
                    lastSeenTime            =   probableDisconnectTime
                    
                    self.logger.debug("Time Since Disconnect set to " + str(timeSinceDisconnected) + " and last seen time " + str(lastSeenTime));
                #elif end
            #if end
            #state remains same as previous iteration
            elif(currentDeviceState ==  lastDeviceState):
                
                # if previous and current state is connected
                if(currentDeviceState   ==  utils.CONNECTED):
                    self.logger.debug("device state remains same, as CONNECTED")
                    
                    lastSeenTime            =   utils.getTime();
                    timeSinceDisconnected   =   0
                    
            
            #elif end
                
            
         
         
           
                
                    
                                                    
                 
                           

            
        
    