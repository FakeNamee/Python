from random import randint

def Mnogochlen_in_Stepen_K(k):  
    Stroka=''
    Okonchnie = ''
    Mnozitel = '*'
    for i in range(k,-1,-1):                    
        Coeficient = randint(0,10)              
        if Coeficient == 0:                      
            STR_Coeficient = ''                    
            Stepen = ''
        else:                                  
            if Coeficient == 1:                     
                STR_Coeficient = ''
                Mnozitel = ''
            else:
                STR_Coeficient =str(Coeficient) 
                Mnozitel = '*'

            if i == 1:                  
                Stepen = STR_Coeficient + Mnozitel+'x'
            else:
                Stepen = STR_Coeficient + Mnozitel+'x^'+str(i)    

    
        if i == 0:               
            if Stroka == '': Stroka = 'x'
            Okonchnie = ' = 0'       
            Stepen = STR_Coeficient

        if  Stepen == '' or Stroka == '':  
            Plus = ''                                        
        else:
            Plus =' + '
        Stroka += Plus  + Stepen + Okonchnie 
    return Stroka

Imput_error = True 
while Imput_error:                                     
    str1 = input('Введите степень многочлена к = ')
    try:
        k = int(str1)
        if k < 0:
            print('Введите положительное число    ')
            Imput_error = True
        else:
            Imput_error = False       
    except ValueError:
        print("Это не правильный ввод, попоробуйте снова")



Imput_error = True 
while Imput_error:                                         
    str1 = input('Введите колличество создаваемых файлов N >=1 ')
    try:
        N = int(str1)
        if N < 0:
            print('Введите число более 0   ')
            Imput_error = True
        else:
            Imput_error = False       
    except ValueError:
        print("Это не правильный ввод, попоробуйте снова")

for i in range(N):                     
    file_Name = 'file' + str(i) + '.txt'    
    file = open(file_Name,'w')               
    Stroka = Mnogochlen_in_Stepen_K(k)        
    file.write(Stroka)                    
    file.close                         
    print(f'В файл и именем {file_Name} записана строка: ',Stroka)