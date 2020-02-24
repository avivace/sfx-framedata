#!/usr/bin/python
import aiofiles
import discord
from fuzzywuzzy import process
from commands.utilities import register, generate_discord_color, get_last_commit


class Help():

    def __init__(self, config=None):
        self.config = config or {}
        self.cmd_ratio_thresh = 80

    @register('!help')
    async def get_help_message(self, msg, *args, **kwargs):
        available_commands = kwargs.get('commands_dict', False)

        if available_commands:
            # Try fuzzy matching on the msg to determine the cmd
            # the user is trying to get help on.
            cmd, ratio = process.extractOne(msg, available_commands.keys())

            # If the ratio is too low we assume the user made
            # an error.
            if ratio < self.cmd_ratio_thresh:
                return ('Allows you to get help on a command. The avaliable'
                        ' commands are ```%s```' % list(available_commands.keys()))
            else:
                return available_commands[cmd]
        else:
            return 'Dict of commands missing :/ .'

    @register('!info')
    async def get_info(self, msg, *args, **kwargs):
        title = "SFX-Framedata"
        url = self.config['repo_url']
        desc = f"""
            _Street Fighter V Discord bot by
            [ricki122](https://twitter.com/ricki122), [Antonio Vivace](https://twitter.com/avivace4), [dennib](https://twitter.com/dennibevilacqua)_

            For feedbacks and contributions please visit
            {url}
        """
        lastCommit = get_last_commit()
        embed = discord.Embed(
            title=title, colour=generate_discord_color(), description=desc, url=url)
        embed.set_footer(
            text=f"Running version: {self.config['version']} - Commit hash: {lastCommit}")
        return (None, embed)
