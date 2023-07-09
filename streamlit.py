import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# Function to perform some action with the name
def process_name(url, product_name):
    # Perform your desired operation here
    driver = webdriver.Chrome('')  # Optional argument, if not specified will search path.
    url = 'https://www.bol.com/nl/nl/l/volleybal-scoreborden/54143/'
    driver.get(url)
    time.sleep(2)
    total_items = get_aantal(driver)
    print(total_items)

    ranking = get_ranking(driver, total_items, url)

    print('It got position: ' + str(ranking))
    time.sleep(2) 
    driver.quit()
    st.write("Total items:", total_items) 
    st.write("Ranking:", ranking)

def get_aantal(driver):
    aantal = driver.find_element(By.XPATH, '/html/body/div[1]/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[2]/div[1]/p')
    result = re.findall(r'\d+', aantal.text)
    if result:
        return int(''.join(result))

def get_ranking(driver, total_items, url):
    plaats = 0
    teller = 1

    for i in range(1, total_items + 1):
        count = (i % 24) or 24
        #print(count)
        ranking = driver.find_element(By.XPATH, '/html/body/div[1]/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[4]/div/ul/li[' + str(count) + ']/div[2]/div/div[1]/wsp-analytics-tracking-event/a')
        #print(ranking.text)
        ranking_text = ranking.get_attribute("textContent")
        print(str(count) + ') ' + ranking_text)
        plaats += 1
        if ranking.text == 'Megaform - Opvouwbaar scorebord - tafelmodel':
            break

        if count == 24:
            teller += 1
            driver.get(url + '?page=' + str(teller) + '&view=list')
            time.sleep(2)
    
    return plaats


def main():
    # Set the page title
    st.title("Bol.com scraper ranking")

    # Add an input box
    url = st.text_input("Url:", "")

    # Add an input box
    product_name = st.text_input("Product name:", "")

    # Add a "Process" button
    if st.button("Process"):
        process_name(url, product_name)
    
    # Add a "Clear" button
    if st.button("Clear"):
        url = ""
        product_name = ""

    # Display the input value
    st.write("Given url: ", url)
    st.write("Given product: : ", product_name)



    

if __name__ == "__main__":
    main()


