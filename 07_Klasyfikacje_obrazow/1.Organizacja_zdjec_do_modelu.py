import os
import shutil
import numpy as np

CLS_1 = 'horse'
CLS_2 = 'lion'
TRAIN_RATIO = 0.7
VALID_RATIO = 0.2
BASE_DIR = r'C:\Users\Misiek\Desktop\Zdjecia'
DATA_DIR = r'C:\Users\Misiek\Desktop\Zdjecia\image'

raw_no_of_files = {}
classes = (CLS_1, CLS_2)

for Class in classes:
    raw_no_of_files[Class] = len(os.listdir(os.path.join(DATA_DIR, Class)))

# print(raw_no_of_files)

train_dir = os.path.join(BASE_DIR, 'train')
valid_dir = os.path.join(BASE_DIR, 'valid')
test_dir = os.path.join(BASE_DIR, 'test')

train_cls_1_dir = os.path.join(train_dir, CLS_1)
valid_cls_1_dir = os.path.join(valid_dir, CLS_1)
test_cls_1_dir = os.path.join(test_dir, CLS_1)

train_cls_2_dir = os.path.join(train_dir, CLS_2)
valid_cls_2_dir = os.path.join(valid_dir, CLS_2)
test_cls_2_dir = os.path.join(test_dir, CLS_2)

setOfDirs = (train_dir, valid_dir, test_dir,
             train_cls_1_dir, valid_cls_1_dir, test_cls_1_dir,
             train_cls_2_dir, valid_cls_2_dir, test_cls_2_dir)

for dir in setOfDirs:
    if not os.path.exists(dir):
        os.mkdir(dir)


cls_1_names = os.listdir(os.path.join(DATA_DIR, CLS_1))
cls_2_names = os.listdir(os.path.join(DATA_DIR, CLS_2))


cls_1_names = [fname for fname in cls_1_names if fname.split('.')[1].lower() in [
    'jpg', 'png', 'jpeg']]
cls_2_names = [fname for fname in cls_2_names if fname.split('.')[1].lower() in [
    'jpg', 'png', 'jpeg']]


# Kopiowanie plików do folderów: treningowych, validacyjnych i testowych


def copy_files(listOfFiles, From, To, source, destination):
    for element in listOfFiles[From:To]:
        src = os.path.join(DATA_DIR, source, element)
        dst = os.path.join(destination, element)
        shutil.copyfile(src, dst)


copy_files(cls_1_names, 0, int(np.floor(TRAIN_RATIO * len(cls_1_names))),
           os.path.join(DATA_DIR, CLS_1), train_cls_1_dir)
copy_files(cls_1_names, int(np.floor(TRAIN_RATIO * len(cls_1_names))), int(np.floor((TRAIN_RATIO +
           VALID_RATIO) * len(cls_1_names))), os.path.join(DATA_DIR, CLS_1), valid_cls_1_dir)
copy_files(cls_1_names, int(np.floor((TRAIN_RATIO + VALID_RATIO) * len(cls_1_names))),
           len(cls_1_names), os.path.join(DATA_DIR, CLS_1), test_cls_1_dir)

copy_files(cls_2_names, 0, int(np.floor(TRAIN_RATIO * len(cls_2_names))),
           os.path.join(DATA_DIR, CLS_2), train_cls_2_dir)
copy_files(cls_2_names, int(np.floor(TRAIN_RATIO * len(cls_2_names))), int(np.floor((TRAIN_RATIO +
           VALID_RATIO) * len(cls_2_names))), os.path.join(DATA_DIR, CLS_2), valid_cls_2_dir)
copy_files(cls_2_names, int(np.floor((TRAIN_RATIO + VALID_RATIO) * len(cls_2_names))),
           len(cls_2_names), os.path.join(DATA_DIR, CLS_2), test_cls_2_dir)
