import pandas as pd
import ast
from datetime import datetime
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import logging
from random import randint
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BotChrome:

    def __init__(self, num_abas=5):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument(r'--user-data-dir=./Profile')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 3) if self.driver else None
        self.abas = [self.driver.current_window_handle]
        
    

    def get_element_by_xpath(self, xpath, ec=None):
        ec = ec if ec else EC.presence_of_element_located
        return self.wait.until(ec((By.XPATH, xpath))) if self.wait else None

        
    def get_elements_by_xpath(self,xpath, ec=None):
        ec = ec if ec else EC.presence_of_all_elements_located
        return self.wait.until(ec((By.XPATH, xpath))) if self.wait else None

    def acessar(self):
        if self.driver:
            self.driver.get('https://playghost.qpanel.top/#/dashboard')
        
    def login(self,email):
        usuario = self.get_element_by_xpath("//input[@name='username']")
        senha = self.get_element_by_xpath("//input[@type='password']")
        usuario.send_keys(f"{os.getenv('username')}")
        senha.send_keys(f"{os.getenv('password')}")
        self.get_element_by_xpath("//button//span[contains(text(),'Continuar')]").click()
        print(email)
        
    def escolhe_teste(self):
        #self.get_element_by_xpath("//button[contains(text(),'Teste 1 Hora C/ Adultos')]").click()
        print('escolhi o teste')
        self.driver.close()
    
    def informacoes_teste(self):
        div = self.get_element_by_xpath("//div[@class='d-flex flex-column pre']")
        return div
    
    def trata(self):
        infos = self.informacoes_teste().text
        infos = infos.replace('✅','').replace('🗓️','').replace('💳','').replace('📺','').replace('🟢','').replace('🌐','')
        linhas = infos.split('\n')
        del linhas[0]
        del linhas[-1]
        lista = [item for item in linhas if item.strip()]
        dados = {}

        for item in lista:
            parts = item.split(': ', 1)
            if len(parts) == 2:
                chave, valor = parts
                dados[chave.strip()] = valor.strip()
        