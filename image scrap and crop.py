#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[2]:


import selenium
from selenium import webdriver
import time
from PIL import Image
import cv2


# In[9]:


driver = webdriver.Chrome(executable_path=r'C:\Users\admin\Downloads\chromedriver_win32\chromedriver.exe')


# In[10]:


search_url = "https://www.slideshare.net/GauravMittal68/convolutional-neural-networks-cnn"
driver.get(search_url)


# In[ ]:


images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))


# In[12]:



for i in range(1,70):
    time.sleep(5)
    search_url="https://image.slidesharecdn.com/cnn-toupload-final-151117124948-lva1-app6892/95/convolutional-neural-networks-cnn-"+str(i)+"-638.jpg?cb=1455889178"
    driver.get(search_url)
    driver.save_screenshot("C:/Users/admin/Downloads/WebScrapping/slide/"+str(i)+".png")
    img = cv2.imread("C:/Users/admin/Downloads/WebScrapping/slide/"+str(i)+".png")
    crop_img = img[120:460, 200:800]
    cv2.imwrite("C:/Users/admin/Downloads/WebScrapping/slide/"+str(i)+"_1.png", crop_img)


# In[7]:





# In[8]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




