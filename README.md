
# 🤖Telegram keyword alert bot ⏰


For alert Channel/Group Keyword messages

If you want to subscribe to `group` messages, make sure normal TG accounts do not need to authenticate to join the group.

Principle: tg command line client to listen for messages and use bot to send messages to subscribed users.

👉  Features：

- [x] Keyword message subscription: send new message alerts based on set keywords and channels
- [x] Support for regular expression matching syntax
- [x] Support multi-channel subscription & multi-keyword subscription
- [x] Support for subscribing to group messages
- [x] Support private channel ID/invite link for message subscription 

  1. https://t.me/+B8yv7lgd9FI0Y2M1  
  2. https://t.me/joinchat/B8yv7lgd9FI0Y2M1 
  

👉 Todo:

- [ ] Private group subscriptions and alerts
- [ ] Private channel message alert full content preview
- [ ] Multi-account support
- [ ] Scan out of useless channels/groups

# DEMO

http://t.me/keyword_alert_bot

![image](https://user-images.githubusercontent.com/10736915/171514829-4186d486-e1f4-4303-b3a9-1cfc1b571668.png)


# USAGE

## General keyword matching

```
/subscribe  Free    https://t.me/tianfutong
/subscribe  Coupons https://t.me/tianfutong

```

## Regular expression matching

Use js regular syntax rules, wrap the regular statement with /, the current match pattern can be used: i,g

```
# Subscribe to the phone model keywords: iphone x, excluding XR, XS and other models, and ignore the case
/subscribe   /(iphone\s*x)(?:[^sr]|$)/ig  com9ji,xiaobaiup
/subscribe   /(iphone\s*x)(?:[^sr]|$)/ig  https://t.me/com9ji,https://t.me/xiaobaiup

# test
/subscribe  /([\S]{2}test)/g  https://t.me/<telegram-channel>

```


## BUILD

### 1. config.yml.default --> config.yml

#### Create Telelgram Account & API

[Open api](https://my.telegram.org/apps) We recommend that you use a newly registered Telegram account.

#### Create BOT 

https://t.me/BotFather  

### 2. RUN

Runtime environment python3.7+

The first run requires a tg account to receive a digital verification code and enter a password (telegram API trigger)

```
$ pipenv install

$ pipenv shell

$ python3 ./main.py
```

### 3. crontab （optional）

 - update telethon

Dependency library telethon may have old versions unavailable or other bugs, please preferably perform dependency updates via timed tasks.

e.g. 
```
0 0 1 * * cd /home/keyword_alert_bot && pipenv update telethon > /dev/null 2>&1
```

## BUG Q&A

- Check the logs and found that individual groups cannot receive messages, the software client receives them normally

Please try to update telethon to solve the problem 🤔 I am also very helpless.
- Subscribe to group messages, the robot does not respond

https://github.com/Hootrix/keyword_alert_bot/issues/20
- ModuleNotFoundError: No module named 'asyncstdlib', No module named '...'

```
$ pipenv  install
```

## BOT HELP

```

Purpose: Subscribe channel news according to keywords

Support multi-keyword and multi-channel subscription, using English comma `,` interval

Use spaces between keywords and channels

Main orders:

/subscribe - subscribe operation: `Keyword1,Keyword2 https://t.me/<telegram-channel>,https://t.me/<telegram-channel>`

/unsubscribe - unsubscribe: `Keyword1, Keyword2 https://t.me/<telegram-channel>,https://t.me/<telegram-channel>`

/unsubscribe_all - unsubscribe from all

/list - Show list of all subscriptions

---

Purpose: Subscribe to channel messages based on keywords

Multi-keyword and multi-channel subscription support, using comma `,` interval.

Use space between keywords and channels

Main command:

/subscribe - Subscription operation: `keyword1,keyword2 https://t.me/tianfutong,https://t.me/xiaobaiup`

/unsubscribe - unsubscribe: `keyword1,keyword2 https://t.me/tianfutong,https://t.me/xiaobaiup`

/unsubscribe_all - cancel all subscriptions

/list - displays a list of all subscriptions
```
