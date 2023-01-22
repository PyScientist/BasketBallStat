from requests import Session
import fake_useragent
import random

proxy_list_inside_long = ['socks5://51.222.146.133:59166',
                          'socks5://147.182.142.189:80',
                          'socks5://54.210.239.35:80',
                          'socks5://161.35.48.185:443',
                          'socks5://167.99.236.14:80',
                          'socks5://51.222.13.193:10084',
                          'socks5://163.116.158.28:8081',
                          'socks5://163.116.158.118:8081',
                          'socks5://172.104.20.199:59166',
                          'socks5://162.216.18.189:59166',
                          'socks5://159.203.13.82:59166',
                          'socks5://159.65.220.89:59166',
                          'socks5://68.183.25.31:59166',
                          'socks5://192.81.216.55:59166',
                          'socks5://157.245.223.201:59166',
                          'socks5://104.45.128.122:80',
                          'socks5://161.35.125.167:59166',
                          'socks5://67.207.89.36:59166',
                          'socks5://157.245.130.145:59166',
                          'socks5://159.89.34.109:59166',
                          'socks5://163.116.158.142:8081',
                          'socks5://159.203.87.195:59166',
                          'socks5://142.44.241.192:59166',
                          'socks5://165.227.79.99:59166',
                          'socks5://159.223.163.14:55894',
                          'socks5://157.245.247.84:59166',
                          'socks5://165.227.187.48:59166',
                          'socks5://157.230.186.5:59166',
                          'socks5://157.245.253.92:59166',
                          'socks5://167.71.190.131:59166',
                          ]

proxy_list_inside_dict = [
              {
               'https': 'socks5://165.227.187.48:59166',
               },
              {
                 'https': 'socks5://157.245.223.201:59166',
              },
              {
                'https': 'socks5://68.183.25.31:59166',
              },
              {
                'https': 'socks5://159.65.220.89:59166',
              },
             ]


def random_proxy(test_url):
    counter = 0
    response = None
    while True:
        counter += 1
        proxies = {'https': random.choice(proxy_list_inside_long)}
        # proxies = random.choice(proxy_list_inside_dict)
        user_agent = fake_useragent.UserAgent().random
        header = {'user-agent': user_agent}
        session = Session()
        session.headers.update(header)
        try:
            response = session.get(test_url, proxies=proxies, headers=header, timeout=3)
            if response.status_code == 200:
                break
        except Exception as e:
            # print(e)
            pass
        if counter > 90:
            break
    return response, proxies


if __name__ == '__main__':
    url = 'https://2ip.ru'
    # url = 'https://www.google.com/'
    for x in range(20):
        print(random_proxy(url))
