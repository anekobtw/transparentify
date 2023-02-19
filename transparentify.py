from rembg import remove
from PIL import Image
import os

for file in os.listdir():
    if file.endswith(".png"):
        img_in = Image.open(file)
        img_out = remove(img_in)
        os.remove(file)
        img_out.save(file)

print("Done!")
print("Press Enter to exit ")
