menu={
    'Fry Rice':100,
    'Veg Momo':80,
    'Veg Chaumein':80,
    'Chicken Momo':120,
    'Chicken Chaumein':100,
    'Samosa':60,
    'Chatpate':50,
    'Milk Tea':20,
    'Black Tea':15,
    'Cold Coffee':100,
    'Latte':150,
    'Lemon Juice':70,

}
print('Welcome to CSITHUB!\nMenu:')
print("Fry Rice: Rs 100\nVeg Momo: Rs 80\nVeg Chaumein: Rs 80\nChicken Momo: Rs 120\nChicken Chaumein: Rs 100\nSamosa: Rs 60\nChatpate: Rs 50\nMilk Tea: Rs 20\nBlack Tea: Rs 15\nCold Coffee: Rs 100\nLemon Juice: Rs 70")
total=0
item1=input("What do you wanna order :")


if item1 in menu:
    
    quantity=int(input('Quantity:'))
    total+=quantity*menu[item1]
    print(f"{quantity} {item1} has been added to your order")
else:
    print("Sorry!Please enter an item that our menu has")
order=input("Do you need other items too? (yes/no):")
if order=='yes':
    item2=input("Enter the item:")
    if item2 in menu:
       
        quantity=int(input('Quantity:'))
        total+=quantity*menu[item2]
        print(f"{quantity} {item2} has been added to your order")
else:
    print("Thank you for your order! Your order will be in a minutes.")

print(f"Your total amount is Rs {total}")