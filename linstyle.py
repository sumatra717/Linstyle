import streamlit as st
import numpy as np
import pandas as pd
error=1
st.title('Linstyle')
st.write("""🕶️🌈 your Linux command stylist


""")
if st.button('Description'):
    st.write("""Features\n
    -delete end spaces\n
    -delete 2 and more spaces in row\n
    -change "–" to "-" after Word working\n
    -add first "/" to path with "mnt" or "home"\n
    -check "--" match to multiple symbols, similarly check "-"\n
    -change to Windows path\n
    -change "–" to "-" after Word working\n
    -remind about a relative path in the command\n
           """)
    st.write("""Usage\n
The program was created for the following reasons: difficulties in correcting commands in the console, errors in writing the command due to the human factor.
Especially useful:
- for Linux newcomers
- to check long commands\n
Try paste the command:    mnt/projects/nbulantsev/salmonella/PROKKA_02052020/PROKKA_02052020.ffn  -output     trinity_emmap --m diamond  –cpu 20


    """)

command = st.text_input('Paste the command', '/mnt/c/Users/' ,type='default')
#agree box

agree_mnt = st.checkbox("add first '/' to path with 'mnt' or 'home'", value=True)
agree_dash = st.checkbox("check '--' match to multiple symbols, similarly check '-'", value=True)
    
agree_win = st.checkbox('switch a command to Windows path')

    
#work_general
com_list=[]
for i, elem in enumerate(command):
    com_list.append(elem)
    #print(i,elem)
    
#print(com_list)
# delete end spaces
while com_list[0] == " " or com_list[-1] == " ":
    for i in com_list:
        if com_list[0]== " ":
            del com_list[0]
        if com_list[-1] == " ":
            del com_list[-1]


# delete 2 spaces in row
round_ = 'start'
while round_ != "end":
    for i, elem in enumerate(com_list):
        #print(i, len(com_list),elem)
        if i == len(com_list)-1:
            round_ = "end"
        if elem == " " and com_list[i+1] == " ":
            del com_list[i]
            break
          
#change "–" to "-" after Word working
new_com = ''.join(com_list)
new_com = new_com.replace('–', '-')
#place = 0
#print(new_com)

# Chapter II - parts. here work with split
#dont forget here new_com_list
#add first / to path with "mnt" or "home"
if agree_mnt:
    #place = 1
    new_com_list = new_com.split(" ")
    for numb,i in enumerate(new_com_list):
        if "mnt/" in i and "/mnt/" not in i:
            #print(numb,i)
            slash_i = "/" + i
            new_com_list[numb] = slash_i
    for numb,i in enumerate(new_com_list):
        if "home/" in i and "/home/" not in i:
            #print(numb,i)
            slash_i = "/" + i
            new_com_list[numb] = slash_i
    new_com = ' '.join(new_com_list)
if agree_dash:
    # check "--" match to multiple symbols, similarly check "-"
    new_com_list = new_com.split(" ")
    for numb,i in enumerate(new_com_list):
        if i.startswith("--") and "/" not in i:
            counter = len(i)
            if counter == 3:
                new_i = i.replace('--', '-')
                new_com_list[numb] = new_i
        if i.startswith("-") and "/" not in i and "--" not in i :
            counter = len(i)
            if counter > 3:
                new_i = '-' + i
                new_com_list[numb] = new_i
            #print(counter)
            #print(numb,i)
    new_com = ' '.join(new_com_list)
if agree_win:
        #change to win path
    #new_com = ' '.join(new_com_list)
    new_com = new_com.replace('/', '\\')
    #print(new_com) 
    
#change to absolute path as a error
new_com_list = new_com.split(" ")
for i in new_com_list:
    if "./"  in i:
        error=0
        text_path= "Probably relative path in the command, try changing to Absolute path."

st.subheader('Corrected command:')
st.write(new_com)#,place)
if error==0:
    st.error(text_path)
    
    
st.write("[Linstyle_Cli version is soon](https://github.com/sumatra717/Linstyle)")       
    
from PIL import Image    

im = Image.open("./IMG_20201101_160949.jpg")


st.image(im, width = 400)

st.subheader("[AG lab](https://scamt.ifmo.ru/science/groups/genome-bioinformatics/)")
st.subheader("[AG lab github](https://github.com/aglabx)")


