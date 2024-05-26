import json
special_chars = "!@#$%^&*()_+[]{};:,./<>?\|`~-='"


def time(content):
    songs_list = []
    for char in special_chars:
        search = content.replace(char, "")
    #載入es_songs.json檔
    with open('..\data\es_songs.json','r',encoding="utf-8") as i:
        data = json.load(i)
        #逐筆搜尋data是否有吻合資料
        for songs in data:
            #找到吻合資料回傳
            if search.find(songs['teams']) != -1 :
                songs_list.append(songs['yt_links'])
        return songs_list[random.randrange(len(songs_list))]