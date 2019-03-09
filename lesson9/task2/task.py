A = int(input()) #рекомендовано
B = int(input()) #не более
H = int(input()) #сон
if H < A :
  print('Недосып')
elif H > B :
  print('Пересып')
else:
  print('Это нормально')