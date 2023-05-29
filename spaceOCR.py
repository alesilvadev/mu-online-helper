import requests

def ocr_space_file():
    payload = {
               'apikey': 'K88610246088957',
               'language': 'eng',
               'OCREngine': 3
               }
    with open('images/screen.jpg', 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={'images/screen.jpg': f},
                          data=payload
                          )
    response = r.json()
    return response["ParsedResults"][0]["TextOverlay"]["Lines"]




