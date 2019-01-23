
#define all the global variables for the program. These variables are all for the first data source
list_of_headlines=[]
list_of_headlines_remote=[]
dictionary_of_propernouns={}
dictionary_of_headlines={}
list2_of_sections=[]
list2_of_sections_remote=[]

list_of_sections_remote={}

# In[74]:
# this function extracts propernouns from a headline it uses the library nltk. please install nltk in your python for this to function

def extractpropernouns(headline):
#using the library nltk extract propernouns from headlines
    import nltk
    from nltk.tag import pos_tag
    propernouns_dict={}
    sentence=headline
    tagged_sent = pos_tag(sentence.split())
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]
    #propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    for word,pos in tagged_sent:
        if(pos=='NNP'):
            propernouns_dict[word]=+1
    return propernouns_dict

#function from prevous homework to scrape datasource 1
def accessdataset1():
    #this code accesses the data from the 1st source and stores it as a list of strings
    # we do web scraping here using beautifulsoup and requests and store the result in the for of a list of strings 
    import requests
    from bs4 import BeautifulSoup
    #print("The data Source is Most Popular Page from LA Times. LA Times selectes many popluar or top headlines and puts them on its most popular page")
    #print(" I am getting this data set by scraping the url: http://www.latimes.com/popular/")
    #print("I am obtaining the headlines of the popular articlesand storethe headlines as a list of strings")
    #print("\n")
    #print("Brief Snapshot of the data:\n")
    page = requests.get(url = 'http://www.latimes.com/popular/')
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.select('[class*="trb_outfit_relatedListTitle_a"]')
    table2=soup.select('[class*="trb_outfit_categorySectionHeading_a"]')
    list_of_table=[]
    list_of_table=table
    list_of_sections={}
    count=0
    for item in list_of_table:
        
        
        
            #print(item.get_text())
            list_of_headlines.append(item.get_text())
            
            for item2 in table2:
                
                
                list_of_sections[item2.get_text()] = 1

                
                list2_of_sections.append(item2.get_text())           
        
            
                

    
    return list_of_sections
#function from prevous homework to scrape datasource 2

def accessdataset2():
#this code accesses data from the 2nd source and stores it as a dictionary of title with description
#this code uses the google news aggregator to collect top stories

    print("The source of data is “top headlines” from “Google News”")
    print("\n")
    print("This data set I am getting it from Google News API API end point 'https://newsapi.org/v2/top-headlines?country=us&apiKey=365ceb93826841d98107debf9558046")
    print("For this data set I am obtaining Title and Description \n")
    print("Snapshot of the data: First Title and then Description\n")

    import urllib.request, urllib.parse, urllib.error
    import json
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=365ceb93826841d98107debf9558046c'
    # request the page and append it with your key
    uh = urllib.request.urlopen(url)
    #get the data
    data = uh.read().decode()
    #data so returned of the format json
    js3 = json.loads(data)
    #extract articles from returned data
    item=js3['articles']
    length=len(js3['articles'])
    count=0
    #create a dictionary of news titles and thier description
    dictofnews={}
    for item2 in item:
        #extract news title
        print(item2['title'])
        #extract newd description
        print(item2['description'])
        key=item2['title']
        value=item2['description']
        #store it in a dictionary where title is the key and descirption is the value
        dictofnews[key]=value
        print("\n")
        count=count+1
        if(count==5):
            break 


# In[75]:

list_of_sections={}
#list_of_sections=accessdataset1()
#print(list_of_sections)
#function from prevous homework to scrape datasource 3

def accessdataset3():
    #this code accesses data from the 3rd source and stores it as a dictionary of title with description
    #this ode uses new york top stories to get the top headlines and their description

    print("The source of data is New York Times. New York times has an API NYT API for accessing top stories. However that API provides integration only for PHP, Javascript, NODEJS and RUBy I wanted something for python so I use a wrapper for it")
    print("\n")
    print("The data I am getting it from nytimes-top-stories is a simple Python wrapper for New York Times’ Top Stories API. Compatible with Python 2.7 and 3+")
    print("To use it do pip install nytimes-top-stories")
    print("API end point  api.get_stories() after a succesful install and import into your code")
    print("\n")
    print("I am obtaining title and abstract(short description of news item)")
    print("\n")
    print("Snapshot of the data: First Title and then Abstract\n")
    #the wrapper built over NYTimes API
    from topstories import TopStoriesAPI
    #My key
    api = TopStoriesAPI('6c83f401974b4736b1f43966cf0a10a2')
    #gets the news stories
    stories = api.get_stories("home")
    count=0
    dictofnews2={}
    for item in stories:
        #extract the title
        print(item['title'])
        #extract teh description
        print(item['abstract'])
        print("\n")
        key2=item['title']
        value2=item['abstract']
        #store it as a dictionary with key as title and value as description
        dictofnews2[key2]=value2
        count=count+1
        if(count==5):
            break

