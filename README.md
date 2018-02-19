# goodmorning

goodmorning is a Spotify alarm clock made using cron & a simple python script. Set up your alarms through the command line, wake up to music, and have a good morning. 

## Requirements 
* HomeBrew
* Python3
* MacOS 

## Quick Setup

Command line setup:

**Install Requirements and Setup Symlink**

```bash
$ git clone https://github.com/sharma0611/goodmorning.git
$ pip install -r requirements
$ brew install dbus
$ brew install proctols
$ ln -s /path/to/goodmorning /usr/local/bin/goodmorning
```

## **Usage**

Copy the spotify URI of the song you want to play for your alarm. Set the value "wakeup_uri" in the goodmorning script to this value. Now you can setup alarms with this song through your terminal. Just set your Mac to never sleep and use hot corners to turn off your display. 


#### Setting Alarms
```bash
$ goodmorning 8:45 AM 
```
The default alarm that is set & reset with this action is alarm 1. 

```bash
$ goodmorning alarm3 8:45 AM 
```
This would setup alarm 3.

```bash
$ goodmorning 8pm alarm5
```
This would setup alarm 5.

Point is, either pass in just a time OR pass in 'alarm{num}' with a time to set that alarm to that time, in any order you please. Feel free to use military time if you want; just check with the output to ensure the correct time is set.

#### Show
```bash
$ goodmorning show
```

This displays all active alarms.

#### Remove
```bash
$ goodmorning remove alarm1
```

This will remove alarm1.

## How it works

Uses crontabs to setup alarms that call spotify interface at given times.
