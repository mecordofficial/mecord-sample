import json
import sys
from mecord import upload

resultDic = {
    "result" : [ 
    ],
    "status" : 0,           #0 is success
    "message" : ""
}

## 输入data参数, JSON格式如下: 
#   {
#      "task_id": [task_id],                    #任务id
#      "widget_id": [widget_id],                #组件id
#      "pending_count": [pending_count],        #待处理任务数
#      "fn_name": "test",
#      "param": {
#          "text":"Hello World"
#      }
#   }
def runTask(data):
    url = upload.upload("c://1.jpg")
    
    resultDic["result"].append({
        "type" : "image",
        "content": [ 
            url
        ],
        "extension" : {
            "info": "",
            "cover_url": ""
        }
    })
    return resultDic
