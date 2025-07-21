# 1. 加入例外處理
# 2. 重複輸入, 直到a=>exit

while True:

    a = input('請輸入第一個數(exit 離開):\n')
    if a == 'exit':
        print('停止運作')
        break
    try:
        a = eval(a)
        b = eval(input('請輸入第二個數:\n'))
        
        if a>b: 
            print(f'a 比較大, 差了 {a-b}\n')

        elif b>a:
            print(f'b 比較大, 差了 {b-a}\n')

        else: print('一樣大')
    except Exception as e:
        print(f'發生錯誤: {e}')


# numbers = input("請輸入a,b兩個數字:")
# numbers = list(map(eval,numbers.split(",")))
# print(numbers)
