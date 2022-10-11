import os
from random import randint


List_of_game = [['1','2','3'],  # Игровое поле))))))
                ['4','5','6'],
                ['7','8','9']]

 


def Getdraw(List):              # Функция определяет наличие свободного пространства выдает True если хоть 1 клетка свободна (не 'x' или 'o')
    draw = False              
    for L in List:
        for i in L:
            if i != 'x' and i != 'o':
                draw = True
    return draw
        
def Spot_in_List(List,x,y):     # Функция   возвращает метку поля по координатам х,у если там х вернет х, если у вернет у иначе вернет ' '
    if List[x][y]=='x' or List[x][y]=='o':
        return List[x][y]
    else: 
        return ' '

def visualizer(List):           # Функция отвечает за отрисовку интерфейса игрового поля
    os.system('cls' if os.name == 'nt' else 'clear')              # очистка экрана
    print('                          Игра КРЕСТИКИ НОЛИКИ')
    print('                             Игровое поле')
    print()  
    print( '                             ╔═══╦═══╦═══╗          ╔═══╦═══╦═══╗')             
    print(f'                             ║ {Spot_in_List(List,0,0)} ║ {Spot_in_List(List,0,1)} ║ {Spot_in_List(List,0,2)} ║          ║ 1 ║ 2 ║ 3 ║')          # 1     2     3
    print(f'                             ╠═══╬═══╬═══╣          ╠═══╬═══╬═══╣')
    print(f'                             ║ {Spot_in_List(List,1,0)} ║ {Spot_in_List(List,1,1)} ║ {Spot_in_List(List,1,2)} ║          ║ 4 ║ 5 ║ 6 ║')          # 4     5     6
    print(f'                             ╠═══╬═══╬═══╣          ╠═══╬═══╬═══╣')
    print(f'                             ║ {Spot_in_List(List,2,0)} ║ {Spot_in_List(List,2,1)} ║ {Spot_in_List(List,2,2)} ║          ║ 7 ║ 8 ║ 9 ║')          # 7     8     9   
    print( '                             ╚═══╩═══╩═══╝          ╚═══╩═══╩═══╝')
    print()

def Kletka_in_List(Number,Player):  # Функция производит определение координат заданной клетки и пятно заполнения и возвращает эти значения
    if Player: spot ='x'
    else: spot = 'o'
    if Number == 1: 
        x = 0
        y = 0
    elif Number == 2:
        x = 1
        y = 0
    elif Number == 3:
        x = 2
        y = 0
    elif Number == 4:
        x = 0
        y = 1
    elif Number == 5:
        x = 1
        y = 1
    elif Number == 6:
        x = 2
        y = 1
    elif Number == 7:
        x = 0
        y = 2
    elif Number == 8:
        x = 1
        y = 2
    elif Number == 9:
        x = 2
        y = 2
    else:
        return False
    return y, x, spot


def WinGAME(List, Player):              # Функция определяет наличие выигрышной линии в зависимости от метки игрока
    if Player: spot ='x'
    else: spot = 'o'
    if List[0][0] == spot and List[0][1] == spot and List[0][2] == spot: # 123
        return True
    elif List[1][0] == spot and List[1][1] == spot and List[1][2] == spot: # 456
        return True
    elif List[2][0] == spot and List[2][1] == spot and List[2][2] == spot: # 789
        return True
    elif List[0][0] == spot and List[1][0] == spot and List[2][0] == spot: # 147
        return True
    elif List[0][1] == spot and List[1][1] == spot and List[2][1] == spot: # 258
        return True
    elif List[0][2] == spot and List[1][2] == spot and List[2][2] == spot: # 369
        return True
    elif List[0][0] == spot and List[1][1] == spot and List[2][2] == spot: # 159
        return True
    elif List[0][2] == spot and List[1][1] == spot and List[2][0] == spot: # 357
        return True
    else:
        return False
    

def Player_Step(List):                        # Функция осуществляет интерфейс игрока
    Cicle = True
    print('                               Ваш ход')
    while Cicle:          
        str1 = input('                       Введите номер свободной клетки  (X):')         # Запрос хода
        try:
            Kletka = int(str1)
            if Kletka > 9 or Kletka < 1:             # проверка на погрешность   1 < Number < 9
                print('Введите число больше 0, но не более 9   ')
            else:
                if List[Kletka_in_List(Kletka,True)[0]][Kletka_in_List(Kletka,True)[1]] =='x' or List[Kletka_in_List(Kletka,True)[0]][Kletka_in_List(Kletka,True)[1]] =='o':    # проверка на свободную клетку
                    print('                             Простите. Данная клетка уже занята, выберете другую')
                else:
                    Cicle = False                        # Введенное число подходит - выходим из цикла
        except ValueError:
            print("Это не правильный ввод. Введите число больше 0, но не более 3") 
    return   Kletka

