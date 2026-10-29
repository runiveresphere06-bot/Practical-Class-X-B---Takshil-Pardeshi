# Name: Takshil Pardeshi
# Class: 10 | Subject: Artificial Intelligence (Practical Record File)
#
# Program 13: Calculate Net Salary
# HRA = 30% of Basic, DA = 20% of Basic, PF = 12% of Basic
# Net Salary = Basic + HRA + DA - PF

basic = float(input("Enter the Basic Salary: "))

hra = basic * 30 / 100
da = basic * 20 / 100
pf = basic * 12 / 100

net_salary = basic + hra + da - pf

print("HRA        :", hra)
print("DA         :", da)
print("PF         :", pf)
print("Net Salary :", net_salary)
