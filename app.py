#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
@desc:  
@author: LIN,WEI-LI
"""

import configparser
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

config = configparser.ConfigParser()
config.read( "ConfigParser.ini")
ACCESS_TOKEN=config.app['ACCESS_TOKEN']
SECRET=config.app['SECRET']

line_bot_api = LineBotApi(str(ACCESS_TOKEN))
handler = WebhookHandler(str(SECRET))



@app.route("/",)
def sayHello():
    return 'Hello World'


# 接受使用者資訊。
@app.route("/callback", methods=['POST'])
def callback():


    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# line 回傳。
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    got_text=event.message.text

    if str(got_text)=='你好':
        got_text='哈囉 需要幫忙嗎？'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=got_text))



if __name__ == "__main__":
    app.run()
