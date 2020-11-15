import os
import tensorflow as tf
from PIL import Image

cwd=r'C:\Users\12991\Desktop\Py_file\experiment_buliding_dataset_10_24\cats_and_dogs_filtered\train'
classes=('resize_cats','resize_dogs')
#Class to write records to a TFRecord file
writer=tf.compat.v1.python_io.TFRecordWriter('cas_and_dogs_train_onehot.tfrecords')

for index,name in enumerate(classes):
    class_path=cwd+'/'+name+'/'
    for img_name in os.listdir(class_path):
        img_path=class_path+img_name
        img=Image.open(img_path)
        img_raw=img.tobytes()
        example=tf.train.Example(features=tf.train.Feature(feature={
            'label':tf.train.Feature(int64_list=tf.train.Int64List(value=[1,0] if index==0 else[0,1])),
            'img_raw':tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
            }))
        writer.write(example.SerializeToString())

writer.close()