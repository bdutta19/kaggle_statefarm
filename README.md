# Kaggle/State Farm Image Classification Challenge
<div align="center">
  <img src="https://kaggle2.blob.core.windows.net/competitions/kaggle/5048/media/output_DEb8oT.gif"><br><br>
</div>
## Introduction
**State Farm** has hosted a computer vision problem to kagglers asking "Can you spot distracted drivers?" Given a dataset of 2D dashboard camera images, State Farm is challenging Kagglers to classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?

**Started:** April 5 2016

**Ends:** August 1 2016 (118 total days)

## Pipeline

### Tools
* Implemented on [Caffe](https://github.com/BVLC/caffe), [Keras](http://keras.io/)
* CNN Models: VGG-16, VGG-19, ResNet-50
#### Related Papers: 
* VGG-16,-19 from [Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/pdf/1409.1556.pdf)
* ResNet-50 from [Deep Residual Learning for Image Recognition](http://arxiv.org/pdf/1512.03385.pdf)

### Image Preprocessing
* Occlusion: Zero out random block of 150x100 to simulate occlusion
* Translation: Random translation upto 0.2*Min(width, height)
* Scale: Scale change of +/- 0.2
* Mean subtraction: Following ImageNet procedure
* Resize: Original image(640x480) to (224x224)

### Convolutional Neural Networks
* VGG-16 with pre-trained weights (Keras) [here](https://gist.github.com/baraldilorenzo/07d7802847aaad0a35d3)
* VGG-19 with pre-trained weights (Keras) [here](https://gist.github.com/baraldilorenzo/8d096f48a1be4a2d660d)
* ResNet-50 with pre-trained weights (Caffe) [here](https://github.com/KaimingHe/deep-residual-networks)

### Hyper Parameter Tuning
* Optimizers: Stochastic Gradient Descent, RMSprop, Adadelta, Adagrad
* Learning Rate: [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
* Epochs: [5, 10, 20] Epochs
* Cross Validation: 7-Fold Cross Validation split by driver
* Image Preprocessing was also part of hyper parameter

### Evaluation & Visualization
* Inhouse Validation loss correlated well with Public Leaderboard
* Visualization inspired by VGG-CAM model in Keras [here](https://github.com/tdeboissiere/VGG16CAM-keras)

### Submission
* Single Best Model: 
* Final Submission: 
* Private Leaderboard: 

## Lessions Learnt
* Resnet-152, the best CNN model who won ImageNet2015, is too big for this model (overfits)
* VGG-16, VGG-19, GoogleNet, ResNet-50 trained from scratch did not converge (frankly, I could not find learning policy to converge)
* Visualizing CNN is cumbersome, but definitely fun!
* Keras is good starting point for CNN, especially validating ideas and brain-storming
* Caffe is fast, efficient and abundant in resources(pre-trained weights, CNN related papers with implementations in Caffe)
* Competition makes me learn
