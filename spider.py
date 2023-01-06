import requests
import json
import time

for i in range(0,9): ############每换一个声优都需要改############
    url = "https://www.voistock.com/ja/voicelist/vlist-ajax.php"

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    } 

    data = '''{
        "columns": [
            {"data": "datalist",       "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "playbtn",        "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "voiceText",      "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "characternames", "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "titleName",      "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "contentsName",   "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "voiceactnames",  "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "playCount",      "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "voiceEmotions",  "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "voiceTags",      "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "voiceLanguage",  "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "userNickname",   "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "submitDate",     "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "download",       "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "favorite",       "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true},
            {"data": "playlist",       "name": "", "searchable": true, "orderable": true, "search": {"value": "", "regex": false}, "searchable": true}
        ],
        "draw": %s,
        "lang": "ja",
        "length": 100,
        "myId": "632320873e418657950e7544",
        "order": [{"column": 12, "dir": "desc"}],
        "search": {"value": "花江夏樹", "regex": false},
        "searchword": "花江夏樹",
        "start": %s
    }'''%(i+1, i*100)

    resp = requests.post(url, headers=headers, data=data.encode())

    print(resp)
    text = json.loads(resp.text)
 
    with open(f'json-desc/花江夏樹Hanae Natsuki/{str(i).zfill(4)}.json', mode="w", encoding="utf-8") as file:
        file.write(json.dumps(text, indent=4, ensure_ascii=False))
    
    time.sleep(1)
    resp.close()
