import chromedriver_binary
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.mizuhobank.co.jp/market/historical.html")
link = driver.find_elements(By.TAG_NAME, "a")

href_list = []
for i in link:
    href_list.append(i.get_attribute("href"))

href_list.index("https://www.mizuhobank.co.jp/market/csv/tm_quote.csv")

csv_path = href_list[119]

df = pd.read_csv(csv_path, encoding="shift_jis")
df.to_csv("fx_mizuho_rate.csv")


# print(df)
# print(df.iloc[-1, 1])
