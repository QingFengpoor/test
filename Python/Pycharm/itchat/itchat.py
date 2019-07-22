# codeing=utf8

import requests
import itchat

Key="b6c592efc06e46a89dbdb3adff2f454b"

def get_response(msg):
    print("bei diao yong!")
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    api_data = {"apikey": Key,
                "info":msg,
                }
    try:
        r=requests.post(api_url,data=api_data).json()
        return r.get('text')
    except:
        print("fa sheng cuo wu")
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    print(msg.User)
    print(msg.User['NickName']+msg['Text'])
    defaultReply="I received:"+msg['Text']
    reply="I am a Robot:"+get_response(msg['Text'])
    return reply or defaultReply
itchat.auto_login(hotReload=False)
itchat.run()
