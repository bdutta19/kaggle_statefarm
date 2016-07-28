# Kaggle/State Farm Image Classification Challenge
<div align="center">
  <img src="https://kaggle2.blob.core.windows.net/competitions/kaggle/5048/media/output_DEb8oT.gif"><br><br>
</div>
## Introduction
**State Farm** has hosted a [computer vision problem](https://www.kaggle.com/c/state-farm-distracted-driver-detection) to kagglers asking "Can you spot distracted drivers?" Given a dataset of 2D dashboard camera images, State Farm is challenging Kagglers to classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?

Competition requires you to handle raw images with relatively big size(4GB in total). Convolutional Neural Network is a mainstream technique widely used by participants of this competition, Kaggle admin also allowed participants to use pre-trained model to kick-start their performance if and only if a license term is not violated. Hence, various ImageNet pre-trained convolutional neural networks have been used (VGG-16, VGG-19, GoogleNet, Inception, ResNet and Darknets), with VGG and ResNet being the most popular on the forum. 

I approached this competition using a combination of VGG and ResNet implemented in two deep learning platforms - Keras and Caffe. Evaluation metric was [multi-class logarithmic loss](https://www.kaggle.com/wiki/MultiClassLogLoss). My submission scored around 0.25 in Public Leaderboard which ranks around Top 9%.

**Period:** April 5 2016 ~ August 1 2016 (118 total days)

## Related Works
* **VGG-16,-19 Model** from [Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/pdf/1409.1556.pdf)
* **GoogleNet Model** from [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/pdf/1512.00567v3.pdf)
* **ResNet-50,-101,-152 Model** from [Deep Residual Learning for Image Recognition](http://arxiv.org/pdf/1512.03385.pdf)
* VGG-16 ImageNet [pre-trained weights](https://gist.github.com/baraldilorenzo/07d7802847aaad0a35d3) (Keras)
* VGG-19 ImageNet [pre-trained weights](https://gist.github.com/baraldilorenzo/8d096f48a1be4a2d660d) (Keras)
* ResNet ImageNet [pre-trained weights](https://github.com/KaimingHe/deep-residual-networks) (Caffe)
* ResNet ImageNet [pre-trained weights](https://github.com/ry/tensorflow-resnet) (Tensorflow)
* Visualization of CNN inspired by [VGG-CAM](https://github.com/tdeboissiere/VGG16CAM-keras)

## Pipeline

### Tools
* Implemented on [Caffe](https://github.com/BVLC/caffe), [Keras](http://keras.io/)
* CNN Models: VGG-16, VGG-19, ResNet-50

### Image Preprocessing
* Occlusion: Zero out random block of 150x100 to simulate occlusion
* Translation: Random translation upto 0.2*Min(width, height)
* Scale: Scale change of +/- 0.2
* Mean subtraction: Following ImageNet procedure
* Resize: Original image(640x480) to (224x224)

### Convolutional Neural Networks
* VGG-16, VGG-19
* ResNet-50 

### Hyper Parameter Tuning
* Optimizers: Stochastic Gradient Descent, RMSprop, Adadelta, Adagrad
* Learning Rate: [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
* Epochs: [5, 10, 20] Epochs
* Cross Validation: 7-Fold Cross Validation split by driver
* Image Preprocessing was also part of hyper parameter

### Evaluation & Visualization
* Inhouse Validation loss correlated well with Public Leaderboard
* Visualization inspired by VGG-CAM model in Keras

### Submission
* Single Best Model: 
* Final Submission: 
* Private Leaderboard: 

## Lessons Learnt
* Resnet-152, the best CNN model who won ImageNet2015, is too big for this model (overfits)
* VGG-16, VGG-19, GoogleNet, ResNet-50 trained from scratch did not converge (frankly, I could not find learning policy to converge)
* Visualizing CNN is cumbersome, but definitely fun!
* Keras is good starting point for CNN, especially validating ideas and brain-storming
* Caffe is fast, efficient and abundant in resources(pre-trained weights, CNN related papers with implementations in Caffe)
* Intended same setup in Keras, Caffe, Tensorflow, but results differ -> need to dig deeper into implementation of each platforms
* After all, I have the same tools/model architecture as top ranking kagglers. I need to improve on Machine Learning part (cross-validation, generalization, quick and smart iteration)
* Competition makes me learn
