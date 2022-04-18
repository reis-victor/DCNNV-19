#Importação das bibliotecas necessárias
import pandas as pd
from PIL import Image
import ast
import os
import cv2
import csv

root = '<diretorio_origem>' #diretório contendo todas as imagens a serem processadas
dst = '<diretorio_origem>' 
seed_arr = []
file = open('<arquivo_texto>', newline='', encoding="utf8") #arquivo texto de treino, validação ou teste a ser lido
csv_reader = csv.reader(file, delimiter=',')

#Iteração por todos os arquivos de imagem do diretório origem baseaando-se no arquivo texto fornecido
for index, line in enumerate(csv_reader):
    if index == 0:
        continue
    seed_arr.append(line)
file.close()    
                                     
#Este trecho itera todo o arquivo texto lendo cada linha e valores das colunas para cada arquivo
for index, line in enumerate(seed_arr):
    
    filename = line[0] #nome do arquivo
    class_name = line[1] #classe
    xmin = line[2] #limite esquerdo da caixa delimitadora
    ymin = line[3] #limite inferior da caixa delimitadora
    xmax = line[4] #limite direito da caixa delimitadora
    ymax = line[5] #limite superior da caixa delimitadora
    
    #Atribui a variáveis respectivamente: local de carregamento da imagem, destino da imagem salva e nome do arquivo salvo
    load_img_path = os.path.join(root, filename)
    save_class_path = os.path.join(dst, class_name)
    save_img_path = os.path.join(save_class_path, str(index) +".png") #Foi adicionado o sufixo .png ao nome do arquivo salvo
    
    #Este bloco realiza a leitura da imagem, corte baseado na caixa delimitadora, redimensionamento, armazenamento e imprime na tela o arquivo sendo salvo no momento
    img = Image.open(load_img_path)
    crop_img = img.crop((int(xmin) ,int(ymin) ,int(xmax) ,int(ymax)))
    newsize = (224, 224) 
    im1 = crop_img.resize(newsize) 
    im1.save(save_img_path, 'png')
    print('save ' + save_img_path)
file.close() 