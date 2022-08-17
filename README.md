## DCNNV-19: Uma rede neural convolucional profunda para detecção de COVID-19 em tomografias computadorizadas torácicas


### Jupyter Notebook
https://github.com/reis-victor/DCNNV-19/blob/main/DCNNV-19.ipynb

### Script em python utilizado para corte das imagens baseando-se nas caixas delimitadoras, além de redimensionamento e alocação para o subdiretório adequado
https://github.com/reis-victor/DCNNV-19/blob/main/corte_redimensionamento_organizacao.py

### Modelo final do Tensorflow salvo:
Por utilizar um otimizador customizado, para carregar o modelo é necessário o código adicional "custom_objects={"AdaBeliefOptimizer": AdaBeliefOptimizer}"
https://github.com/reis-victor/DCNNV-19/tree/main/model 

### Link do dataset utilizado, COVIDx-CT2, no Kaggle:
https://www.kaggle.com/datasets/c395fb339f210700ba392d81bf200f766418238c2734e5237b5dd0b6fc724fcb/versions/4
