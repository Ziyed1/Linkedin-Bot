import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service

# ID de connexion
USERNAME = 'hitsugaya2011@hotmail.fr'
PASSWORD = 'UZUmaki0147!'
# ======================================

TIMEOUT = 15

def follow():
    job = input('[Obligatoire] - Saisie l\'intitulé de l\'emploi des personnes que tu veux ajouter: ')

    user_numbers = int(
        input('[Obligatoire] - Combien veux-tu ajouter de personne ? (1-10 max): ')
    )

    # Configuration des options de page chrome
    config = webdriver.ChromeOptions()

    # Désactive le mode restrictif de sécurité
    config.add_argument('--no-sandbox')
    config.add_argument('--log-level=3')
    config.add_argument('--start-maximized')

    # Instance d'une page web Chrome + les options
    bot = webdriver.Chrome(service=Service(CM().install()), options=config)

    bot.get('https://www.linkedin.com/home')

    # Suspend l'execution pendant 1sec
    time.sleep(1)

    # Verifie le type de page de connexion
    # Si on a le H1 class = 'main_subtitle ect...'
    # Alors on prend un XPATH spécifique
    # Sinon on prend l'autre XPATH
    


    # Attendre jusqu'à 10 secondes que le champs 'username' soit visible sur la page Web (ref stocker)
    username = WebDriverWait(
       bot, 10).until(EC.element_to_be_clickable(
       (By.ID, "session_key")))
    
    # Attendre jusqu'à 10 secondes que le champs 'password' soit visible sur la page Web (ref stocker) 
    password = WebDriverWait(
       bot, 10).until(EC.element_to_be_clickable(
       (By.ID, "session_password")))

    # Entrer les éléments "USERNAME" & "PASSWORD"
    # Clear pour être sur qu'il n'y a rien dans les champs
    username.clear()
    username.send_keys(USERNAME)
    password.clear()
    password.send_keys(PASSWORD)

    # IDEM : On cherche et clique sur le bouton 'login'
    button = WebDriverWait(
       bot,2).until(EC.element_to_be_clickable((
       By.XPATH, "/html/body/main/section[1]/div/div/form[1]/div[2]/button"))).click()
    
    time.sleep(7)

    print('[Info] - Connexion réussie ! ')

    # Recherche de la barre 'search'
    search = WebDriverWait(
    bot, 5).until(EC.element_to_be_clickable(
       (By.XPATH, "/html/body/div[6]/header/div/div/div/div[1]/input")))

    search.send_keys(job)
    search.send_keys(Keys.ENTER)

    time.sleep(7)

    # Cliquer sur la section 'Personnes'
    section = WebDriverWait(
    bot, 3).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@aria-pressed='false'][normalize-space()='Personnes']"))).click()

    time.sleep(7)

    nb = 0
    element = bot.find_elements(By.XPATH, "//*[text()[contains(.,'Se connecter')]]")
    elementNext = bot.find_elements(By.XPATH, "//*[text()[contains(.,'Suivant')]]")
    
    while nb < user_numbers:
      if element:
       
       BtnConnect = WebDriverWait(
        bot, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']"))).click()
       
       btnSend = WebDriverWait(
         bot, 2.5).until(EC.element_to_be_clickable(
         (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]/span"))).click()
       
       nb=nb+1
       
       time.sleep(3)
      elif elementNext:
       BtnNext = WebDriverWait(bot,10).until(EC.element_to_be_clickable(
          (By.XPATH, "//*[text()[contains(.,'Suivant')]]"))).click()    
       
       

      

    
    # for i in range(user_numbers):
      # BtnConnect = WebDriverWait(
       # bot, 10).until(EC.element_to_be_clickable(
        # (By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']"))).click()
       
      # btnSend = WebDriverWait(
       # bot, 2.5).until(EC.element_to_be_clickable(
       # (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]/span"))).click()
       
       # time.sleep(3)


    # Cliquer sur 'Se connecter'
   # for btn in range(user_numbers):
        
      #  ActionChains(bot).send_keys(Keys.END).perform()

       # time.sleep(1)

        #BtnConnect = WebDriverWait(
        #bot, 3.5).until(EC.element_to_be_clickable(
        #(By.XPATH, "/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[1]/div/div/div[3]/div/button/span"))).click()

        #btnSend = WebDriverWait(
        #bot, 2.5).until(EC.element_to_be_clickable(
        #(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]/span"))).click()

    

if __name__ == '__main__':
 follow()