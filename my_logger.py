

import time;
import logging;
import utils

def getLogger(name, logFileName=None, minLevel = logging.DEBUG):
    
    if(logFileName is None ):
        logFileName=utils.getLogFileName();
        
    logging.basicConfig(filename=logFileName, format=utils.getLoggerFormatString())
    
    _logger =   logging.getLogger(name);
    _logger.propogate   =   False;
    _logger.setLevel(minLevel);
    
    _logger.info('Logger Initilized');
    return _logger
 
    

    
    
       
