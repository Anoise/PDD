# This file must be put in the same dir with dataset.
import glob

path = '/home/dl/data/datasetupload/'

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.jpg'):
            print(jpg_file,'dd')
            tf.write(jpg_file + '\n')

generate_train_and_val(path + 'trainimg/', 'train.txt')
generate_train_and_val(path + 'testimg/', 'val.txt')

print('ok ...')