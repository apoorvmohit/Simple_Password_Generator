import random
pass_lst = """1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=[]{}\|;:'".><,"""
password = ""
n = int(input("Enter the desired length of password: "))
for i in range(n):
    password += random.choice(pass_lst)
print(password)
