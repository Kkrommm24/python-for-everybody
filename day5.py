# employee_file = open("employee.txt", "r") # must run in the same folder as file
# print(employee_file.readlines()[2])
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# employee_file = open("employee.txt", "a") # "a" ghi vào đáy file, "w" ghi đè toàn bộ file
# employee_file.write("Toby - HR")
# employee_file.write("\nLaura - Customers Service")
# employee_file.close()

# employee_file = open("employee1.txt", "w") # "w" tự tạo file mới nếu chưa có file
# # employee_file.write("Toby - HR")
# employee_file.write("\nLaura - Customers Service")
# employee_file.close()

# employee_file = open("index.html", "w") 
# employee_file.write("<p> This is HTML </p>")
# employee_file.close()

# import useful_tool

# print(useful_tool.roll_dice(10))

from Student import Student

student1 = Student("Jim", "IT", 3.6)
student2 = Student("Odf", "Art", 3.3)
print(student1.on_honor_roll())
print(student2.on_honor_roll())

#Inheritance
#file Chef.py và file ChineseChef.py

#ChineseChef.py:

# from Chef import Chef

# class ChineseChef(Chef): 
#     ...
# => ChineseChef kế thừa toàn bộ hàm của Class Chef
