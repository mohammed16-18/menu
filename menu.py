menu = {
    "maggi":30,
    "puff":40,
    "fried_rice":60,
    "sushi":1000,
}#our items in menu with their prices
money=[]#list to store the money inserted by the user
money.append(int(input()))#user inputs the money list
total_money =sum(money)#calculate the total money 
order =input("what do you want to order?")#it will ask the user what they want to order
if(order in menu):#check if the order is in the menu
    print("available")#if the order is available
    if(total_money >= menu[order]):#check if the user has enough money to buy the order
        print("yes you can afford it")#if the user has enough money to buy the order
    else:
        print("you can't afford ")#if the user doesn't have enough money to buy the order
else:
    print("not available")#if the order is not available