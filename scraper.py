import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

# specifies the path to the chromedriver.exe
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com")

# locate email form by_class_name
username = driver.find_element(By.ID,'session_key')

# send_keys() to simulate key strokes
username.send_keys('plokeshn25@gmail.com')

# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
password = driver.find_element(By.ID,'session_password')

# send_keys() to simulate key strokes
password.send_keys('Loki@1234')
time.sleep(0.5)


# locate submit button by_xpath
sign_in_button = driver.find_element(By.XPATH,"//button[@class='sign-in-form__submit-button']")

# .click() to mimic button click
sign_in_button.click()


# paste the link of the where all job aplications are listed
website='https://www.linkedin.com/hiring/jobs/3348079253/applicants/11926936656/detail/?r=UNRATED%2CGOOD_FIT%2CMAYBE'
driver.get(website)
time.sleep(3)
page=driver.find_element(By.XPATH,"//ul[@class='artdeco-pagination__pages artdeco-pagination__pages--number']")
items=page.find_elements(By.TAG_NAME,'li')
n=(len(items))

linkedin_urls=[]


time.sleep(3)
for i in range(1,n+1):
    page=driver.find_element(By.XPATH,"//button[@aria-label='Page "+str(i)+"']")
    time.sleep(3)
    page.click()
    time.sleep(3)

    names_elements=driver.find_elements(By.XPATH,'//a[@classnames="hiring-applicants-list-item__link link-without-hover-visited"]')
    # collage=[]
    time.sleep(5)
    print(len(names_elements))
    c=0
    for i in names_elements:
        time.sleep(3)
        i.click()
        time.sleep(4)
        try:
            fullpro_btn=driver.find_element(By.XPATH,'//a[@class="ember-view artdeco-button artdeco-button--2 artdeco-button--tertiary"]')
            time.sleep(2)
            linkedin_urls.append(fullpro_btn.get_attribute("href"))
        except:
            linkedin_urls.append("NONE")
    time.sleep(3)


for it in linkedin_urls:
    if it == 'NONE':
        continue
    profile_url=it
    driver.get(profile_url)
    time.sleep(3)   
    print(profile_url)     # this will open the link

    time.sleep(3)
    exp = driver.find_elements_by_xpath('//h1[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]') #for getting name
    time.sleep(3)
    print("NAME:")
    for i in exp:
        print(i.text)
    
    bio = driver.find_elements_by_xpath('//div[@class="display-flex ph5 pv3"]')    
    time.sleep(3)
    print("BIO:")
    for z in bio:
        print(z.text) 
        
    url = str(it)+"details/experience"
    # print(url)
    driver.get(url)
    time.sleep(3)
    exp = driver.find_elements_by_xpath('//div[@class="display-flex flex-column full-width align-self-center"]')
    time.sleep(3)
    print("EXPERIENCE:")
    for i in exp:
        print(i.text)

    edu_url = str(it)+"details/education"
    # print(edu_url)
    driver.get(edu_url)
    time.sleep(3)
    edu = driver.find_elements_by_xpath('//div[@class="display-flex flex-column full-width align-self-center"]')
    time.sleep(3)
    print("EDUCATION:")
    for j in edu:
        print(j.text)
    
    #for skills
    skill_url = str(it)+"details/skills"
    driver.get(skill_url)
    time.sleep(3)
    sk = driver.find_elements_by_xpath('//div[@class="display-flex flex-column full-width align-self-center"]')
    time.sleep(3)
    print("SKILLS:")
    for j in sk:
        print(j.text)

    #awards
    award_url = str(it)+"details/honors"
    driver.get(award_url)
    time.sleep(3)
    awd = driver.find_elements_by_xpath('//div[@class="display-flex flex-column full-width align-self-center"]')
    time.sleep(3)
    print("AWARDS:")
    for i in awd:
        print(i.text)
