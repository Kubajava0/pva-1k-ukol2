import random

options = ["1", "2", "3"] # 1 = Kámen, 2 = Nůžky, 3 = Papír

win = 0
loss = 0
tie = 0

print("Vítejte ve hře Kámen, Nůžky, Papír!")
print("Hru ukončíte zadáním: 0\n")

while True:
    player = input("Možnosti: \nKámen = 1\nNůžky = 2\nPapír = 3\nZadejte svou volbu: ").strip().lower()
    
    if player == "0":
        break
    if player not in options:
        print("Neplatná volba, zkus to znovu.\n")
        continue

    print(f"\nZvolil jsi: {"Kámen" if player == "1" else "Nůžky" if player == "2" else "Papír"}")
    computer = random.choice(options)
    print(f"Počítač zvolil: {"Kámen" if computer == "1" else "Nůžky" if computer == "2" else "Papír"}")
    
    if player == computer:
        print("Je to remíza!")
        tie += 1
    elif (player == "1" and computer == "2") or \
         (player == "2" and computer == "3") or \
         (player == "3" and computer == "1"):
        print("Vyhrál jsi!")
        win += 1
    else:
        print("Počítač vyhrál!")
        loss += 1
    
    print(f"Skóre: Výhry: {win}, Prohry: {loss}, Remízy: {tie}\n")

print("\nKonec hry:")
print(f"Celkové skóre: Výhry: {win}, Prohry: {loss}, Remízy: {tie}")
