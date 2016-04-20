from utils import *
import my_logger
import tracker_daemon

#tracker_daemon.init();


logger = my_logger.getLogger(__name__ )

time    =   12343232323.90
deviceId = "sd102900lop"

logger.debug("New Device %s Connected %s " , deviceId , time )
