import requests
import re
import os
# https://hosts.gitcdn.top/hosts.txt


"""
订阅更新hosts使github访问通畅
作者：清凉禹

cron: 0 8 * * *
"""

def get_hosts(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except:
        return False


def edit_hosts(file,new_hosts):
    with open(file, 'r', encoding='UTF-8') as f:
        # 读取hosts文件,删除github部分原内容
        old = f.read()
        new = re.sub(r'# fetch-github-hosts begin[\n.a-z0-9\u4e00-\u9fa5 -:]*# fetch-github-hosts end', '', old)
    with open(file,'w',encoding='UTF-8') as f:
        # 追加新hosts
        if new[-1] != '\n':
            new=new+'\n'
        f.write(new+new_hosts[:-2])



def main():
    hosts_url = 'https://hosts.gitcdn.top/hosts.txt'
    hosts = '\etc\hosts'
    if os.path.exists(hosts) == False:
        print('hosts文件不存在，请检查hosts路径')
        exit()
    new_hosts = get_hosts(hosts_url)
    if new_hosts:
        edit_hosts(hosts, new_hosts)
        print('hosts更改完成')
    else:
        print('hosts文件源获取异常')
        exit()




if __name__ == '__main__':
    main()


