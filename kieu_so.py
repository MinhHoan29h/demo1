#1. so nguyen
#gan cho bien a gia tri la 4. 4 la kieu so nguyen
a = 4
print(a)

#2. in kieu du lieu cua a 
print(type(a))

#chuoi
b = "minh hoan"
#in kieu du lieu cua b la string
print(type(b))

#so thuc
##gan cho bien c gia tri la 1.96. 1.96 la kieu so thuc
c = 1.96
print(type(c))

#so thuc chi luu dc sau dau phay 12 so neu muon hon phai dung decimal


#lay toan bo noi dung của thư viện decimal
from decimal import*

#lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal
# dùng để set số thập phân lấy
getcontext().prec = 30

# in ra ket qua tinh 10:3
print(Decimal(10)/Decimal(3))
# chỉ cần 1 số là Decimal
d = Decimal(10)/3
print(d)

#3. phan so

# phải import thư viện fractions để dùng phân số
from fractions import* 
# day la phan so 6/9
frac = Fraction(6,9)
print(frac)
print(type(frac))

frac1 = Fraction(5,9)
frac2 = Fraction(5,10)
frac3 = frac1 + frac2
print(frac3)




