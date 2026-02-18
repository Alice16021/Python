def cadastrar_contato(nome, telefone=''):
    agenda = [nome, [telefone],]
    return agenda

def atualizar_contato(agenda, indice, new_info):



print(cadastrar_contato('Fulano', '2194838291'))
    
    
    
    from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot: 
    def __init__(self, username, password):
         self.username = username
         self.password = password
         self.driver = webdriver.Firefox(executable_path=")

    def login(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get("https://web.whatsapp.com//")
        time.sleep(3)
        driver.get("https://web.whatsapp.com/p//")
        time.sleep(3)
        try:
            comentarios = ["Ola","Oi","Ola","Bom dia!","Oi"]
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentario = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2,5))
            self.digite_como_uma_pessoa(random.choice(comentarios), campo_comentario)
            time.sleep(random.randint(30,40))
            driver.find_element_by_xpath("//button[contains(text(),'Enviar')]").click()
            time.sleep(5)
        except Exception as e:
                print(e)
                time.sleep(5)
    

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)
            
            
            
             comentarios = ["Ola","Oi","Ola","Bom dia!","Oi"]
    driver.find_element_by_class_name('Ypffh').click()
    campo_comentario = driver.find_element_by_class_name('Ypffh')
    time.sleep(random.randint(2, 5))

    for i in range(len(comentarios)):
        self.digite_como_uma_pessoa(random.choice(comentarios), campo_comentario)
        time.sleep(random.randint(30, 40))
        driver.find_element_by_xpath("//button[contains(text(),'Enviar')]").click()
        time.sleep(5)
