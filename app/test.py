
array=[[1,22,34,543],[2,34,45,43],[1,3,45,54]] #EXAMPLE
S=int(input())
R=int(input())
for i in array:
      indexsum=0
      elementsum=0
      for j in i:
            indexsum+=j
            elementsum+=i[j]
      ostatok=elementsum% R
      if (indexsum < S) and (ostatok %2==0):
            print(array[i])