#!/usr/bin/python
from twisted.internet import reactor, protocol
from twisted.words.protocols.irc import IRCClient
import utils
import yaml
import time


class MessageLogger:
    '''
    Very basic logger class, that does what it says on the box.
    '''
    def __init__(self, file):
        self.file = file

    def log(self, message):
        timestamp = time.strftime("[%H:%M:%S]", time.localtime(time.time()))
        self.file.write('%s %s\n' % (timestamp, message))
        # self.file.flush()

    def close(self):
        self.file.close()


class Bot(IRCClient):

    def __init__(self):
        config_path = 'bots.yaml'
        config = yaml.load(open(config_path).read())
        self.loggers = {}
        frinkiac = utils.Frinkiac()
        arbitary = utils.Arbitary()
        gifs = utils.Gifs()
        boards = utils.Boards()
        frames = utils.Frames(config['frame_data'])
	commands = utils.AddCommands(config['add_commands']['irc'])	

        self.simpsons_gif = frinkiac.get_gif
        self.captioned_gif = frinkiac.get_captioned_gif
        self.shuffle = arbitary.shuffle
        self.casuals = boards.get_thread_posters
        self.tourney = arbitary.get_tourneys
        self.giffy_gif = gifs.get_gif
        self.get_frames = frames.get_frames
	self.add_command = commands.add_command
	self.get_command = commands.get_command

        self.commands = config['common-actions']
        # self.commands.update(config['irc-actions'])

    def _get_nickname(self):
        return self.factory.nickname

    nickname = property(_get_nickname)

    def signedOn(self):
        for channel in self.factory.channels:
            self.join(channel)
            filename = '%s_logs.txt' % channel
            self.loggers[channel] = MessageLogger(open(filename, "a"))

        print ('Signed on as %s' % self.nickname)

    def joined(self, channel):
        print ('Joined %s' % channel)

    def privmsg(self, user, channel, message):

        if channel == self.nickname:
            self.msg(channel, ("Sneaky communication isn't nice,"
                               " play with the group"))
        else:
            for command in self.commands.keys():
                if message.lower().startswith(command.lower()):
                    message = message[len(command):].strip()
                    response = getattr(self, self.commands[command])(message,
                                                                     user)
                    self.msg(channel, response.encode('ascii', 'ignore'))
                    break
            user = user.split('!', 1)[0]
            self.loggers[channel[1:].lower()].log("<%s> %s" % (user, message))


class BotFactory(protocol.ClientFactory):
    '''
    Factory that creates the bots and logs various connection issues.
    '''

    protocol = Bot

    def __init__(self, channels, nickname='Yaksha'):
        self.channels = channels
        self.nickname = nickname

    def startedConnecting(self, connector):
        print ('Started connecting')

    def clientConnectionFailed(self, connector, reason):
        print ('Connection failed because of %s. Trying to reconnect' % reason)
        connector.connect()

    def clientConnectionLost(self, connector, reason):
        print ('Connection failed because of %s. Trying to reconnect' % reason)
        connector.connect()


def main():
    print ('Starting up the bot.')
    channels = ['tomtest']
    reactor.connectTCP('irc.quakenet.org', 6667,
                       BotFactory(channels))
    reactor.run()

# Standard python boilerplate.
if __name__ == '__main__':
    main()
