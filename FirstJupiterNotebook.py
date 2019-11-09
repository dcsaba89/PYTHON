#!/usr/bin/env python
# coding: utf-8

# In[343]:


# LIST  --- collection of certain items, separated by coma between square brackets


# In[344]:


L = [1, '11', "1da", [1, 3], ["X", 10, (11, 7)]] # lists can have different types of elements


# In[345]:


type(L) # return the type of a variable


# In[346]:


empty = [] # empty list has no elements
empty


# In[347]:


len(empty) # number of elements in a list


# In[348]:


f = [11, 12, 13, 14] # create a list of elements 11, 12, 13, 14
f


# In[349]:


f += [15, 16] # add 15 and 16 right after 14 to f
f


# In[350]:


# to add a single element 17 to the end of the list f
f.append(17) #, more likely append is the same as the incrementation, but takes exactly 1 element.
f


# In[33]:


# f.append(18, 19, 20) # is not correct


# In[351]:


f.extend([18, 19, 20])
f


# In[352]:


# insert element at a particular location
f.insert(0,8) # insert 8 to the first element (which is indexed by 0)
f


# In[353]:


f.insert(1,9)
f


# In[194]:


f.index(100) # returns the first index of a value 9 in a list f if the value already exists in a list


# In[354]:


9 in f #decide simply if an element appears in a list


# In[355]:


#if an element appears in a list we can return its index


# In[356]:


b = -1
if 100 in f:
    b = f.index(100)
b


# In[357]:


b = -1
if 9 in f:
    b = f.index(9)
b


# In[358]:


# if an element exists in a list we can insert something directly after that.
f.insert(f.index(9)+1, 10)
f


# In[359]:


f.remove(8) # remove element 8 from list f
f


# In[360]:


f.remove(8) # remove element 8 from list f (only if the element exists in the list)
f


# In[361]:


p = f.pop() # remove and return the last element from the list
f


# In[362]:


p


# In[363]:


f.sort() # sort elements (by default in ascending order)
f


# In[364]:


f.sort(reverse=True) # sort elements in descending order
f


# In[365]:


f.reverse() # reverse the list
f


# In[366]:


max(f)


# In[367]:


min(f)


# In[368]:


f.count(10) # how many times an item appears in a list


# In[369]:


f.count(5)


# In[370]:


f.clear() # remove all the elements from a list
f == []


# In[ ]:





# In[371]:


L = list(range(10))
L


# In[372]:


L[0] # get the first element from the list


# In[373]:


L[1] # get the second element from the list


# In[374]:


len(L) # number of elements in the list, last element is indexed by len(L)-1


# In[375]:


L[len(L)-1] # the last element in the list


# In[376]:


L[len(L)-2] # second element from the back


# In[377]:


L[-1] # different way of indexing elements last element is indexed by -1


# In[378]:


L[-2] == L[len(L)-2]


# In[379]:


list(range(10)) # list of numbers from 0 to 10 (including 0, but excluding 10, range(10)=[0,10))


# In[380]:


g = []
k = 0
while k < 10:
    if (k % 2 == 0):
        g.append(k)
    k+=1
del k
g


# In[381]:


g = []
for k in range(10):
    if (k % 2 == 0):
        g.append(k)
g


# In[431]:


[k for k in range(10) if k % 2 == 0] # create a list of even numbers using list comprehension


# In[ ]:





# In[383]:


[L[0], L[1], L[2]] # create a new list of the first three element from the list


# In[384]:


[L[k] for k in range(3)]


# In[385]:


L[0:3] # first 3 elements in the list L[0:3] = [L[0], L[1], L[2]]


# In[386]:


L[:3] # if the first argument is not specified, it means it is zero (L[:3]==L[0:3])


# In[387]:


L[3:] # if the second argument is not specified it means it is the last element


# In[388]:


L[:] # from the first to the last (both arguments neither specified) which means it is the whole list


# In[432]:


list(range(0,10,2)) # exactly the same, but the most efficient way (create a range from 0 to 10 but exclude every second item)


