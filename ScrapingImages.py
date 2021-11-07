# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 06:40:06 2021

@author: edita
"""

from selenium import webdriver
import time
import requests
#from io import BytesIO
#from PIL import Image

#------------------------------------------------
def load_requests(source_url):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:
        aSplit = source_url.split('/')
        ruta = "D:/1_UOC/UOC/1_Tipologia&CicloDeVidaDatos/Practica1/"+aSplit[len(aSplit)-1]
        print(ruta)
        output = open(ruta,"wb")
        for chunk in r:
            output.write(chunk)
        output.close()  
# -----------------------------------------------        

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.senamhi.gob.pe/?&p=satelites-goes16")

# Codigo para evitar restricciones---------------
#try:
#    page1 = requests.get(ap)
#except requests.exceptions.ConnectionError:
#    r.status_code = "Connection refused"
#time.sleep(5)

images = driver.find_elements_by_tag_name('img')

imagenes = []
i = 0
for imgs in images:
    imagenes.append(imgs.get_attribute('src'))
    print(imagenes)
    load_requests(imagenes[i])
    i = i+1

driver.quit()
