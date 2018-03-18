import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-file', type=str)

args = parser.parse_args()

filename1 = '/home/chicm/ml/kaggle/dsb2018/data/__download__/stage1_train/%s/images/%s.png'%(args.file, args.file)
filename2 = '/home/chicm/ml/kaggle/dsb2018/data/image/stage1_train/images/%s.png'%(args.file)

img1_c = cv2.imread(filename1)
img1_g = cv2.imread(filename1, 0)

img2_c = cv2.imread(filename2)
img2_g = cv2.imread(filename2, 0)

cv2.imshow('img1c', img1_c)
cv2.imshow('img1g', img1_g)
cv2.imshow('img2c', img2_c)
cv2.imshow('img2g', img2_g)

cv2.waitKey(0)
cv2.destroyAllWindows()

