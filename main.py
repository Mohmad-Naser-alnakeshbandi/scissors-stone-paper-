from random import choice

print("Schere, Stein oder Papier?")
x=str(input())

Possibility = [1,2,3]
Decision=choice(Possibility)
if Decision== 1:
    print("Schere")
if Decision== 2:
    print("Stein")
if Decision== 3:
    print("Papier")

# erte Möglichkeit
if x=="Schere" and Decision==1:
    print("Keiner hat Gewonnen")

if x=="Schere" and Decision==2:
    print("Bot hat Gewonnen")

if x=="Schere" and Decision==3:
    print("Du hast Gewonnen")

#Zweite Möglichkeit
if x=="Stein" and Decision==1:
    print("Du hast Gewonnen")

if x=="Stein" and Decision==2:
    print("keiner hat Gewonnen")

if x=="Stein" and Decision==3:
    print("Bot hat Gewonnen")

# Dritte Möglichkeit
if x == "Papier" and Decision == 1:
    print("Bot hat Gewonnen")

if x == "Papier" and Decision == 2:
    print("Du hast  Gewonnen")

if x == "Papier" and Decision == 3:
    print("keiner hat Gewonnen")