# 1) შექმენით პროგრამა რომელიც temp ცვლადში ინახავს ტემპერატურას (integer, რიცხვით მნიშვნელობას), ხოლო cloudy ცვლადში boolean (True/False) მნიშვენლობას, პროგრამამ უნდა დაადგინოს walk ცვლადის მნიშვენლობა შემდეგი პირობებიდან გამომდინარე, თუ ტემპერატურა მეტია 20 გრადუს ცელსიუზე და ამინი არ არის ღრუბლიანი მხოლოდ მაშინ უნდა გახდეს walk ცვლადის მნიშვნელობა ჭეშმარიტი

temp = 25  
cloudy = False  
walk = temp > 20 and not cloudy  
print("Can go for a walk:", walk)
