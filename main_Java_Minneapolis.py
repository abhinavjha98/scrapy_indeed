#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import requests
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()
import urllib.request
from warnings import warn
import math


# In[17]:


url = "https://www.indeed.com/jobs?q=Java+&l=Minneapolis%2C+MN"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)
browsers = webdriver.Chrome("chromedriver.exe")
browsers.get(url)


# In[3]:


url_max = url+"&start=10000"
browser.get(url_max)
count = browser.find_element_by_class_name("searchCount-a11y-contrast-color")
page_count = count.text
page_count = page_count.replace(" ", "")
page_count = page_count.split("Page")
page_count = page_count[1].split("of")
page_count_int = int(page_count[0])
page_count_int = int(1)

data_page=[]
for j in range(page_count_int+1):
    data_page.append(url+"&start="+str(j))


# In[ ]:


title = []
company_name = []
description = []
location=[]
salary = []
jobs_type=[]
logo=[]
link_apply=[]
for i in data_page:

    browser.get(i)
    data = browser.find_elements_by_xpath("//a[contains(@class, 'turnstileLink ')]")
    for j in data:
        browsers.get(j.get_attribute("href"))
        try:
            job_name = browsers.find_element_by_class_name("jobsearch-JobInfoHeader-title")
            title.append(job_name.text)
        except NoSuchElementException:
            title.append("")
        try:
            co_name = browsers.find_element_by_class_name("jobsearch-InlineCompanyRating")
            c_name = co_name.text
            c_name = c_name.split("reviews\n-\n")
            location.append(c_name[1])
        except IndexError:
            location.append("")
        except NoSuchElementException:
            location.append("")
            
        try:
            job_names = browsers.find_element_by_class_name("jobsearch-CompanyAvatar-companyLink")
            company_name.append(job_names.text)
        except NoSuchElementException:
            company_name.append("")
        try:    
            job_name = browsers.find_element_by_css_selector("span.icl-u-xs-mr--xs")
            salary.append(job_name.text)
        except NoSuchElementException:
            salary.append("")
        try:    
            job_name = browsers.find_element_by_class_name("jobsearch-jobDescriptionText")
            job_name = job_name.text.replace('\n','')
            description.append(job_name)
        except NoSuchElementException:
            description.append("")
            
        try:
            apply_link = browsers.find_elements_by_xpath("//a[contains(@class, 'icl-Button--primary')]")
            sleep(10)
            apply_links = browsers.find_elements_by_xpath("//button[contains(@class, 'icl-Button')]")
            for i in apply_link:
                if "Apply On Company Site" in i.text:
                    r = requests.get(i.get_attribute("href")) 
                    link_apply.append(r.url)
                    print(r.url)
                    break
            for i in apply_links:
            	if "Apply Now" in i.text:
            		link_apply.append(browsers.current_url)
            		print(link_apply.append(browsers.current_url))
            		break
            if link_apply is None:
                print("Hello")
        except NoSuchElementException:
            link_apply.append("")
       	
       	


            
            
#         try:
#             flag = 0
#             type_job = ""
#             job_name = browsers.find_elements_by_css_selector("div")
#             job_type = ""
#             try:
#                 for i in job_name:
#                     try:
#                         sleep(2)
#                         job_type = job_type + str(i.text)
#                     except NoSuchElementException:
#                         jobs_type.append("")
#                 if "Part-time" in job_type:
#                     type_job = ""
#                     flag=1
#                     type_job += "Part-time"
#                 if "Full-time" in job_type:
#                     type_job = ""
#                     flag=2
#                     type_job += "Full-time"
#                 if "Part-time" in job_type:
#                     if "Full-time" in job_type:
#                         type_job = ""
#                         flag=3
#                         type_job += "Part-time Full-time"
#                 if flag==0:
#                     type_job +=" "
#                 jobs_type.append(type_job)
#             except NoSuchElementException:
#                 jobs_type.append("")
#         except NoSuchElementException:
#             jobs_type.append("")
        try:
            logo_name = browsers.find_element_by_xpath("//img[contains(@class,'jobsearch-CompanyAvatar-image')]")
            logo.append(logo_name.get_attribute("src"))
        except NoSuchElementException:
            logo.append("")
    


# In[7]:


import pandas as pd 
   
lst = [title,company_name,salary,description] 
 
df = pd.DataFrame(list(zip(logo,title,company_name,location,salary,description,link_apply)), columns =['Logo','Title','Company','Location','Salary','Description','Apply Link']) 
df
df.to_csv('Indeed_ex1_java_minn.csv',index=False)


# In[14]:


# In[ ]:




