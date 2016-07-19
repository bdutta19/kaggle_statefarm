import sys 
caffe_root = '/root/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe
import os
import glob
import pandas as pd
import datetime
import math
import numpy as np

print 'Loading a model...'
caffe.set_mode_gpu()
model_def = 'model-predict.prototxt'
model_weights = 'weights/snapshot_iter_72000.caffemodel'
net = caffe.Net(model_def, model_weights, caffe.TEST)

# Preprocessing
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
mean_file = np.array([103.939, 116.779, 123.68])
transformer.set_mean('data', mean_file) # subtract mean
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))
net.blobs['data'].reshape(1,3,224,224)

print 'Predicting test images...'
path = os.path.join('../data/test/*.jpg')
files = glob.glob(path)
ids = []
preds = [] 
count = 0
thr = math.floor(len(files)/10)
for fl in files:
	flbase = os.path.basename(fl)
	ids.append(flbase)
	image = caffe.io.load_image(fl)
	transformed_image = transformer.preprocess('data',image)
	net.blobs['data'].data[...] = transformed_image
	output = net.forward()
	output_prob = output['prob'][0]
	preds.append(list(output_prob))
	count += 1
	if count % thr == 0:
		print 'Predicted {} images from {}'.format(count, len(files))
print 'Predicted all images from {}'.format(len(files)) 

# Creating submission
print 'Creating submission...'
result = pd.DataFrame(preds, columns = ['c0','c1','c2','c3','c4','c5','c6','c7','c8','c9'])
result.loc[:, 'img'] = pd.Series(ids, index=result.index)
now = datetime.datetime.now()
subm_path = 'subm'
if not os.path.isdir(subm_path):
	os.mkdir(subm_path)
sub_file = os.path.join(subm_path,'submission_' + str(now.strftime("%Y-%m-%d-%H-%M")) + '.csv')
result.to_csv(sub_file, index=False)
