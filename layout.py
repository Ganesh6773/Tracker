
    #   same device got connected
        def sameDeviceConnectedHandler():
        
    # Different Device Cobbected
        def diffDeviceConnectedHandler():
    
    # Timeout while waiting for connction of last connected device
        def maxDisconnectedTimeElapsed(args):
            
    # new device connected when no entry for last connected device found   
        def firstTimeConnectionHandler():
              
        
      
 
 '''
 conditions :
    
    1   -   new device conncted 
            
                this event should happen when
                a.  first device connected after boot
                    --add new device connected entry ro db
                    
                
               
                
    2    -  same device disconnected and connected before elapsing getMaxTimeToChangeStatus
    
                This is should only happen 
                a. SAme device is connected before maxTimeTOChangeStatusTime is elapsed.
                    -- no entry to db, just re-initialize the vars.
                
    3   -   device disconnected
            
            This event should happen only when 
            
            a.  device stay disconnected to more than maxTimeToChangeStatus.
                -- add device disconnected enntry to db
                
    4   -   same device remain connected
        
            This evnets happens only when
            
            a.  same device remains connected in next iteration also
                -- no db entry, re-initialize appropiate vars
                
    5   -   different device connected 
    
            This event should happen only when,
            
            a.   new ( differnet thatn previous ) device got connected, without seeing disconnected entry for previous device.
                    -- add disconnected entry for previous device to db
                    -- add device connection entry for currently connected device.
                    
    6   -   no device connected .
    
            This event should happen only when
            a.  no device seen connected in
                -   just re-initialize the variable and continue to next iteration.
                
                    
 '''              
            
 
   