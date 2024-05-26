import re
import json
import urllib
 
from plurk_oauth import PlurkAPI
import es_gacha as ga
import new_data as new

with open('./keys/API.keys', 'r+') as f: 
    key = json.load(f)
    plurk = PlurkAPI(key["CONSUMER_KEY"], key["CONSUMER_SECRET"])
    plurk.authorize(key["ACCESS_TOKEN"], key["ACCESS_TOKEN_SECRET"])
    comet = plurk.callAPI('/APP/Realtime/getUserChannel')
    comet_channel = comet.get('comet_server') + "&new_offset=%d"
    jsonp_re = re.compile('CometChannel.scriptCallback\((.+)\);\s*');
    new_offset = -1
    while True:
        plurk.callAPI('/APP/Alerts/addAllAsFriends')
        req = urllib.request.urlopen(comet_channel % new_offset, timeout=80)
        rawdata = req.read().decode('utf-8')
        match = jsonp_re.match(rawdata)
        if match:
            rawdata = match.group(1)
        data = json.loads(rawdata)
        new_offset = data.get('new_offset', -1)
        msgs = data.get('data')
        if not msgs:
            continue
        for msg in msgs:
            pid = msg.get('plurk_id')
            if msg.get('type') == 'new_response':
                content = msg['response'].get('content_raw')
                user_id = msg['response']['user_id']
                #確認呼叫ES工程師
                if ("es工程師" in content ) or ("ES工程師" in content ):
                    new.check_member(user_id)
                    es_response = ""
                    #偶像查詢
                    if ("抽卡" in content ):
                        es_response = ga.draw_ten(user_id)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    if ("攜手空間" in content ):
                        es_response = ga.member_data(user_id)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    if ("卡片總覽" in content ):
                        es_response = ga.stars_cards(user_id)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                        es_response = ga.cos_cards(user_id)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                        es_response = ga.rhy_cards(user_id)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                        es_response = ga.new_di_cards(user_id)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                else:
                    continue