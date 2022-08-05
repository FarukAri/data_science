# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:21:35 2022

@author: FARI
"""
import numpy as np
import pandas as pd

number_of_student = int(input("Sınıftaki öğrenci sayısını giriniz: "))

stu_list = np.arange(1,number_of_student+1)

names_list = []
surnames_list = []
numbers_list = []
exam_scores_list = []
statuses_list = []
final_scores_list = []

for i in list(stu_list):

    name = input(f"{i}.Öğrenci adı : ")
    surname = input (f"{i}.Öğrenci soyadı : ")
    number = input(f"{i}.Öğrenci no : ")
    exam_score = int(input (f"{i}.Öğrenci puanı : "))
    
    if  exam_score > 60 and exam_score <=100 :
        print(f'{number} numaralı öğrenci {name} {surname} : Geçti')
        status = "Pass"
    else :
        print(f'{number} numaralı öğrenci {name} {surname} : Kaldı')
        status = "Fail"
        
    if  100 >= exam_score >= 90 :
        final_score = "AA"
    elif  90 > exam_score >= 85 :
        final_score = "BA"
    elif  85 > exam_score >= 80 :
        final_score = "BB"    
    elif  80 > exam_score >= 75 :
        final_score = "CB"  
    elif  75 > exam_score >= 70 :
        final_score = "CC"
    elif  70 > exam_score >= 65 :
        final_score = "CD"  
    elif  65 > exam_score >= 60 :
         final_score = "DD"     
    elif  60 > exam_score >= 50 :
        final_score = "FD"  
    elif  50 > exam_score >= 0 :
        final_score = "FF"  
    else :
        print("Sınav notunuz 0 ile 100 arasında olmalıdır")
        i = i - 1
     
    
    names_list.append(name)
    surnames_list.append(surname)
    numbers_list.append(number)
    exam_scores_list.append(exam_score)
    statuses_list.append(status)
    final_scores_list.append(final_score)
    

ogrenciler = {
    "Name" : names_list,
    "Surname" : surnames_list,
    "Number" : numbers_list,
    "Exam Score" : exam_scores_list ,
    "Lesson Status" : statuses_list,
    "Letter Grade" : final_scores_list
        } 
    
ogrenciler_df = pd.DataFrame(ogrenciler, index=stu_list)
ogrenciler_df.to_csv("ogrenciler.csv")

