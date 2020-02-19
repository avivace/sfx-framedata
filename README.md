# sfx-framedata

Un bottino per i combattenti di strada cinque. Runs on discord-py 1.31 or more recent (post-rewrite API).

## Deploy

#### Discord application

[Create a Discord Bot](https://discordpy.readthedocs.io/en/latest/discord.html). Put the token (not the secret) in the `conf/bots.yaml` configuration file.

#### Steam authentication

TODO

#### Run the bot

```bash
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt
python3 src/discord-bot.py
```


## Commands

A sample of the commands available to the bot, see [config file](conf/bots.yaml) for the full list. 

* !gif: Returns the most relevant gif for the caption using Giffy. ```!gif obama mic drop```
* !frames: 
    Get SFV frame data for the specified char and move. ```!frames Ryu cr.mk```
* !simpsons: Get a simpsons gif that best matches the specified caption. ```!simpsons nothing at all```
* !futurama: Get a futurama gif that best matches the specified caption. ```!futurama Shut up and take my money! The new eyephone is wonderful```
* !blacklist: Blacklists a user from using the bot functions ```!blacklist user1 [user2 user3]```
* !vote: Start a vote in the channel for the specified length and
    topic, and options. ```!vote[--time] Vote topic [param1, param2] ```  
* !remindme: 
    Get Yaksha to remind to at a specified time similar to slackbot. ```!remindme <time period> [optional string]```
* !whens: Get status of registered streams. Usage ```!whens```
* !shuffle: 
    Randomly select a word from a supplied list of words.
    Usage ```!shuffle yes no maybe```
* !help: 'Get help on a command. Usage ```!help command_name```

  

Originally based on [Yaksha](https://github.com/ellipses/Yaksha) bot by [ellipses](https://github.com/ellipses)
