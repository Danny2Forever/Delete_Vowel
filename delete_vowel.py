txt = input("Type something")
aei = ['a','e','i','o','u','A','E','I','O','U']
txt01 = ""
for i in txt:
  if i in aei:
    continue
  else:
    txt01 += i
print(txt01)