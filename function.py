
# date:26/11/2022
  ---------------
'''
#wap to fetch all odd numbers into one list and all even numbers into another list.
'''
                          #note:  dont take 0 into any list
lst=[3,7,2,0,4,7]
def fetchevenandodd (lst):
    lst1=[]
    lst2=[]
    for i in lst:
        if i==0:
            pass
        elif i%2==0:
                lst1.append(i)
        else:
                    lst2.append(i)
                    print(lst1)
                    print(lst2)
fetchevenandodd (lst)                          #output:
                                                      [2, 4]
                                                       [3, 7, 7]
        
'''
#wap to fetch all words which start with vowel.
'''
st="python is simple and easy language"
st= st.split()
def fetchwordsbyvowel(st):
    for i in st:
     if i[0]in 'aeiou':
       print(i)
fetchwordsbyvowel(st)                        #output:
                                                    is
                                                    and
                                                    easy
                                                    
'''

#wap to fetch all words which start with vowelin list.
'''
st="python is simple and easy language"
st= st.split()
def fetchwordsbyvowel(st):
    lst1=[]
    for i in st:
     if i[0]in 'aeiou':
         lst1.append(i)
         print(lst1)
fetchwordsbyvowel(st)                      output:
                                                  ['is', 'and', 'easy']
'''
#wap to fetch all words which contain 'a' character two or more than two times.
'''
st="python narayana teaches python language"
st=st.split()
def fetchallword(st):
    for i in st:
        if i.count('a')>=2:
            print(i)
fetchallword(st)                          #output:
                                                  narayana
                                                  language

'''
#wap to fetch all words which contain 'a' character two or more than two times in new list.
'''
st="python narayana teaches python language"
st=st.split()
def fetchallword(st):
    lst1=[]
    for i in st:
        if i.count('a')>=2:
            lst1.append(i)
            print(lst1)
fetchallword(st)                          #output:
                                                  ['narayana', 'language']
'''
#wap to fetch the length of each word.
'''
st="python narayana teaches python language"
st=st.split()
def fetchalllength(st):
    for i in st:
        print(i,'-',len(i))
fetchalllength(st)                       #output:
                                                 python - 6
                                                 narayana - 8
                                                 teaches - 7
                                                 python - 6
                                                 language - 8

''' 
                                                
#wap to fetch the length of each word in list.
'''
st="python narayana teaches python language"
st=st.split()
def fetchalllength(st):
    lst1=[]
    for i in st:
        lst1.append(i)
        print(lst1,'-',len(i))
fetchalllength(st)                       #output:
                                                 ['python'] - 6
                                                 ['python', 'narayana'] - 8
                                                 ['python', 'narayana', 'teaches'] - 7
                                                 ['python', 'narayana', 'teaches', 'python'] - 6
                                                 ['python', 'narayana', 'teaches', 'python', 'language'] - 8
'''