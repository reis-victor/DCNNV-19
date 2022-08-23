## DCNNV-19: A Deep Convolutional Neural Network for COVID-19 Detection in Chest Computed Tomographies

### Paper
https://arxiv.org/abs/2208.09349

### Jupyter Notebook
https://github.com/reis-victor/DCNNV-19/blob/main/DCNNV-19.ipynb

### Python script for trimming the images based on their bounding boxes, and also to resize and alocate them to the proper subdirectory
https://github.com/reis-victor/DCNNV-19/blob/main/corte_redimensionamento_organizacao.py

### Tensorflow files of the final model:
Due to the custom optimizer,use "custom_objects={"AdaBeliefOptimizer": AdaBeliefOptimizer}" to load the model.
https://github.com/reis-victor/DCNNV-19/tree/main/model 

### Dataset link (COVIDx-CT2):
https://www.kaggle.com/datasets/c395fb339f210700ba392d81bf200f766418238c2734e5237b5dd0b6fc724fcb/versions/4
