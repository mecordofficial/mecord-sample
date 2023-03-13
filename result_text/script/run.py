import cv2
import requests
import os

def errorResult(msg):
    return {
        "result" : [ ],
        "status" : -1,
        "message" : msg
    }

def successResult(txt1, txt2):
    return {
        "result" : [ 
                {
                    "type" : "text",
                    "content": [ 
                        txt1,
                        txt2
                    ],
                    "extention" : {
                        "info": "",
                        "cover_url": ""
                    }
                }
        ],
        "status" : 0,
        "message" : ""
    }

def runTask(data):
    inputUrl = data["param"]["url"]
    savePath = "c://result_text.mp4"
    download_res = requests.get(inputUrl)
    with open(savePath, "wb") as c:
        c.write(download_res.content)

    if os.path.exists(savePath) == False:
        return errorResult("file not found")
    cap = cv2.VideoCapture(savePath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
   
    return successResult(f"video size is {width}x{height}", 
                         f"video fps is {fps}")
