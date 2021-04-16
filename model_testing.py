# -*- coding: utf-8 -*-
"""Model_Testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kYyqDpgcNZFduFx_MGXZxKQMEpZL8yg_
"""

#pipeline for evaluating modified u net performance w.r.t to brats validation dataset via nnUnet prediction masks
# dictionary mappings of tumor class : '0':Necrotic '1':Edema '2':Enhancing
dictionary_of_validation_score_of_nnUnet_from_brats_competiton = {'1':0.9719,'0':0.8524,'2':0.7945}
#Generating coarse binary mask from nnUnet using brats validation dataset
coarse_validation_ground_truth_from_nnUnet = np.zeros((125,240,240,155,3))
for i in range(100):
  h5data = h5py.File('/content/drive/MyDrive/BraTS2020_validation_data/volume_'+str(i), 'r')
  validation_data = np.array(h5data['data'])
  validation_data = np.expand_dims(validation_data,0)
  predicted_mask_nnUnet = nnUnet(validation_data)
  predicted_mask_nnUnet = predicted_mask_nnUnet.to_numpy()
  predicted_mask_nnUnet = np.where(predicted_mask_nnUnet>0.5,1,0)
  coarse_validation_ground_truth_from_nnUnet[i] = predicted_mask_nnUnet
#Generate predicted mask from modified u net model using brats validation dataset
predicted_mask_from_modified_unet = np.zeros((125,240,240,155,3))
for i in range(100):
  h5data = h5py.File('/content/drive/MyDrive/BraTS2020_validation_data/volume_'+str(i), 'r')
  validation_data = np.array(h5data['data'])
  #Flair matching
  validation_data[:,:,:,0] = hist_match(validation_data[:,:,:,0],target[:,:,:,0])
  #T1 weighted matching
  validation_data[:,:,:,1] = hist_match(validation_data[:,:,:,1],target[:,:,:,1])
  validation_data = np.expand_dims(validation_data,0)
  predicted_mask_modified_unet = modified_u_net(validation_data)
  predicted_mask_modified_unet = predicted_mask_modified_unet.to_numpy()
  predicted_mask_from_modified_unet[i] = predicted_mask_modified_unet

#Obtain Coarse Dice Score for modified u net model
dictionary_of_coarse_dice_score_per_tumor_class = validation_soft_dice_accuracy(predicted_mask_from_modified_unet,coarse_validation_ground_truth_from_nnUnet)

#Obtain Final Dice Score for modified u net model

dictionary_of_final_dice_score_per_tumor_class['0'] = dictionary_of_coarse_dice_score_per_tumor_class['0']*dictionary_of_validation_score_of_nnUnet_from_brats_competiton['0']
dictionary_of_final_dice_score_per_tumor_class['1'] = dictionary_of_coarse_dice_score_per_tumor_class['1']*dictionary_of_validation_score_of_nnUnet_from_brats_competiton['1']
dictionary_of_final_dice_score_per_tumor_class['2'] = dictionary_of_coarse_dice_score_per_tumor_class['2']*dictionary_of_validation_score_of_nnUnet_from_brats_competiton['2']






def validation_soft_dice_accuracy(y_pred,y_true,epsilon = 1e-6):
    a = {}
    for j in range(y_true.shape[-1]):
      total_sample_per_channel_loss = 0
      for i in range(y_true.shape[0]):
        numerator = 2*np.sum(y_pred[i,:,:,:,j]*y_true[i,:,:,:,j]) + epsilon
        denominator =  np.sum(y_true[i,:,:,:,j]**2) + np.sum(y_pred[i,:,:,:,j]**2) + epsilon
        total_sample_per_channel_loss = total_sample_per_channel_loss + numerator/denominator
      a[str(j)] = total_sample_per_channel_loss/y_true.shape[0]
    return a