import os
from PIL import Image

#region direction
#base direction
base_dir=r'C:\Users\12991\Desktop\Py_file\experiment_buliding_dataset_10_24\cats_and_dogs_filtered'
train_dir=os.path.join(base_dir,'train')
val_dir=os.path.join(base_dir,'validation')
train_cats_dir=os.path.join(train_dir,'cats/')
train_dogs_dir=os.path.join(train_dir,'dogs/')
val_cats_dir=os.path.join(val_dir,'cats/')
val_dogs_dir=os.path.join(val_dir,'dogs/')

#list file path
train_cats_fname=os.listdir(train_cats_dir)
train_dogs_fname=os.listdir(train_dogs_dir)
val_cats_fname=os.listdir(val_cats_dir)
val_dogs_fname=os.listdir(val_dogs_dir)

#Create directories in digital permission mode
os.mkdir(train_dir+'/resize_cats')
os.mkdir(train_dir+'/resize_dogs')
os.mkdir(val_dir+'/resize_cats')
os.mkdir(val_dir+'/resize_dogs')

#resize
for i in train_cats_fname:
    original_img=Image.open(train_cats_dir+i)
    clipping_img=original_img.resize((150,150),Image.ANTIALIAS)
    clipping_img.save(train_dir+'/resize_cats/'+i)
for i in train_dogs_fname:
    original_img=Image.open(train_dogs_dir+i)
    clipping_img=original_img.resize((150,150),Image.ANTIALIAS)
    clipping_img.save(train_dir+'/resize_dogs/'+i)
for i in val_cats_fname:
    original_img=Image.open(val_cats_dir+i)
    clipping_img=original_img.resize((150,150),Image.ANTIALIAS)
    clipping_img.save(train_dir+'/resize_cats/'+i)
for i in val_dogs_fname:
    original_img=Image.open(val_dogs_dir+i)
    clipping_img=original_img.resize((150,150),Image.ANTIALIAS)
    clipping_img.save(train_dir+'/resize_dogs/'+i)

#endregion
