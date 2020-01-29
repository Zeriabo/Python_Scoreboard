import array as arr
s = []
ss = []
f = 0
p1=input("Player 1 Name :")

p2=input("Player 2 Name :")
print("enter value And 0 to Finish the game")
v=int(input(p1))

while v!=0:

  s.append(v)
  v=int(input(p2))
  if v == 0:
    break

  ss.append(v)
  v=int(input(p1))
  if v == 0:
    break

s.sort()
ss.sort()
sm=sum(s)
sx=sum(ss)
print("The sorted Scores of Player 1  ",s)
print("The sorted Scores of Player 2  ",ss)
print("The sum of the scores of",p1,"is :",sm)
print("The sum of the scores of ",p2,"is :",sx)
if(sm>sx):
  print("Player 1 wins",p1)
elif(sx>sm):
  print("Player 2 wins",p2)
else:
   print(p1,"Result equal",p2)
print("Game ends")