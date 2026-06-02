file_name = "whichassignmentisthis"

coding_hours = None
pushup_minutes = None
Flying_hours = None
Secondary_tests = None
Officer_name = None






            # print(line.replace("_HOURS_", coding_hours, "_MINUTES_", pushup_minutes, "_SECONDARYHOURS_", Flying_hours, "_TESTS_", Secondary_tests, ))

def get_data():
    global coding_hours, pushup_minutes, Flying_hours, Secondary_tests, Officer_name
    coding_hours = input("Enter how many hours to code: ")
    pushup_minutes = input("Enter number of pushup minutes: ")
    Flying_hours = input("Enter number of hours to fly: ")
    Secondary_tests = input("Enter number of tests to take: ")
    Officer_name = input("Enter officer name: ")
    

def load_ticket(ticket_name):
    with open(ticket_name, "r") as file:
        full_text = file.read()
    
    full_text = full_text.replace("_HOURS_", coding_hours)
    full_text = full_text.replace("_MINUTES_", pushup_minutes)
    full_text = full_text.replace("_SECONDARYHOURS", Flying_hours)
    full_text = full_text.replace("_TESTS", Secondary_tests)
    full_text = full_text.replace("_D_P_E_U_D_T_Y_", Officer_name)
    print(full_text)
    

        



def main():
    get_data()
    load_ticket("ticket.txt")


if __name__ == "__main__":
    main()