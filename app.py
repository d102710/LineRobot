#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
@desc:  
@author: LIN,WEI-LI
@software: PyCharm
"""

import os
import requests
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

ACCESS_TOKEN = 'znOzkGEVO4xe8HSQThRXHKDYxJj1Xgial9nf2cBS1ZEgscTKGQN7sYrlfAxJXwqs1fAcypDfL/mQtLpsf+St+9OLFQTLMp6UUvRFsU06B+GtBQ4ViVaNhdXcOXHwzEIwPoz5S6A/8NgqFlIjsoOdPQdB04t89/1O/w1cDnyilFU='
SECRET = '122dfcdf84786ab8d0e2842f4826119e'

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
        got_text='有事嗎你？'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=got_text))



if __name__ == "__main__":
    app.run()
