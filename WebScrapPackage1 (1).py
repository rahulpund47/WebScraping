#!/usr/bin/env python
# coding: utf-8

# In[2]:


def get_page(name):
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'C:\Users\admin\Downloads\chromedriver_win32\chromedriver.exe', options=chrome_options)


    driver.get('https://in.finance.yahoo.com/') 

    driver.find_element_by_xpath("//input[@class='Pos(r) W(100%) H(35px) M(0) O(0) O(0):f Bgc($lv2BgColor) Z(2) Bxsh(n) Bxsh(n):f Pt(6px) Pb(8px) Ff($yahooSansFinanceFont) Fz(m) Px(20px) Bdrs(0) Bdrsbstart(2px) Bdrststart(2px) Va(t)']").click()
    
    time.sleep(5)
    driver.find_element_by_xpath("//input[@class='Pos(r) W(100%) H(35px) M(0) O(0) O(0):f Bgc($lv2BgColor) Z(2) Bxsh(n) Bxsh(n):f Pt(6px) Pb(8px) Ff($yahooSansFinanceFont) Fz(m) Px(20px) Bdrs(0) Bdrsbstart(2px) Bdrststart(2px) Va(t)']").send_keys(name)
    time.sleep(5)
    driver.find_element_by_xpath("//li[@class='P(0) ']").click()
    time.sleep(5)
    mainlist=[]
    mainlist=get_col(mainlist,driver)
    time.sleep(5)
    mainlist=get_val(mainlist,driver)
    time.sleep(5)
    df=get_DataFrame(mainlist,driver)
    
    return df



def get_col(ml,driver):
    sublist=[]
    sublist=['Previous close','Open','Bid','Ask',"High","Low",'52-week range','Volume','Avg. volume','Market cap','Beta (5Y monthly)','PE ratio (TTM)','EPS (TTM)','Earnings date','Forward dividend & yield','Ex-dividend date','1y target est',"DateTime"]

    #for i in range(len(col_Nam)):
    #    sublist.append(col_Nam[i].text)
    #sublist.append("DateTime")
    ml.append(sublist)
    #print(ml)
    return ml



def get_val(ml,driver):
    import time
    from time import gmtime, strftime

    go=True
    cnt=0
    while go:
        Values=driver.find_elements_by_xpath("//td[@class='Ta(end) Fw(600) Lh(14px)']")
        sublist=[]
        try:
            for i in range(len(Values)):
                if(i!=4):    
                    sublist.append(Values[i].text)
                else:
                    high=Values[i].text.split('-')[1]
                    sublist.append(high)
                    low=Values[i].text.split('-')[0]
                    sublist.append(low)
        except:
            sublist.append('NULL')
        a=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        sublist.append(a)
        ml.append(sublist)
        time.sleep(5)
        cnt=cnt+2
        print(cnt)
        if(cnt==10):
            go=False
    #print(ml)
    return ml



def get_DataFrame(mainlist,driver):
    import pandas as pd
    df=pd.DataFrame(mainlist)


    new_header = df.iloc[0] 
    df = df[1:] 
    df.columns = new_header 

    df.drop(df.columns[[6,11,12,13,14]], axis = 1, inplace = True) 


    df['Volume'] = df['Volume'].str.replace(',', '')
    df['Volume'] = df['Volume'].astype(int)


    df['Avg. volume'] = df['Avg. volume'].str.replace(',', '')
    df['Avg. volume'] = df['Avg. volume'].astype(int)

    
    return df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




