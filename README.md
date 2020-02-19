# sfx-framedata

Un bottino per i combattenti di strada cinque. Runs on discord-py 1.31 or more recent (post-rewrite API).

Built and mantained by [ricki122](https://twitter.com/ricki122), [Antonio Vivace](https://twitter.com/avivace4), [d3nnib](https://twitter.com/dennibevilacqua)

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

* !frames: 
    Get SFV frame data for the specified char and move. ```!frames Ryu cr.mk```
* !blacklist: Blacklists a user from using the bot functions ```!blacklist user1 [user2 user3]```
* !help: 'Get help on a command. Usage ```!help command_name```

  

Originally based on [Yaksha](https://github.com/ellipses/Yaksha) bot by [ellipses](https://github.com/ellipses)
