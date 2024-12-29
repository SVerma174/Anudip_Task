print("Welcome to My Hotel")

while True:
	print("\n 1: Veg \n2: Non-veg ")
    choice=int(input("Select your food type"))


    print("\n 1: Dine \n2: Take-Away ")
    choice=int(input("Select your choice"))

	print("\n1: Starters\n2: Main Course\n3: Desserts\n4: Drinks\n5: Exit")
   	choice = int(input("Select what you went to order: ")) 
        
    if choice == 1:
        print("\nStarters Menu:")
        print("1: Item1 - 250 Rs")
        print("2: Item2 - 200 Rs")
        st = int(input("Select your food: "))
        if st == 1:
            print("your select item 1 Greate Choice")
        elif st == 2:
            print("your select item 2 Greate Choice.")
        else:
            print("Invalid option for Starters.")
        
    elif choice == 2:
            print("\nMain Course Menu:")
            print("1: Item1 - 500 Rs")
            print("2: Item2 - 450 Rs")
            mc = int(input("Select your food: "))
            if mc == 1:
                print("your select item 1 Greate Choice")
            elif mc == 2:
                print("your select item 2 Greate Choice.")
            else:
                print("Invalid option for Main Course.")
        
    elif choice == 3:
            print("\nDesserts Menu:")
            print("1: Item1 - 150 Rs")
            print("2: Item2 - 120 Rs")
            ds = int(input("Select your option: "))
            if ds == 1:
                print("your select item 1 Greate Choice.")
            elif ds == 2:
                print("your select item 2 Greate Choice")
            else:
                print("Invalid option for Desserts.")
        
    elif choice == 4:
            print("\nDrinks Menu:")
            print("1: Item1 - 100 Rs")
            print("2: Item2 - 80 Rs")
            dr = int(input("Select your option: "))
            if dr == 1:
                print("your select item 1 Greate Choice.")
            elif dr == 2:
                print("your select item 2 Greate Choice.")
            else:
                print("Invalid option for Drinks.")
        
    elif choice == 5:
            print("Thank you for visiting! Goodbye.")
            break
        
    else:
            print("Invalid option. Please select from the menu.")
    