# In[124]:
#the paradigm is to define datamodel for each data source using define as a prefix when naming the function. definedatamodesource1() defines the data model for 
#source 1 using sqlalchemy 
#defining data model for source 1
def definedatamodesource1():
    import os
    import sys
    from sqlalchemy import Column, ForeignKey, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship
    from sqlalchemy import create_engine
    Base = declarative_base()
# these classes have equivalent tables in data base
    class Latimes_section_of_newspaper(Base):
        __tablename__ = 'la_times_section_of_newspaper'
    # Here we define columns for the table la_times_section_of_newspaper
    # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False,unique=True)
    class Latimes_Propernouns(Base):
        __tablename__ = 'la_times_propernouns'
        id=Column(Integer, primary_key=True)
        name=Column(String(250), nullable=False,unique=True)
    class LAtimes_Headline(Base):
        __tablename__ = 'latimes_headline'
    # Here we define columns for the table la_times_propernouns
    # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        la_times_section_of_newspaper_id = Column(Integer, ForeignKey('la_times_section_of_newspaper.id'))
        la_times_section_of_newspaper = relationship(Latimes_section_of_newspaper)
        name_of_section=Column(String(250))
    
    class Latimes_Headlines_with_propernouns(Base):
        __tablename__ = 'latimes_headlines_with_propernouns'
    # Here we define columns for the table latimes_headlines_with_propernouns.
    # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        latimes_headline_id = Column(Integer, ForeignKey('latimes_headline.id'))
        latimes_headline = relationship(LAtimes_Headline)
        la_times_propernouns_id=Column(Integer, ForeignKey('la_times_propernouns.id'))
        la_times_propernouns=relationship(Latimes_Propernouns)

# sqlalchemy_example.db file.
    engine = create_engine('sqlite:///newsfinal.db')
 
  #Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
    Base.metadata.create_all(engine)


# In[125]:
#inserting values in the datamodel defined above using sqlite

def insertdatamodelsource1(list_of_sections):
    import sqlite3
    conn=sqlite3.connect('newsfinal.db')
    cur=conn.cursor()
    for key in list_of_sections:
#ensure no duplicates
        cur.execute("SELECT name FROM la_times_section_of_newspaper WHERE (name=?)", (key,))
        entry_of_section=cur.fetchone()
        if(entry_of_section is None):
            cur.execute('INSERT INTO "la_times_section_of_newspaper" (name) values (?)',(key,))
            conn.commit()
    
    i=0
    for every_headline2 in list_of_headlines:
            my_value=list2_of_sections[i]
            i=i+1

            entry=cur.execute("SELECT id FROM la_times_section_of_newspaper WHERE (name=?)",(my_value,))
            entry = cur.fetchone()
            cur.execute("SELECT name, la_times_section_of_newspaper_id FROM latimes_headline WHERE (name=?)", (every_headline2,))
            entry2=cur.fetchone()
            if(entry2 is None):

                cur.execute('INSERT INTO "latimes_headline" (name,la_times_section_of_newspaper_id,name_of_section) values (?,?,?)',(every_headline2, entry[0], my_value,))
                conn.commit()



    for every_headline in list_of_headlines:
            
            propernouns2=extractpropernouns(every_headline)
            for each_propernoun in propernouns2:
                cur.execute("SELECT name, id FROM la_times_propernouns WHERE (name=?)",(each_propernoun,))
                entry3=cur.fetchone()
            
                if(entry3 is None):
                    cur.execute('INSERT INTO "la_times_propernouns" (name) values (?)',(each_propernoun,))
                    conn.commit()
            cur.execute("SELECT id FROM latimes_headline WHERE (name=?)",(every_headline,))
            entry4= cur.fetchone() 

            for each_propernoun2 in propernouns2:
                    cur.execute("SELECT name, id FROM la_times_propernouns WHERE (name=?)",(each_propernoun2,))
                    entry5=cur.fetchone()
                    cur.execute("SELECT * FROM latimes_headlines_with_propernouns WHERE (latimes_headline_id=? AND la_times_propernouns_id=?)",(entry4[0], entry5[1],))
                    entry6=cur.fetchone()
                    if(entry6 is None):
                        cur.execute('INSERT INTO "latimes_headlines_with_propernouns" (latimes_headline_id,la_times_propernouns_id) values (?,?)',(entry4[0], entry5[1],))
                        conn.commit()
                    else:
                        continue
    
