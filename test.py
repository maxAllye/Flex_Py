#------------------------ testing dbc load -------------------------------
# import cantools
# import json

# # Load the DBC file
# dbc_file = "Full.dbc"
# database = cantools.database.load_file(dbc_file)

# # Create a dictionary to store the JSON representation
# json_data = {}

# # Iterate through messages and add them to the JSON dictionary
# for message in database.messages:
#     message_info = {}
    
#     # Iterate through signals within the message and add them to the message dictionary with initial value 0
#     for signal in message.signals:
#         message_info[signal.name] = 0
    
#     # Add the message dictionary to the JSON data
#     json_data[message.name] = message_info

# # Convert the dictionary to a JSON string
# json_string = json.dumps(json_data, indent=4)

# # Print or save the JSON data as needed
# print(json_string)

# # Optionally, save the JSON data to a file
# with open("message_signal_initial_values.json", "w") as json_file:
#     json.dump(json_data, json_file, indent=4)

#--------------------------------------------------------------------------

#------------------------------- 

class my_class:
    def __init__(self):
        
        self.my_variable = 27

        return
    

classs = my_class()

print(classs.my_variable)

