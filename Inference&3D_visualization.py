{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Inference&3D visualization.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPeQUC1y1TdWh4VgiQ2wYUe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Shivam4444336/Modified-U-net-for-brain-tumor-segmentation-and-3D-visualisation-/blob/main/Inference%263D_visualization.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uy_SgSsaexca"
      },
      "source": [
        "#inference and 3D visualization script per sample\n",
        "import numpy as np\n",
        "import trimesh\n",
        "import h5py\n",
        "from skimage import measure\n",
        "from stl import mesh\n",
        "\n",
        "a = h5py.File('/content/drive/MyDrive/BraTS2020_training_data/volume_'+str(val_Id[1]), 'r')\n",
        "data = np.array(a['data'])\n",
        "data = np.swapaxes(data,0,1)\n",
        "output = model(np.expand_dims(data,0))\n",
        "for k in range(3):\n",
        "  verts, faces, normals, values = measure.marching_cubes_lewiner(output[0,:,:,:,k])\n",
        "  mesh_object = np.zeros(faces.shape[0],dtype=mesh.Mesh.dtype)\n",
        "  tumor_mesh_object = mesh.Mesh(mesh_object,remove_empty_areas=False)\n",
        "  for i,f in enumerate(faces):\n",
        "    for j in range(3):\n",
        "      tumor_mesh_object.vectors[i][j] = verts[f[j]]\n",
        "  tumor_mesh_object.save('/content/tumor_mesh_predicted'+str(k)+'.stl')\n",
        "tumormesh = trimesh.load('/content/tumor_mesh_predicted0.stl')\n",
        "tumormesh.show()\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}