def BotStep(List,Step,Number,Player, PastStep):
    if Player:          # комп ходит после игрока               ДАННЫЙ КОД ВЫПОЛНЕН НА 50%
        if Step == 1:
            if List[1][1] != 'x':
                return 5
            else:
                return 1
        elif Step == 2:                 # STEP 2
            if List[1][1] == 'o':
                if Number == 2:
                    if List[1][2] =='x':
                        return 3
                    elif List[1][0] =='x':
                        return 1
                    elif List[0][0] =='x':
                        return 3
                    elif List[0][2] =='x':
                        return 1
                    
                if Number == 4:
                    if List[0][1] =='x':
                        return 1
                    elif List[2][1] =='x':
                        return 7
                    elif List[0][0] =='x':
                        return 3
                    elif List[2][0] =='x':
                        return 1
                    else: return 1


                if PastStep == 5:
                    if List[0][0] !='x' and List[0][2] !='x' and List[2][0] !='x' and List[2][2] !='x':
                        return 7

        elif Step == 3:                     # STEP 3
            if List[1][1] == 'o':
                if PastStep == 7:
                    if Number !=3:
                        return 3            # WIN
                    else:
                        if  List[0][1] == 'x':
                                return 1
                        elif List[1][2] == 'x':
                            return 9
                        else:
                            return 1
                if PastStep == 1:
                    if Number == 9:
                        if List[2][0] != 'x': 
                            return 8
                        else:
                            return 6                    
        elif Step == 4:             # STEP 4
            if List[1][1] == 'o':
                if PastStep == 9:           # Предыдущий ход 9
                    if Number != 1:         # WIN
                        return 1
                    else:
                        return 8
                elif PastStep == 1:         # Предыдущий ход 1
                    if Number != 4:
                        if List[1][0] != 'x':
                            return 4            # WIN
                        else: 
                            return 8
                # else:
                #     if List[1][0] == '4':
                #         return 4            # WIN
                #     else:
                #         return 9
                if Number != 9:
                    return 9
                else:
                    return 2

        







    else:               # комп ходит перед игроком              ДАННЫЙ КОД ВЫПОЛНЕН НА 100%
        if Step == 1:
            return 5
        else:
            if Step == 2:                           # STEP 2
                if Number == 2 or Number == 8:      # WIN
                    return 4 
                if Number == 4 or Number == 6:      # WIN
                    return 2

                if Number == 1 or Number == 9:      # Ничья
                    return 7

                if Number == 3 or Number == 7:      # Ничья
                    return 1

            elif Step == 3:                         # STEP 3
                if PastStep == 4:                   # WIN
                    if Number == 6:                 # WIN
                        return 7
                    else: 
                        return 6                    # Ничья
                elif PastStep == 2:                  # WIN
                    if Number == 8:                  # WIN
                        return 3
                    else: 
                        return 8                        # Ничья
            
                if PastStep == 7:
                    if Number != 3:
                        return 3                      # WIN
                    else:
                        if  List[0][0] == '1':
                            return 6
                        else:
                            return 2                        # Ничья
                if PastStep == 1:                   #dug
                    if List[0][2] == '3':
                        if Number != 9:
                            return 9                        # WIN
                        else:
                            return 8                        # Ничья
                    else:
                        return 6

            elif Step == 4:                             # STEP 4
                if PastStep == 7:                       # WIN
                    if Number != 1:                     # WIN
                        return 1
                    else: 
                        return 3                        # Ничья
                elif PastStep == 3:                     # WIN                       
                    if Number != 1:                     # WIN
                        return 1
                    else: 
                        return 7                        # Ничья
                elif PastStep == 2:
                    if Number != 8:
                        return 8                        # WIN
                    else:
                        return 4

                elif PastStep == 6:
                    if Number != 4:
                        return 4                     # WIN
                    else: 
                        return 2                    # Ничья
                elif PastStep == 8:
                    if Number !=2:
                        return 2                    # WIN
                    else:
                        return 6                    # Ничья
                elif PastStep == 1:
                    if List[2][2] != 'x':
                        return 9                    # WIN
                    else:
                        if List[0][1] != 'x':
                            return 2
                        else:
                            return 6

            elif Step == 5:                             # STEP 5
                if PastStep == 2:
                    if Number != 8:
                        return 8                     # WIN
                    else:
                        if List[0][0] == '1': 
                            return 1            # Ничья
                        elif List[2][0] == '7':
                            return 7
                        else:
                            return 9            # Ничья

                if PastStep == 6:
                    if Number != 4:
                        return 4                    # WIN
                    else:
                        if List[2][0] == '7': 
                            return 7            # Ничья
                        else:
                            return 3            # Ничья 
                if PastStep == 4:
                    if Number != 6:
                        return 6                # WIN
                    else:
                        return 9                # Ничья
                    
            else:                               # на входе неизвестные данные ктото мухлюет
                print('Я сдаюсь')
                exit()

   



