import random
List = []

for i in range(15):
    List.append(random.randint(0, 100))

print("Начальный сисок:\n",List)

EvenList =[]

for i in range(15):
    if List[i] % 2 == 0:
        EvenList.append(List[i])

print("Итоговый срисок:\n",EvenList)