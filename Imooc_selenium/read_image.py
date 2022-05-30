#codinng=utf-8
import ddddocr
oct = ddddocr.DdddOcr(old=True)
with open("D:/mooc_images/test1.png", "rb") as f:
    image = f.read()
res = oct.classification(image)
print(res)
