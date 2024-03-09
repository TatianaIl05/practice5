import turtle as t
xc = float(input('xc = '))
yc = float(input('yc = '))
r = float(input('r = '))
x = float(input('x = '))
y = float(input('y = '))
t.up()
t.setposition(xc, yc - r)
t.down()
t.circle(r)
t.up()
t.setposition(x, y)
t.down()
t.dot(5, 'red')

if t.distance(xc, yc) == r:
    text_for_pos = 'Точка на окружности'
    print('Точка на окружности')
elif t.distance(xc, yc) > r:
    text_for_pos = 'Точка вне окружности'
    print('Точка вне окружности')
else:
    text_for_pos = 'Точка внутри окружности'
    print('Точка внутри окружности')

t.up()
t.setposition(xc, yc - r - 20)
t.down()
t.color('red')
t.write(text_for_pos, False, align='center')
t.mainloop()
