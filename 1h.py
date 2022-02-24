import time
for i in range(10):
    seconds = time.time() #it will give to you as a float values
    local_time = time.ctime(seconds) #it will gives to you as a current local time
    print("Local time:", local_time)
    time.sleep(10)
    


