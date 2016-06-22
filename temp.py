from utils import *
import my_logger
import tracker_daemon

#tracker_daemon.init();


logger = my_logger.getLogger(__name__ )

time    =   12343232323.90
deviceId = "sd102900lop"

logger.debug("New Device %s Connected %s " , deviceId , time )




''' #will loop until first device connection not found
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
                
            
         '''