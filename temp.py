from flask import Flask,request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from flask_ngrok import run_with_ngrok
from settings import CHANNEL_SECRET, CHANNEL_ACCESS_TOKEN
from number import *
from main import wei7018 , all_lunch
app = Flask(__name__)
# run_with_ngrok(app)

line_bot_api =LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent,message=TextMessage)
def handler_message(event):
    msg = event.message.text
    if '我要點餐' in msg:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='您好：',
                text='請問您要點の是',
                actions=[
                    MessageTemplateAction(
                        label='admin',
                        text='偉:D',
                    ),
                    MessageTemplateAction(
                        label='全部人',
                        text='全部訂餐',
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    if '我要點午餐' in msg:
        message = TextSendMessage(text='請輸入(姓名+我要訂X餐)')
        line_bot_api.reply_message(event.reply_token,message)
    if '王世偉,我要訂午餐' in msg:
        wei7018()
        message = TextSendMessage(text='王世偉,已幫您完成訂餐')
        line_bot_api.reply_message(event.reply_token,message)
    if '全部訂餐' in msg:
        all_lunch()
        message = TextSendMessage(text='全部人,已完成所有訂餐程序,可自行查看')
        line_bot_api.reply_message(event.reply_token,message)
if __name__ =='__main__':
    app.run()