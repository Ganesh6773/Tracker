
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
_MAX_WAIT_TIME_TO_PARSE_THREAD_RUN          =   30 * 60      # after this time the method parseAndUpdate() from device_connection_tracking_status will run


# -------------- small server constants
_SERVER_IP                                  =   None
_SERVER_URL                                 =   'http//localhost:8081'

_UPDATE_DISCONNECTED_DEVICE_URL                   =   'update'       # this string will be added to server utl to call nodejs update url location
_ADD_DEVICE_CONNECTION_URL                         =   'add'
#_-------------- getters -------------

def getConfigDir():
    ''' Returns Config directory path, where all config infomation is stored'''
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
    '''Returns time to wait to check device connection state '''
    return _MAX_WAIT_BETWEEN_DEV_CONNECTION_CHECK;
   
   
def getMaxTimeToChangeStatus():
    ''' Returns the time after which device disconnected entry needs to be added to db, until this time even 
        if device is disconnected, it is hoped that it will be rebooting or hang or being
         flashed and not considered as disconnected.
    '''
    return _MAX_TIME_TO_CHANGE_STATUS;

def getMaxTimeToParseThreadRun():
    return _MAX_WAIT_TIME_TO_PARSE_THREAD_RUN

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
def getMeanTime(time1 , time2 ):
    return int(diffBetTime(time1, time2) / 2 )
       
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
                        
            logger.log("i", "One device connected " + state);_
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
        


#----------------server utils

@staticmethod
def getServerIp():
    ''' returns the server ip'''
    return _SERVER_IP
    

@staticmethod
def getServerURL():
    ''' return server URL '''
    return _SERVER_URL    
    
@staticmethod
def getUpdateURL():
    ''' nodejs url for updating the DISCONNECTED device entry'''
    return getServerURL() + '/' + _UPDATE_DISCONNECTED_DEVICE_URL
    
    
@staticmethod
def getAddURL():
    ''' nodejs url for adding new connected device entry'''
    return getServerURL() + '/' + _ADD_DEVICE_CONNECTION_URL
