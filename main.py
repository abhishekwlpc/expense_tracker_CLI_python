import user_action_methods

# Welcome message
print("Welcome to the Python Express Tracker!")
while True:
    try:
        # Operation decision
        print("\n===============================EXPENSE TRACKER===================================\n")
        operation = input("** Enter following number to proceed\n-> To Add expense, type 1 and press enter\n-> To See all expenses and total amount you send, type 2 and press enter\n-> To See total spend amount, type 3 and press enter\n-> To Delete an expense from the list, type 4 and press enter\n-> To Delete all expenses from the list, type 5 and press enter\n-> To quit please enter q\n")

        match(operation):
            case "1":
                user_action_methods.add_expense()
            case "2":
                user_action_methods.view_expenses_list()
            case "3":
                user_action_methods.get_total_spent_amount()
            case "4":
                user_action_methods.delete_expense_from_list()
            case "5":
                user_action_methods.delete_all_expenses()
            case "q":
                break

    except ValueError as e:
         print("Please type 1 or 2 or 3 or 4 or q", e)

    except Exception as e:
        print("Some Error Occured: ", e)