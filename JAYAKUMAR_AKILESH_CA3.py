# Name: Jayakumar Akilesh
# Student ID: 10229951
# Module: Problem Solving
# Exam: CA3 Individual Assignment

# Python Version 3.10.0

def get_valid_input(prompt, valid_options):
    """Prompt the user for input and ensure it is within the valid options."""
    user_input = input(prompt)
    while user_input not in valid_options:
        print(f"Invalid input. Please enter one of the following: {
              ', '.join(valid_options)}")
        user_input = input(prompt)
    return user_input


def enter_data(times, location, type_of_hazard, risk):
    """Allow the user to enter data multiple times."""
    data_entries = []
    for _ in range(times):
        location_input = get_valid_input("Enter Location: ", location)
        hazard_input = get_valid_input(
            "Enter Type of Hazard: ", type_of_hazard)
        risk_input = get_valid_input("Enter Risk Level: ", risk)
        data_entries.append([location_input, hazard_input, risk_input])
    return data_entries


def display_menu():
    """Display the main menu and get the user's choice."""
    print("\n:: Option Menu ::\n1. Parameter Settings\n2. Show Report Summary\n3. End The Program")
    choice = int(get_valid_input("Enter Your Choice Here: ", ["1", "2", "3"]))
    return choice


def main():
    location = ("Living room", "Dining room", "Kitchen", "Bedroom", "Bathroom")
    type_of_hazard = ("Fire hazard", "Physical hazard",
                      "Water leakage", "Electricity outage")
    risk = ("High", "Medium", "Low", "None")

    print("\n\n" + ":" * 30 + " Welcome To " + ":" * 42)
    print("Home Inspection Visualisation | Artificial Intelligence and Digitalization Solutions")
    print(":" * 84 + "\n")

    records = []
    while True:
        choice = display_menu()

        if choice == 1:
            times = int(
                input("\nHow Many Times Do You Want To Enter Your Data? : "))
            records.extend(enter_data(times, location, type_of_hazard, risk))

        elif choice == 2:
            if records:
                print("\nYour Report Summary Is: ")
                for record in records:
                    print(record)
            else:
                print("\nNo data entered. Please enter data before viewing the summary.")

        elif choice == 3:
            print("\nThis Program Has Ended. Thank You For Using Home Inspection Visualisation. We Hope You Come Back Again. Have A Nice Day!")
            break


if __name__ == "__main__":
    main()
