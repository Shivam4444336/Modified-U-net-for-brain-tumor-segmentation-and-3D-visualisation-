# Abstract
Accurate estimation of the relative volume of the subcomponents of a braintumour is critical for monitoring progression, radiotherapy planning, outcomeassessment and follow-up studies. For this, accurate delineation of the tumour isrequired. Manual segmentation and 2 Dimensional Per Channel Per Plane analysis poses significant challenges for human experts in monitoring progression, radiotherapy planning, outcome
assessment because of the need to consult multiple images from different MRI sequences in order to classifytissue type correctly in 2D domain for 3D approximation. This laborious effort is not only time consuming but prone
to human error and results in significant intra- and inter-rater variability. To address this problem, an end to end automated project pipeline is developed and tested for 3D segmentation of tumor using Deep Learning and 3D visualisation of predicted tumor volume for effective analysis.
# Methodology :
## Project Pipeline consists two parts:
### Deep Learning:
- Data Set Acquisition
- Model Search
- Model Development
- Model Testing
- Model Tuning based on test results.
### 3D Rendering
- Acquiring 3D model attributes from voxel data using marching cubes algorithm
- Creating Mesh object of those attributes
- Creating Stl file
- Feeding stl file into viewer
- Empirical smoothing

## Dataset Acquisition:
For model training we have used brats 2020 dataset which provides volumetric data of MRI modality of four channels : flair, t1, t1-post-contrast and t2 per patient sample with ground truths of 3 classes : Enhancing Tumor, Edema & Necrotic.
- Volumetric Data Size per sample per channel  = 240,240,155
- Total Samples = 369
## Model Search:
U net has became ideal choice for medical image segmentation among researchers and deep learning engineers.
Various variants of U net model are proposed by researchers.
- [1] Proposed a variant of U net with following modifications:
  - Replaced Batch Normalisation with Group Normalisation
  - Used Res-Net Blocks as backbone
  - Addition of Auto Encoder branch to encoder endpoint.
- [2] Proposed a variant of U net with following modifications:
  - Employed Two Stage Cascaded U net 
  - First Stage U net was used to generate coarse prediction for Second stage U net.
  - Second Stage U net has two decoder branch with different deconvolution strategies.
- [3] Proposed a variant of U net with following modifications:
  - Auxiliary segmentation outputs, which are used for deep supervision, branch off at two lowest resolutions in the decoder with softmax non linearity. 
  - Used Instance Normalisation.
## Model Development:
### Model architecture and details:
The model architecture follows U net configuration and resnet block as backbone with below mentioned modifications.
- Proposed model takes whole multichannel 3D volumetric data as input without slicing it into patch.
- Group Normalization is used instead of Batch because of batch size constraints.
- Model encoder pools the input data up to reasonable stride of 8 . 
- Convolution operation pools the volumetric data instead of conventional Max Pooling Operations.
- Use of swish activation function in intermediate layers instead of relu.  
  -Reason : 
    - Use of relu activation function can hinder learning of some tumor patterns. 
    - Swish activation function makes error space smooth which leverages the probability of better convergence.
- Use of two 3*3*3 kernels parallely to reduce overfitting.
- Collective use of Convolution Transpose and Linear Interpolation technique to leverage probability of good accuracy.




