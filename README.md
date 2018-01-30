# goodmorning - A spotify alarm clock

goodmorning is a simple Spotify alarm clock using cron.

## Requirements 
* npm 
* HomeBrew
* Python3

## Quick Setup

Command line setup:

1) **Setup spotify from npm**

```bash
$ npm install spotify-cli-mac -g
```

Now we have to configure the command line spotify command.
Run the spotify command in your terminal and enter your client ID and client secret you will get from beta.developer.spotify.com. Log in there, make an app, get the keys. When you run `$ spotify` you will be prompted for those keys, enter them and you are done configuring the cmd line spotify.

1) **Install Requirements**

```bash
$ git clone https://github.com/sharma0611/goodmorning.git
$ pip install -r requirements
$ brew install dbus
$ brew install proctols
$ chmod +x wakeup
$ chmod +x goodmorning.py
$ chmod +x spotify_ctrl
```

3) **Usage**

Copy the spotify URI of the song you want to play for your alarm. Set the value "wakeup_uri" in goodmorning.py to this value. Now you can setup alarms on the fly!

```bash
$ ./goodmorning 8:45 AM 
```
It will confirm with you the time you have set the alarm.
This alarm will stay set and will play everyday at the same time until you set another alarm. Currently only supporting one alarm at a time. Best use case: going to bed after a long day of programming and simply typing "./goodmorning 7 AM" to wake up at that time.
