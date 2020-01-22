#validating python version
import sys
if sys.version_info[0] < 3:
    print("Error: You must use Python 3, try running $ python3 app.py or updating the python interpreter")

#their exercise code starts here
import json
from DataStructures import Queue

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")

def show_main_menu():
    print('''
What would you like to do (type a number and press Enter)?
    - Type 1: For adding someone to the Queue.
    - Type 2: For removing someone from the Queue.
    - Type 3: For printing the current Queue state.
    - Type 4: To export the queue to the queue.json file.
    - Type 5: To import the queue from the queue.json file.
    - Type 6: To quit
    ''')
    response = input()
    return response

#1
def enqueue():
    print('\nWho would you like to add to the queue?')
    person = input()
    queue.enqueue( person )
    next_in_line = queue.size() - 1 if queue._mode == 'FIFO' else 0
    amt = 'is one person' if next_in_line == 1 else f'are {next_in_line} people'
    print(f'{person} added to queue. There are {amt} before them.')

#2
def dequeue():
    person = queue.dequeue()
    print(f'{person} has been removed from the queue.')

#3
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

#4
def export_queue():
    print('Exporting queue to JSON file...')
    jsonfile = open('queue.json' , 'w')
    json.dump(queue.get_queue() , jsonfile)
    jsonfile.close()
    print('JSON file has been created successfully')

#5
def import_queue():
    print('Importing queue from JSON file')
    jsonfile = open('queue.json' , 'r')
    global queue
    queue = Queue (mode='FIFO', current_queue = json.load(jsonfile))
    jsonfile.close()
    print_queue()


def start():
    
    print("\nHello, this is the Command Line Interface for a Queue Management application.")
    while True:
        
        option = show_main_menu()
        
        try: #converting the user input into an integer
            option = int(option)
        except ValueError:
            print("Invalid option "+str(option))

        # add your options here using conditionals (if)
        if option == 1:
            enqueue()
        elif option == 2:
            dequeue()
        elif option == 3:
            print_queue()
        elif option == 4:
            export_queue()
        elif option == 5:
            import_queue()
        elif option == 6:
            print("Bye bye!")
            return None
        else:
            print("Invalid option "+str(option))

    
start()
