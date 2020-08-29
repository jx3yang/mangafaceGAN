import cv2
from PIL import Image
from glob import glob

INPATH = 'output/full/'
OUTPATH = 'output/faces/'

HEIGHT_SCALE = 0.3
WIDTH_SCALE = 0.15
CASCADE_FILE = 'lbpcascade_animeface.xml'

TARGET_DIM = (64, 64)

cascade = cv2.CascadeClassifier(CASCADE_FILE)

def detect(filename):
    global cascade
    image = cv2.imread(filename, cv2.IMREAD_COLOR)

    stem = (filename.split('/')[-1]).split('.')[0]

    scale_percent = 300 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(
        gray,
        # detector options
        scaleFactor = 1.1,
        minNeighbors = 4,
        minSize = (5, 5)
    )

    for i, (x, y, w, h) in enumerate(faces):
        x_shift = int(w * WIDTH_SCALE)
        y_shift = int(h * HEIGHT_SCALE)

        face_image = cv2.resize(
            resized_image[
                max(0, y - y_shift) : min(y + y_shift + h, resized_image.shape[0]),
                max(0, x - x_shift) : min(x + x_shift + w, resized_image.shape[1])
            ],
            TARGET_DIM,
            interpolation=cv2.INTER_AREA
        )

        cv2.imwrite(
            f'{OUTPATH}{stem}-face{i}.jpg', face_image
        )

if __name__ == "__main__":
    files = glob(INPATH + '*')

    from multiprocessing import Pool

    with Pool(8) as pool:
        pool.map(detect, files)
