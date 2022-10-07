Number1 = int(input('Введите число '))                  
Number = Number1    

Lern_of_Number = []

Delenie_Vozmogno = False
for i in range(2,100):              
                                    
    Del = True
    while Del:                                  
        if Number % i == 0: 
            Lern_of_Number.append(i)
            Number = Number // i
            Delenie_Vozmogno = True
        else:
            Del=False
if  Delenie_Vozmogno == False:      
    Lern_of_Number = [Number1]
    
print(Lern_of_Number)