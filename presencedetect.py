import subprocess
import time

filename_presencelog = '/home/pi/motion_conf/presencedetect.log'

fdebug_path = '/home/pi/motion_capture/debugpresencedetect-' + time.strftime("%Y-%m-%d") + '.log'
fdebug = open(fdebug_path, 'a')
fdebug.write('\n' + time.strftime("%Y-%m-%d %H:%M:%S") + ' Starting \n')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' import subprocess \n')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' import time \n')

# Presence check for these occupants:
occupant = ["John", "Tom", "Kate"]

# MAC addresses of the phones
address = ["XX:XX:XX:XX:XX:XX", "XX:XX:XX:XX:XX:XX", "XX:XX:XX:XX:XX:XX"]

fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' we are looking for: ' + address[0] + ' & ' + address[1] + ' & ' + address[2] + '\n')
fdebug.close()

i = 0
fdebug = open(fdebug_path, 'a')
fdebug.write('\n' + time.strftime("%Y-%m-%d %H:%M:%S") + ' Starting ARP scan \n')
fdebug.close()
output = subprocess.check_output("sudo arp-scan -l", shell=True)
time.sleep(20) # give the arp-scan enough time
fdebug = open(fdebug_path, 'a')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' arp-scan: \n' + output + '\n')
fdebug.close()

while i < 3:
    if address[i] in output:
        # File-Stuff needs to happen here
        # building the file name
        try:
            fpl = open(filename_presencelog, 'w')
            time_now = time.time()
            fpl.write(str(time_now) + '\n')
            fpl.close()
            fdebug = open(fdebug_path, 'a')
            fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' ' + occupant[i] + ' present written down \n')
            fdebug.close()
        except:
            fdebug = open(fdebug_path, 'a')
            fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' access to ' + filename_presencelog + ' failed \n')
            fdebug.close()
    else:
        fdebug = open(fdebug_path, 'a')
        fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' ' + occupant[i] + ' not present written down \n')
        fdebug.close()
    i = i +1

fdebug = open(fdebug_path, 'a')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' Stopping \n')
fdebug.close()

