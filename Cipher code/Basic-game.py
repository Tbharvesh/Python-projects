import random
def draw():
  l=[]
  for i in range(5):
    l.append([])
    for j in range(10):
      l[i].append(' ')
  for p in range(10):
    l[0][p]='.'
    l[4][p]='.'
  for q in range(5):
    l[q][0]='.'
    l[q][9]='.'
  return l
def setup():
  xpof=random.randint(1,3)
  ypof=random.randint(1,7)
  return xpof,ypof

t=draw()
#print(t)
x,y=setup()
#print(x,y)
t[x][y]=8
t[1][1]='o'

for i in t:
  for j in i:
    print(j,end=' ')
  print(end='\n')

#def input():
 # print('Enter next move:(w,a,s,d)')
  #m=input()
  #return m
out=False 
def logic(o):
  for i in t:
   if 'o' in i:
    tx,ty=t.index(i),i.index('o')
   
  if o=='w':
    temp=t[tx][ty]
    t[tx][ty]=' '
    t[tx-1][ty]='o'
  if o=='a':
    temp=t[tx][ty]
    t[tx][ty]=' '
    t[tx][ty-1]='o'
  if o=='s':
    temp=t[tx][ty]
    t[tx][ty]=' '
    t[tx+1][ty]='o'    
  if o=='d':
    temp=t[tx][ty]
    t[tx][ty]=' '
    t[tx][ty+1]='o'
  
tx,ty=0,0
score=0
c=1
while not out:
  print('score:',score)
  print('Enter next move:(w,a,s,d)')
  p=input()
  logic(p)
  for i in t:
   if 'o' in i:
    tx,ty=t.index(i),i.index('o')
  if tx==0 or tx==4 or ty==0 or ty==9:
     out=True
  if not out:
   for i in t:
    for j in i:
     print(j,end=' ')
    print(end='\n')
  else:
    print('game over')
    print('score:',score)
  if tx==x and ty==y:
    score=score+5
    c=c+1
    #for i in range(c):
     #t[tx][ty+i]='o'
    x,y=setup()
    t[x][y]=8
    for i in t:
     for j in i:
      print(j,end=' ')
     print(end='\n')
  
    