#this function also gets more data from source 1 and inserts in db and is used for more computations
def insertdatamodelremotesource1():
    import sqlite3
    conn=sqlite3.connect('newsfinal.db')
    cur=conn.cursor()
    #finding sections and storing them
    for key in list_of_sections_remote:

        cur.execute("SELECT name FROM la_times_section_of_newspaper WHERE (name=?)", (key,))
        entry_of_section=cur.fetchone()
        if(entry_of_section is None):
            cur.execute('INSERT INTO "la_times_section_of_newspaper" (name) values (?)',(key,))
            conn.commit()
    
    #every headline is parsed to extract propernouns and then stored in the database in its appropriate table 
    i=0
    for every_headline in list_of_headlines_remote:
            my_value=list2_of_sections_remote[i]
            i=i+1
            cur.execute("SELECT id FROM la_times_section_of_newspaper WHERE (name=?)",(my_value,))
            entry = cur.fetchone()
            cur.execute("SELECT name, id FROM latimes_headline WHERE (name=?)",(every_headline,))
            entry2=cur.fetchone()
            
            if(entry2 is None):
                cur.execute('INSERT INTO "latimes_headline" (name,la_times_section_of_newspaper_id,name_of_section) values (?,?)',(every_headline, entry[0],my_value,))
                conn.commit()
            propernouns2=extractpropernouns(every_headline)
            for each_propernoun in propernouns2:
                cur.execute("SELECT name, id FROM la_times_propernouns WHERE (name=?)",(each_propernoun,))
                entry3=cur.fetchone()
            
                if(entry3 is None):
                    cur.execute('INSERT INTO "la_times_propernouns" (name) values (?)',(each_propernoun,))
                    conn.commit()
            cur.execute("SELECT id FROM latimes_headline WHERE (name=?)",(every_headline,))
            entry4= cur.fetchone() 

            for each_propernoun2 in propernouns2:
                    cur.execute("SELECT name, id FROM la_times_propernouns WHERE (name=?)",(each_propernoun2,))
                    entry5=cur.fetchone()
                    cur.execute("SELECT * FROM latimes_headlines_with_propernouns WHERE (latimes_headline_id=? AND la_times_propernouns_id=?)",(entry4[0], each_propernoun2,))
                    entry6=cur.fetchone()
                    if(entry6 is None):
                        cur.execute('INSERT INTO "latimes_headlines_with_propernouns" (latimes_headline_id,la_times_propernouns_id) values (?,?)',(entry4[0], entry5[1],))
                        conn.commit()
                    else:
                        continue       
        
#the paradigm is to define datamodel for each data source using define as a prefix when naming the function. definedatamodelsource2() defines the data model for 
#source 2 using sqlalchemy 
#defining data model for source 2

def definedatamodelsource2():
    import os
    import sys
    from sqlalchemy import Column, ForeignKey, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship
    from sqlalchemy import create_engine
    Base = declarative_base()

    class Google_news_source_of_news(Base):
        __tablename__ = 'google_news_source_of_news'
    # Here we define columns for the table google_news_source_of_news, google_news_source_of_news,google_news_author,google_news_master
    # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=True)
        google_source_id = Column(String(250), nullable=True)


    class Google_news_Propernouns(Base):
        __tablename__ = 'google_news_propernouns'
        id=Column(Integer, primary_key=True)
        name=Column(String(250), nullable=False)
        title=Column(String(250))

    class Google_news_author(Base):
        __tablename__ = 'google_news_author'
        id=Column(Integer, primary_key=True)
        name=Column(String(250), nullable=True,unique=True)

    class Google_news_Master(Base):
        __tablename__ = 'google_news_master'
        id=Column(Integer, primary_key=True)
        index=Column(Integer)
        source_id=Column(String(250))
        source_name=Column(String(250))
        author=Column(String(250))
        title=Column(String(250))
        description=Column(String(500))
        url=Column(String(250))
        publishedat=Column(String(250))       
        
