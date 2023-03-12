# This function displays the current value
# on the calculator
def display_current_value():
    print("Current value: " + str(current_value))
    
# This function adds the argument to the
# current value
def add(to_add):
    global current_value
    current_value += to_add
    print("+ " + str(to_add))
    memory()
    
# This function substracts the argument
# from the current value
def subtract(to_subtract):
    global current_value
    current_value -= to_subtract
    print("- " + str(to_subtract))
    memory()
    
# This function multiplies the argument
# to the current value
def multiply(to_multiply):
    global current_value
    current_value *= to_multiply
    print("x " + str(to_multiply))
    memory()
    
# This function divides the argument from
# the current value
def divide(to_divide):
    global current_value
    if to_divide != 0:
        current_value /= to_divide
        print("/ " + str(to_divide))
        memory()
    else:
        current_value = "Error"
        
# Thi function stores a 
def store(position):
    if "storage" not in globals():
        global storage
        storage = []
        for i in range(position):
            storage.append(0)
    else:
        if len(storage) < position:
            for i in range(position-len(storage)):
                storage.append(0)
    storage[position-1] = current_value
    print(str(current_value) + " has been stored to position " + str(position))


''' * * * * * d[ictionary version * * * * * '''

def store_dict(position):
	# Define dictionary if it hasn't been defined yet
	if "storage_dict" not in globals():
		global storage_dict
		storage_dict = {}
	# Store the current_value to the key position
	storage_dict[position] = current_value
	print(str(current_value) + " has been stored to position " +
	str(position))

def recall_dict(position):
	global current_value
	# Access the value at key position
	current_value = storage_dict[position]
	print("Position " + str(position) + " has been recalled")





def recall(position):
    global current_value
    current_value = storage[position-1]
    print("Position " + str(position) + " has been recalled")
   
def memory():
    if "memory_storage" not in globals():
        global memory_storage
        memory_storage = []
        memory_storage.append(0)
    memory_storage.append(current_value)

def undo():
    global memory_storage
    global current_value
    if len(memory_storage) > 1:
      memory_storage.pop(-1)
      current_value = memory_storage[-1]
    else:
      current_value = 0
    
if __name__ == "__main__":
    print("Welcome to the calculator program.")
    current_value = 0
    display_current_value()
    add(5)
    display_current_value()
    store(1)
    multiply(10)
    store(5)
    recall(1)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()

    print("\n\nWelcome to the calculator program dict.")
    current_value = 0
    display_current_value()
    add(5)
    display_current_value()
    store_dict(1)
    multiply(10)
    store_dict(5)
    recall_dict(1)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()




    del current_value
    del storage
    del memory_storage
    
   
