# -*- coding: utf-8 -*-
"""Training_Metrics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FVomR1C2pMuTIZDK5FnsVuqUgE5Fo7Oc
"""

def soft_dice_loss(y_pred,y_true,epsilon = 1e-6):
  total_channel_loss = 0
  for j in range(y_true.shape[-1]):
    numerator = 2.*K.sum(y_pred[:,:,:,:,j]*y_true[:,:,:,:,j]) + epsilon
    denominator =  K.sum(y_true[:,:,:,:,j]**2) + K.sum(y_pred[:,:,:,:,j]**2) + epsilon
    total_channel_loss = total_channel_loss + 1-(numerator/denominator)
  average_channel_loss = total_channel_loss/y_true.shape[-1]
  return average_channel_loss

def soft_dice_accuracy(y_pred,y_true,epsilon = 1e-6):
  total_channel_accuracy = 0
  for j in range(y_true.shape[-1]):
    numerator = 2.*K.sum(y_pred[:,:,:,:,j]*y_true[:,:,:,:,j]) + epsilon
    denominator =  K.sum(y_true[:,:,:,:,j]**2) + K.sum(y_pred[:,:,:,:,j]**2) + epsilon
    total_channel_accuracy = total_channel_accuracy + numerator/denominator
  average_channel_accuracy = total_channel_accuracy/y_true.shape[-1]
  return average_channel_accuracy