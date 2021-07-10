import random
start = input('請決定最小值: ')
end = input('請決定最大值: ')
start = int(start)
end = int(end)
answer = random.randint(start, end)#產生隨機數
maximum = end #建立最大值變數
minimum = start #建立最小值變數
guess = input('請猜一個數字: ')#讓使用者輸入/建立變數guess
while True:
    if guess.isdigit() == True:
        guess = int(guess)
        break
    else:
        print('只能輸入整數啦白癡 = =')
        guess = input('請猜一個數字(1~100): ')
if guess == answer:
    print('恭喜答對!')
if guess < minimum or guess > maximum:
    print('只能輸入', minimum, '到', maximum, '的數字喔')
    guess = input('請猜一個數字(1~100): ')
    guess = int(guess)
while guess <= maximum or guess >= minimum:
    if guess < minimum or guess > maximum: #如果超過範圍的處理
        print('只能輸入', minimum , '到', maximum, '的數字喔' )
        print('範圍:', '(', minimum, '~', maximum, ')')
        guess = input('請猜一個數字: ')
        guess = int(guess)
    elif guess > answer: #數字比答案大
        maximum = guess - 1
        print('範圍:', '(', minimum, '~', maximum, ')')
        guess = input('請猜一個數字: ')
        guess = int(guess)
    elif guess < answer: #數字比答案小
        minimum = guess + 1
        print('範圍:', '(', minimum, '~', maximum, ')')
        guess = input('請猜一個數字: ')
        guess = int(guess)
    else:
        print('恭喜答對')
        break
