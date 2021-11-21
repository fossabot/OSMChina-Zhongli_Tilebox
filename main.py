import wget
import random

TILE_SERVER={
    "OpenStreetMap Default(Carto)":["{protocol}{random}.tile.openstreetmap.org/{z}/{x}/{y}.png",["https","http"],"a-c"],
    "OpenStreetMap HOT":["{protocol}{random}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",["https","http"],"a-c"],
    "OSMChina":["{protocol}{random}.tile.openstreetmap.fr/{z}/{x}/{y}.png",["https","http"],""],
}

def fullURL(x:int,y:int,z:int,name):
    PROTOCOL_PREFIX_HTTPS = "https://"
    PROTOCOL_PREFIX_HTTP = "http://"
    PROTOCOL_PREFIX_FTP = "ftp://"
    Src=TILE_SERVER[name][0]
    Protocol_list=TILE_SERVER[name][1]
    if Random != "":
        Random_list=[TILE_SERVER[name][2].split("-")[0],TILE_SERVER[name][2].split("-")[1]]
    else:
        Random_list=""
    if Protocol_list[0]=="https":
        Src=Src.replace("{protocol}",PROTOCOL_PREFIX_HTTPS)
    elif Protocol_list[0]=="ftp":
        Src=Src.replace("{protocol}",PROTOCOL_PREFIX_FTP)
    else:
        Src=Src.replace("{protocol}",PROTOCOL_PREFIX_HTTP)
    if Random_list!="":
        Src=Src.replace("{random}",)


def RandomChar(begin:str,end:str):
    Range=int(ord(end)-ord(begin))
    tmp = random.randint(0, Range-1)
    return chr(ord(begin)+tmp)

for i in range(50):
    print(RandomChar("a","g"))


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
