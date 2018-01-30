# goodmorning - A spotify /Users/shivam/dev/goodmorning/README.mdalarm clock

goodmorning is a simple Spotify alarm clock using cron.

## Requirements 
* npm 
* Python3




## Quick Setup

Command line setup:

1) Setup script in user scripts

```bash
$ git clone https://github.com/sharma0611/goodmorning.git
$ pip install -r requirements
$ npm install spotify-cli-mac -g

$ chmod +x shutwake
$ cp shutwake /usr/local/sbin/shutwake
```
2) Setup crontab to be run at certain time every day

```
$ crontab -e
```
Add the following to make your computer shutdown at certain time; 

