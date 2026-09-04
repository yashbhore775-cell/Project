#define the menu of cafe
menu = {                            
    "sprite":50,
    "juice":40,
    "coffee":70,
    "tea":20,
    "pizza":80,
}

#Greet
print("welcome to yash cafe")
print("Sprite: RS-50\nJuice: RS-40\nCoffee: RS-70\nTea: RS-20\nPizza: RS-80\n")

order_total = 0
#80 + 20

item_1 = input("enter the name of item you want to order = ")                   
if item_1 in menu:
  order_total += menu[item_1]#0 + 50
  print(f"your item {item_1}has been added to your order")

else:
  print(f"ordered item{item_1}in not available yet")       

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
  item_2 = input("enter the name of second item =")
  if item_2 in menu:
    order_total += menu[item_2]
    print(f"item {item_2}has been added to order")
  else:
    print(f"ordered item{item_2}is not available!")

print(f"the total amount of items to pay is {order_total}")


