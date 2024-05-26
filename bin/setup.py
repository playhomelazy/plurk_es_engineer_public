import re
import json
import urllib
 
from plurk_oauth import PlurkAPI
import es_info as info
import es_songs as songs

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
        if not msgs :
            continue
        for msg in msgs:
            pid = msg.get('plurk_id')
            if msg.get('type') == 'new_response':
                content = msg['response'].get('content_raw')
                #確認呼叫ES工程師
                if ("抽卡" in content) or ("攜手空間" in content) or ("卡片總覽" in content):
                    continue
                if ("es工程師" in content ) or ("ES工程師" in content ):
                    es_response = ""
                    #偶像查詢
                    if ("查詢" in content ):
                        es_response = info.info(content)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    #隨機隊伍選歌呼叫
                    if ("歌" in content ):
                        es_response = songs.choose(content)
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    #抽出幸運偶像(隨機挑選)
                    if ("幸運偶像" in content ) :
                        es_response = info.lucky_idol()
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    elif ("幸運組合" in content ) :
                        es_response = info.lucky_group()
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    if ("格言" in content ):
                        es_response = info.motto()
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    if ("悄悄話" in content ):
                        es_response = info.secret()
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })
                    if es_response == "":
                        es_response = "怎麼了(•ω•`)?"
                        plurk.callAPI('/APP/Responses/responseAdd',{'plurk_id': pid, 'content': es_response,  'qualifier': ':' })    
                else:
                    continue