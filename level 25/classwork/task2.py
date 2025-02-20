"""2) შექმენით პროგრამა, რომელშიც მომხმარებელს შემოატანინებთ ქულას, შემდეგ კი if განხადების საშვალებით გამოუტანთ 2 შესაძლო შედეგს: "You have passed" ან "You failed"""
score = input("enter you test score: ")

if int(score) > 20:
    print("you have pass")

if int(score) < 20:
    print("you falled")