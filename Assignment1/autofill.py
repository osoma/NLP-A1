
'''this app is dealing with Arabic Language '''
# -*- coding: utf-8 -*-
import tkinter
from functools import partial  
from tkinter import Label,Entry,Listbox,Button
import operator
#import the file
file=open('businesscnnAr08biz (2).html.txt',encoding='utf-8')
words=[]
words=file.read().split()  #p(W) all words
letters=20#limited letters for word (minimum)
index=0

words_count=[]
tuples_word=[]
for i in range(0,len(words)-2):
    temp=[]
    for j in range(i,i+3):
        temp.append(words[j])
    tuples_word.append(temp)

def run(index,letters,word):
    results=[]
    for item in tuples_word:   #item is a Tuple
        if index==letters:
            break
        if len(word)==1:
            if word[0]==item[0] :
                index +=1
                results.append(item)
            else:
                continue
        elif len(word)==2:
            if word[0]==item[0] and word[1]==item[1]:
                index +=1
                results.append(item)
            else:
                continue
        else:
            if word[-1]==item[0]:
                index +=1
                results.append(item)   
            else:
                continue
    results=adj(results)
    return results


def adj(results):
    words_2=[]
    words_3=[]
    words2_count=[]
    words3_count=[]
    for res in results:
        words_3.append(res[0]+" "+res[1]+" "+res[2])#trigram
        words_2.append(res[0]+" "+res[1]) #bigram
    for p in words_3:
        words3_count.append(words_3.count(p))
    for p in words_2:
        words2_count.append(words_2.count(p))
    result_2=list(zip(words_2,words2_count))
    result_3=list(zip(words_3,words3_count))
    word2,count2=zip(*result_2)
    word3,count3=zip(*result_3)
    probability=[]
    prob=1
    for i in range(0,len(result_3)):
        prob *= count3[i]/count2[i]
        probability.append(prob)
    result3=list(zip(list(word3),probability))
    sorted_result= sorted(result3, key=operator.itemgetter(1) , reverse=True) 
    px , counts= zip(*sorted_result)
    px=list(dict.fromkeys(px))
    return px

def output(e1,root):
    count=0
    word=e1.get().split()
    results=run(index,letters,word)
    Lb = Listbox(root) 
    for i in results:
        Lb.insert(count,i)
        count=count+1
    Lb.grid(column=1) 

#GUI_Main
root = tkinter.Tk() 
root.title("Arabic Auto Fill")
Label(root, text='Enter').grid(row=0) 
e1 = Entry(root) 
e1.grid(row=0, column=1) 
call=partial(output,e1,root)
Button(root, text='Suggestion', command=call).grid(row=1,column=1)
root.mainloop()