import json
import random
special_chars = "!@#$%^&*()_+[]{};:,./<>?\|`~-=' 　"

#查詢偶像資料
def info(content):
    for char in special_chars:
        search = content.replace(char, "")
    search = search.replace(" ","").replace("es工程師","").replace("ES工程師","").replace("查詢","")
    #載入es_data.json檔
    with open('./data/es_data.json','r',encoding="utf-8") as i:
        data = json.load(i)
        #逐筆搜尋data是否有吻合資料
        for idol in data:
            #找到吻合資料回傳 and 判斷關鍵字非空白
            if idol['name'].find(search) >= 0 and search != "":
                idol_name = "偶像：" + idol['name']+ "\n"
                idol_team = "團體：" + idol['team']+ "\n"
                idol_hight = "身高：" + str(idol['hight']) +"cm"+ "\n"
                idol_weight = "體重：" + str(idol['weight']) + "kg"+ "\n"
                idol_blood = "血型：" + idol['blood'] + "\n"
                idol_birth = "生日：" + idol['birth']+ "\n"
                idol_star_sign = "星座：" + idol['star_sign']+ "\n"
                idol_profile = idol['profile']
                idol_owna1a = idol['owna1a']
                return(idol_name + idol_team + idol_hight + idol_weight + idol_blood + idol_birth + idol_star_sign +idol_profile+ " " + idol_owna1a)

        return("要跟我說是誰喔！( •̀ ω •́ )✧")    
    
#幸運偶像
def lucky_idol():
    lucky_num = random.randrange(49)
    with open('./data/es_data.json','r',encoding="utf-8") as i:
        data = json.load(i)
        idol = data[lucky_num]
        idol_name = "偶像：" + idol['name']
        idol_team = " (" + idol['team']+ ")\n"
        idol_profile = idol['profile']
        idol_owna1a = idol['owna1a']
        return("**幸運偶像是！！！**\n\n" + idol_name + idol_team  +idol_profile + " " + idol_owna1a)
    
#幸運組合
def lucky_group():
    with open('./data/es_data.json','r',encoding="utf-8") as i:
        cp_01 = random.randrange(49)
        cp_02 = random.randrange(49)
        while cp_01 == cp_02:
            cp_02 = random.randrange(49)
        data = json.load(i)
        idol01 = data[cp_01]
        idol02 = data[cp_02]
        
        idol01_name = idol01['name']
        idol02_name = idol02['name']

        idol01_team = " (" + idol01['team']+ ")"
        idol02_team = " (" + idol02['team']+ ")\n"

        idol01_img = idol01['owna1a']
        idol02_img = idol02['owna1a']

        return("**這次的幸運組合是！！！**\n\n" + idol01_name + idol01_team + " 和 " + idol02_name + idol02_team  + idol01_img + " "  +idol02_img)


#偶像夢幻祭格言    
def motto():
    with open('./data/es_motto.json','r',encoding="utf-8") as i:
        data = json.load(i)
        num = random.randrange(len(data))
        motto = data[num]
        motto_num = str(motto['number'])
        motto_top = '**【' + motto['motto'] + '】**\n'
        motto_content = motto['content']
        return("#偶像夢幻祭格言" + motto_num + "\n" + motto_top  + motto_content)
    
#偶像夢幻祭悄悄話
def secret():
    with open('./data/es_secret.json','r',encoding="utf-8") as i:
        data = json.load(i)
        num = random.randrange(len(data))
        secret = data[num]
        secret_num = str(secret['number'])
        secret_content = secret['content']
        return("#ES大樓悄悄話" + secret_num + "\n"  + secret_content)