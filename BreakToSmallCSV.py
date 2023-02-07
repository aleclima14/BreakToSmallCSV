#################################################################################################### 
# Script criado para separar arquivos CSV em partes menores
#                                                                                                  
# Codigo criado por alecsander.lima                                                                
# 06/Fev/2023 - Campinas, SP
# 
#################################################################################################### 

import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Abre janela para procurar arquivo
Tk().withdraw() 
CSVExtractedFile = askopenfilename() 

# Abre o arquivo CSV e separa em linhas
with open(CSVExtractedFile) as fileCSV:
   lines = fileCSV.readlines()

with open(CSVExtractedFile) as fileCSV:
   firstLine = fileCSV.readline()
   
# Pega o titulo do arquivo, excluindo o ".csv" do final
fileName = os.path.basename(CSVExtractedFile)
fileName = fileName.replace(".csv", "")

# Quantidade de linhas que o arquivo vai ter
numberOfLines = 1990

splitFileNumber = 0 
initialValue = 0 
endValue = 0 

# Varre o arquivo e vai contando as linhas, ao chegar no valor de 
# "numberOfLines" salva o arquivo com o "_Parte_x" correspondente
rangeloop = len(lines)//numberOfLines 
if (len(lines) % numberOfLines > 0): 
   rangeloop += 1
for x in range(rangeloop):
   splitFileNumber += 1 
   endValue += numberOfLines
   fileExport = open(fileName + "_Parte_" + str(splitFileNumber) + ".csv", 'w')

   # Adiciona o header para cada arquivo criado
   if(initialValue > 0):
      fileExport.write(firstLine)
   fileExport.write(''.join(lines[initialValue:endValue]))
   initialValue = endValue
   fileExport.close()