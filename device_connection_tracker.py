# ------------------------------------------
#	This tread will track connection disconnection of devices.
#-------------------------------------------


import utils
import my_logger
import threading
import my_logger
import db

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
        lastSeenTime        =   0   # the last time, dev seen without waiting for maxTimeToChangeStatus 
        
        lastDeviceState     =   utils.DISCONNECTED
        currentDeviceState  =   utils.DISCONNECTED
        
        timeSinceDisconnected    =   0
        
        self.lastConnectedDeviceId      =   utils.getConnectedDeviceId();
        self.currentConnectedDeviceId   =   utils.getConnectedDeviceId();
        
        #always running loop
        while(True):
                        
            currentDeviceState              =   utils.getDeviceConnectioState();
            self.currentConnectedDeviceId   =   utils.getConnectedDeviceId();
            
            self.logger.debug("currentDeviceState = " + str(currentDeviceState) + "Device Id : " + str(self.currentConnectedDeviceId))
            
            #if different device connected
            if(self.currentConnectedDeviceId    !=  self.lastConnectedDeviceId):
                #found new device adding rec to db
                
            
            #device state changer from previous state    
            if( ( currentDeviceState   != lastDeviceState ) and ( currentDeviceState == utils.DISCONNECTED )):
                
                if(timeDisconnected <=  utils.getMaxTimeToChangeStatus()):
                    timeDisconnected    =   timeDisconnected +  utils.getMaxWaitBetweenDeviceConnectionCheck();
                    self.logger.debug("Device ID : " + str(self.lastConnectedDeviceId) +   "Total time disconnected " + str(timeDisconnected))
                else:
                    
                    #if max disconnected time elapsed, 
                    #the call to db entry, and re-initilize raw parameters
                    
                    self.logger.debug("Max waiting time to re-connecte device is elapsed, adding rec to db as device disconnected");
                    self.logger.debug("Device TYpe : " | str(dType))
                    result=db.addStatusChangeDBEntry(dType, utils.DISCONNECTED  , self.lastConnectedDeviceId, firstConnectionTime, lastSeenTime);
                    
                    if(result):
                        
                        self.logger.debug("Successfully added entry into db");
                    else:
                        self.logger.warning("Failed to make disconnected device entry into db. Result : " + result )
            else:
                
                #if( self.lastConnectedDeviceId  != self.currentConnectedDeviceId):
                    
                                                                                    
                                           
                           
                    
                
                
                            
                
            
            
            
            
        
    