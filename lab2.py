import random
score_2 = 0
score = 0
i = 0

while i < 3:
  x = input("First player ready. if you ready enter 'yes': ")

  if x == 'yes':
    bones_1 = random.randint(1,6)
    bones_2 = random.randint(1,6)
    score += bones_1 + bones_2
    print(bones_1,",",bones_2,'\n','Общее:',score)
  else:
    print("if you ready enter 'yes'",'Общее:',score)

  x = input("Second player ready. if you ready enter 'yes': ")

  if x == 'yes':
    bones_3 = random.randint(1,6)
    bones_4 = random.randint(1,6)
    score_2 += bones_3 + bones_4
    print(bones_3,",",bones_4,'\n','Общее:',score_2)
  else:
    print("if you ready enter 'yes'",'Общее:',score_2)
  i+=1

if (score_2 > score):
  print('The second player WON!','Общий счет:',score_2)
else:
  print('The first player WON!', score)



 
