import random 
h = 0 
bt = 0 
bot = ("камень","ножницы","бумага") 
while True: 
    human = input() 
    b = random.choice(bot) 
    print(b) 
    if human == 'камень' and b == 'ножницы': 
        h += 1 
    elif human == 'камень' and b == 'бумага': 
        h += 1 
    elif human == 'ножницы' and b == 'камень': 
        bt += 1 
    elif human == 'бумага' and b == 'камень': 
        bt += 1 
    elif human == 'ножницы' and b == 'бумага': 
        h += 1 
    elif human == 'бумага' and b == 'ножницы': 
        bt += 1 
    if h == 3: 
        print('человек выйграл') 
        break 
    if bt == 3: 
        print('бот выйграл') 
        break


