
import logging
import os
import getpass												# lib used to get user name and paswword '	


_APPLICATION_NAME    =   "tracker";
_APPLICATION_VERSION =   "1.0 v";
   
_CONFIG_DIR	    =	"/home/" + getpass.getuser()+ "/.tracker/";
_CONFIG_FILE	=	"tracker_config.conf";
_LOG_FILE       =   _CONFIG_DIR + _APPLICATION_NAME + "_execution_logs.log";

_DEFAULT_LOG_LEVEL      =   logging.DEBUG ;
_LOGGER_FORMAT_STRING   =   '[ %(asctime)-15s ] [ %(levelname)s ] [ %(threadName)s ] : %(message)s' ;


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
    

    
    
    