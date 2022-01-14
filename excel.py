from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

letter = ["A","B","C","D","E","F","G","H","I","J","K"]
x = 0
y = 0
for i in range(100):
    sheet[letter[x]+str(y+1)] = str(i)
    y = y+1
    # if 
    #     sheet[letter[i]+"1"] = str(i)
    if i == 9:
        x = x + 1
        y = 0
    if i == 19:
        x = x + 1
        y = 0
    if i == 29:
        x = x + 1
        y = 0
    if i == 39:
        x = x + 1
        y = 0
    if i == 49:
        x = x + 1
        y = 0
    if i == 59:
        x = x + 1
        y = 0
    if i == 69:
        x = x + 1
        y = 0
    if i == 79:
        x = x + 1
        y = 0
    if i == 89:
        x = x + 1
        y = 0


workbook.save(filename="hello.xlsx")