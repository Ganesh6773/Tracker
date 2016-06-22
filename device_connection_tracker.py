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
        self.devType                =   utils.TYPE_REFERENCE_DEVICE
        self.firstConnectionTime    =   None
        self.hostId                 =   utils.getHostId()
    def firstConnectionHandler(self):
        ''' device connected first time since pc boot'''
        self.logger.debug("FirstTimeConnection handler called")
        self.lastConnectedDeviceId  =  self.currentConnectedDeviceId 
       
        
        #add db entry for device connection
        db.addDevConnectedEntry(utils.TYPE_REFERENCE_DEVICE, utils.CONNECTED,self.currentConnectedDeviceId, self.firstConnectionTime)

    def addDeviceDisconnectedEntry(self):
        ''' this is wrapper, calls db.addDevConnectedEntry() with approproate parameters '''
        self.logger.log("Addind db entry from device connected from host@"+str(host))
        db.addDevConnectedEntry(self.devType, devStatus=utils.CONNECTED, self.currentConnectedDeviceId, self.firstConnectionTime, self.hostId)
        
    def updateDeviceConnectedEntry(self):
        ''' this is wrapper, calls db.updateDevConnectedEntry() with approproate parameters '''
        
        
        
    def checkAndUpdate(self, dType=utils.TYPE_REFERENCE_DEVICE):
        '''  This function will keep checking the device state, and if changed for it will call db thread to update
        accordingly'''
        
        #initialize state
        self.firstConnectionTime =   -1   # the time when the ID dev connected first
        self.lastSeenTime        =   -1   # the last time, dev seen without waiting for maxTimeToChangeStatus 
        
        self.lastDeviceState     =   utils.DISCONNECTED
        self.currentDeviceState  =   utils.DISCONNECTED
        
        self.timeSinceDisconnected    =   0
        
        self.lastConnectedDeviceId      =   utils.getConnectedDeviceId(dType);
        self.currentConnectedDeviceId   =   utils.getConnectedDeviceId(dType);
        
        
        #This flag is to set whe
        addedDbEntryFlag                =   False
        #always running loop after every utils.getMaxWaitBetweenDeviceConnectionCheck()
        while(True):
                        
            time.sleep(utils.getMaxWaitBetweenDeviceConnectionCheck())
            self.currentDeviceState              =   utils.getDeviceConnectioState(dType);
            
            #if no device connected since boot
            if((self.lastConnectedDeviceId    ==  None) and (currentDeviceState == utils.DISCONNECTED)):
                self.logger.debug("No Device connected since PC Boot or last device disconnected")
                continue
            
            self.currentConnectedDeviceId   =   utils.getConnectedDeviceId()
            
            if(self.currentDeviceState  ==  utils.CONNECTED ):
                #self.logger.debug("Some Device is found Connected " + str(self.currentConnectedDeviceId))
                
                if(self.lastConnectedDeviceId   ==   self.currentConnectedDeviceId):
                    self.logger.info("Same device is still connected" + str(self.currentConnectedDeviceId))
                    #do reinitialization
                    
                    self.lastConnectedDeviceId  =   self.currentConnectedDeviceId
                    self.timeSinceDisconnected  =   0
                    self.lastSeenTime           =   utils.getTime()
                    continue
                #lastdevId != currentConnectedDeviceId    
                else:
                    self.logger.debug("Last Connected Device is not the same as current one: in else" )
                    
                    self.firstConnectionTime    =   utils.getMeanTime(utils.getTime(), utils.getTime() - utils.getMaxWaitBetweenDeviceConnectionCheck())
                    self.lastSeenTime   =   self.lastSeenTime   +   self.firstConnectionTime
                    
                    self.logger.debug("Updating old device disconnection entry");
                    self.updateDeviceDisconnectedEntry()
                    self.logger.debug("Adding new connection device connection entry");
                    self.addDeviceConnectedEntry()
            #last device id is not in none
            else:
                self.logger.debug("No device connected block")
                
                if(self.timeSinceDisconnected >= utils.getMaxTimeToChangeStatus()):
                    self.logger.info("Device disconnected for long time than allowed, marking as disconnected");
                    
                    self.updateDeviceConnectedEntry();
                    
                    self.lastConnectedDeviceId      =   None
                    self.timeSinceDisconnected      =   0
                    self.currentConnectedDeviceId   =   None
                    self.lastSeenTime               =   -1
                    self.firstConnectionTime        =   -1
                    self.lastDeviceState            =   utils.DISCONNECTED
                    
                else:
                    
                    self.timeSinceDisconnected   +=  utils.getMaxWaitBetweenDeviceConnectionCheck()
                    self.logger.debug("Device disconnected since " + str(self.timeSinceDisconnected) )
                    
                                    
            
                    
                        
                        
                    
                    
                
         
           
                
                    
                                                    
                 
                           

            
        
    