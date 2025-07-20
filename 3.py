# a = eval(input('請輸入第一個數: '))
# b = eval(input('請輸入第二個數: '))
# c = abs(a-b)

# if a>b: 
#     print(f'a 比較大, 差了 {c}')

# elif b>a:
#     print(f'b 比較大, 差了 {c}')

# else: print('一樣大')

numbers = input("請輸入a,b兩個數字:")
numbers = list(map(eval,numbers.split(",")))
print(numbers)