# sqlalchemy_example.db file.
    engine = create_engine('sqlite:///newsfinal.db')
 
  #Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
    Base.metadata.create_all(engine)


    
#inserting values in the datamodel defined above using sqlite
   


def insertdatamodelsource2():
    import pandas as pd
    import sqlite3
    from sqlalchemy import create_engine
#use pandas datafame to fetch and store data as lists using mykey
    df=pd.read_json('https://newsapi.org/v2/top-headlines?country=us&apiKey=365ceb93826841d98107debf9558046c',orient='columns')
    source_name=[]
    source_id=[]
    author=[]
    title=[]
    description=[]
    url=[]
    publishedat=[]
    allnews=[]
    mlab = sqlite3.connect('newsfinal.db')
    engine = create_engine('sqlite:///newsfinal.db')
    #data so extracted from the data frames is now very carefully persisted in db
    #ensured that no redundancy happens we first check is that entry exist
    #also we extract propernons from each headline and store it in propernouns table with its right title in db
    
    cur=mlab.cursor()
    for item in df['articles']:
        source_id.append(item['source']['id'])
        source_name.append(item['source']['name'])
        cur.execute("SELECT id FROM google_news_source_of_news WHERE (google_source_id=?)",(item['source']['id'],))
        entryforsourcenews=cur.fetchone()
        if(entryforsourcenews is None):
            cur.execute('INSERT INTO "google_news_source_of_news" (name, google_source_id) values (?,?)',(item['source']['name'], item['source']['id'],))
            mlab.commit()
        author.append(item['author'])

        
        if(item['author']!=''):
            cur.execute("SELECT id FROM google_news_author WHERE (name=?)", (item['author'],))
            entryforauthor=cur.fetchone()

            if(entryforauthor is None):
                cur.execute('INSERT INTO "google_news_author" (name) values (?)', (item['author'],))
                mlab.commit()
        title.append(item['title'])
        propernouns2=extractpropernouns(item['title'])
        for each_propernoun in propernouns2:
                cur.execute("SELECT name, id FROM google_news_propernouns WHERE (name=? AND title=?)",(each_propernoun, item['title'],))
                entry3=cur.fetchone()

                if(entry3 is None):
                    cur.execute('INSERT INTO "google_news_propernouns" (name, title) values (?,?)',(each_propernoun, item['title'],))
                    mlab.commit()
        description.append(item['description'])
        url.append(item['url'])
        publishedat.append(item['publishedAt'])
    newsdataframe = pd.DataFrame(
        {'source_id': source_id,
         'source_name': source_name,
         'author': author,
         'title': title,
         'description':description,
         'url': url,
         'publishedat': publishedat
        })
    mlab = sqlite3.connect('newsfinal.db')
    engine = create_engine('sqlite:///newsfinal.db')

    # Write our pandas dataframe to the SQLite database
    
    cur=mlab.cursor()
    #cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='google_news_master'")
    #entryfortable=cur.fetchone()
    cur.execute("SELECT * FROM'google_news_master'")
    itemintable=cur.fetchone()
    if(itemintable is None):
        newsdataframe.to_sql('google_news_master', engine, if_exists='append')
    #else:
        #print("Remotely entered data in db")
        #cur.execute("SELECT * FROM google_news_master")
        #demo_data=cur.fetchone()
        #print(demo_data)

