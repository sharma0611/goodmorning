# goodmorning - A spotify alarm clock

goodmorning is a simple Spotify alarm clock using cron.

## Requirements 
* HomeBrew
* Python3
* MacOS 

## Quick Setup

Command line setup:

**Install Requirements**

```bash
$ git clone https://github.com/sharma0611/goodmorning.git
$ pip install -r requirements
$ brew install dbus
$ brew install proctols
```

### **Usage**

Copy the spotify URI of the song you want to play for your alarm. Set the value "wakeup_uri" in goodmorning.py to this value. Now you can setup alarms on the fly!

```bash
$ ./goodmorning 8:45 AM 
```
The default alarm that is set & reset with this action is alarm1. 


It will confirm with you the time you have set the alarm.
This alarm will stay set and will play everyday at the same time until you set another alarm. Best use case: going to bed after a long day of programming and simply typing "./goodmorning 7 AM" to wake up at that time.

#### Multiple Alarms

```bash
$ ./goodmorning alarm3 8:45 AM 
```

OR

```bash
$ ./goodmorning 8pm alarm5
```

Point is, either pass in just a time OR pass in 'alarm{num}' with a time to set that alarm to that time, in any order you please. Feel free to use military time if you want; just check with the output to ensure the correct time is set.

#### How it works

Uses crontabs to setup alarms that call spotify interface at given times.

## Add it to your path

Some preconfigured bash scripts to call the python script with presupplied arguments: 

```bash
$ cd goodmorning
$ ln -s $(pwd)/show /usr/local/bin/show
$ ln -s $(pwd)/alarm_set /usr/local/bin/ls
2:alarm_set
$ ln -s $(pwd)/remove /usr/local/bin/remove
```

Now you can use it like this:

```bash
$ show
$ remove alarm1
$ alarm_set alarm1 4am
```