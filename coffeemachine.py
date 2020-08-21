water = 400
milk = 540
bean = 120
cups = 9
money = 550
def remaining():  
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(bean) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")       
action = input("Write action (buy, fill, take, remaining, exit):\n")
while action != "exit":   
    if action == "buy":
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee != "back":
            if int(coffee) == 1:
                water = (water - 250)
                milk = (milk - 0)
                bean = (bean - 16)
                cups -= 1
                money = (money + 4)  
                if water >= 0 and milk >= 0 and bean >= 0 and cups >= 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    print("Sorry, not enough water!")
                    water += 250
                    milk += 0
                    bean += 16
                    cups += 1
                    money -= 4
            elif int(coffee) == 2:
                water = (water - 350)
                milk = (milk - 75)
                bean = (bean - 20)
                cups -= 1
                money = (money + 7) 
                if water >= 0 and milk >= 0 and bean >= 0 and cups >= 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    print("Sorry, not enough water!")
                    money -= 7
                    water += 350
                    milk += 75
                    bean += 20
                    cups += 1
            elif int(coffee) == 3:
                water = (water - 200)
                milk = (milk - 100)
                bean = (bean - 12)
                cups -= 1
                money = (money + 6)
                if water >= 0 and milk >= 0 and bean >= 0 and cups >= 0:
                    print("I have enough resources, making you a coffee!")
                else:
                    print("Sorry, not enough water!")
                    money -= 6
                    water += 200
                    milk += 100
                    bean += 12
                    cups += 1
            
    elif action == "fill":
        water = water + int(input("Write how many ml of water do you want to add:\n"))
        print(water)
        milk += int(input("Write how many ml of milk do you want to add:\n"))
        bean += int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        money += 0
    elif action == "take":
        print("I gave you $" + str(money))
        money = 0
    elif action == "remaining":
        remaining()
    
    action = input("Write action (buy, fill, take, remaining, exit):\n")
