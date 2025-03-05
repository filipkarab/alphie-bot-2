from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep
import random


TIMEOUT_DELAY = 30
DYCHACI_DELAY = 0.5
ODPOVEDE = {
    "letisko": "der Flughafen",
    "hotel": "das Hotel",
    "pevnosť": "die Festung",
    "obchod": "das Geschäft",
    "plaváreň": "die Schwimmhalle",
    "ulica": "die Straße",
    "cukráreň": "die Konditorei",
    "dóm": "der Dom",
    "ulička": "die Gasse",
    "stanica": "der Bahnhof",
    "lekáreň": "die Apotheke",
    "pekáreň": "die Bäckerei",
    "kníhkupectvo": "die Buchhandlung",
    "zmrzlináreň": "die Eisdiele",
    "mäsiarstvo": "die Metzgerei",
    "supermarket": "der Supermarkt",
    "drogéria": "die Drogerie",
    "stánok": "der Kiosk",
    "trh": "der Markt",
    "pošta": "die Post",
    "štadión": "das Stadion",
    "banka": "die Bank",
    "kostol": "die Kirche",
    "námestie": "der Platz"
}


def pockaj_na_element(by: By, selektor: str):
    try:
        WebDriverWait(driver, TIMEOUT_DELAY).until(EC.presence_of_element_located((by, selektor)))
        sleep(DYCHACI_DELAY)
    except TimeoutException:
        print("CHYBA: Skontroluj internetové pripojenie a jeho stabilitu/rýchlosť!")
        exit()


print()
[print("-", end="") for _ in range(10)]
print(" ALPHIE BOT v2.0 pre vzdelavacie ucely ", end="")
[print("-", end="") for _ in range(10)]
[print() for _ in range(3)]

meno = input("Zadaj prihlasovacie meno (NIE EMAIL).. ")
heslo = input("Zadaj heslo.. ")
spravnost = int(input("Zadaj požadované % správnych odpovedí.. "))

[print() for _ in range(2)]
print("Spúšťam program, ak si zadal zle heslo, nezistíš to nijak, iba tak že ti program nepôjde, resp. sa zasekne alebo vyhodí chybu.")
print("Program beží plne na pozadí, nezatvárajte toto okno, iba ak chcete program ukončiť.")


options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")
driver = webdriver.Edge(options=options)

driver.get("https://app.alphie.app/app/classes/422/homeworks/5756/detail")

pockaj_na_element(By.ID, "username")

usernameElem = driver.find_element(By.ID, "username")
usernameElem.clear()
usernameElem.send_keys(meno)

passElem = driver.find_element(By.ID, "password")
passElem.clear()
passElem.send_keys(heslo)

sleep(0.5)

passElem.send_keys(Keys.RETURN)

pockaj_na_element(By.XPATH, "//a[@class='tag _green _alt']")

spustitElem = driver.find_element(By.XPATH, "//a[@class='tag _green _alt']")

pockaj_na_element(By.XPATH, "//a[@class='tag _green _alt']")
spustitElem.click()

while True:

    sleep(1)
    pockaj_na_element(By.XPATH, "//button[@class='bttn _primary _next']")

    spustitElem = driver.find_element(By.XPATH, "//button[@class='bttn _primary _next']")
    spustitElem.click()

    pockaj_na_element(By.XPATH, "//button[@class='bttn _full  href _green']")

    spustitElem = driver.find_element(By.XPATH, "//button[@class='bttn _full  href _green']")
    spustitElem.click()

    pockaj_na_element(By.XPATH, "//button[@class='bttn _primary _next']")

    dalejElem = driver.find_element(By.XPATH, "//button[@class='bttn _primary _next']")
    otazkaCislo = 0

    while True:
        try:

            if otazkaCislo == 0:
                pockaj_na_element(By.XPATH, "//button[@class='bttn _primary _next']")
            dalejElem = driver.find_element(By.XPATH, "//button[@class='bttn _primary _next']")

            pockaj_na_element(By.CLASS_NAME, "test-question")
            otazka = driver.find_element(By.CLASS_NAME, "test-question").find_element(By.XPATH, "following-sibling::*[1]").find_element(By.XPATH, ".//*").find_element(By.XPATH, ".//*").find_element(By.XPATH, ".//*").find_element(By.XPATH, ".//*").get_attribute("innerText")
            
            if otazka in ODPOVEDE.keys():
                odpoved = ODPOVEDE[otazka]
            else:
                for kluc in ODPOVEDE.keys():
                    if ODPOVEDE[kluc] == otazka:
                        odpoved = kluc
            
            if random.randint(1, 100) in range(1, spravnost):
                for i in range(4):
                    odpovedElem = driver.find_element(By.ID, f"answer{otazkaCislo}_{i}").find_element(By.XPATH, "following-sibling::*[1]")

                    if odpovedElem.get_attribute("innerText").lower() == odpoved.lower():
                        odpovedElem.click()
                        print(f"Program práve zodpovedal správne na otázku: '{otazka}' -> '{odpoved}'.")

            else:
                        print("Program naschval neodpovedal na otázku podľa zadanej správnosti.")
            
            pockaj_na_element(By.XPATH, "//button[@class='bttn _primary _next']")
            driver.find_element(By.XPATH, "//button[@class='bttn _primary _next']").click()
            driver.find_element(By.XPATH, "//button[@class='bttn _primary _next']").click()
            
            sleep(0.4)
            otazkaCislo += 1

        except NoSuchElementException:
            print("Program správne vyriešil celú úlohu, ide znovu...")
            break

    sleep(1)
    pockaj_na_element(By.XPATH, "//div[@class='bttn _green _next _full']")
    driver.find_element(By.XPATH, "//div[@class='bttn _green _next _full']").click()
