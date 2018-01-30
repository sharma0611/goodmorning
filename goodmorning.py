#!/usr/bin/env python3
import subprocess
import sys
import getpass
from dateutil import parser

#CONFIG
wakeup_uri = ""

#Usage:
#shutwake 8:00AM 
# in order to shutdown your computer in 30 mins 

wake_time = sys.argv[1:]
wake_time = " ".join(wake_time)
wake_time_dt = parser.parse(wake_time)

user = getpass.getuser()
