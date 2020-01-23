#morse code translator

l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',]

def menu():
    i=int(input('1. translate morsecode to english // 2. translate english to morsecode: '))
    return i



def morstoeng(mors):
    c=''
    bits=[]
    for i in mors:
        if i=='/':
            bits.append(c)
            c=''
        else:
            c=c+i
    bits.append(c)
    
    s=''
    for item in bits:
        ind1=l2.index(item)
        s=s+(l1[ind1])
    return s

def engtomors(eng):
    c=''
    bits=[]
    for i in eng:
        if i==' ':
            bits.append(' ')
            
        else:
            bits.append(i)
            
    
    
    s=''
    for item in bits:
        if item==' ':
            s=s+'/'
        else:
            ind2=l1.index(item)
            s=s+(l2[ind2])
    return s

inp=menu()
if inp==1:
    stri=input('enter morsecode: ')
    print(morstoeng(stri))
if inp==2:
    stri=input('enter message: ')
    print(engtomors(stri))
