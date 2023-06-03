import requests
import ast
import arrow

def getResultsApi():
    start = arrow.now()
    url = 'http://45.35.7.24:8080/ocr'
    image_path = 'images/screen.jpg'
    
    with open(image_path, 'rb') as f:
        files = {'image': f}
        r = requests.post(url, files=files)
    
    response = r.json()
    results = response["data"]
    results = [[ast.literal_eval(item[0]), item[1], item[2]] for item in results]
    #print(arrow.now() - start)
    return results




