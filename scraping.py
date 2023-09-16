from selenium import  webdriver
import pandas as pd
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

urls = [
    'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/','https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/'
]
data=[]
# Loop through the URLs and scrape data
for url in urls:
    # Navigate to the webpage
    driver.get(url)
    a = driver.find_elements_by_tag_name('p')
    t=[]
    for i in a:
        t.append(i.text)
    data.append(t)

driver.quit()
df= pd.DataFrame(data)
df.