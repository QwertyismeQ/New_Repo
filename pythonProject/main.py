print(f'Приветствую! Это моя программа: ')

while True:

        shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],

                ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200],

                ['седло', 2700]]

        detail = input("Название детали: ")
        count = 0
        cost = 0

        for i_detail in shop:

                for j in range(len(i_detail) - 1):

                        if i_detail[0] == detail:
                                count += 1
                                cost += i_detail[1]

        print(f'Количество деталей: {count}\nОбщая стоимость: {cost}')
        print()
