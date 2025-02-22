from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

horario_desejado = "07:55"
dia = 23

driver = webdriver.Chrome()
driver.get("https://www.cp.pt/passageiros/pt/comprar-bilhetes")


boxPartida = driver.find_element(
    By.NAME, "textBoxPartida")  # Example for a search bar
boxPartida.send_keys("Carregal do Sal")

boxPartida = driver.find_element(
    By.NAME, "textBoxChegada")  # Example for a search bar
boxPartida.send_keys("Lisboa Oriente")

# Find the hidden input
hidden_input = driver.find_element(By.NAME, "departDate")
hidden_input.click()

dayElement = driver.find_element(
    "xpath", f"//div[contains(@class, 'picker__day') and text()='{dia}']")
dayElement.click()


button = driver.find_element(
    "xpath", "//input[@type='submit' and @value='Pesquisar »']")
button.click()


# ponto porque o input ta dentro de muitas camadas
rows = driver.find_elements(By.XPATH, "//tr[.//input[@type='radio']]")
print(len(rows))


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


time.sleep(10)


terms = driver.find_element("xpath", "//label[@for='travelTerms']")
terms.click()


conti = driver.find_element(By.NAME, "buttonNext")
conti.click()
time.sleep(10)
