import requests
from bs4 import BeautifulSoup
import lxml.html
import re

def race_info(url):
    r=requests.get(url)
    r.encoding = r.apparent_encoding
    r=r.text
    #html=r.content
    html = lxml.html.fromstring(r)
    soup = BeautifulSoup(r,'html.parser')
    result=[]
    l=[]
    b=True
    for h in html.cssselect('div>span'):
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")[0].replace(" ","")
        if column=="":
            continue

        if column=="馬名":
            result.append(l)
            l=[]
            break
        l.append(column)

    ll=[["枠","馬番","馬名","性齢","斤量","騎手","厩舎","馬体重","url"]]
    l=[]
    for h in html.cssselect('tr.HorseList>td'):
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")[0].replace(" ","")
        if column=="--◎◯▲△☆&#10003消" or column=="---.-" or column=="":
            continue
        if column=="**":
            ll.append(l)
            l=[]
            continue
        l.append(column)

    for i in range(1,len(ll)):
        s=ll[i][2]
        url2=str(str(soup.find_all("a", attrs={"target": "_blank","title":s})[0]).split()[1]).replace("href=","").replace("\"","")
        ll[i].append(url2)

    result.append(ll)
    return result



def race_result(url):
    r=requests.get(url)
    r.encoding = r.apparent_encoding
    r=r.text
    #html=r.content
    html = lxml.html.fromstring(r)
    soup = BeautifulSoup(r,'html.parser')
    result=[]

    for h in html.cssselect('#tab_ResultSelect_1_con > div > table >thead> tr'):
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")
        l=[]
        for i in column:
            if i!="":
                l.append(i)
        result.append(l)

    for h in html.cssselect('#tab_ResultSelect_1_con > div > table >tbody> tr'):
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")
        l=[]

        for i in column:
            if i!="":
                l.append(i.replace(" ",""))
        result.append(l)

    for i in range(len(result)):
        if i==0:
            result[0].append("url")
        else:
            s=result[i][3]
            url2=str(str(soup.find_all("a", attrs={"target": "_blank","title":s})[0]).split()[1]).replace("href=","").replace("\"","")
            result[i].append(url2)
    return result

def zensou(url):
    r=requests.get(url)
    r.encoding = r.apparent_encoding
    r=r.text
    #html=r.content
    html = lxml.html.fromstring(r)
    soup = BeautifulSoup(r,'html.parser')
    result=[]
    l=[]
    b=False
    fi="1234567890"
    for h in html.cssselect('tbody >tr> td > a'):
        column = ((",".join(h.text_content().split("\n"))).lstrip(",").rstrip(",")).split(",")[0].replace(" ","")
        if b:
            l.append(column)
            b=False
        if column!="":
            if column[0] in fi and column[1] not in fi and column[-1] in fi:
                b=True
        if len(l)>=4:
            break
    ll=[]
    for i in l:
        url2="https://db.netkeiba.com"+str(str(soup.find_all("a", attrs={"title":i})[0]).split()[1]).replace("href=","").replace("\"","")
        ll.append([i,url2])
    return ll


url="https://race.netkeiba.com/race/shutuba.html?race_id=202009030806&rf=race_submenu"
r,l=race_info(url)

uma=[]
for ll in l[1:]:
    bamei=ll[2]
    url2=ll[-1]
    race=zensou(url2)
    uma.append([bamei,race])

print(r)
for i in uma:
    print(i)




    #url2=str(str(soup.find_all("a", attrs={"target": "_blank","title":s})[0]).split()[1]).replace("href=","").replace("\"","")
    #s=soup.find_all("a", attrs={"target": "_blank"})
    #print(s)