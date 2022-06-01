def addNumber(lists1:list,lists2:list):
    num1 = int(''.join(str(i) for i in lists1)[::-1])
    num2 = int(''.join(str(i) for i in lists2)[::-1])
    sumList=[int(i) for i in str(num1+num2)]
    sumList.reverse()
    return sumList
list1=[9,9,9,9,9,9,9]
list2=[9,9,9,9]

print(addNumber(list1,list2))
