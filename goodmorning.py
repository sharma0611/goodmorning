#!/usr/bin/env python3
import os
import subprocess
import sys
import getpass
from dateutil import parser
from shutil import copyfile
from crontab import CronTab

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

#CONFIG
wakeup_uri = "spotify:track:6kl1qtQXQsFiIWRBK24Cfp"

#Usage:
#goodmorning.py 8:00AM 

wake_time = sys.argv[1:]
wake_time = " ".join(wake_time)
wake_time_dt = parser.parse(wake_time)
print("Setting alarm time for: ")
print(wake_time_dt.strftime("%H:%M"))


#setup environment
#env_path = "./curr.env"
#env_path = os.path.abspath(env_path)
#env_crt_cmd = """
#env | sed 's/=\(.*\)/="\1"/' > """ + env_path
#process = subprocess.Popen(env_crt_cmd, shell=True)

#setup path to wake up
wakeup_path = "./wakeup"
wakeup_path = os.path.abspath(wakeup_path)
ctrlr_path = "./spotify_ctrl"
ctrlr_path = os.path.abspath(ctrlr_path)
make_executable(wakeup_path)
make_executable(ctrlr_path)

#Grab user & cron jobs
user = getpass.getuser()
print("current crontab user: " + str(user))
my_cron = CronTab(user)

#remove any existing alarms
try:
    my_cron.remove(comment="alarm")
    my_cron.write()
except:
    pass

#add new alarm
cmd = wakeup_path + " " + wakeup_uri + " " + ctrlr_path 
job = my_cron.new(command=cmd, comment='alarm')
job.hour.on(int(wake_time_dt.strftime("%H")))
job.minute.on(int(wake_time_dt.strftime("%M")))

my_cron.write()
