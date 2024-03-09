pounds, inches = map(float, input('Введите вес (в фунтах) и рост (в дюймах): ').split())
kgs = pounds*0.45359237
cms = inches*2.54
bmi = round(kgs/(cms/100)**2, 2)

if bmi >= 40:
    print('ожирение третьей степени')
elif bmi >= 35:
    print('ожирение второй степени')
elif bmi >= 30:
    print('ожирение первой степени')
elif bmi >= 25:
    print('избыточная масса тела')
elif bmi >= 18.5:
    print('норма')
elif bmi >= 16:
    print('недостаточная масса тела')
else:
    print('выраженный дефицит массы тела')
 