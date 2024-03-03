import requests
from bs4 import BeautifulSoup

import pandas as pd

url="https://github.com/topics"
r=requests.get(url)
content=r.text

# with open('topics.html','w',encoding='utf-8') as f:
#     f.write(content)

parsed_doc=BeautifulSoup(content,'html.parser')

title_tags=parsed_doc.find_all('p',
                {'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})
description_tags=parsed_doc.find_all('p',{'class':"f5 color-fg-muted mb-0 mt-1"})

link_tags=parsed_doc.find_all('a',{'class':'no-underline flex-1 d-flex flex-column'})
# topic_page_url='https://github.com'+link_tags[0]['href']
# print(topic_page_url)

topic_title=[]
for tag in title_tags:
    topic_title.append(tag.text)
# print(topic_title)  #3d


topic_desc=[]
for tag in description_tags:
    topic_desc.append(tag.text.strip())
# print(topic_desc) #3d ko description

topic_urls=[]
i=0
for topic_url in link_tags:
    topic_url='https://github.com'+link_tags[i]['href']
    i+=1
    topic_urls.append(topic_url)
# print(topic_urls)  #url ko list
    
topic_dict={'Topic':topic_title,
            'Description':topic_desc,
            'Url':topic_urls
            }


topics_df=pd.DataFrame(topic_dict)
# print(topics_df)


topics_df.to_csv('topics.csv',index=None)


#getting the information from the topics url

#scrapping another page of github

for topic in topic_urls:
    print(topic)


