from datetime import datetime

current_hour = datetime.now().hour

# Formal greeting function
def greetings_formal(guest_name):
    print("Welcome:", guest_name, "we are glad you are coming.")

# Informal greeting function
def greetings_informal(guest_name):
    print("Welcome:", guest_name, "welcome my friend.")

# Guest data
guest_list = ["James", "Jacob", "Benjamin", "William", "Alexander"]
time_list = [11, 11, 14, 19, 20]
greetings_type = ["formal", "formal", "informal", "formal", "informal"]

# Time-based greeting function
def welcome_to(greeting_time):
    if 5 <= greeting_time < 12:
        return "Good Morning"
    elif 12 <= greeting_time < 17:
        return "Good Afternoon"
    elif 17 <= greeting_time < 21:
        return "Good Evening"
    else:
        return "Good Night"

# Greet all guests
def greetings_all(guest_list, time_list, greetings_type):
    for guest_name, greet_time, greet_type in zip(guest_list, time_list, greetings_type):
        greeting_message = welcome_to(greet_time)
        if greet_type == "formal":
            print(f"{greeting_message}! ", end="")
            greetings_formal(guest_name)
        elif greet_type == "informal":
            print(f"{greeting_message}! ", end="")
            greetings_informal(guest_name)

# Call the greetings function for all guests
greetings_all(guest_list, time_list, greetings_type)