# In[389]:


L[1:4] # 3 elements after the first


# In[390]:


[L[4], L[5], L[6]]


# In[391]:


[L[k] for k in range(4,7)]


# In[392]:


L[4:7]


# In[393]:


L[4:7:1] # specify a skipping (1 means every element included between 4th and 7th (7th still excluded))


# In[394]:


L[4:7:2] # hold every second element


# In[395]:


L[-3:-1] # -1 is the last element (which is excluded) 


# In[396]:


L[-3:] # we can include the last element as well


# In[397]:


L[-3:-1:1] # number of steps can be specified


# In[398]:


L[:-4:-1] # if the number of steps is negative it means the order of the elements will be reversed


# In[399]:


L[::-1] # all the elements in reversed order


# In[400]:


L.reverse()
L


# In[401]:


reversed(L)


# In[299]:


list(reversed(L))


# In[402]:


L[1:3] = [11, 12] # slice assignment
L


# In[403]:


L[1:3]=[] # remove elements using slicing assignment
L


# In[404]:


LL = L # looks like this assignment create a copy of list L, but it is just a reference
LL


# In[405]:


LL[0]=100 # we change the first element of LL
LL


# In[406]:


L # as LL is a reference to L, L[0] changed to 100 as well


# In[407]:


LLL=list(LL) # now we copied the LL list, LLL is not a reference to LL
LLL


# In[408]:


LLL[0]=1
LLL


# In[409]:


LL # LL list remains the same


# In[410]:


# this approach fails when the list has list elements


# In[411]:


X = [[10, 2], [20, 3], [30, 4]]
X


# In[412]:


Y = list(X)
Y


# In[413]:


Y[0][0] = 100
Y


# In[414]:


X


# In[415]:


import copy


# In[416]:


Y = copy.deepcopy(X)


# In[417]:


X[0][0] = 10
X


# In[418]:


Y


# In[419]:


import itertools


# In[420]:


flatY=list(itertools.chain(*Y))


# In[421]:


flatY


# In[422]:


X = [1, 1, 2, 3, 3, 4, 5, 3, 2, 3]
X


# In[423]:


[k for k in X if X.count(k)>1] # find all the repeated elements


# In[425]:


list(set([k for k in X if X.count(k)>1])) # these are the duplicated elements in X


# In[426]:


from collections import deque


# In[427]:


Z=deque(X)


# In[428]:


Z.rotate(1)


# In[430]:


list(Z)


# In[ ]:





# In[ ]:


import numpy as np


# In[ ]:


list(np.arange(0,10, 2))


# In[ ]:


np.linspace(0, 8, 5, dtype="int")  # by default, np.linspace returns an array filled with doubles


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#  STRING


# In[433]:


sentence = "I got this feeling on the summer day when you were gone"
sentence


# In[440]:


type(sentence)


# In[441]:


sentence[0] # we can access the characters in the string the same way as in lists


# In[442]:


sentence[-1]


# In[ ]:





# In[435]:


sentence_list = sentence.split(" ")
sentence_list


# In[436]:


type(sentence_list)


# In[437]:


s = " ".join(sentence_list)
s


# In[154]:


word = "hello"


# In[155]:


word_list = list(word) # create a list from a string


# In[438]:


integer = 12345
integer


# In[159]:


integer_list = list(integer) # this not works


# In[439]:


integer_list = list(str(integer)) # is there any way to specify datatype ???
integer_list


# In[174]:


np.array(integer, dtype="int")


# In[176]:


[k for k in str(integer)]


# In[ ]:





# In[ ]:





# In[ ]:


# DICTIONARY


# In[177]:


d={'A': 1, 'B' : 2, 'C' : 3, 'D' : 4}


# In[178]:


d


# In[179]:


d.keys()


# In[180]:


type(d.keys())


# In[181]:


d.values()


# In[182]:


type(d.values())


# In[ ]:





# In[ ]:





# In[ ]:




