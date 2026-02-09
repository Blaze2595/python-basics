# bounce.py
#
# Exercise 1.5
height = 100
rebounce = 3 / 5
count = 1

while count < 11:
    height = round(height * rebounce,4)
    print('Bounce No : ', count, end=' ')
    print(' Height : ',height)
    count = count + 1

