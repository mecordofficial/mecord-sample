import ffmpy
import cv2
import requests
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
    func = data["fn_name"]
    if func != "testMedia":
        return

    errorCode = 0
    url = ""
    try:
        duration = float(data["param"]["duration"])
        size = (544, 960)

        saveImage = "c://result_video_audio_image.jpg"
        imgRes = requests.get(data["param"]["image"])
        with open(saveImage, "wb") as c:
            c.write(imgRes.content)

        saveAudio = "c://result_video_audio_audio.mp3"
        audioRes = requests.get(data["param"]["audio"])
        with open(saveAudio, "wb") as c:
            c.write(audioRes.content)

        videoWritter = cv2.VideoWriter(r'c://out.mp4', -1, 30, size)
        imgData = cv2.imread(saveImage)
        for i in range(duration*30):
            videoWritter.write(imgData)
        videoWritter.release()

        url = upload.upload('c://out.mp4', "video/mpeg4")
        
        resultDic["result"].append({
            "type" : "video",
            "content": [ 
                url
            ],
            "extention" : {
                "info": "",
                "cover_url": ""
            }
        })
    except:
        errorCode = -1
        msg = "somthing error happen "
        
    resultDic["status"] = errorCode
    resultDic["message"] = msg
    return resultDic
