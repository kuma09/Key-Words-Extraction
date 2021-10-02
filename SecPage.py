# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 01:10:14 2019

@author: Force Technologies
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:39:48 2019

@author: Force Technologies
"""
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

import f
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
from collections import Counter
from nltk.stem.isri import ISRIStemmer
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.util import everygrams
import nltk
from snowballstemmer import stemmer
import os


class SecPage(QDialog):
	def __init__(self):
            super(SecPage,self).__init__()
            loadUi('interface.ui',self)
            self.pushButton.clicked.connect(self.entree)
            self.pushButton_3.clicked.connect(self.enter)
            self.pushButton_5.clicked.connect(self.ent)
            self.pushButton_4.clicked.connect(self.entt)

            

	def entree(self):	
            name = QFileDialog.getOpenFileName(self,'pushButton','/home')
            if name[0]:
              f= open(name[0], 'r',encoding='utf-8')
              with f:
                  text=f.read()
                  self.plainTextEdit_2.setPlainText(text)
            train = [
    ('هاتف سامسونغ غالاكسي.', 'تكنولوجيا'),           
    ('اندرويد.', 'تكنولوجيا'),            
    ('فيروسات.', 'تكنولوجيا'),            
    ('شركة مايكروسوفت.', 'تكنولوجيا'),            
    ("اجهزة تلفزيون", 'تكنولوجيا'),           
    ('انترنت', 'تكنولوجيا'),          
    ('فايرفوكس.', 'تكنولوجيا'),           
    ("متصفح", 'تكنولوجيا'),           
    ('قراصنة', 'تكنولوجيا'),          
    
    ('غوغل.', 'تكنولوجيا'),           
    ('هواتف ذكية.', 'تكنولوجيا'),         
    ('اوفيس.', 'تكنولوجيا'),          
    ("تطبيقات", 'تكنولوجيا'),         
    ('نظام تشغيل', 'تكنولوجيا'),          
    ('ابل.', 'تكنولوجيا'),            
    ("ويندوز", 'تكنولوجيا'),          
  ('زواحف.', 'علوم'),            
    ('تحليل اسنان.', 'علوم'),            
    ('تماسيح.', 'علوم'),         
    ('ارض.', 'علوم'),            
    ("قمر", 'علوم'),         
    ('نظام شمسي', 'علوم'),           
    ('تلسكوب.', 'علوم'),         
    ("فضاء", 'علوم'),            
    ('ناسا', 'علوم'),            
    
    ('علوم.', 'علوم'),           
    ('أبحاث.', 'علوم'),          
    ('مجرات.', 'علوم'),          
    ('حياة.', 'علوم'),           
    ('نباتات.', 'علوم'),         
    ('حمض نووي.', 'علوم'),           
    ("دراسة", 'علوم'),           
    ("بلوتو", 'علوم'),           


    ('اتحاد اوروبي.', 'اقتصاد'),          
    ('استثمار.', 'اقتصاد'),           
    ('شركة بترول.', 'اقتصاد'),            
    ("عملة بتكوين", 'اقتصاد'),            
    ('عملات رقمية', 'اقتصاد'),            
    ('استثمارات.', 'اقتصاد'),         
    ("منتجات", 'اقتصاد'),         
  
        ('اسواق', 'اقتصاد'),          
('ليرة', 'اقتصاد'),           
    
    ('اسعار وقود.', 'اقتصاد'),            
    ('صندوق نقد.', 'اقتصاد'),         
    ('اسعار.', 'اقتصاد'),             
    ('اقتصاد.', 'اقتصاد'),            
    ('عملات.', 'اقتصاد'),         
    ('يورو.', 'اقتصاد'),          
    ("دينار", 'اقتصاد'),          
    ("استرليني", 'اقتصاد'),           
            ]
            test = [
    ('هاتف نقال.', 'تكنولوجيا'),          
    ('هواوي', 'تكنولوجيا'),             
     ('غوغل.', 'تكنولوجيا'),          
    ('سامسونغ.', 'تكنولوجيا'),            
    ('ثلاثية ابعاد.', 'تكنولوجيا'),           
    ("تطبيقات", 'تكنولوجيا'),         
    ('نظام تشغيل', 'تكنولوجيا'),          
    ('نظام شمسي.', 'علوم'),          
    ("زحل", 'علوم'),         
    ('رواد فضاء', 'علوم'),           
    
    ('علماء.', 'علوم'),          
    ('محطة فضاء دولية.', 'علوم'),            
    ('بكتيريا.', 'علوم'),            
    ("مريخ", 'علوم'),            
            
            ]
            cl = NaiveBayesClassifier(train)



            # Classify a Text
            
                
            blob = TextBlob(text, classifier=cl)
            print(blob)
            print("\n la précision est : {0} \n".format(cl.accuracy(test)))
            self.plainTextEdit.setPlainText(' تصنيف النص هو :   '+str(blob.classify()))




    
	def enter(self):
        
            zz=self.plainTextEdit_2.toPlainText()
            e=zz       
            e=zz.split(" ")
        
            w=[]
            for x in e:
                val=x.strip()
                w.append(val)
                clean_text=list(filter(''.__ne__,w))
            filtered_words = [word for word in clean_text if word not in stopwords.words('arabic')]
            t=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:.",37*" ")
            b=str(filtered_words).translate(t)
            d=re.sub(r'[0-9]+'," ",b)
            f=re.sub(r'[a-zA-Z]+'," ",d)
        
        
        
            zz = re.sub("ة", "ه", zz)
            zz = re.sub("[إأآا]", "ا", zz)
            zz = re.sub("ؤ", "ء", zz)
            zz = re.sub("ئ", "ء", zz)
            zz = re.sub("ي", "ى", f)
            zz = re.sub("ة", "7", zz)
            zz = re.sub("ات", "1", zz)
            zz = re.sub("ن", "2", zz)
            zz = re.sub("ة", "ه", zz)
            rr=re.findall(r'(\w+)',zz)
        
        
            ar_stemmer = stemmer("arabic")
            liste=[ar_stemmer.stemWord(x) for x in rr]
            zzz = re.sub("ى", "ي", str(liste))
            zzz = re.sub("ه", "ة", zzz)
            zzz = re.sub("1", "ات", zzz)
            zzz = re.sub("ة", "ه", zzz)
            zzz = re.sub("2", "ن", zzz)
            zzz = re.sub("7", "ة", zzz)
            rrr=re.findall(r'(\w+)',zzz)
            print(str(rrr))

            
            beta = [word for word in rrr if word not in stopwords.words('arabic')]    
            for word in beta:
                if word=='و':
                   beta.remove(word)
            str1=' '.join(str(eee) for eee in beta)
            with open('C:/Users/Force Technologies/Desktop/abc.txt',encoding='utf-8') as f:
                f_content = f.read()   
                ww=[]
                tt=f_content
                
                
                
                '''    segmentation    '''
            
               
                e=tt.split(".")          
                e=tt.split(" ")
                
                
                
                '''     filtrage    '''
            
                for x in e:
                    vale=x.strip()
                    ww.append(vale)
                    clean_texte=list(filter(''.__ne__,ww))  
                filtered_wordse = [word for word in clean_texte if word not in stopwords.words('arabic')]
                
                
                
                '''     la normalisation   '''
            
                tot=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:.",37*" ")
                bob=str(filtered_wordse).translate(tot)
                
                
                dod=re.sub(r'[0-9]+'," ",bob)
                fof=re.sub(r'[a-zA-Z]+'," ",dod)
                kok=re.findall(r'(\w+)',fof)
                ttot=[word for word in beta if word not in kok]
                
                
                '''        pos taggg      '''
                
                
                java_path = "C:/Program Files/Java/jdk1.8.0_111/bin/java.exe"
                os.environ['JAVAHOME'] = java_path 
                arabic_postagger = POS_Tag('C:/Users/Force Technologies/Desktop/stanford-postagger-full-2018-10-16/models/arabic.tagger','C:/Users/Force Technologies/Desktop/stanford-postagger-full-2018-10-16/stanford-postagger.jar')
                sentence = ttot    
                arabic_postagger._SEPARATOR = '/' 
                xx=arabic_postagger.tag(sentence) 
                print(xx)
                

    
                '''   élémination les post tag non utulisé   '''
                
                sent_clean = [x for (x,y) in xx if y not in ('VBD','VBP','IN','NOUN_QUANT','ADJ_NUM')]
                print('TEXT SANS VERBS')
                print(sent_clean)
                
                
                
                '''    la liste de n_gramme jus'q a 3    '''
                
                print('\n la liste de n_gramme jusq a 3 \n')
                gama=list(everygrams(sent_clean,max_len=3))
                
                
                
                ''' calcule de frequence de n_gramms'''
                
                counts = Counter(gama)
                print('\n',counts,'\n')
                
                
                
                ''' choisir le nombre de mot clés'''
                maissa=[]
                kuma=sorted( ((v,k) for k,v in counts.items()), reverse=True)
                xxxx=10
                for i in range(0,xxxx):      
                    maissa.append(kuma[i])
                    
                
                ''' return seulment  les mot clés '''
                str1=''.join(str(eee) for eee in maissa)
                str2=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:'.",38*" ")
                str3=str(str1).translate(str2)
                deff=re.sub(r'[0-9]+',",",str3)
                feff=re.sub(r'[a-zA-Z]+',"",deff)
                kastro=''.join(str(eeee) for eeee in feff)
                king=(kastro.strip())
                csgo=(re.sub(' +', ' ',king))
                cs=csgo.split(',')
                del cs[0]
                newList = []

                for item in cs:
                  unique = True
                  current = cs.pop()  
                
                  for string in cs:
                    if current in string:
                      unique = False
                
                  if unique:
                    newList.append(current)  
                
                  cs.insert(0, current)
                
                LL=[]
                nombre=self.plainTextEdit_3.toPlainText()
                nombre=int(nombre)

                for i in range(0,nombre):
                    cur=newList.pop()
                    LL.append(cur)
                LLL=','.join(str(eee) for eee in LL)
                self.plainTextEdit.setPlainText(str(LLL))
                name = QFileDialog.getOpenFileName(self,'pushButton','/home')
                if name[0]:
                    f= open(name[0], 'r',encoding='utf-8')
                    with f:
                        text=f.read()
                    f_contentt = text   
                    wzw=[]
                    tzt=f_contentt
                    e1=tzt.split(",") 
                    w1=[]
                    for x in e1:
                        val=x.strip()
                        w1.append(val)
                        clean_text1=list(filter(''.__ne__,w1))  
                    filtered_words1 = [word for word in clean_text1 if word not in stopwords.words('arabic')]
                    t2=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:.",37*" ")
                    b2=str(filtered_words1).translate(t)  
                    d2=re.sub(r'[0-9]+'," ",b2)
                    f2=re.sub(r'[a-zA-Z]+'," ",d2)
                    LL1=re.findall(r'(\w+)',f2)
                    print('\n',LL1,'\n')
                    LLL4=re.findall(r'(\w+)',LLL)
                    print('\n',LLL4,'\n')
                    
                    
                    '''    Evaluation    '''
                    i=0
                    rap=0
                    pre=0
                    corec=0
                    all1=len(LL1)
                    all2=len(LLL4)
                    corec=len([x for x in LL1 if x in LLL4])
                    print('Le nombre de mot clés',corec)      
                    rap=corec/all1
                    pre=corec/all2
                    print('Le rappel est :',rap)
                    print('La précision est :',pre) 

	def ent(self):
            zz=self.plainTextEdit_2.toPlainText()


            e=zz
            e=zz.split(" ")        
            w=[]
            for x in e:
                val=x.strip()
                w.append(val)
                clean_text=list(filter(''.__ne__,w))        
        
            filtered_words = [word for word in clean_text if word not in stopwords.words('arabic')]        
            t=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:.",37*" ")
            b=str(filtered_words).translate(t)            
            d=re.sub(r'[0-9]+'," ",b)
            f=re.sub(r'[a-zA-Z]+'," ",d)
        
        
        
            zz = re.sub("ة", "ه", zz)
            zz = re.sub("[إأآا]", "ا", zz)
            zz = re.sub("ؤ", "ء", zz)
            zz = re.sub("ئ", "ء", zz)
            zz = re.sub("ي", "ى", f)
            zz = re.sub("ة", "7", zz)
            zz = re.sub("ات", "1", zz)
            zz = re.sub("ن", "2", zz)
            zz = re.sub("ة", "ه", zz)
            rr=re.findall(r'(\w+)',zz)
                
            ar_stemmer = stemmer("arabic")
            liste=[ar_stemmer.stemWord(x) for x in rr]
            zzz = re.sub("ى", "ي", str(liste))
            zzz = re.sub("ه", "ة", zzz)
            zzz = re.sub("1", "ات", zzz)
            zzz = re.sub("ة", "ه", zzz)
            zzz = re.sub("2", "ن", zzz)
            zzz = re.sub("7", "ة", zzz)
            rrr=re.findall(r'(\w+)',zzz)
            self.plainTextEdit.setPlainText(str(rrr))


        		  




	def entt(self):
            zz=self.plainTextEdit_2.toPlainText()


            e=zz
            e=zz.split(" ")
            w=[]
            for x in e:
                val=x.strip()
                w.append(val)
                clean_text=list(filter(''.__ne__,w))
        
        
        
            filtered_words = [word for word in clean_text if word not in stopwords.words('arabic')]
        
            t=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:.",37*" ")
            b=str(filtered_words).translate(t)
            d=re.sub(r'[0-9]+'," ",b)
            f=re.sub(r'[a-zA-Z]+'," ",d)
        
        
        
            zz = re.sub("ة", "ه", zz)
            zz = re.sub("[إأآا]", "ا", zz)
            zz = re.sub("ؤ", "ء", zz)
            zz = re.sub("ئ", "ء", zz)
            zz = re.sub("ي", "ى", f)
            zz = re.sub("ة", "7", zz)
            zz = re.sub("ات", "1", zz)
            zz = re.sub("ن", "2", zz)
            zz = re.sub("ة", "ه", zz)
            rr=re.findall(r'(\w+)',zz)
        
        
            ar_stemmer = stemmer("arabic")
            liste=[ar_stemmer.stemWord(x) for x in rr]
            zzz = re.sub("ى", "ي", str(liste))
            zzz = re.sub("ه", "ة", zzz)
            zzz = re.sub("1", "ات", zzz)
            zzz = re.sub("ة", "ه", zzz)
            zzz = re.sub("2", "ن", zzz)
            zzz = re.sub("7", "ة", zzz)
            rrr=re.findall(r'(\w+)',zzz)

            
            beta = [word for word in rrr if word not in stopwords.words('arabic')]    
            for word in beta:
                if word=='و':
                   beta.remove(word)
            str1=' '.join(str(eee) for eee in beta)
            with open('C:/Users/Force Technologies/Desktop/abc.txt',encoding='utf-8') as f:
                f_content = f.read()   
                ww=[]
                tt=f_content
                
                
                
                '''    segmentation    '''
            
               
                e=tt.split(".")
                
                e=tt.split(" ")
                
                
                
                '''     filtrage    '''
            
                for x in e:
                    vale=x.strip()
                    ww.append(vale)
                    clean_texte=list(filter(''.__ne__,ww))  
                filtered_wordse = [word for word in clean_texte if word not in stopwords.words('arabic')]
                
                
                
                '''     la normalisation   '''
            
                tot=str.maketrans("<>٪۱۲۳۴۵۶۷۸۹۰&?!#{[|\@]}()-_)=/*-;,:.",37*" ")
                bob=str(filtered_wordse).translate(tot)
                
                
                dod=re.sub(r'[0-9]+'," ",bob)
                fof=re.sub(r'[a-zA-Z]+'," ",dod)
                kok=re.findall(r'(\w+)',fof)
                
                
                ttot=[word for word in beta if word not in kok]
                
                
                '''        pos taggg      '''
                
                
                java_path = "C:/Program Files/Java/jdk1.8.0_111/bin/java.exe"
                os.environ['JAVAHOME'] = java_path 
                arabic_postagger = POS_Tag('C:/Users/Force Technologies/Desktop/stanford-postagger-full-2018-10-16/models/arabic.tagger','C:/Users/Force Technologies/Desktop/stanford-postagger-full-2018-10-16/stanford-postagger.jar')
                sentence = ttot    
                arabic_postagger._SEPARATOR = '/' 
                xx=arabic_postagger.tag(sentence) 
                self.plainTextEdit.setPlainText(str(xx))