#the paradigm is to define datamodel for each data source using define as a prefix when naming the function. definedatamodelsource3() defines the data model for 
#source 3 using sqlalchemy 
#defining data model for source 3
def definedatamodelsource3():
    import os
    import sys
    from sqlalchemy import Column, ForeignKey, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship
    from sqlalchemy import create_engine
    Base = declarative_base()

    class Nytimes_section_of_newspaper(Base):
        __tablename__ = 'ny_times_section_of_newspaper'
    # Here we define columns for the table ny_times_section_of_newspaper,ny_times_propernouns,ny_times_news_master,ny_times_news_master,ny_times_location
    # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False,unique=True)


    class Nytimes_Propernouns(Base):
        __tablename__ = 'ny_times_propernouns'
        id=Column(Integer, primary_key=True)
        name=Column(String(250), nullable=False)
        title=Column(String(250))

    

    class Nytimes_news_Master(Base):
        __tablename__ = 'ny_times_news_master'
        id=Column(Integer, primary_key=True)
        index=Column(Integer)
        title=Column(String(250))
        abstract=Column(String(500))
        section=Column(String(500))

    class Nytimes_keywords(Base):
        __tablename__='ny_times_keyword'
        id=Column(Integer, primary_key=True)
        keyword=Column(String(250))
        title=Column(String(250))
    class Nytimes_location(Base):
        __tablename__='ny_times_location'
        id=Column(Integer,primary_key=True)
        location=Column(String(250))
        title=Column(String(250))
    
            
        
# sqlalchemy_example.db file.
    engine = create_engine('sqlite:///newsfinal.db')
 
  #Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
    Base.metadata.create_all(engine)


    
    
   #here a pie chart is created for la times and Nytimes to understand the distribution oof news over sections
def pieplot():

    import matplotlib.pyplot as plt
    import sqlite3
    conn=sqlite3.connect('newsfinal.db')
    cur=conn.cursor()
