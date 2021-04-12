# Abstract
Accurate estimation of the relative volume of the subcomponents of a braintumour is critical for monitoring progression, radiotherapy planning, outcomeassessment and follow-up studies. For this, accurate delineation of the tumour isrequired. Manual segmentation and 2 Dimensional Per Channel Per Plane analysis poses significant challenges for human experts in monitoring progression, radiotherapy planning, outcome
assessment because of the need to consult multiple images from different MRI sequences in order to classifytissue type correctly in 2D domain for 3D approximation. This laborious effort is not only time consuming but prone
to human error and results in significant intra- and inter-rater variability. To address this problem, an end to end automated project pipeline is developed and tested for 3D segmentation of tumor using Deep Learning and 3D visualisation of predicted tumor volume for effective analysis.
# Methodology :
## Project Pipeline consists two parts :
### Deep Learning :
-Data Set Acquisition
-Model Search
-Model Development
-Model Testing
-Model Tuning based on test results.
### 3D Rendering
-Acquiring 3D model attributes from voxel data using marching cubes algorithm
-Creating Mesh object of those attributes
-Creating Stl file
-Feeding stl file into viewer
-Empirical smoothing
