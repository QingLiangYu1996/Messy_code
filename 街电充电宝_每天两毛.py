# -- coding:UTF-8 --
import base64
import time, sys  # re 用于正规则处理,os可能要用于文件路径读取与判断
import requests as req
import multiprocessing as mp

# import urllib.parse  # 用于url code 的编解码
# from costtime import time_counts  # 用来统计时间
# import sendNotify  # 发通知
# from requests import HTTPError

#################################
'''
使用方法
入口：微信打开：http://u3v.cn/6vJFM2 跳转游览器打开，网页登陆，抓包unionid、token的值
 作者：newhackerman 
 日期：2023-10-15
 功能 	街电充电宝  骗子项目 ,不要充钱
  header:unionid token
    变量格式：export jdcdbck='unionid值&token值'
    多账号换行分割
 定时：1天一次
 cron: 2 8 * * *  设置提现时间，24小时一次

 [task_local]

 [rewrite_local]

 [MITM]

 '''
#################################

import os, sys  # line:1

configfile = '/ql/data/config/config.sh'  # line:4
configfile1 = './config.sh'  # line:5
configdict = {}  # line:7


def get_configdict():  # line:8
    if os.path.exists(configfile):  # line:9
        with open(configfile, 'r', encoding='utf8') as O00O0O000O000O0O0:  # line:10
            O0OO0O00OOOO00OOO = O00O0O000O000O0O0.readlines()  # line:11
            if O0OO0O00OOOO00OOO is None:  # line:12
                sys.exit()  # line:13
            for OO0OO0OO0O00000O0 in O0OO0O00OOOO00OOO:  # line:14
                OO0OO0OO0O00000O0 = str(OO0OO0OO0O00000O0).replace('\n', '').replace('\'', '', -1).replace('\"', '',
                                                                                                           -1)  # line:15
                if OO0OO0OO0O00000O0 == '' or OO0OO0OO0O00000O0 is None:  # line:16
                    continue  # line:17
                if OO0OO0OO0O00000O0.strip()[0] == '#':  # line:18
                    continue  # line:19
                if 'export' in OO0OO0OO0O00000O0.strip():  # line:20
                    OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.replace('export', '', -1)  # line:21
                OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.split('=', 1)  # line:22
                if len(OO0OO0OO0O00000O0) < 2:  # line:23
                    continue  # line:24
                OOO0O0000OOOOOOO0 = OO0OO0OO0O00000O0[0].strip()  # line:25
                O00OO0O0OO00OO00O = OO0OO0OO0O00000O0[1].strip()  # line:26
                configdict[OOO0O0000OOOOOOO0] = O00OO0O0OO00OO00O  # line:27
    elif os.path.exists(configfile1):  # line:28
        with open(configfile1, 'r', encoding='utf8') as O00O0O000O000O0O0:  # line:29
            O0OO0O00OOOO00OOO = O00O0O000O000O0O0.readlines()  # line:30
            if O0OO0O00OOOO00OOO is None:  # line:31
                sys.exit()  # line:32
            for OO0OO0OO0O00000O0 in O0OO0O00OOOO00OOO:  # line:33
                OO0OO0OO0O00000O0 = str(OO0OO0OO0O00000O0).replace('\n', '').replace('\'', '', -1).replace('\"', '',
                                                                                                           -1)  # line:34
                if OO0OO0OO0O00000O0 == '' or OO0OO0OO0O00000O0 is None:  # line:35
                    continue  # line:36
                if OO0OO0OO0O00000O0.strip()[0] == '#':  # line:37
                    continue  # line:38
                if 'export' in OO0OO0OO0O00000O0.strip():  # line:39
                    OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.replace('export', '', -1)  # line:40
                OO0OO0OO0O00000O0 = OO0OO0OO0O00000O0.split('=', 1)  # line:41
                if len(OO0OO0OO0O00000O0) < 2:  # line:42
                    continue  # line:43
                OOO0O0000OOOOOOO0 = OO0OO0OO0O00000O0[0].strip()  # line:44
                O00OO0O0OO00OO00O = OO0OO0OO0O00000O0[1].strip()  # line:45
                configdict[OOO0O0000OOOOOOO0] = O00OO0O0OO00OO00O  # line:46
    else:  # line:47
        print('未找到配置文件！！，请检查配置文件路径与文件名')  # line:48


get_configdict()  # line:50


def getconfig(O0000O0OOO0000O0O):  # line:52
    return configdict[O0000O0OOO0000O0O]  # line:53


def setconfig(OO0OO0O0O0O0O0O00, O0OOO00OOOOO0O000):  # line:56
    configdict[OO0OO0O0O0O0O0O00] = O0OOO00OOOOO0O000  # line:57


