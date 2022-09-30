from ast import Index
from typing import Text, Union
from fastapi import FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel
import uvicorn
import urllib
import facebook
import pymysql.cursors  
import greenlet
import cryptography

app=FastAPI()

#connection 
#on change host=localhost pour insertion dans la BD local sur mysql
#on change de host par nom de conteneur de  "jovial_hypatia " pour insertion les donnes dans la base créer dans conteneur 
connection = pymysql.connect(host='jovial_hypatia',
                             user='root',
                             password='ouma97',                             
                             db='dataextract',
                             port=3306,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor) 
    





@app.get("/page/details/test")
async def scrapping():

    token='EABTupnvbgCwBAFs6D01bS0ZB0tcPE6QhQGsXKZBMUGQHZAyeyC4j1YT4571Req34gY21SoHJhxZCyZCr9VIUgS72rtPMpOxnzkD369tcXg74dUVIelqNdukJ1w7hzxj5BaMf4UdKGfPZA7TG8qMJDqZB8u7IAoIiBGSDs8ZC1dxcYKQo1Vi1ffl1'
    #les donnees de ma page c
    graph=facebook.GraphAPI(access_token=token, version= 2.9)
    details=graph.request('/me/?fields=feed,name') 
    return  details      
     
@app.get("/page/details")
async def scrapping_save():

    token='EABTupnvbgCwBAFs6D01bS0ZB0tcPE6QhQGsXKZBMUGQHZAyeyC4j1YT4571Req34gY21SoHJhxZCyZCr9VIUgS72rtPMpOxnzkD369tcXg74dUVIelqNdukJ1w7hzxj5BaMf4UdKGfPZA7TG8qMJDqZB8u7IAoIiBGSDs8ZC1dxcYKQo1Vi1ffl1'
    #scrapping les donnees de ma page c par .GraphAPI 
    graph=facebook.GraphAPI(access_token=token, version= 2.9)
    details=graph.request('/me/?fields=feed,name')  
    #save les données 
    for key in details:
         if(key=='id'):
            idglobal= details[key]
         elif((key=='name')):
           nameglobal=details[key]       
         elif((key=='feed')):
            feed=details[key]
            for k in details[key]:
             if(k=='data'):
                data=details[key][k]
                details[key][k][0].update(story=None) 
                for kk in details[key][k][0]:
                        if(kk=='id'):
                           iddata=details[key][k][0][kk]
                        elif(kk=='story'):
                           storydata=details[key][k][0][kk]
                        elif(kk=='created_time'):
                           timedata=details[key][k][0][kk]
                for kk in details[key][k][1]:
                        if(kk=='id'):
                           iddata1=details[key][k][1][kk]
                        elif(kk=='story'):
                           storydata1=details[key][k][1][kk]
                        elif(kk=='created_time'):
                           timedata1=details[key][k][1][kk]    
                for kk in details[key][k][2]:
                        if(kk=='id'):
                           iddata2=details[key][k][2][kk]
                        elif(kk=='story'):
                           storydata2=details[key][k][2][kk]
                        elif(kk=='created_time'):
                           timedata2=details[key][k][2][kk]
                for kk in details[key][k][3]:
                        if(kk=='id'):
                           iddata3=details[key][k][3][kk]
                        elif(kk=='story'):
                           storydata3=details[key][k][3][kk]
                        elif(kk=='created_time'):
                           timedata3=details[key][k][3][kk]    
         elif(k=='paging') :
          pagging=details[key][k]
         for kl in details[key][k]:
                     if(kl=='cursors'):
                        cursor=1
                        for kj in details[key][k][kl]:
                           if(kj=='before'):
                               before=details[key][k][kl][kj]
                           elif(kj=='after'):
                              after=details[key][k][kl][kj]      
      
         idd=[]
         storyy=[]
         timee=[]
       
         id=idd.append(iddata)
         id=idd.append(iddata1)
         id=idd.append(iddata2)
         id=idd.append(iddata3)
         story=storyy.append(storydata)
         story=storyy.append(storydata1)
         story=storyy.append(storydata2)
         story=storyy.append(storydata3)
         time=timee.append(timedata)
         time=timee.append(timedata1)
         time=timee.append(timedata2)
         time=timee.append(timedata3) 
         #création des table sur ma base données ""dataextract"""
         cursor = connection.cursor() 
         sql ="CREATE TABLE data ( id_data VARCHAR(255)  ,story VARCHAR(255) ,time VARCHAR(255) )"
      
         cursor.execute(sql)  
         cursor = connection.cursor() 
         sql1 ="CREATE TABLE detail (id_detail VARCHAR(255), name VARCHAR(255), padding_before Text, padding_after Text)"   
         cursor.execute(sql1)      

         #Insertion les données dans la table ""data"""
         cursor = connection.cursor() 
         sql =  "Insert into data (id_data, story,time) "  + " values (%s, %s,%s) " 
         cursor.execute(sql, (idd[0], storyy[0],timee[0] ) )
         cursor.execute(sql, (idd[1], storyy[1],timee[1] ) ) 
         cursor.execute(sql, (idd[2], storyy[2],timee[2] ) ) 
         cursor.execute(sql, (idd[3], storyy[3],timee[3] ) )  
         connection.commit()
         
         for key in details:
            if(key=='id'):  
               idglobal=details[key]
            elif (key=='name'):    
                idglobal=details[key]
         nameglobal=details['name']
         idglobal=details['id']
                  #Insertion les données dans la table ""detail"""

         cursor = connection.cursor() 
         sql =  "Insert into detail (id_detail, name,padding_before,padding_after) "  + " values (%s, %s,%s,%s) " 
         cursor.execute(sql, (idglobal, nameglobal,before,after) )             
         connection.commit()
         
                
           
   
      
         return details


 