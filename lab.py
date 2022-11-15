
first = '######' 

second = '!!!!!!!!!'

text = '###### Рельеф форма  ###### очертания ###### поверхности ###### совокупность ###### ###### неровностей ###### твёрдой земной поверхности.'
print(text,'\n')

myList = text.split()

myArray = []

for i in range(0,len(myList)):

  if myList[i] =='######':
    if i % 2 == 0:
      myList[i]  = '?'
    else:
      myList[i]  = '!!!!!!!!!'

  if myList[i] !='######':
    myArray = myList

new_sting = " ".join(myArray)

print(new_sting)

    



  







