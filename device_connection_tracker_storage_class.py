# not sure if want to use this
import os
import utils
import my_logger
import time
import db_ops as db

DEV_CON_TIME        =   0
DEV_STATUS          =   1
DEV_ID              =   2
class DeviceStatusClass:
    ''' this class store local status for few hours '''
    
    connectionTime  =   []      #  the time when activiry happened
    devStatus       =   []      # what is dev status at that time
    devId           =   []      # deviceId at that time, or NONE if no device
    logger          =   my_logger.getLogger();
    
    
    @staticmethod
    def getAndRemoveFirst():
        retList =   []
        if(len(DeviceStatusClass.connectionTime) > 0):
                 
            retList.append(DeviceStatusClass.connectionTime[0])
            retList.append(DeviceStatusClass.devStatus[0])
            retList.append(DeviceStatusClass.devId)[0]
            
            DeviceStatusClass.connectionTime.pop(0)
            DeviceStatusClass.devStatus.pop(0)
            DeviceStatusClass.devId.pop(0)
            
            DeviceStatusClass.debug("removed First erntry from device" + __file__ + str(retList));
            return retList;
            
    
    @staticmethod
    def add(time_, status_, id_):
        
        DeviceStatus.connectionTime.append(time)
        DeviceStatus.devStatus.append(status_)
        DeviceStatus.devId.append(id_);
        DeviceStatus.logger.debug("added Device entry DeviceStatusClass Time : " + str(time_) + ", Status : " + str(status_) + " , Id : " + str(id_));    
        
   
    @staticmethod
    def parseAndUpdate():
        ''' This method will parse the lists and update the status accordongly '''
        
        devFirstConTime = 0
        devId           =   None
        devPrevStatus   =   None
        lastSeenTime    =   -1
           
        while (True ):
            
            firstTuple  =   DeviceStatusClass.getAndRemoveFirst();
            if(devFirstConTime  ==  0):
                
                DeviceStatusClass.logger("First Time Initailization in parseAndUpdate")
                devFirstConTime         =   firstTuple[DEV_CON_TIME]
                devPrevStatus           =   firstTuple[DEV_STATUS]
                devId                   =   firstTuple[DEV_ID]
                lastSeenTime            =   devFirstConTime;
                #also add entry to db saying new dev connected.
                
                dbOpResult=db.addDevConnectedEntry(utils.TYPE_REFERENCE_DEVICE, devId, devFirstConTime) ;
                if(dbOpResult):
                    DeviceStatusClass.logger.info("Device connection entry added afrer first time initialization. Dev Id " + str(devId) + "Connection Time " + str(devFirstConTime));
                else:
                    
                    
            elif (firstTuple[DEV_ID] != devId):
                #new Device Connected
                #add disconnected entry from prev device.
                DeviceStatusClass.logger.debug("New Connected Device found " + firstTuple[devId])

                probableDiscTime    =   utils.getMeanTime() -2
                dbOpResult=db.addSDevDisconnectedDBEntry(utils.TYPE_REFERENCE_DEVICE, utils.DISCONNECTED, devId, devFirstConTime,probableDiscTime)
                
                if(dbOpResult):
                    DeviceStatusClass.logger.debug("Added Dev Disconnected entry of device Id " + str(devId) + " Successfully")
                else:
                    DeviceStatusClass.logger.error("Failed to add device disconnection entry to deb for device id : " + str(devId))
                
                #now add New Device Connection entry
                
                dbOpResult  =   db.addDevConnectedEntry(utils.TYPE_REFERENCE_DEVICE, utils.CONNECTED, firstTuple[DEV_ID], probableDiscTime + 2 )
                
                if(dbOpResult):
                    DeviceStatusClass.logger.debug("Added Dev Connected entry of device Id " + str(firstTuple[DEV_ID]) + " Successfully")
                else:
                    DeviceStatusClass.logger.error("Failed to add new device Connection entry to db for device id : " + str(firstTuple[DEV_CON_TIME]))
                
                #Re-initialise all the variables
                
                devFirstConTime =   probableDiscTime + 2 ;
                devId           =   firstTuple[DEV_ID]
                devPrevStatus   =   utils.CONNECTED
                lastSeenTime    =   devFirstConTime
                probableDiscTime =  0
                
           
           #if status changed from connected to disconnected,
           # then iterate till new connection entry found, or getMaxTimeToChangeStatus() elapsed.
                          
           elif (firstTuple[DEV_STATUS] !=  devPrevStatus):
           #device connected or disconnected
                 
                 
            
                
            
            
            
            
            
            
           time.sleep(utils.getMaxTimeToParseThreadRun) 


if __name__ == '__main__' :
    print(deviceStatus.connectionTime)
    deviceStatus.add(34,34,34)
         