visualizer(List_of_game)
Step = 1            # Счетчик ходов
Kletka = 0          # Начальное положение 

Player = randint(0,1)           # Определяем порядок ходов 1(True) - ходит игрок          0(False) - ходит компьютер

if Player:
    print('                     Вы ходите первым') 
else:

    print('                     Компьютер ходит первым. Нажмите Enter'
    )
    input()

NotEndGame = True               # индикатор окончания игры
PastStep = 0                    # Предыдущий ход компа

while  NotEndGame == True:     # игровое тело если игра окончена или пока есть свободные клетки
    if Player:                  # Игрок ходит первым
        
        Kletka = Player_Step(List_of_game) 
        List_of_game[Kletka_in_List(Kletka, True)[0]][Kletka_in_List(Kletka, True)[1]] = Kletka_in_List(Kletka, True)[2]    # вносим новые данные в игровое поле List_of_game
        visualizer(List_of_game)                                                                    # Проводим отрисовку игрового интерфейса
        if Getdraw(List_of_game) == False and WinGAME(List_of_game, False) == False: break          # Прорверка на наличие ходов(свободных клеток)
        if WinGAME(List_of_game, True):                                                              # Проверка на победу
              print('Это победа !!!!!')   
              NotEndGame = False
        else:  
   
            Kletka = BotStep(List_of_game, Step, Kletka, Player, PastStep)           # Ход компьютера   
            PastStep = Kletka
            List_of_game[Kletka_in_List(Kletka, False)[0]][Kletka_in_List(Kletka, False)[1]] = Kletka_in_List(Kletka, False)[2]     # вносим новые данные в игровое поле List_of_game
            visualizer(List_of_game)                                            # Проводим отрисовку игрового интерфейса
            print(f'                       Компьютер выбрал клетку: (o) {Kletka}')
            if WinGAME(List_of_game, False):                        # Проверка на победу
                print('Это поражение(((((')   
                NotEndGame = False 
            if Getdraw(List_of_game) == False: break            # Прорверка на наличие ходов(свободных клеток)
        
    else:                    # Игрок ходит вторым    (50% на победу если игрок сходит 2,6,8,4 победа компа 100%)
        Kletka = BotStep(List_of_game, Step, Kletka, Player, PastStep)                  # Ход компьютера

        PastStep = Kletka
        List_of_game[Kletka_in_List(Kletka, False)[0]][Kletka_in_List(Kletka, False)[1]] = Kletka_in_List(Kletka, False)[2]             # вносим новые данные в игровое поле List_of_game
        visualizer(List_of_game)                                                                    # Проводим отрисовку игрового интерфейса
        print(f'                       Компьютер выбрал клетку: (o) {Kletka}')
        if Getdraw(List_of_game) == False and WinGAME(List_of_game, False) == False: break              # Прорверка на наличие ходов(свободных клеток)
        if WinGAME(List_of_game, False):                                                         # Проверка на победу
              print('Это поражение(((((')   
              NotEndGame = False
        
        else:
            Kletka = Player_Step(List_of_game)                      # ХОД ИГРОКА  
            List_of_game[Kletka_in_List(Kletka,True)[0]][Kletka_in_List(Kletka,True)[1]] = Kletka_in_List(Kletka,True)[2]           # вносим новые данные в игровое поле List_of_game
            visualizer(List_of_game)                            # Проводим отрисовку игрового интерфейса
            if Getdraw(List_of_game) == False: break            # Прорверка на наличие ходов(свободных клеток)
            if WinGAME(List_of_game,True):                      # Проверка на победу   НЕВЕРОЯТНО МОЖНО БЫЛО НЕ ДЕЛАТЬ ЛИШНИЙ КОД
                    print('Это победа !!!!!')                    
                    NotEndGame = False
            

    Step += 1
    
    
           
if NotEndGame:                              # ИГРА ЗАВЕРШИЛАСЬ НИЧЬЁЙ
    print('                 Это НИЧЬЯ :)')
    print()