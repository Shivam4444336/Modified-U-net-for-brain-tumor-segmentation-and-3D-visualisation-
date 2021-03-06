# -*- coding: utf-8 -*-
"""Data_Augmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12fIDyyctXkJKeyustw1BM7mxyzODnOPc
"""

# Workflow of data augmentation : Direct grid distortion function selects one of the three axis randomly and applies grid distortion, then after zoom in from randomly selected factor from discrete set of value is applied

import albumentations
from scipy.ndimage import zoom

def grid_distortion_axis_0(data,mask):
  data = np.swapaxes(data,0,2)
  mask = np.swapaxes(mask,0,2)
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_grid = np.zeros(shape=data.shape)
  mask_grid = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    dict_ = albumentations.GridDistortion(p=1,distort_limit=0.7)(image = data[:,:,:,i],mask = mask[:,:,:,i])
    data_grid[:,:,:,i] = dict_['image']
    mask_grid[:,:,:,i] = dict_['mask']
  data = np.swapaxes(data_grid,0,2)
  mask = np.swapaxes(mask_grid[:,:,:,0:-1],0,2)
  return data,mask

  
  
def grid_distortion_axis_1(data,mask):
  data = np.swapaxes(data,1,2)
  mask = np.swapaxes(mask,1,2)
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_grid = np.zeros(shape=data.shape)
  mask_grid = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    dict_ = albumentations.GridDistortion(p=1,distort_limit=0.7)(image = data[:,:,:,i],mask = mask[:,:,:,i])
    data_grid[:,:,:,i] = dict_['image']
    mask_grid[:,:,:,i] = dict_['mask']
  data = np.swapaxes(data_grid,1,2)
  mask = np.swapaxes(mask_grid[:,:,:,0:-1],1,2)
  return data,mask
  

def grid_distortion_axis_2(data,mask):
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_grid = np.zeros(shape=data.shape)
  mask_grid = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    dict_ = albumentations.GridDistortion(p=1,distort_limit=0.7)(image = data[:,:,:,i],mask = mask[:,:,:,i])
    data_grid[:,:,:,i] = dict_['image']
    mask_grid[:,:,:,i] = dict_['mask']
  
  return data_grid,mask_grid[:,:,:,0:-1]


def zoom_factor_1(data,mask):
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_zoom = np.zeros(shape=data.shape)
  mask_zoom = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    output_data = zoom(data[:,:,:,i],(0.83,0.83,0.83))
    data_zoom[:,:,:,i] = np.pad(output_data,pad_width=((21,20),(21,20),(13,13)))
    output_mask = zoom(mask[:,:,:,i],(0.83,0.83,0.83))
    mask_zoom[:,:,:,i] = np.pad(output_mask,pad_width=((21,20),(21,20),(13,13)))
  return data_zoom,mask_zoom[:,:,:,0:-1]

def zoom_factor_2(data,mask):
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_zoom = np.zeros(shape=data.shape)
  mask_zoom = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    output_data = zoom(data[:,:,:,i],(0.77,0.77,0.77))
    data_zoom[:,:,:,i] = np.pad(output_data,pad_width=((28,27),(28,27),(18,18)))
    output_mask = zoom(mask[:,:,:,i],(0.77,0.77,0.77))
    mask_zoom[:,:,:,i] = np.pad(output_mask,pad_width=((28,27),(28,27),(18,18)))
  return data_zoom,mask_zoom[:,:,:,0:-1]

def zoom_factor_3(data,mask):
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_zoom = np.zeros(shape=data.shape)
  mask_zoom = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    output_data = zoom(data[:,:,:,i],(0.71,0.71,0.71))
    data_zoom[:,:,:,i] = np.pad(output_data,pad_width=((35,35),(35,35),(23,22)))
    output_mask = zoom(mask[:,:,:,i],(0.71,0.71,0.71))
    mask_zoom[:,:,:,i] = np.pad(output_mask,pad_width=((35,35),(35,35),(23,22)))
  return data_zoom,mask_zoom[:,:,:,0:-1]

def zoom_factor_4(data,mask):
  mask = np.append(mask,np.zeros(shape=mask.shape[:-1]),axis=-1)
  data_zoom = np.zeros(shape=data.shape)
  mask_zoom = np.zeros(shape.data.shape)
  for i in range(data.shape[-1]):
    output_data = zoom(data[:,:,:,i],(0.67,0.67,0.67))
    data_zoom[:,:,:,i] = np.pad(output_data,pad_width=((40,39),(40,39),(26,25)))
    output_mask = zoom(mask[:,:,:,i],(0.67,0.67,0.67))
    mask_zoom[:,:,:,i] = np.pad(output_mask,pad_width=((40,39),(40,39),(26,25)))
  return data_zoom,mask[:,:,:,0:-1]

def zoom_in(data,mask):
  zoom_in_factors = [zoom_factor_1,zoom_factor_2,zoom_factor_3,zoom_factor_4]
  data,mask = zoom_in_factors[random.randrange(4)](data,mask)
  return data,mask
#augmentation function
def direct_grid_distortion(data,mask):
  grid_distortions = [grid_distortion_axis_0,grid_distortion_axis_1,grid_distortion_axis_2]
  data,mask = grid_distortions[random.randrange(3)](data,mask)
  zoom_yes_or_not = [zoom_in,no_zoom]
  data,mask = zoom_yes_or_not[random.randrange(2)](data,mask)
  return data,mask

def no_zoom(data,mask):
  return data,mask