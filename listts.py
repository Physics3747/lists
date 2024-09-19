#l = [1, 2, 3, 4, 5, 6, 7]
#l[3] = 10 #เปลี่ยนตำแหน่ง3
#l.append(11) #เพิ่ม11เข้าไป
#l.remove(2) #ลบตำแหน่ง2
#for x in l:
#    print(x)

'''
lists = [1, 3, 5, 8, 1, 4, 11, 21, 20]
lists1 = [23, 26]
#lists.sort() #เรียงลำดัวเลข
#print(lists.index(21)) #ถามลำดับตัวเลข

if len(lists) != len(set(lists)): #หาว่่ามีเลขซ้ำกันมั้ย
    print("ซ้ำ")
else:
    print("ไม่ซ้ำ")

#lists_1 = lists[:3] #ปริ้นตัว0-3
#print(lists_1)
#print(lists+lists1) #รวมลิสต์เข้าด้วยกัน
'''

'''
l = [1, 2, 3, 4] 
double = [i ** 2 for i in l]
print(double) #หากำลัง2ในลิสต์
'''
'''
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for i in lists:
    total+=i
print(total) #หาsumในลิสต์
'''

#lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(max(lists)) #หาค่ามากสุด
#print(min(lists)) #หาค่าน้อยสุด
'''
# หาavg
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def sumlist():
    total = sum(lists)
    avg = total/len(lists)
    return avg
r = sumlist()
print(r)
print(sum(lists))
'''
"""
#เทียบความยาว
l1 = [1, 2, 3, 4]
l2 = [5, 6]
def lenlist():
    if len(l1) > len(l2):
        return "l1 > l2"
    else:
        return "l1 < l2"
s = lenlist()
print(s)
"""