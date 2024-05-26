import random
import json
import math

card_pool = [0]*9000 + [1]*700 + [2]*300

#10抽
def draw_ten(id):
    pool = []
    idol = []
    for i in range(10):
        pool.append(random.choice(card_pool))
        idol.append(random.randrange(49))

    #存檔
    show = save_data(id, pool, idol)
    show_3stars = "、".join(show[0])
    show_4stars = "、".join(show[1])
    show_5stars = "、".join(show[2])
    result = "抽卡10抽，結果如下：\n"
    if show_5stars != "":
        result = result + "5★：" + show_5stars +"\n"
    if show_4stars != "":
        result = result + "4★：" + show_4stars +"\n"
    if show_3stars != "":
        result = result + "3★：" + show_3stars +"\n"
    return result


#存檔
def save_data(id, pool, idol):
    show_list = [[],[],[]]
    with open('./member/' + str(id) + '.json','r',encoding="utf-8") as json_data:
        load_data = json.load(json_data)
        exp = load_data['exp']
        fans = load_data['fans']
        stars3 = load_data['3_stars']
        stars4 = load_data['4_stars']        
        stars5 = load_data['5_stars']
        with open('./data/es_data.json','r',encoding="utf-8") as idol_json_data:
            idol_data = json.load(idol_json_data)
            for i in range(len(pool)):
                if(pool[i] == 0):
                    stars3[idol[i]] = stars3[idol[i]] + 1
                    fans = fans + 10
                    show_list[0].append(idol_data[idol[i]]["second_name"])
                elif(pool[i] == 1):
                    stars4[idol[i]] = stars4[idol[i]] + 1
                    fans = fans + 70
                    show_list[1].append(idol_data[idol[i]]["second_name"])
                elif(pool[i] == 2):
                    stars5[idol[i]] = stars5[idol[i]] + 1
                    fans = fans + 300
                    show_list[2].append(idol_data[idol[i]]["second_name"])
            #經驗值+10
            exp = exp + 10

            update = {
                'exp': exp,
                '3_stars': stars3,
                '4_stars': stars4,
                '5_stars': stars5,
                'fans': fans
            }
            
            load_data.update(update)
            update_data = json.dumps(load_data, ensure_ascii=False) 
            with open('./member/' + str(id) + '.json','w',encoding="utf-8") as write_data:
                write_data.write(update_data)
            return show_list

#個人資料
def member_data(id):
    with open('./member/' + str(id) + '.json','r',encoding="utf-8") as json_data:
        load_data = json.load(json_data)
        exp = load_data["exp"]
        level = str(math.floor(math.sqrt(exp / 10)))
        stars3 = str(sum(load_data["3_stars"]))
        stars4 = str(sum(load_data["4_stars"]))
        stars5 = str(sum(load_data["5_stars"]))
        return "【攜手空間】\n等級：" + level + "\n" + "總粉絲數：" + str(load_data["fans"] )+ "人" + "\n5星卡總數：" + stars5 + "張\n4星卡總數：" + stars4 + "張\n3星卡總數：" + stars3 +"張"
    
def stars_cards(id):
    with open('./member/' + str(id) + '.json','r',encoding="utf-8") as json_data:
        load_data = json.load(json_data)
        stars3 = load_data["3_stars"]
        stars4 = load_data["4_stars"]
        stars5 = load_data["5_stars"]
        star_pro_cards = "【STARMAKER PRODUCTION】：(由左至右，5★至3★)\n"
        with open('./data/es_data.json','r',encoding="utf-8") as idol_json_data:
            idol_data = json.load(idol_json_data)
            for i in range(17):
                star_pro_cards = star_pro_cards + "[emo150]" + idol_data[i]["second_name"] + "：" + str(stars5[i]) + "、" + str(stars4[i]) + "、" + str(stars3[i]) +"  "
        return star_pro_cards

def cos_cards(id):
    with open('./member/' + str(id) + '.json','r',encoding="utf-8") as json_data:
        load_data = json.load(json_data)
        stars3 = load_data["3_stars"]
        stars4 = load_data["4_stars"]
        stars5 = load_data["5_stars"]
        cos_pro_cards = "【COSMIC PRODUCTION】：(由左至右，5★至3★)\n"
        with open('./data/es_data.json','r',encoding="utf-8") as idol_json_data:
            idol_data = json.load(idol_json_data)
            for i in range(17, 29):
                cos_pro_cards = cos_pro_cards + "[emo150]" + idol_data[i]["second_name"] + "：" + str(stars5[i]) + "、" + str(stars4[i]) + "、" + str(stars3[i]) +"  "
        return cos_pro_cards
    
def rhy_cards(id):
    with open('./member/' + str(id) + '.json','r',encoding="utf-8") as json_data:
        load_data = json.load(json_data)
        stars3 = load_data["3_stars"]
        stars4 = load_data["4_stars"]
        stars5 = load_data["5_stars"]
        rhy_cards = "【Rhythm Link】：(由左至右，5★至3★)\n"
        with open('./data/es_data.json','r',encoding="utf-8") as idol_json_data:
            idol_data = json.load(idol_json_data)
            for i in range(29, 40):
                rhy_cards = rhy_cards + "[emo150]" + idol_data[i]["second_name"] + "：" + str(stars5[i]) + "、" + str(stars4[i]) + "、" + str(stars3[i]) +"  "
        return rhy_cards
    
def new_di_cards(id):
    with open('./member/' + str(id) + '.json','r',encoding="utf-8") as json_data:
        load_data = json.load(json_data)
        stars3 = load_data["3_stars"]
        stars4 = load_data["4_stars"]
        stars5 = load_data["5_stars"]
        new_di_cards = "【NEW DIMENSION】：(由左至右，5★至3★)\n"
        with open('./data/es_data.json','r',encoding="utf-8") as idol_json_data:
            idol_data = json.load(idol_json_data)
            for i in range(40, 49):
                new_di_cards = new_di_cards + "[emo150]" + idol_data[i]["second_name"] + "：" + str(stars5[i]) + "、" + str(stars4[i]) + "、" + str(stars3[i]) +"  "
        return new_di_cards
