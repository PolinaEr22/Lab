import random

def roll_dice():
    dice = random.randint(1, 6)
    print(f"Выпало: {dice}")
    
    if dice >= 5:
        print("Вы выиграли!")
    elif dice >= 3:
        print("Продолжаем...")
        roll_dice()
    else:
        print("Вы проиграли.")

roll_dice()
