import streamlit as st
import os, sys

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = installff()
from selenium import webdriver
from selenium.webdriver import ChromeOptions
opts = ChromeOptions()
#opts.add_argument("--headless")
browser = webdriver.Chrome(options=opts)

browser.get('https://www.bol.com/nl/nl/l/volleybal-scoreborden/54143/')
st.write(browser.page_source)