from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os


horario_desejado = "18:39"
dia = 15
prefAcentos = [68, 58, 67, 57]

driver = webdriver.Chrome()
driver.get("https://www.cp.pt/passageiros/pt/comprar-bilhetes")


boxPartida = driver.find_element(
    By.NAME, "textBoxPartida")  # Example for a search bar
boxPartida.send_keys("Lisboa Oriente")

boxPartida = driver.find_element(
    By.NAME, "textBoxChegada")  # Example for a search bar
boxPartida.send_keys("Carregal do Sal")

# Find the hidden input
hidden_input = driver.find_element(By.NAME, "departDate")
hidden_input.click()

dayElement = driver.find_element(
    "xpath", f"//div[contains(@class, 'picker__day picker__day--infocus') and text()='{ dia }']")
dayElement.click()


button = driver.find_element(
    "xpath", "//input[@type='submit' and @value='Pesquisar »']")
button.click()


# ponto porque o input ta dentro de muitas camadas
rows = driver.find_elements(By.XPATH, "//tr[.//input[@type='radio']]")


i = 0
for row in rows:

    partida = row.find_element(
        "xpath", ".//td[@headers='part']").text.strip()
    if (partida == horario_desejado):

        chooseTrain = driver.find_element(
            "xpath", f"//input[@id='j_idt59-{i}-GO' ]")
        chooseTrain.click()
        # "//input[@id='j_idt59-5-GO' and @value='6']"

        break
    i = i+1

terms = driver.find_element("xpath", "//label[@for='travelTerms']")
terms.click()


conti = driver.find_element(By.NAME, "buttonNext")
conti.click()

load_dotenv("things.env")
email = os.getenv("BOT_EMAIL")
password = os.getenv("BOT_PASS")
psvNumber = os.getenv("PSV_NUMBER")
emailHolder = driver.find_element(
    "xpath", "//input[@name='username' and @placeholder='Email' and @id='username']")
emailHolder.send_keys(email)

passHolder = driver.find_element(
    "xpath", "//input[@name='password' and @placeholder='Palavra-passe' ]")
passHolder.send_keys(password)

contiButton = driver.find_element(
    "xpath", "//input[@id ='buttonNext' and @name = 'buttonNext']")
contiButton.click()


discountDropDown = driver.find_element(
    "xpath", "//button[@type = 'button' and @data-id = 'descontoview0']")
discountDropDown.click()

passeFerroVerde = driver.find_element(
    "xpath", "//a[span[@class='text' and contains(text(), 'Passe Ferroviário Verde')]]")
passeFerroVerde.click()

okAlertButton = driver.find_element(
    "xpath", "//input[@id = 'alert-button' and @class= 'btn btn-primary btn-green']")
okAlertButton.click()

psvNumberHolder = driver.find_element("xpath", "//input[@id='input0']")
psvNumberHolder.send_keys(psvNumber)

ValueTopay = driver.find_element(By.ID, "buttonNext")
ValueTopay.click()


ZeroPayContinue = driver.find_element(
    "xpath", "//input[@id = 'buttonNext' and @name = 'j_idt138']")
ZeroPayContinue.click()


assento = driver.find_element(
    By.XPATH, "//img[contains(@data-id, '0:2')]")
print("Encontrado:", assento.get_attribute("data-id"))
# Vai buscar o elemento pai (provavelmente um <div>)
assento_pai = assento.find_element(By.XPATH, "./..")
assento_pai.click()

nextcarre = driver.find_element(By.ID, "nextButton_0")
nextcarre.click()

time.sleep(1)
i = 0
for a in prefAcentos:
    assentoLIvre = driver.find_elements(
        By.XPATH, f"//img[contains(@data-id, '{a}:1:0:0')]")
    print(a)
    if assentoLIvre:
        assentoLIvre[i].find_element(By.XPATH, "./..").click()
        break
    i = i+1


time.sleep(10)
