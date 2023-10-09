import json
from threading import Event

class SharedContext:
    # Constructor
    def __init__(self, default_values = {}, timeout = 10):
        self.data = default_values
        self.event = Event()
        self.timeout = timeout

    # Private function that checks if the event is set
    def __check_event(self):
        return self.event.is_set()

    # Writes data to the SharedContext
    def write(self, *new_data):
        # Check if the event is set, if it is, wait for it to be cleared
        if self.__check_event():
            expired = self.event.wait(self.timeout)
            # If a timeout occurs, return False
            if expired:
                return False
        # Set the event for this write operation
        self.event.set()
        # Write the data
        for data in new_data:
            self.data.update(data)
        # Clear the event
        self.event.clear()

    # Writes data to a specific key in the SharedContext
    def write_specific(self, key, value):
        # Check if the event is set, if it is, wait for it to be cleared
        if self.__check_event():
            expired = self.event.wait(self.timeout)
            # If a timeout occurs, return False
            if expired:
                return False
        # Set the event for this write operation
        self.event.set()
        # Write the data
        self.data[key] = value
        # Clear the event

    # Reads data from the SharedContext
    def read(self):
        return self.data
    
    # Read Specific Data from the SharedContext
    def read_specific(self, key):
        return self.data[key]
    

    # Reads data from the SharedContext and returns it as a JSON string
    def read_json(self):
        return json.dumps(self.data, ensure_ascii=False)