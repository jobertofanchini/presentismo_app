contador = 10000
x = 0
switch1 = False
switch2 = False
switch3 = False

while contador > 0:
    print("█" * (x * 2))
    
    
    if switch1 == False and switch2 == False and switch3 == False:
        x = 0
        
        switch3 = True 
        switchSentido = False
        
    elif switch1 == False and switch2 == False and switch3 == True:
        x = 1
        
        if switchSentido == False:
            switch1 = False
            switch2 = True
            switch3 = False
        elif switchSentido == True: 
            switch1 = False
            switch2 = False
            switch3 = False
    
    elif switch1 == False and switch2 == True and switch3 == False:
        x = 2
        
        if switchSentido == False:
            switch1 = False
            switch2 = True
            switch3 = True
        elif switchSentido == True: 
            switch1 = False 
            switch2 = False
            switch3 = True
            
    elif switch1 == False and switch2 == True and switch3 == True:
        x = 3
        
        if switchSentido == False:
            switch1 = True
            switch2 = False
            switch3 = False
        elif switchSentido == True: 
            switch1 = False 
            switch2 = True
            switch3 = False
        
    elif switch1 == True and switch2 == False and switch3 == False: 
        x = 4 
        
        switch1 = False
        switch2 = True
        switch3 = True
        switchSentido = True
    
    contador -= 1 
        
     
