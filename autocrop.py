from PIL import Image
import os
import time
import datetime

mappings = {
    # Image resolution -> Crop area
    (1080, 2220): (0, 66, 1080, 2088),
    # ...
}

def scan():
    for root, _, files in os.walk("."):
        for name in files:
            if not name.endswith(".png"):
                continue
            full_path = os.path.join(root, name)
            crop_if_need(full_path)


def crop_if_need(path):
    im = Image.open(path)
    if im.size in mappings:
        area = mappings[im.size]
        im.crop(area).save(path, quality=100)
        print('%s | Cropping %s' % (get_time(), path))


def get_time():
    now = datetime.datetime.now()
    return '%s:%s' % (now.hour, now.minute)


if __name__ == '__main__':
    print('Watching changes')
    while True:
        try:
            scan()
        except:
            pass
        time.sleep(1)
