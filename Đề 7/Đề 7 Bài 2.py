n = int(input("Nhập số số nguyên: "))
nums = [int(input(f"Nhập số nguyên thứ {_+1}: ")) for _ in range(n)]
even_sum = sum(num for num in nums if num%2==0)
max_num, min_num = max(nums), min(nums)
maxnum_pos = nums.index(max_num)+1
minnum_pos = nums.index(min_num)+1
DAYTANG = False
for i in range(1,n):
    if nums[i] < nums[i-1]:
        DAYTANG = False
        break
    DAYTANG = True
print("Tổng các số nguyên chẵn là", even_sum)
print("Số lớn nhất là", max_num,",ở vị trí thứ",maxnum_pos)
print("Số nhỏ nhất là", min_num,",ở vị trí thứ",minnum_pos)
print("DAY TANG" if DAYTANG else "DAY KHONG TANG")