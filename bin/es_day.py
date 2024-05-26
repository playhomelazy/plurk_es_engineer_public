import json

#查詢偶像生日
def birth(content):
    search = content.replace("es工程師","").replace("生日","").replace(" ","")
    #載入es_data.json檔
    with open('../data/es_data.json','r',encoding="utf-8") as i:
        data = json.load(i)
        #逐筆搜尋data是否有吻合資料
        for idol in data:
            #找到吻合資料回傳
            if idol['name'].find(search) != -1 :
                idol_name = "偶像：" + idol['name']
                idol_birth = "生日：" + idol['birth']
                idol_team = "團體：" + idol['team']
                idol_profile = idol['profile']
                idol_img01 = idol['img01']
                return(idol_name + "\n" + idol_birth + "\n" + idol_team + "\n" + idol_profile +" " + idol_img01)
        return(0)    