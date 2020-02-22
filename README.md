# sfx-framedata

Un bottino per i combattenti di strada cinque. Runs on discord-py 1.31 or more recent (post-rewrite API).

Built and mantained by [ricki122](https://twitter.com/ricki122), [Antonio Vivace](https://twitter.com/avivace4), [d3nnib](https://twitter.com/dennibevilacqua)

## Commands

A sample of the commands available to the bot, see [config file](conf/bots.yaml) for the full list. 

* `!frames`: 
    Get SFV frame data for the specified char and move. ```!frames Ryu cr.mk```
* `!blacklist`: Blacklists a user from using the bot functions ```!blacklist user1 [user2 user3]```
* `!help`: 'Get help on a command. Usage ```!help command_name```
* `!info`: 'Get suppport/feedback contacts and show some technical data. Usage ```!info```


## Run

#### 0. Requirements

Python3 and a recent version of Node are required.

```
# Clone the repository
git clone https://github.com/avivace/sfx-framedata
cd sfx-framedata

# Install pipenv
pip install --user pipenv

# Activate the virtualenv
pipenv shell
# Install python dependencies
```

You should now be ready to run everything.

#### 1. Data pulling

`Giovannino` is a node script powered by Puppeteer to pull raw HTML pages from capcom website. Handles the steam login.

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

#### 2. Data scraping

TODOCUMENT (`data/` folder)


#### 3. Discord Bot

[Create a Discord Bot](https://discordpy.readthedocs.io/en/latest/discord.html). Put the token (not the secret) in the `conf/bots.yaml` configuration file.

```bash
cd discord
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt
python3 discord-bot.py
```
#### 4. API

Run

```
cd api
python3 server.py
```

Endpoints:

```
localhost:8080/api/v1/$METHOD$
localhost:8080/api/v1/ui
```

## Architecture

<img src=".meta/sfx.svg">


### Notes

Originally based on [Yaksha](https://github.com/ellipses/Yaksha) bot by [ellipses](https://github.com/ellipses)


Rewriting history because Antuz commits passwords in clear:

```bash
git clone --bare git@github.com:avivace/sfx-framedata.git
java -jar bfg-1.13.0.jar --replace-text password.txt sfx-framedata.git/
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git push (-f ?)
git grep PASSWORD $(git rev-list --all)
# not working 
# ! [remote rejected] refs/pull/1/head -> refs/pull/1/head (deny updating a hidden ref)
# probably for the previous commits (PR?)

```