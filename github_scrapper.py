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

import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_topics():
    url="https://github.com/topics"
    r=requests.get(url)
    content=r.text
    # with open('topics.html','w',encoding='utf-8') as f:
    #     f.write(content)
    parsed_doc_1=BeautifulSoup(content,'html.parser')

    title_tags=parsed_doc_1.find_all('p',
                    {'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})
    description_tags=parsed_doc_1.find_all('p',{'class':"f5 color-fg-muted mb-0 mt-1"})

    link_tags=parsed_doc_1.find_all('a',{'class':'no-underline flex-1 d-flex flex-column'})
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
    return topic_urls

def get_sub_topic():
    topic_urls=get_topics()
    for topic in topic_urls:
        print(f"-----{topic.removeprefix('https://github.com/topics/')}----")
        new_url=topic
        response=requests.get(new_url)
        sub_topic_content=response.text
        parsed_doc_2=BeautifulSoup(sub_topic_content,'html.parser')
        sub_topic_username=parsed_doc_2.find_all('h3',{'class':'f3 color-fg-muted text-normal lh-condensed'})
        username=[]
        username_url=[]
        repo_url=[]
        repo_name=[]
        for i in range(0,len(sub_topic_username)):
            user_tag=sub_topic_username[i].find_all('a')
            username.append(user_tag[0].text.strip())
            username_url.append("https://github.com/"+user_tag[0].text.strip())
            repo_name.append(user_tag[1].text.strip())
            repo_url.append("https://github.com/"+user_tag[1].text.strip())
        
        #for stars in that repo
        star=parsed_doc_2.find_all('span',{'id':'repo-stars-counter-star'})

        star_count=[]
        for i in range(len(star)):
            star_count.append(star[i].text)
        repo_dict={
            'Username':username,
            'Username Url':username_url,
            'Repository Name':repo_name,
            'Repo Url':repo_url,
            'Star Count':star_count
        }
        repo_datas=pd.DataFrame(repo_dict)
        print(repo_datas)
        # print(repo_df)
        # repo_df.to_csv('repos.csv',index=None)
   


if __name__=="__main__":
    get_sub_topic()


