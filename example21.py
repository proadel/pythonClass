# Limite-access to coding files
#-----------------------------------
import wmi
c = wmi.WMI()
serial = c.Win32_BaseBoard()[0].SerialNumber.strip()
if (serial == 'DDFFRGYHR' ):
    print ("YOUR JOB codes is Allowed")
else:
    print ("=======================================")
    print (" Sorry, you are Not Allowed to ACCESS!")
    print ("  Please contact to leasrn more about")
    print ("Dev. by Adel MD. | Umbrella Corporation")
    print ("         be free to contact")
    print (" +967 733 477 848 | adeldawood@live.com")
    print ("=======================================")

#---------------------------------------------------
#print (c.Win32_BaseBoard()[0].SerialNumber.strip())