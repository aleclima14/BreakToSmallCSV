#################################################################################################### 
# Script criado para separar arquivos CSV em partes menores
#                                                                                                  
# Codigo criado por alecsander.lima                                                                
# 06/Fev/2023 - Campinas, SP
# 
#################################################################################################### 
import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog)

from PyQt6.QtSerialPort import (QSerialPort, QSerialPortInfo)
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon

# from pathlib import Path

import os
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

# # Abre janela para procurar arquivo
# Tk().withdraw() 
# CSVExtractedFile = askopenfilename() 

# # Abre o arquivo CSV e separa em linhas
# with open(CSVExtractedFile) as fileCSV:
#    lines = fileCSV.readlines()

# with open(CSVExtractedFile) as fileCSV:
#    firstLine = fileCSV.readline()
   
# # Pega o titulo do arquivo, excluindo o ".csv" do final
# fileName = os.path.basename(CSVExtractedFile)
# fileName = fileName.replace(".csv", "")

# # Quantidade de linhas que o arquivo vai ter
# numberOfLines = 1990

# splitFileNumber = 0 
# initialValue = 0 
# endValue = 0 

# # Varre o arquivo e vai contando as linhas, ao chegar no valor de 
# # "numberOfLines" salva o arquivo com o "_Parte_x" correspondente
# rangeloop = len(lines)//numberOfLines 
# if (len(lines) % numberOfLines > 0): 
#    rangeloop += 1
# for x in range(rangeloop):
#    splitFileNumber += 1 
#    endValue += numberOfLines
#    fileExport = open(fileName + "_Parte_" + str(splitFileNumber) + ".csv", 'w')

#    # Adiciona o header para cada arquivo criado
#    if(initialValue > 0):
#       fileExport.write(firstLine)
#    fileExport.write(''.join(lines[initialValue:endValue]))
#    initialValue = endValue
#    fileExport.close()


class Windows(QWidget):
   def __init__(self):
      super(Windows,self).__init__()
      self.initUI()
      
   def initUI(self):
      # self.setWindowIcon(QIcon("Python/led-icon.png"))
      self.setWindowTitle("Break To Small CSV")
      self.setContentsMargins(20, 20, 20, 20)
      # self.resize(400, 170)
      self.setFixedSize(600, 200)
      

      layout = QVBoxLayout()
      self.setLayout(layout)

      line0 = QHBoxLayout()
      line0.setSpacing(5)
      layout.addLayout(line0)

      line1 = QHBoxLayout()
      line1.setSpacing(5)
      layout.addLayout(line1)

      line2 = QHBoxLayout()
      line2.setSpacing(5)
      layout.addLayout(line2)

      line3 = QHBoxLayout()
      line3.setSpacing(5)
      layout.addLayout(line3)

      line4 = QHBoxLayout()
      line4.setSpacing(5)
      layout.addLayout(line4)

      line5 = QHBoxLayout()
      line5.setSpacing(5)
      layout.addLayout(line5)
      
      self.labelInoutFileBox = QLabel()
      self.labelInoutFileBox.setText("File (CSV) to break: ")

      self.labelExportFileBox = QLabel()
      self.labelExportFileBox.setText("Path to export files: ")

      self.labelLinesPerFile = QLabel()
      self.labelLinesPerFile.setText("Lines per file: ")

      # Input file box
      self.inputFileBox = QLineEdit()
      self.inputFileBox.setText("Input path")
     
      # Button to open file
      self.openFile = QPushButton("...")
      self.openFile.setMaximumWidth(40)
      self.openFile.setMinimumWidth(40)
      self.openFile.clicked.connect(self.getFileName)

      # Export file box  
      self.pathExportBox = QLineEdit()
      self.pathExportBox.setText("Export path")

      # Button to choose export path
      self.pathExportFile = QPushButton("...")
      self.pathExportFile.setMaximumWidth(40)
      self.pathExportFile.setMinimumWidth(40)
      self.pathExportFile.clicked.connect(self.getDirectory)

      # Number of lines in files
      self.numberOfLines = QLineEdit()
      self.numberOfLines.setText("2000")
      self.numberOfLines.setMaximumWidth(80)
      self.numberOfLines.setMinimumWidth(80)

      # Export button
      self.exportButton = QPushButton("Break it!")
      
      line0.addWidget(self.labelInoutFileBox)
      line1.addWidget(self.inputFileBox)
      line1.addWidget(self.openFile)
      line2.addWidget(self.labelExportFileBox)
      line3.addWidget(self.pathExportBox)
      line3.addWidget(self.pathExportFile)  
      line4.addWidget(self.labelLinesPerFile) 
      line5.addWidget(self.numberOfLines)
      line5.addWidget(self.exportButton)

   def getFileName(self):
      fileTypesFilter = "Arquivos de texto (*.csv *.txt)"
      response = QFileDialog.getOpenFileName(parent = self, caption = "Select a file", directory = os.getcwd(), filter = fileTypesFilter)
      self.inputFileBox.setText(str(response))

   def getDirectory(self):
      response = QFileDialog.getExistingDirectory(
            self,
            # caption='Select a folder'
      )
      self.pathExportBox.setText(str(response))
   
def window():
   applicationWindow = QApplication(sys.argv)
   windowApp = Windows()

   windowApp.show()

   sys.exit(applicationWindow.exec())

window()