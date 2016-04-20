
import os

import getpass												# lib used to get user name and paswword '	
import my_logger
import utils

def main():
	# ------------------------------------------
	#	Starting function
	#-------------------------------------------
    
    if( os.path.exists(utils.getConfigDir()) == False ):
        init();

    run();				#Configuration file to hold temporory data.


def init():
	# ------------------------------------------
	#	performs initialization first time only
	#-------------------------------------------
	
    try:     
        
        os.mkdir(utils.getConfigDir())
        config_file	=	open(utils.getConfigDir() + "/" + utils.getConfigFileName, "w" )
		
		
    except Exception as ex:
        exit(1);


        
if(__name__ == '__main__'):
    main();