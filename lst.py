"""
#หาเลขกับตัวอักษร
w = str(input("Enter string: "))
letters = 0
number = 0
for i in w:
    if i.isalpha():
        letters +=1
    elif i.isdigit():
        number +=1
print("Number of alphabets:",letters)
print("Number of digits:",number)
"""
from lib2to3.fixes.fix_tuple_params import find_params

""""
# หาตัวซ้ำแล้วไม่ซ้ำ แล้วปริ้นออกมา
scores = []
unique = []
duplicate = []
while True:
    score =input("Enter score: ")
    if score == "":
        break
    score = int(score)
    scores.append(score)
for i in scores:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
        unique.remove(i)
print("Unique items list:",unique)
print("Duplicate items list:",duplicate)
"""


"""
# หาavg และ หาต่ำสุด
scores = []
while True:
    score =input("Enter score: ")
    if score == "":
        break
    score = int(score)
    scores.append(score)
sum = 0
for i in scores:
    sum+=i
avg = sum/len(scores)
min_ = min(scores)
print("avg score is:",avg)
print("scores below avg:",min_)
"""


"""
numbers = [12, 34 ,45, 65, 11, 18, 21, 1]
numbers.sort() # เรียงจากน้อยไปมาก
size = len(numbers)
print(numbers)
print("Smallest element is:",numbers[0]) #หาตัวแรก
print("Largest element is:",numbers[-1]) #หาตัวท้าย
print("Max:",max(numbers))
print("Min:",min(numbers))
"""