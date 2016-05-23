
def function2():
    print("called function 2 ")
    
def function1(callback1):
    print("In Function 1 , calling cabllback1")
    callback1.__call__()

if( __name__ == "__main__"):
    
    function1(function2);
    
    