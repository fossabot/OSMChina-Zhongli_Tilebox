import wget

url1 = "https://"


def randomc():
    import random
    tmp = random.randint(0, 2)
    if tmp == 0:
        return 'a' + "."
    elif tmp == 1:
        return 'b' + "."
    elif tmp == 2:
        return 'c' + "."


# url2 = "tile.openstreetmap.org/15/26679/13744.png"
# url2 = "tile.osmchina.org/15/26679/13744.png"
url2 = "tile.osmchina.org/0/0/0.png"
url = url1 + url2
# url=url1+randomc()+url2

# file = wget.download(url,"user-agent"=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
file = wget.download(url)
print(file)

# useragent="Mozilla/5.0"
# # useragent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
#
# import os
# cmd="wget "+url+" --user-agent "+useragent
# print(cmd)
# os.system(cmd)
