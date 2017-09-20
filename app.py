# encoding: utf-8
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
import inspect
app = Flask(__name__)

#line_bot_api = LineBotApi('') #Your Channel Access Token
#handler = WebhookHandler('') #Your Channel Secret
line_bot_api = LineBotApi('PhDjdnkZ/9aQxmJSbynyMWi1RWOGi/tNiV5+7I0s9h5hoDU+TI6Cyqb32K62uI8L6afXPbB4UAkexqG9nHg/XJhBXWrjPjAulfrHUy7DyQH7uWH9oReBtWTjbZ2aMK3i4X5iqW58+v2ZqnZzf8xMTgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('507a265f755e0af4a585c597d981197d')
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

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user    
    
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ตู้กาก\n' +  str(event.__dict__))
            )

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088)
