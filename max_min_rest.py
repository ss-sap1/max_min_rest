'''на вход три целых числа и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.'''
'''l = [a,b,c]
l.sort()
print('Max:', l[2])
print('Min:', l[0])
print('Other:', l[1])'''

a = int(input())
b = int(input())
c = int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))
