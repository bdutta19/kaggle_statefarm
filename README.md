# Kaggle/State Farm Image Recognition Challenge
<div align="center">
  <img src="https://kaggle2.blob.core.windows.net/competitions/kaggle/5048/media/output_DEb8oT.gif"><br><br>
</div>
## Introduction
**State Farm** has hosted a computer vision problem to kagglers asking "Can you spot distracted drivers?" Given a dataset of 2D dashboard camera images, State Farm is challenging Kagglers to classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?

**Started:** April 5 2016

**Ends:** August 1 2016 (118 total days)

## Pipeline

### Tools
* Implemented on Caffe, Keras
* CNN Models: VGG-16, VGG-19, ResNet-50

### Image Preprocessing
* Occlusion: Zero out random block of 150x100 to simulate occlusion
* Translation: Random translation upto 0.2*Min(width, height)
* Scale: Scale change of +/- 0.2
* Mean subtraction: Following ImageNet procedure
* Resize: Original image(640x480) to (224x224)

### Learning Algorithm
* VGG-16 with pre-trained weights (Keras)
* VGG-19 with pre-trained weights (Keras)
* ResNet-50 with pre-trained weights (Caffe)

### Hyper Parameter Tuning
* Optimizers: Stochastic Gradient Descent, RMSprop, Adadelta, Adagrad
* Learning Rate: [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
* Epochs: [5, 10, 20] Epochs
* Cross Validation: 7-Fold Cross Validation split by driver
* Image Preprocessing was also part of hyper parameter

### Evaluation & Visualization
* Inhouse Validation loss correlated well with Public Leaderboard
* Visualization inspired by VGG-CAM

### Submission
* Single Best Model: 
* Final Submission: 
* Private Leaderboard: 

### Lessions Learnt
* Resnet-152, the best CNN model who won ImageNet2015, is too big for this model (overfits)
* VGG-16, VGG-19, GoogleNet, ResNet-50 trained from scratch did not converge (frankly, I could not find learning policy to converge)
* Visualizing CNN is cumbersome, but definitely fun!
* Keras is good starting point for CNN, especially validating ideas and brain-storming
* Caffe is fast, efficient and abundant in resources(pre-trained weights, CNN related papers with implementations in Caffe)
* Competition makes me learn
