"""9) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს"""


password = input("enter your password: ")
my_password = "tornike123"
while password != my_password:
    password =  input("enter your password: ")