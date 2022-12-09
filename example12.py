# progress scrollbar ..100%
#-------------------------------------------
from tqdm import tqdm, trange
import time
with tqdm(total=100) as pbar:
    for i in range(100):
        #time.sleep(0.1) #//seconds
        time.sleep(1)
        #pbar.update(1)  #//seconds
        pbar.update(1)
print ("FINISH")
input ("Thanks... to EXIT! press ENTER")
#---------------------------------------------