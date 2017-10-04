#!/bin/bash
#script to initialize DBUS & DISPLAY then run spotify alarm
source /home/shivam/.envs/shivam.env
export $(dbus-launch)
#sessionfile=`find "${HOME}/.dbus/session-bus/" -type f`
#export `grep "DBUS_SESSION_BUS_ADDRESS" "${sessionfile}" | sed '/^#/d'`
#eval $(tr '\0' '\n' </proc/$(pidof gvfsd)/environ | grep DBUS_SESSION_BUS_ADDRESS) 
eval $(tr '\0' '\n' </proc/$(pidof gvfsd)/environ | grep DISPLAY) || DISPLAY=:0
export DISPLAY DBUS_SESSION_BUS_ADDRESS 
spotify-rise spotify:track:6kig1UFggPUyZBCvXD3Wod
