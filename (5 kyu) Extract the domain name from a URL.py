import re

lst = ['https://www.cnet.com', 'http://www.zombie-bites.com',
       'http://wolf-bites.com', 'http://google.co.jp', 'https://pythex.org/',
       'www.xakep.ru', 'codewars']


def site_string(url):
    if ('www' or '//') in url:
        nome = re.search(r"\b((?<=[/.]).+(?=\.))", url)
        # print('a:', nome)
        if 'www' in nome.group(1):
            nome = re.search(r".+(?:w.)(.+)", str(nome))
            return ('a:', str(nome.group(1)[:-2]))
        elif '.' in nome.group(1):
            x = nome.group(1)
            print(x)
            nome = re.search(r"(.+)(?<=\b\.)", x).group(1)
            nome = nome.strip('.')
            return ('b:',nome)
        return (str(nome.group(1)))
    # else:
    #     if '.' in url:
    #         nome = re.search(r"((?<=).+(?=\.))", url)
    #         return (str(nome.group(1)))




for i in lst:
    print(site_string(i))

