from random import sample
x = input('Birinchi sonni kiritig')
y = input('Oxirgi sonni kiriting')
z = input('Sizga nechta tasodifiy raqam kerak')
x = int(x)
y = int(y)
z = int(z)
son = sample(range(x, y),z) 
print(f'Tahminiy son {son}')