import re
S = input("Nhập xâu S: ")
count=0
for ch in S:
    if ch.isdigit():
        count+=1
nums = re.findall(r'\d+', S)
sum = sum(int(n) for n in nums)
print(f"S có {count} kí tự")
print(f"Tổng các số là", sum)