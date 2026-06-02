file_name = "whichassignmentisthis"

coding_hours = None
pushup_minutes = None
Flying_hours = None
Secondary_tests = None
Officer_name = None






            # print(line.replace("_HOURS_", coding_hours, "_MINUTES_", pushup_minutes, "_SECONDARYHOURS_", Flying_hours, "_TESTS_", Secondary_tests, ))

def get_data(ticket_name):
    global coding_hours, pushup_minutes, Flying_hours, Secondary_tests, Officer_name
    coding_hours = input("Enter how many hours to code: ")
    pushup_minutes = input("Enter number of pushup minutes: ")
    Flying_hours = input("Enter number of hours to fly: ")
    Secondary_tests = input("Enter number of tests to take: ")
    Officer_name = input("Enter officer name: ")

def load_ticket(ticket_name):
    with open(ticket_name, "r") as file:
        for line in file.readlines():
            print(line.rstrip())




load_ticket("ticket.txt")