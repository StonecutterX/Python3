# /usr/bin/python
# -*- coding: utf-8 -*-

# usage of itchat, which can be used to load your own wechat and manage the message
# shawn 2018/1/20
## reference: https://pypi.python.org/pypi/itchat

import itchat
from itchat.content import *
from pprint import pprint

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # load friend
    itchat.send_msg('Nice to meet you! It is a test instance.', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s ' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

def analysisGender(friendList):
    male = female = other = 0
    for i in friendList:
        gender = i['Sex']
        if gender == 1:
            male += 1
        elif gender == 0:
            female += 1
        else:
            other += 1
    friendNum = len(friendList)
    print('   here   ')
    print('Num of male: %d %.2f' % (male, float(100*male/friendNum)))
    print('Num of female: %d %.2f' % (female, float(100*female/friendNum)))
    print('Num of other: %d %.2f' % (other, float(100*other/friendNum)))
            

# itchat.auto_login()
itchat.auto_login(hotReload=True) #enableCmdQR=True
# itchat.run()

# friends is list, its element denotes the info of all your friend with one dict type for one member
friends = itchat.get_friends(update=True)[0:]
print(type(friends), len(friends))

# MemberList, UserName, City, DisplayName, PYQuanPin, RemarkPYInitial, Province, KeyWord, RemarkName, 
# PyInitial, EncryChatRoomId, Alias, Signature, NickName, RemarkPYQuanPin, HeadImgUrl, UniFriend, Sex,
# AppAccountFlag, VerifyFlag, ChatRoomId, HideInputBarFlag,.....
#print(friends[0])
#print(friends[1])
pprint(friends)

analysisGender(friends)

#itchat.get_friends(userName='@')
