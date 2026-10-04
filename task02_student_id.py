name = input("Enter your name: ")
id = input("Enter your student ID: ")
department = input("Enter your department: ")
year = input("Enter your university year: ")
university = input("Enter your university: ")
phone = input("Enter your phone number: ")
student_id = f'''
+-----------------------+
| AKIBA STUDENT ID CARD |
+-----------------------+
|Name: {name}
|ID: {id}
|Department: {department}
|Year: {year}
|University: {university}
|Phone: {phone}'
+-----------------------+
'''
print(student_id)
