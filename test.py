from spaceOCR import ocr_space_file
import arrow

print(arrow.now())
results = ocr_space_file()
try:
    items = results["ParsedResults"][0]["TextOverlay"]["Lines"]
    for item in items:
        print(item)
        text = item["LineText"]
        itemResult = { "name": text, "coords":  {"x": int(text["Words"][0]["left"]),"y": int(text["Words"][0]["top"])}}
        if("Jewel" in text):
            print(text)        
except Exception as e:
    print(e)
    pass

print(arrow.now())