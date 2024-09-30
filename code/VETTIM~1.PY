#Ovija Vettimayilnathan (Student B)
#CIP02 F23 Projekt
#Gruppe 16
#Galaxus Scraping


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import pandas as pd

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# Funktion um alle Produkte auf einer Seite anzuzeigen bevor die Daten geholt/gekratzt werden können
def show_all_products():
    # Webseite, die gecrawlt werden soll
    url = "https://www.galaxus.ch/de/s1/producttype/smartphone-24"
    # Chrome browser mit der mitgegebenen URL laden/öffnen
    driver.get(url)
    # 2.5 Sekunden warten bevor NoSuchElementException ausgelöst wird. Homepage ist nicht sofort komplett geladen, dauert 2-3 Sekunden bis alle notwendigen Informationen verfügbar sind
    driver.implicitly_wait(10)
    time.sleep(3)

    # While-Loop um so oft auf den "Mehr anzeigen" Button zu klicken, bis der Button nicht mehr ersichtlich ist
    while True:
        try:
            # Button anhand der ID identifizieren
            show_more_button = driver.find_element(By.XPATH, '//*[@id="productListingContainer"]/div[5]/button')
            # Warten bis der Button klickbar ist
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productListingContainer"]/div[5]/button')))
            # Button klicken
            show_more_button.click()
        except:
            # Loop stoppen wenn der Button nicht mehr ersichtlich ist
            break
    return

# Funktion um die Daten zu holen
def get_product_info():
    # DataFrame erstellen
    df_ProdFinal = pd.DataFrame()

    # Seite mit dem Beautiful Soup einlesen und ein Objekt erstellen. Dabei wird der HTML-Parser 'lxml' verwendet.
    soup = bs(driver.page_source, 'lxml')

    # Jedes Produkt hat dieselbe Klasse. Hier werden alle Elemente mit der Klasse 'sc-pr6hlf-0 cPjAzI' identifiziert und in der Liste 'articles' gespeichert.
    articles = soup.find_all('div',class_= 'sc-pr6hlf-0 cPjAzI')

    # Für jedes Produkt in der Liste Artikel die vorhandenen Informationen holen
    for article in articles:
        price = article.find('span', class_= 'sc-pr6hlf-1 bxvxkL')
        brand = article.findNext('strong')
        model = article.findNext('span', class_= 'sc-1l1ysqm-0 kauxfw')
        details = article.findNext('p', class_='sc-15xtbzo-9 hyDgMl')
        # 'details' beinhaltet mehrere Attribute. Ursprünglich war der Fall diese Variable gleich aufzusplitten. Jedoch mussten wir feststellen, dass je nach Produkt nicht alle Atrribute vorhanden waren und teilweise auch andere Reihenfolge.
        # Somit ist ein einfacher Split und Zuweisung zu einer Variable nicht möglich. Das wird dann in der Cleaning Phase gemacht.
        # detailsSplit = details.text.split(',')

        # aus den gefundenen Informationen wird ein Dictionary erstellt.
        productInfos = {
            'price': price,
            'brand': brand,
            'model': model,
            'details': details
            #dieser Split, den wir nachfolgend versucht haben, funktioniert nur wenn alle Produkte dieselben Attribute haben und diese in derseleben Reihenfolge vorhanden sind. Da dies hier nicht der Fall war, wurde der Split erst in der Cleaning Phase gemacht.
            #'storage': detailsSplit[0],
            #'colour': detailsSplit[1],
            #'display': detailsSplit[2],
            #'sim': detailsSplit[3],
            #'camera': detailsSplit[4],
            #'cellular': detailsSplit[5]
        }
        # Dictionary in DataFrame umwandeln.
        df_ProdInfo = pd.DataFrame(productInfos, index=[0])
        # diesen DataFrame von einem spezifischen Produkt dem finalen DataFrame, wo alle Produkte zusammengetragen werden, anhängen.
        df_ProdFinal = pd.concat([df_ProdFinal, df_ProdInfo], sort=False)

    # den finalen DataFrame returnieren
    return df_ProdFinal


def main():
    print("Start of scraping")
    # Funktion aufrufen um alle Produkte auf einer Seite anzuzeigen
    show_all_products()
    # Funktion aufrufen um alle Produkt Informationen zu holen
    df_ProdInfo = get_product_info()
    # DataFrame in ein CSV schreiben
    #file_path = os.path.join(os.getcwd(), '..', 'Vettimayilnathan_Ovija_studentB_Data/Vettimayilnathan_Ovija_studentB_Data_stage1.csv')
    #df_ProdInfo.to_csv(file_path, index=False)
    df_ProdInfo.to_csv("Scrape.csv")
    print()
    print("End of scraping")

if __name__=="__main__":
    main()