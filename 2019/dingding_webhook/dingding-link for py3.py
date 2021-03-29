#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Fighter.Kun'
__time__ = '2019/11/15 15:05'

import sys

from dingtalkchatbot.chatbot import DingtalkChatbot
# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=0d2f29c6e1cb0657dd67f16b0ee9a3d5ccd32100d050233dc6abfae8a46712af'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Link消息
if __name__ == '__main__':
    title = sys.argv[1]
    text = sys.argv[2]
    message_url = sys.argv[3]
    xiaoding.send_link(title=title, text=text, message_url=message_url)