# sfx-framedata

Un bottino per i combattenti di strada cinque. Runs on discord-py 1.31 or more recent (post-rewrite API).

Built and mantained by [ricki122](https://twitter.com/ricki122), [Antonio Vivace](https://twitter.com/avivace4), [d3nnib](https://twitter.com/dennibevilacqua)

## Run

#### Data pulling

pup-sfx is a Puppeteer script to pull raw HTML pages from capcom website. Handles the steam login.

Get things ready:

```
cd pup
sudo sysctl -w kernel.unprivileged_userns_clone=1
npm install
```

Run:

```
node index.js
```

#### Discord Bot

[Create a Discord Bot](https://discordpy.readthedocs.io/en/latest/discord.html). Put the token (not the secret) in the `conf/bots.yaml` configuration file.

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
