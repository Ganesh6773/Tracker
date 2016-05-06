
import logging
import os
import getpass												# lib used to get user name and paswword '	
import time


#------------------- Constants -----------------

DISCONNECTED                                =   -1      # constants represents device status
CONNECTED                                   =   1

TYPE_REFERENCE_DEVICE                         =   1
TYPE_REFERENCE_DEVICE_CHECK_CMD             =   ["adb", "devices", "-l"]

_APPLICATION_NAME                           =   "tracker";
_APPLICATION_VERSION                        =   "1.0 v";
   
_CONFIG_DIR	                                =	"/home/" + getpass.getuser()+ "/.tracker/";
_CONFIG_FILE	                            =	"tracker_config.conf";
_LOG_FILE                                   =   _CONFIG_DIR + _APPLICATION_NAME + "_execution_logs.log";

_DEFAULT_LOG_LEVEL                          =   logging.DEBUG ;
_LOGGER_FORMAT_STRING                       =   '[ %(asctime)-15s ] [ %(levelname)s ] [ %(threadName)s ] : %(message)s' ;

_MAX_WAIT_BETWEEN_DEV_CONNECTION_CHECK      =   5  * 60      #( 300 secs)
_MAX_TIME_TO_CHANGE_STATUS                  =   20 * 60      # even if the same dev is connected after this time, it will cause new entry in db  

#_-------------- getters -------------

def getConfigDir():
    return _CONFIG_DIR;
    
def getConfigFileName():
    return _CONFIG_FILE;
    
def getLogFileName():
    return _LOG_FILE;
    
def getLoggingLevel():
    return _DEFAULT_LOG_LEVEL;
  
def getLoggerFormatString():
    return _LOGGER_FORMAT_STRING ;
    
def getMaxWaitBetweenDeviceConnectionCheck():
    return _MAX_WAIT_BETWEEN_DEV_CONNECTION_CHECK;
   
def getMaxTimeToChangeStatus():
    return _MAX_TIME_TO_CHANGE_STATUS;



#------------------- static utility methods -----------------
@staticmethod
def getTime():
    ''' returns current time in seconds'''
    return int(time.time());


@staticmethod
def diffBetTime(prevTime):
    ''' Returns time between given Time and current time in seconds.'''
    return int(prevTime) - int(time.time());
    
   
@staticmethod
def getConnectedDeviceId(type=TYPE_REFERENCE_DEVICE):
    ''' Return Device id if connected else DISCONNECTED '''
    if(type	==	UserConfig.TYPE_REFERENCE_DEVICE ):
               
        proc=subprocess.Popen((UserConfig.TYPE_REFERENCE_DEVICE_CHECK_CMD), stdout=subprocess.PIPE)
        
        state	=	proc.stdout.read()
        dev	=	state.split('\n')[1];
        
        if(dev	==	""):
            logger.log("i", "No Connected Device");
            return DISCONNECTED
        else:
                        
            logger.log("i", "One device connected " + state);
            return dev.split(" ")[0];
        
    
    
    
@staticmethod
def getDeviceConnectioState(type=TYPE_REFERENCE_DEVICE):
    ''' This will check if the device is connected based on command'''
    
    if(type	==	UserConfig.TYPE_REFERENCE_DEVICE ):
    
        proc=subprocess.Popen((UserConfig.TYPE_REFERENCE_DEVICE_CHECK_CMD), stdout=subprocess.PIPE)
        
        state	=	proc.stdout.read()
        dev	=	state.split('\n')[1];
        
        if(dev	==	""):
            logger.log("i", "No Connected Device");
            return DISCONNECTED
        else:
                        
            logger.log("i", "One device connected " + state);
            return CONNECTED
        


    
    
    