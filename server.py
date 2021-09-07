import requests
from flask import Flask, request

import api

app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    # msg = request.get_json().get('raw_message')
    if request.get_json().get('message_type') == 'private':  # 如果是私聊信息
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        if (message[0:13] == '/kaxi Sulaian') & (int(len(message)) == 13 or int(len(message)) == 14):  # 苏拉词典功能
            requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
                'Os chi kala de questa?\nChi kaxi questa?\n请输入需要查询的苏拉语词汇！'))
        elif (message[0:13] == '/kaxi Sulaian') & (len(message) > 14):
            api.dic(-1, uid, message[14:])
        else:
            api.keyword_sev(message, uid)
    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        if (message[0:13] == '/kaxi Sulaian') & (len(message) == 13 or len(message) == 14):  # 苏拉词典功能
            requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
                '[CQ:at,qq=' + str(uid) + r']' + '\nOs chi kala de questa?\nChi kaxi questa?\n请输入需要查询的苏拉语词汇！'))
        elif (message[0:13] == '/kaxi Sulaian') & len(message) > 14:
            api.dic(gid, uid, message[14:])
        else:
            api.keyword(message, uid, gid)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=7700)
