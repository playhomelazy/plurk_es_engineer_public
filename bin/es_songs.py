import json
import random
special_chars = "!@#$%^&*()_+[]{};:,./<>?\|`~-=' "


def choose(content):
    songs_list = []
    count = 0
    for char in special_chars:
        search = content.replace(char, "").replace('es工程師', "").replace('ES工程師', "").replace('歌', "")
    print(search)
    #載入es_songs.json檔
    with open('./data/es_songs.json','r',encoding="utf-8") as i:
        data = json.load(i)
        #逐筆搜尋data是否有吻合資料
        for songs in data:
            #找到吻合資料回傳
            if (search in songs['teams']): 
                songs_list.append(songs['yt_links']) 
                
            else: count += 1
        #如有找到指定隊伍，則隊伍隨機選歌
        list_len = len(songs_list)
        if(list_len != 0): return songs_list[random.randrange(list_len)]
        #隨機選歌
        elif(list_len == 0): return data[random.randrange(count)]["yt_links"]
        else: return "工程師查無此歌！"