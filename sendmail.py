import subprocess
import sys
import time

fdebug_path = '/home/pi/motion_capture/debugsendmail-' + time.strftime("%Y-%m-%d") + '.log'
fdebug = open(fdebug_path, 'a')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' Starting \n')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' import subprocess \n')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' import sys \n')
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' import time \n')

# File name for image
image_to_send = sys.argv[1]
recipient = sys.argv[2]
fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' given image: ' + image_to_send + ' given recipient ' + recipient + '\n')


try:
    fpl = open('/home/pi/motion_conf/presencedetect.log', 'r')
    last_presence = str(fpl.readline())
    fpl.close()
except:
    fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' access to /home/pi/motion_conf/presencedetect.log failed \n')
    last_presence = '0'

time_now = time.time()
# print (time_now)
# print (last_presence)
time_diff_presence = time_now - float(last_presence)
# print (time_diff)


try:
    fsl = open('/home/pi/motion_conf/sentmail.log', 'r')
    last_sentmail = str(fsl.readline())
    fsl.close()
except:
    fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' access to /home/pi/motion_conf/sentmail.log failed \n')
    last_sentmail = '0'

time_diff_sentmail = time_now - float(last_sentmail)

if time_diff_presence > 1800  and time_diff_sentmail > 600:
    subprocess.call(["mpack", "-s", "Your Mighty Security Camera has detected Motion!", image_to_send, recipient])
    # print ("Mail Sent")
    fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' Mail sent - Time diff lastpresence: ' + str(int(time_diff_presence)) +  ' seoncds - Time diff lastsentmail: ' + str(int(time_diff_sentmail)) + ' seconds \n')
    fsl = open('/home/pi/motion_conf/sentmail.log', 'w')
    time_now = time.time()
    fsl.write(str(time_now) + '\n')
    fsl.close()
else:
    # print ("No Mail Sent")
    fdebug.write(time.strftime("%Y-%m-%d %H:%M:%S") + ' Mail not sent - Time diff lastpresence: ' + str(int(time_diff_presence)) +  ' seoncds - Time diff lastsentmail: ' + str(int(time_diff_sentmail)) + ' seconds \n')

fdebug.close()
