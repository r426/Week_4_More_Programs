celsius = int(input("What's the temperature in degrees Celsius? – "))

fahrenheit = int((celsius * 1.8) + 32)

degree_sign = u'\N{DEGREE SIGN}'

print('''Temperature:
{}{}C
{}{}F'''.format(celsius, degree_sign, fahrenheit, degree_sign))