def change_param_value_tofile(OO0O0O000O0O00O0O, OO000OOOOO0O00O0O):  # line:59
    if os.path.exists(configfile):  # line:61
        O00O000O00OO0O00O = []  # line:62
        with open(configfile, 'r', encoding='utf8') as O0000OOOO0OOOO0OO:  # line:63
            O0O00OOO0O0000O00 = O0000OOOO0OOOO0OO.readlines()  # line:64
            for O00OO0O00O00OOO00 in O0O00OOO0O0000O00:  # line:65
                if OO0O0O000O0O00O0O in O00OO0O00O00OOO00.strip():  # line:66
                    OOOO0000OO0OO0OO0 = getconfig(OO0O0O000O0O00O0O)  # line:67
                    O00OO0O00O00OOO00 = O00OO0O00O00OOO00.replace(OOOO0000OO0OO0OO0, OO000OOOOO0O00O0O)  # line:68
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:69
                else:  # line:70
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:71
        if len(O00O000O00OO0O00O) > 0:  # line:73
            with open(configfile, 'r', encoding='utf8') as OOOO00O0OOO0O000O:  # line:74
                OOOO00O0OOO0O000O.writelines(O00O000O00OO0O00O)  # line:75
    elif os.path.exists(configfile1):  # line:77
        O00O000O00OO0O00O = []  # line:78
        with open(configfile1, 'r', encoding='utf8') as O0000OOOO0OOOO0OO:  # line:79
            O0O00OOO0O0000O00 = O0000OOOO0OOOO0OO.readlines()  # line:80
            for O00OO0O00O00OOO00 in O0O00OOO0O0000O00:  # line:81
                if OO0O0O000O0O00O0O in O00OO0O00O00OOO00:  # line:83
                    OOOO0000OO0OO0OO0 = getconfig(OO0O0O000O0O00O0O)  # line:84
                    print('替换前：', O00OO0O00O00OOO00)  # line:85
                    O00OO0O00O00OOO00 = O00OO0O00O00OOO00.replace(OOOO0000OO0OO0OO0, OO000OOOOO0O00O0O)  # line:86
                    print('替换后：', O00OO0O00O00OOO00)  # line:87
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:88
                else:  # line:89
                    O00O000O00OO0O00O.append(O00OO0O00O00OOO00)  # line:90
        if len(O00O000O00OO0O00O) > 0:  # line:93
            with open(configfile1, 'w', encoding='utf8') as OOOO00O0OOO0O000O:  # line:94
                OOOO00O0OOO0O000O.writelines(O00O000O00OO0O00O)  # line:95
        else:  # line:96
            print('未找到配置文件')  # line:97


def getcookies(env):  # line:99
    cookies = os.getenv(env).split('\n')
    result = []
    for cookie in cookies:
        result.append(cookie)
    return result


def dict_to_str(OO0000O000O0000O0):  # line:106
    O0OOO0OOO0OOO00O0 = ''  # line:107
    if OO0000O000O0000O0:  # line:108
        if isinstance(OO0000O000O0000O0, dict):  # line:109
            for O00000OOO0OO00OOO, O00O0O00OO0O000O0 in OO0000O000O0000O0.items():  # line:111
                O0O0O0OO0000OOO0O = f'%s: %s \n' % (O00000OOO0OO00OOO, O00O0O00OO0O000O0)  # line:112
                O0OOO0OOO0OOO00O0 += O0O0O0OO0000OOO0O  # line:113
        else:  # line:114
            return OO0000O000O0000O0  # line:115
    return O0OOO0OOO0OOO00O0


# ------------------------------
session = req.session()  # line:1


def starttask(OO0OOO0OO000OOO00, OO0OO0O000OOOO000, OO000O00OO000000O):  # line:2
    OOO00O0OO0OO0OO00 = tasks(OO0OOO0OO000OOO00, OO0OO0O000OOOO000, OO000O00OO000000O)  # line:3
    OOO00O0OO0OO0OO00.runtasklist()  # line:4