#get the names of all sections from latimes headlines
    cur.execute("SELECT name_of_section FROM latimes_headline")
    entry=cur.fetchall()
    #count the no.of sections
    count_of_sections={}
    for item in entry:
        if(item in count_of_sections.keys()):
            count_of_sections[item]=count_of_sections[item]+1
        else:
            count_of_sections[item]=1
    key2=[]
    value2=[]
    # after getting counts for each section store them as lists
    for item2 in count_of_sections.keys():
        key2.append(item2[0])
    for item3 in count_of_sections.values():
        value2.append(int(item3))
    labels = key2
    sizes = value2
    #plot the values
    fig, ax1= plt.subplots()

    
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("LA Times distribution of top headlines over different sections")
    plt.show()
    #follow similarly for ny times 
    cur.execute("SELECT section FROM ny_times_news_master")
    entry2=cur.fetchall()
    count_of_sections2={}
    for item4 in entry2:
        if(item4 in count_of_sections2.keys()):
            count_of_sections2[item4]=count_of_sections2[item4]+1
        else:
            count_of_sections2[item4]=1
    key3=[]
    value3=[]
    for item3 in count_of_sections2.keys():
        key3.append(item3[0])
    for item4 in count_of_sections2.values():
        value3.append(int(item4))
    sizes = value3
    fig2,ax2=plt.subplots()
    ax2.pie(value3, labels=key3, autopct='%1.1f%%',
        shadow=False, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title("New York Times distribution of top headlines over different sections")



    plt.show()


    




    
def insertdatamodelsource3():
    import pandas as pd
    import sqlite3
    from topstories import TopStoriesAPI
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///newsfinal.db')
    mlab = sqlite3.connect('newsfinal.db')
    cur=mlab.cursor()
#use a wrapper built to fetch the data

    #My key
    api = TopStoriesAPI('6c83f401974b4736b1f43966cf0a10a2')
    stories = api.get_stories("home")
    list_of_titles=[]
    list_of_abstract=[]
    list_of_section=[]
    list_of_keywords=[]
    list_of_location=[]
     #data so extracted from the data frames is now very carefully persisted in db
    #ensured that no redundancy happens we first check is that entry exist
    #also we extract propernons from each headline and store it in propernouns table with its right title in db
    for item in stories:
        #extract the title
            
        list_of_titles.append(item['title'])
        #extract the description
        propernouns2=extractpropernouns(item['title'])
        for each_propernoun in propernouns2:
                cur.execute("SELECT name, id FROM ny_times_propernouns WHERE (name=? AND title=?)",(each_propernoun, item['title'],))
                entry3=cur.fetchone()

                if(entry3 is None):
                    cur.execute('INSERT INTO "ny_times_propernouns" (name, title) values (?,?)',(each_propernoun, item['title'],))
                    mlab.commit()


        
        list_of_abstract.append(item['abstract'])

        if(item['section']!=''):
            list_of_section.append(item['section'])
            cur.execute("SELECT name FROM ny_times_section_of_newspaper WHERE (name=?)", (item['section'],))
            entry_of_section=cur.fetchone()
            if(entry_of_section is None):
                cur.execute('INSERT INTO "ny_times_section_of_newspaper" (name) values (?)',(item['section'],))
                mlab.commit()

        if(item['des_facet']!=[]):
            
            list_of_keywords.append(item['des_facet'])
            for everykeyword in item['des_facet']:

                cur.execute("SELECT * from ny_times_keyword WHERE (keyword=? AND title=?)",(everykeyword, item['title'],))
                entryforkeyword=cur.fetchone()
                if(entryforkeyword is None):
                    cur.execute("INSERT INTO ny_times_keyword (keyword, title) VALUES (?,?)",(everykeyword, item['title'] ))
                    mlab.commit()
        if(item['geo_facet']!=[]):
            
            list_of_location.append(item['geo_facet'])
            for location in item['geo_facet']:

                cur.execute("SELECT * from ny_times_location WHERE (location=? AND title=?)",(location, item['title'],))
                entryforlocation=cur.fetchone()
                if(entryforlocation is None):
                    cur.execute("INSERT INTO ny_times_location (location, title) VALUES (?,?)",(location, item['title'] ))
                    mlab.commit()
        
        
    #use pandas datafame to fetch and store data as lists

    df2=pd.DataFrame()
    df2['title']=list_of_titles
    df2['abstract']=list_of_abstract
    df2['section']=list_of_section
    mlab = sqlite3.connect('newsfinal.db')
    cur=mlab.cursor()
    cur.execute("SELECT * FROM ny_times_news_master ")
    entry=cur.fetchone()
    if(entry is None):
        df2.to_sql('ny_times_news_master', engine, if_exists='append')
        #print("writing to db")
    #else:
        #print("writing to db")

#this function does the computation on stored db. depending upon the newspaper it extracts the titles where trump featured and plots the result as a bar chart
def featuretrump():
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import sqlite3
    #connect to the database
    mlab = sqlite3.connect('newsfinal.db')
    cur=mlab.cursor()
    #get all the titles with propernoun trump
    cur.execute("SELECT title from google_news_propernouns WHERE name like 'Trump%'")
    entryfortrump=cur.fetchall()
    count_for_google=0
    count_for_newyork=0
    count_for_latimes=0

    #for each of the newspaper LA Times, NY Times and Google news, store the counts wof headlines where Trump featured

    for item in entryfortrump:
        
        count_for_google=count_for_google+1
    cur.execute("SELECT title from ny_times_propernouns WHERE name like 'Trump%'")
    entryfortrump2=cur.fetchall()
    for item2 in entryfortrump2:
        count_for_newyork=count_for_newyork+1
    cur.execute("SELECT id from la_times_propernouns WHERE (name=?)", ("Trump",))
    idfortrump=cur.fetchone()
    cur.execute("SELECT latimes_headline_id from latimes_headlines_with_propernouns WHERE (la_times_propernouns_id=?)", (idfortrump[0],))
    entryfortrumplatimes=cur.fetchall()
    for item5 in entryfortrumplatimes:
        count_for_latimes=count_for_latimes+1
    
    final_count=[]
    final_count.append(count_for_newyork)
    final_count.append(count_for_latimes)
    final_count.append(count_for_google)
    # plot these values against each of the newspapers
    objects = ["New York Times", " LA Times", "Google News"]
    y_pos = np.arange(len(objects))
    performance = final_count
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=6)
    plt.ylabel('no. of headlines')
    plt.title('No. of top headlines featuring President Trump!')

    plt.show()





#this function plots the headlines according to the leyword in New York Times

def plotbarnewyorktimes():
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    import sqlite3
    conn=sqlite3.connect('newsfinal.db')
    cur=conn.cursor()
