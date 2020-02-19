#!/usr/bin/python
import aiofiles
from fuzzywuzzy import process
from commands.utilities import register

class Help():

    def __init__(self, config=None):
        self.config = config or {}
        self.cmd_ratio_thresh = 80

    @register('?help')
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


class Blacklist():

    def __init__(self, config=None):
        config = config or {}
        self.blacklist_file = config.get('blacklist_file')

    @register('!blacklist')
    async def blacklist(self, message, *args, **kwargs):
        '''
        Blacklists the user by adding their 'uid' to the
        currently maintained list of blacklisted users and updates the file.
        '''
        blacklisted_users = kwargs['blacklisted_users']
        users = message.split(' ')
        # Remove users who might have already been blacklisted.
        users = [user for user in users if user not in blacklisted_users]
        blacklisted_users.extend(users)

        users = [user + '\n' for user in users]
        async with aiofiles.open(self.blacklist_file, mode='a') as f:
            await f.writelines(users)

    @register('!unblacklist')
    async def unblacklist(self, message, *args, **kwargs):
        '''
        Unblacklists the user by removing their 'uid' from the currently maintained
        list of blacklisted users and removes it from the file.
        '''
        users = message.split(' ')
        blacklisted_users = kwargs['blacklisted_users']
        users = [user for user in users if user in blacklisted_users]

        for user in users:
            del blacklisted_users[blacklisted_users.index(user)]

        users = [user + '\n' for user in users]
        async with aiofiles.open(self.blacklist_file, mode='r') as f:
            saved_users = await f.readlines()
            for user in users:
                del saved_users[saved_users.index(user)]

        async with aiofiles.open(self.blacklist_file, mode='w') as f:
            await f.writelines(saved_users)