class tasks():  # line:5
    def __init__(OOOO0OOO0OO0O00OO, OO00O0OOO00O0OO00, O00O0OOOO0O0O00OO, OOO0O0O0OO0O0O000):  # line:6
        OOOO0OOO0OO0O00OO.times = 0  # line:7
        O0O00OOO0OO00OOOO = '第%s 个账号' % (OOO0O0O0OO0O0O000)  # line:8
        OOOO0OOO0OO0O00OO.resultdict = {}  # line:9
        OOOO0OOO0OO0O00OO.resultdict['说明'] = '街电充电宝 web 骗子项目 1天签到领0.2到提现到支付宝'  # line:10
        OOOO0OOO0OO0O00OO.resultdict[O0O00OOO0OO00OOOO] = ''  # line:11
        OOOO0OOO0OO0O00OO.unionid = OO00O0OOO00O0OO00  # line:12
        OOOO0OOO0OO0O00OO.token = O00O0OOOO0O0O00OO  # line:13
        OOOO0OOO0OO0O00OO.headers = {'Host': 'www.hmytuea.cn', 'Connection': 'keep-alive', 'Content-Length': '42',
                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                                     'unionid': OOOO0OOO0OO0O00OO.unionid, 'token': OOOO0OOO0OO0O00OO.token,
                                     'Content-Type': 'application/json', 'Accept': '*/*',
                                     'Origin': 'http://www.ngsuazw.cn', 'Referer': 'http://www.ngsuazw.cn/',
                                     'Accept-Encoding': 'gzip, deflate',
                                     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}  # line:14

    def runtasklist(OOOOO0O00000OOO00):  # line:15
        O00OOOOOO00OO000O = OOOOO0O00000OOO00.jdcdbck_sign()  # line:16
        time.sleep(0.2)  # line:17
        OOOOO0O00000OOO00.jdcdbck_pushcash()  # line:18
        print(OOOOO0O00000OOO00.resultdict)  # line:19
        print('执行结果：', OOOOO0O00000OOO00.resultdict)  # line:20

    def jdcdbck_sign(O0OOOOO000O00O0O0):  # line:21
        OOO0O0000O0OOOOO0 = base64.decodebytes(
            'aHR0cDovL3d3dy5obXl0dWVhLmNuL3VzZXIvYWRkbXlvcmRlcjA='.encode('utf8'))  # line:22
        OO0OOO0O0O00O0OOO = OOO0O0000O0OOOOO0  # line:23
        O0OO00OO00O000OOO = {"unionid": O0OOOOO000O00O0O0.unionid}  # line:24
        try:  # line:25
            OOOOOOOO0OO0O0O00 = session.post(url=OO0OOO0O0O00O0OOO, headers=O0OOOOO000O00O0O0.headers,
                                             json=O0OO00OO00O000OOO, timeout=5)  # line:26
            if OOOOOOOO0OO0O0O00.status_code == 200:  # line:27
                O00OOO00OOOO000OO = OOOOOOOO0OO0O0O00.json()  # line:28
                if O00OOO00OOOO000OO.get('content'):  # line:29
                    O0OOOOO000O00O0O0.resultdict['签到获得'] = O00OOO00OOOO000OO['content']  # line:30
            else:  # line:31
                print(OOOOOOOO0OO0O0O00.content.decode('utf8'))  # line:32
        except BaseException as O00O0OO0O0O0O0OOO:  # line:33
            print(O00O0OO0O0O0O0OOO)  # line:34

    def jdcdbck_pushcash(O0O00O0O00O0OO000):  # line:35
        OOOO0O0000O0O00OO = base64.decodebytes(
            'aHR0cDovL3d3dy5obXl0dWVhLmNuL3RyYWRlL3B1c2hjYXNo'.encode('utf8'))  # line:36
        OO0O00O0O0O00O0O0 = OOOO0O0000O0O00OO  # line:37
        O0O000O0O0O00000O = {"unionid": O0O00O0O00O0OO000.unionid, "money": 0.2}  # line:38
        try:  # line:39
            O000O00O0O000OO0O = session.post(url=OO0O00O0O0O00O0O0, headers=O0O00O0O00O0OO000.headers,
                                             json=O0O000O0O0O00000O, timeout=5)  # line:40
            if O000O00O0O000OO0O.status_code == 200:  # line:41
                O00O00OOO00O0OO0O = O000O00O0O000OO0O.json()  # line:42
                if O00O00OOO00O0OO0O.get('data') == 1:  # line:43
                    O0O00O0O00O0OO000.resultdict['提现'] = '提现成功，请在支付宝查看'  # line:44
                else:  # line:45
                    O0O00O0O00O0OO000.resultdict['提现'] = O00O00OOO00O0OO0O.get('content')  # line:46
            else:  # line:47
                print(O000O00O0O000OO0O.content.decode('utf8'))  # line:48
        except BaseException as O0OOO00OO00OO0OO0:  # line:49
            print(O0OOO00OO00OO0OO0)  # line:50


if __name__ == '__main__':  # line:51
    cookies = getcookies('jdcdbck')  # line:52
    if len(cookies) > 5:  # line:53
        print('请勿一次性跑太多账号，造成服端与本机压力！')  # line:54
    i = 0  # line:55
    if cookies is not None:  # line:56
        for cookie1 in cookies:  # line:57
            cookie = str(cookie1).split('&')  # line:58
            unionid = cookie[0]  # line:59
            token = cookie[1]  # line:60
            i += 1  # line:61
            process = mp.Process(target=starttask, args=(unionid, token, i,))  # line:62
            process.start()  # line:63
            if i % 5 == 0:  # line:64
                time.sleep(120)  # line:65
        sys.exit()  # line:66
    else:  # line:67
        print('未配置cookies')  # line:68
        sys.exit(0)  # line:69