#get the keywords from the db
    cur.execute("SELECT keyword FROM ny_times_keyword")
    entry=cur.fetchall()
    #count the no.of keywords and store unique ones with their counts
    count_of_keyword={}
    for item in entry:
        if(item in count_of_keyword.keys()):
            count_of_keyword[item]=count_of_keyword[item]+1
        else:
            count_of_keyword[item]=1
    key2=[]
    value2=[]
    for key,value in count_of_keyword.items():
        
        if((value>2)):
            value2.append(value)
            key2.append(key[0])
 
    objects = key2
    y_pos = np.arange(len(objects))
    performance = value2
 #plot the no.of headlines with the keyword
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=6)
    plt.ylabel('no. of headlines')
    plt.title('No. of top headlines according to keyword in New York Times')
    plt.show()


#this function plots location of news headlines of news featuring in NY Times
def plotbarnewyorktimeslocation():
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    import sqlite3
    import geocoder
    #geocoder is a library that can map a city, state to its appropriate country

    conn=sqlite3.connect('newsfinal.db')
    cur=conn.cursor()

    cur.execute("SELECT location FROM ny_times_location")
    entry=cur.fetchall()
    count_of_location={}
    #find out all the location referenced headlines of ny_ times
    #find out the country so referenced using geocoder

    for item in entry:
    
        g=geocoder.geonames(item[0], key='raveena')
        item_country=g.country
        if(item_country is not None):

            if(item_country in count_of_location.keys()):
                count_of_location[item_country]=count_of_location[item_country]+1
            else:
                count_of_location[item_country]=1
    key2=[]
    value2=[]
    for key,value in count_of_location.items():

        if((value>0)):
            value2.append(value)
            key2.append(key)
#plot the no.of headlines against country for ny times
 
    objects = key2
    y_pos = np.arange(len(objects))
    performance = value2
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=6)
    plt.ylabel('no. of headlines')
    plt.title('No. of top headlines according to country in New York Times (for US edition) ')
    plt.show()

#this function finds out the distribution of news against sources in google news
def topnewssourcesongooglenews():
    import matplotlib.pyplot as plt
    import sqlite3
    mlab = sqlite3.connect('newsfinal.db')
    cur=mlab.cursor()
    # every headline in google news master is stored with the source
    #query to find out all the sources

    cur.execute("SELECT source_name FROM google_news_master")
    entry=cur.fetchall()
    count_of_source={}
    #create a count of sources
    for item in entry:
        if(item in count_of_source.keys()):
            count_of_source[item]=count_of_source[item]+1
        else:
            count_of_source[item]=1
    key2=[]
    value2=[]
    for item2 in count_of_source.keys():
        key2.append(item2[0])
    for item3 in count_of_source.values():
        value2.append(int(item3))
    labels = key2
    sizes = value2
    fig2, ax1 = plt.subplots()
#plot the count of sources with their values as a pie chart
    
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Google News distribution of top headlines over different News Sources")
    plt.show()




#using mail function we call all define and insert functions to actually build our data model
#the system args them do specific computation based on your choice          
if __name__ == '__main__':
    import sys
    list_of_sections=accessdataset1()
    definedatamodesource1()
    insertdatamodelsource1(list_of_sections)
    definedatamodelsource2()
    insertdatamodelsource2()
    definedatamodelsource3()
    insertdatamodelsource3()
    
    

    
#for this code to work correctly please specify the which source whether remote or local"
#remote source remotely queries the geocoder API to find out the right location of headlines, it happens when plotbarnewyorktimeslocation is invoked

    if (sys.argv[1]=='-source=remote'):
        print("Capturing data from geocoder to get location for new york times headlines \n")
        print("Doing the following computation : how much news from different countries reported in New York Times US version")
        print("plotted the graph of how news from various countries is displayed in NY Times")
        plotbarnewyorktimeslocation()
        
        
#local source presents insights from data so collectied and stored from remote sources

    
    if (sys.argv[1]=='-source=local'):
        print("Retreiving data from local storage to perform the following computation and storing it in database :\n")
        print("Finding the distribution of section of news amongst headlines for LA Times and New York Times")
        print("Finding distribution of news sources in google news \n")
        print("Finding the usage of keywords in headlines of New York Times ")
        print("Finding the no.of headlines in google news, LA times and New York times featuring President Trump \n")
        pieplot()
        topnewssourcesongooglenews()
        plotbarnewyorktimes()
        featuretrump()


    
        
   



