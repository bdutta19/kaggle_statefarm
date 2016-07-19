## Preparation
* Prepare LMDB data and place it in the 'data/statefarm_train_lmdb' path ([How to make LMDB file](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html))
* change path for 'net' and 'snapshot_prefix' in solver.prototxt
* change path for 'model_def' and 'model_weights' in make_submission.py

## Usage
Assuming caffe_root is your path to caffe directory
* **root_caffe/build/tools/caffe train -solver solver.prototxt -weights weights.caffemodel**
