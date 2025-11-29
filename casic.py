import random

def casino():
    list_symbol = ['1', '7', '9', '0', '3', '5']
    curr_balance = 0

    print('_________________________')
    print('Добро пожаловать в лудку!')
    balance = input('Какую сумму будем депать? ')
    print('_____________________________')

    try:
        curr_balance = int(balance)
        if curr_balance &lt; 0:
            print('Введите положительное число!')
        else:
            print(f'Ваш депозит: {curr_balance} рублей')
            print('Для входа в игру введите "Play"')

            if input().lower() == 'play':
                while curr_balance &gt; 0:
                    while True:
                        bet = input(f'\nВаш баланс: {curr_balance}р. Введите ставку: ')
                        if bet.isdigit() and int(bet) &lt;= curr_balance:
                            bet_sum = int(bet)
                            break
                        else:
                            print('Неверная ставка!')
                    
                    result = [random.choice(list_symbol) for _ in range(4)]
                    print(f"Результат: {result}")
                    
                    curr_balance = check_win(result, bet_sum, curr_balance)
                    
                    if curr_balance &lt;= 0:
                        print('Деньги закончились(((')
                        break
                    
                    restart = input('Продолжить игру?')
                    if restart.lower() != 'да':
                        print(f'Финальный баланс: {curr_balance}р.')
                        break
    except ValueError:
        print('Ввод только чисел!')

def check_win(array: list, bet: int, balance: int) -> int:
    if array[0] == array[1] == array[2] == array[3]:
        win = bet * 5
        new_balance = balance + win
        print(f'Бинго!!! (+{win}р.)')
        print(f"Ваш баланс: {new_balance}р.")
        return new_balance
        
    elif array[0] == array[1] or array[0] == array[2] or array[1] == array[2] or array[0] == array[3] or array[2] == array[3] or array[3] == array[1]:
        win = bet * 2
        new_balance = balance + win
        print(f"Дупло!! (+{win}р.)")
        print(f"Ваш баланс: {new_balance}р.")
        return new_balance
    else:
        new_balance = balance - bet
        print("Мимо!")
        print(f"Ваш баланс: {new_balance}р. (-{bet}р.)")
        return new_balance

casino()
