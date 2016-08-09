import caffe
import numpy as np
import cv2
import random

class AugDataLayer(caffe.Layer):

	def setup(self, bottom, top):
		pass

	def reshape(self, bottom, top):
		pass

	def forward(self, bottom, top):
		top[0].data[...].shape = bottom[0].data[...].shape		
		_, __, rows, cols = bottom[0].data[...].shape

		for batch in range(bottom[0].data[...].shape[0]):
			img = bottom[0].data[...][batch]

			# Flip left/right
			if random.random() > 0.5:
				img = cv2.flip(img,1)

			# Translation # -44 ~ 44 pixels (20%)
			'''
			if random.random() > 0.5:
				ratio = 0.2
				x = random.choice([1,-1])*int(cols*ratio*random.random())
				y = random.choice([1,-1])*int(rows*ratio*random.random())
				print x,y
				M = np.float32([[1,0,x],[0,1,y]])
				img = cv2.warpAffine(img, M, (cols, rows))
			'''
			
			# Brightness # Brighter
			if random.random() > 0.5:
				inc = 0.3*random.random()
				white = np.zeros((rows,cols)); white += 255
				for c in range(3):
					img[c,:,:] += ((white-img[c,:,:])*inc).astype(np.uint8)
			
			# Brightness # Darker	
			if random.random() > 0.5:
				inc = 0.5 * random.random() + 0.5
				black = np.zeros((rows,cols))
				for c in range(3):
					img[c,:,:] = (img[c,:,:]*inc).astype(np.uint8)
			
			# Occlusion
			if random.random() > 0.5:
				ratio = 0.2
				x = int(random.random()*cols*(1-ratio))
				y = int(random.random()*rows*(1-ratio))
				img[:, y:y+int(rows*ratio), x:x+int(cols*ratio)] = 0

			# Subtract vgg mean
			img = img.astype(np.float32)
			mean_pixel = [103.939, 116.779, 123.68]
			for c in range(3):
				img[c,:,:] -= mean_pixel[c]
			img = img.astype(np.uint8)
			top[0].data[...][batch] = img

	def backward(self, bottom, top):
		pass
