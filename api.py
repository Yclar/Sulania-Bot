import requests
from bs4 import BeautifulSoup

dix = ([[0, 0] for x in range(10001)])  # 单词存储
area = ([[0, 0] for x in range(0, 5001)])  # 地区存储
global area_cnt  # 地区数量统计
area_cnt = 0
global word_num  # 单词数量统计
word_num = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63'
                 ' Safari/537.36'
}  # 爬虫用headers


def read_file(filename):  # 读入文件
    if filename == 'dic':  # 苏拉语词典用
        f = open("dic", encoding='utf-8')
        num = 0
        for line in f:
            pure_line = line.replace('\n', '')
            word_str = pure_line.split('#')
            dix[num][0] = word_str[0]
            dix[num][1] = word_str[1]
            num += 1
        f.close()
        global word_num
        word_num = num
    elif filename == 'area':  # 墨迹天气用
        global area_cnt
        f = open("area", encoding='utf-8')
        for line in f:
            pure_line = line.replace('\n', '')
            area_infor = pure_line.split('#')
            area[area_cnt][0] = area_infor[0]
            area[area_cnt][1] = area_infor[1]
            area_cnt += 1
        f.close()
    return


def keyword_sev(message, uid):  # 私人对话用
    if message[0:5] == '/help':
        help_list(-1, uid)
    elif message[0:5] == '/setu':
        setu(-1, uid)
    elif message[0:13] == '/risonix_setu':
        real_setu(-1, uid)
    elif message[0:2] == '骂我':
        fk(-1, uid)
    elif message[0:8] == '/weather':
        weather(-1, uid, message[9:])
    elif message[0:6] == '/music':
        music(-1, uid, message[7:])
    return


def keyword(message, uid, gid):  # 群聊用
    if message[0:5] == '/setu':
        setu(gid, uid)
    elif message[0:5] == '/help':
        help_list(gid, uid)
    elif message[0:13] == '/risonix_setu':
        real_setu(gid, uid)
    elif message[0:2] == '骂我':
        fk(gid, uid)
    elif message[0:8] == '/weather':
        weather(gid, uid, message[9:])
    return


def real_setu(gid, uid):  # R18的色图
    url = 'https://api.lolicon.app/setu?size1200=true&r18=1'
    menu = requests.get(url)
    setu_url = menu.json()['data'][0]['url']
    print(menu.json())
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            '[CQ:image,file=' +str(setu_url) + r']'))
    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            '[CQ:image,file=' +str(setu_url) + r']'))


def setu(gid, uid):  # 普通的色图
    url = 'https://api.lolicon.app/setu?size1200=true'
    menu = requests.get(url)
    setu_url = menu.json()['data'][0]['url']  # 对传回来的涩图网址进行数据提取
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            '[CQ:image,file=' + str(setu_url) + r']'))
    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            '[CQ:image,file=' + str(setu_url) + r']'))


def help_list(gid, uid):  # 帮助列表
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            'Monasi~\nDe os Sulania!\nNa nowa,tot contilu os:\n'
            '1.help\n'+'2.setu'+'3./kaxi Sulaian <word>'))
    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            'Monasi~\nDe os Sulania!\n'+'Na nowa,tot '+'contilu os:\n'
            '1./help\n'+'2./setu\n'+'3./kaxi Sulaian <word>'))
    return


def fk(gid, uid):
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            '[CQ:at,qq=' + str(uid) + r'] ' + '就这？你还没有我主人变态呢！（笑）'))

    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            '就这？你还没有我主人变态呢！（笑）'))

    return


def dic(gid, uid, message):  # 苏拉语词典
    read_file('dic')
    msg = message
    print(msg)
    for i in range(0, word_num + 1):
        if msg == dix[i][0]:
            if gid != -1:
                requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
                    '[CQ:at,qq= ' + str(uid) + r']\n' + '这是' + str(dix[i][1]) + '的意思！'))
            else:
                requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
                    '这是' + str(dix[i][1]) + '的意思！'))
            return
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            '[CQ:at,qq= ' + str(uid) + r']\n' + '啊咧，你在糊弄我吗？没有这个词欸~'))
    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            '啊咧，你在糊弄我吗？没有这个词欸~'))
    return


def weather(gid, uid, loc):  # 墨迹天气抓取
    read_file('area')
    global area_cnt
    for i in range(0, area_cnt+1, 1):
        if loc == area[i][0]:
            r = requests.get(area[i][1], headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            infor = soup.find_all('meta')[2].attrs['content']
            if gid != -1:
                requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
                    '[CQ:at,qq= ' + str(uid) + r']\n' +infor))
            else:
                requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid, infor))
            return
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            '[CQ:at,qq= ' + str(uid) + r']\n' + '抱歉，目前还没有收录该地区~'))

    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            '抱歉，目前还没有收录该地区~'))
    return


def music(gid, uid, sch):
    r = requests.get(url='https://api.ayano.top/music/index.php?api=search&music=netease&search=' + sch)
    id_ = r.json()[0]['id']
    # r = requests.get(url='https://api.ayano.top/music/index.php?api=url&music=netease&id=' + str(id_))
    # music_file = r.json()['url']
    # 音乐自定义时再用QAQ
    if gid != -1:
        requests.get(url='http://127.0.0.1:5000/send_group_msg?group_id={0}&message={1}'.format(gid,
            '[CQ:music,type=163,id=' + str(id_) + r']'))
    else:
        requests.get(url='http://127.0.0.1:5000/send_private_msg?user_id={0}&message={1}'.format(uid,
            '[CQ:music,type=163,id=' + str(id_) + r']'))
    return


# 非常感谢《【Re：从零开始的QQ机器人搭建】——基于go-cqhttp和python》这篇文章以及其作者 “世界第一可爱不咕鸟”
# 是TA为本代码提供了根基（就是有一点小bug，已修复，应该是port的问题,除此以外还有 lolicon_api 已不需要 key）
