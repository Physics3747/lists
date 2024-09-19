'''
#สร้าง List ที่เก็บตัวเลขตั้งแต่ 1 ถึง 10
s = list(range(1, 11))
for i in s:
    print(i)
'''

'''
fruits = ["apple", "banana", "organe", "coconut"]
#print(fruirs[2]) #ตำแหน่ง2
#print(fruirs[1:3]) #ตำแหน่ง1-3
#print(len(fruits)) #ความยาว
#print(fruirs[::-1]) #ย้อนกลับ
#print("banana" in fruits) #ตรวจสอบว่าอยู่ใน[]มั้ย
#fruits.append("pineapple") #เพิ่มต่อท้าย
#fruits.remove("apple") #ลบ
#fruits.insert(0, "mango") #เพิ่มเข้าไปที่ตำแหน่ง0
#fruits.sort() #แสดงข้อมูลว่ามีอะไรบ้าง
#fruits.reverse() #ย้อนกลับ
#print(fruits.index("apple")) #ถามตำแหน่ง
#print(fruits)
#fruit_char = [fruit[0] for fruit in fruits] # ถามว่าตำแหน่ง0คือตัวอะไร
#print(fruit_char)
'''

#list comprehensions
'''
double = []
for x in range(1, 11):
    double.append(x * 2)
print(double)
'''
'''
#ฉบับย่อ
double = [x * 2 for x in range(1, 11)]
print(double)
'''
'''
#ทำตัวใหญ่
fruits = [fruit.upper() for  fruit in ["apple", "banana", "organe", "coconut"]]
print(fruits)
'''
'''
#หาเลขคู่คี่
numbers = [1, 2, 3 ,4, 5, 6 ,7, 8]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 == 1]
print(even)
print(odd)
'''

