#!/usr/bin/env python
# coding: utf-8




def nonvuoto(mat,n,m):
    if mat[n,m] != 0:
            return true
    return false





def show(mat):
    for r in mat:
        for c in r:
            print(c, end=' ')
        print()





def inserisciOr(parola,mat,n,m):
    if m + len(parola) <= len(mat[0])-1:
        for poslet,lettera in enumerate(parola): # checking if it can be filled
            index=m+poslet
            if not(mat[n][index]==0 or mat[n][index]== lettera) :
                return False
        for poslet,lettera in enumerate(parola): #actual filling
            index=m+poslet
            mat[n][index]= lettera
        return True
            





def inserisciVr(parola,mat,n,m):
    if n + len(parola) <= len(mat)-1:
        for poslet,lettera in enumerate(parola):
            index=n+poslet
            if not (mat[index][m]==0 or mat[index][m]== lettera) :
                return False
        for poslet,lettera in enumerate(parola):
            index=n+poslet
            mat[index][m]= lettera
        return True
                
            





def inserisciDg(parola,mat,n,m):
    if n + len(parola) <= len(mat)-1 and m + len(parola) <= len(mat[0])-1:
        for poslet,lettera in enumerate(parola):
            indexo=m+poslet
            indexv=n+poslet
            if not (mat[indexv][indexo]==0 or mat[indexv][indexo]== lettera ):
                return False
        for poslet,lettera in enumerate(parola):
            indexo=m+poslet
            indexv=n+poslet
            mat[indexv][indexo]= lettera
        return True
                
            





import random

def piazzaparola(p,mat): # randomly picks whether insert a word horizontally, vertically or diagonally
    # it  tries also to cover all the grid in an increasing order
    caso=random.randint(0,2)
    inserito = False
    m=random.randint(0,len(mat[0])-1)
    n=random.randint(0,len(mat)-1)
    mi=0
    ni=0

    while not inserito and  mi<=len(mat[0])-1 and ni<=len(mat)-1:
                n=random.randint(ni,len(mat[0])-1)
                m=random.randint(mi,len(mat)-1)
                if caso== 0:
                    inserito =inserisciOr(p,mat,m,n)
                elif caso == 1:
                    inserito =inserisciVr(p,mat,m,n)
                else:
                    inserito =inserisciDg(p,mat,m,n)
                mi+=1
                ni+=1
    if not inserito:
            return False
    return True





def fillvoids(mat): # substitute the 0 with random characters
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                mat[i][j]=chr(random.randrange(97, 97 + 26))

        




# words to be added in the grid
listaparole =["karin","locura","biascica","michieletto","autostop","zaytsev","osmani","hockey"]






mat=[[0  for i in range(14) ]for j in range(14)]





for parola in listaparole:
    
    #this one to enable also backward words
    if random.randint(1,2) ==1:
        parola=parola[::-1]
    
    messo=piazzaparola(parola,mat)
    while not messo:
        messo=piazzaparola(parola,mat)





fillvoids(mat)

show(mat)

