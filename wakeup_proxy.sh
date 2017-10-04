#!/bin/bash
#machinectl shell .host --uid=1000 $(export pid=$(pgrep -xn pulseaudio) && export DBUS_SESSION_BUS_ADDRESS="$(sudo grep -ao -m1 -P '(?<=DBUS_SESSION_BUS_ADDRESS=).*?\0' /proc/"$pid"/environ)" && /usr/local/bin/spotify-rise spotify:track:6kig1UFggPUyZBCvXD3Wod)
#XDG_RUNTIME_DIR=/run/user/1000 DISPLAY=:0 /usr/local/bin/spotify-rise spotify:track:6kig1UFggPUyZBCvXD3Wod
#XDG_RUNTIME_DIR=/run/user/1000 DISPLAY=:0 spotify
#machinectl shell .host --uid=1000 /usr/bin/spotify
#eval $(tr '\0' '\n' </proc/$(pidof gvfsd)/environ | grep DBUS_SESSION_BUS_ADDRESS) && eval $(tr '\0' '\n' </proc/$(pidof gvfsd)/environ | grep DISPLAY) && 
#export DISPLAY DBUS_SESSION_BUS_ADDRESS && spotify-rise spotify:track:6kig1UFggPUyZBCvXD3Wod

env - `cat /home/shivam/.envs/shivam.env` /home/shivam/dev/alarm/wakeup.sh
