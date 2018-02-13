k=True
r=0
b=[]
a=[[ 1, 2, 3, 4],
   [ 5, 6, 7, 8],
   [ 9,10,11,12],
   [13,14,15,16]]
for i in range (4):
          print(a[i])
while k:
          while k:
                    while k:
                      if r>=12:         
                       g=input("P1 give up?(y\\n)")
                       if g=="y":
                                print("P2 win")
                                k=False
                                break
                      
                      
                      while 1:
                        x=(input("P1 1st nom:"))
                        
                        f=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
                        ze = True
                        for i in range(16):
                            if (f[i]==x) :
                                ze = False
                                break
                        if ze == False :
                            break
                      x=int(x)
                      

                      while 1:
                        
                        y=(input("P1 2nd nom:"))
                        f=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
                        ze = True
                        for i in range(16):
                            if (f[i]==y):
                                ze = False
                                break
                        if ze == False :
                            break
                      
                      y=int(y)
                          
                      m = True
                      for i in range (4) :
                         for j in range (4) :
                             if a[i][j] == x :
                                 m = False
                                 break
                      n = True        
                      for i in range (4) :
                          for j in range (4) :
                              if a[i][j] == y :
                                  n = False
                                  break
                      while n or m :
                          x=int(input("P1 1st nom:"))
                          y=int(input("P1 2nd nom:"))
                          m = True
                          for i in range (4) :
                              for j in range (4) :
                                  if a[i][j] == x :
                                      m = False
                                      break
                          n = True        
                          for i in range (4) :
                              for j in range (4) :
                                 if a[i][j] == y :
                                     n = False
                                     break
                      
                      if (x==4) and (y==5) or (x==5) and (y==4) or (x==8) and (y==9) or (x==9) and (y==8) or (x==13) and (y==12) or (x==12) and (y==13) or (x>16)or(y>16):
                            print("try again")
                      else:
                              break
          
          
                    if (x==y+4) or (x==y-4) or (x==y-1) or (x==y+1):  
                      for i in range (4):
                        if (a[i][0]==x) or (a[i][0]==y):
                                a[i][0]=0
                                r=r+1
                          
                        if (a[i][1]==x) or (a[i][1]==y):
                                a[i][1]=0
                                r=r+1
                          
                        if (a[i][2]==x) or (a[i][2]==y):
                                a[i][2]=0
                                r=r+1
                           
                        if (a[i][3]==x) or (a[i][3]==y):
                                  a[i][3]=0
                                  r=r+1
                      break
                    else:
                                print("try again")
          b=b+[x]
          b=b+[y]
          if k == False:
                    break
          for i in range (4):
                    print(a[i])
          print(b)

          while k:
                    while k:
                      if r>=12:
                       g=(input("P2 give up?(y\\n)"))
                       if g=="y":
                                print("P1 win")
                                k=False
                                break
                      while 1:
                        z=(input("P2 1st nom:"))
                        
                        f=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
                        zep = True
                        for i in range(16):
                            if (f[i]==z) :
                                zep = False
                                break
                        if zep == False :
                            break
                      
                      z=int(z)
                      
                      while 1:
                        
                        c=(input("P2 2nd nom:"))
                        f=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
                        zep = True
                        for i in range(16):
                            if  (f[i]==c):
                                zep = False
                                break
                        if zep == False :
                            break
                      
                      c=int(c)
                      
                      m = True
                      for i in range (4) :
                         for j in range (4) :
                             if a[i][j] == z :
                                 m = False
                                 break
                      n = True        
                      for i in range (4) :
                          for j in range (4) :
                              if a[i][j] == c :
                                  n = False
                                  break
                      while n or m :
                          z=int(input("P2 1st nom:"))
                          c=int(input("P2 2nd nom:"))
                          m = True
                          for i in range (4) :
                              for j in range (4) :
                                  if a[i][j] == z :
                                      m = False
                                      break
                          n = True        
                          for i in range (4) :
                              for j in range (4) :
                                 if a[i][j] == c :
                                     n = False
                                     break
                      if a[i][0]==0 or a[i][1]==0 or a[i][2]==0 or a[i][3]==0:
                                break
                      if (z==4) and (c==5) or (z==5) and (c==4) or (z==8) and (c==9) or (z==9) and (c==8) or (z==13) and (c==12) or (z==12) and (c==13)or (c>16) or (z>16):
                            print("try again")
                      else:
                              break
          
          
                    if (z==c+4) or (z==c-4) or (z==c-1) or (z==c+1):  
                      for i in range (4):
                        if (a[i][0]==z) or (a[i][0]==c):
                                a[i][0]=0
                                r=r+1
                          
                        if (a[i][1]==z) or (a[i][1]==c):
                                a[i][1]=0
                                r=r+1
                          
                        if (a[i][2]==z) or (a[i][2]==c):
                                a[i][2]=0
                                r=r+1
                           
                        if (a[i][3]==z) or (a[i][3]==c):
                                  a[i][3]=0
                                  r=r+1
                      break
                    else:
                                print("try again")
          b=b+[z]
          b=b+[c]
          if k == False:
                    break
          for i in range (4):
                    print(a[i])
          print(b)

