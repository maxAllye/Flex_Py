import json
import can
import cantools
import time

class CanDevice:

    def __init__(self,channel,dbc=None,timeout=1,defaults=None):
        
        #set flag for initialisation sucsessful
        init_flag = False

        #------ Setup CAN Session ------
        #setup my bus and the buffered input
        self.bus = can.interface.Bus(channel=channel, bustype="socketcan")
        self.buffered_bus = can.BufferedReader(self.bus)
        

        #------ Setup CAN dbc ------
        if dbc is not None:
            #load in the DBC
            self.dbc = cantools.database.load_file(dbc)
            #Generate a Default JSON with 0's to be written to later
            self._GenerateDefaultData() 


        #------ Check Session has been Initialised ------
        #Set t0 for timeout
        t0 = time.time()

        #Check that session has been properly initialised and the netweork is ok
        while (time.time() - t0) < timeout:
            #Check to see if there is anything on the bus
            if self.bus.get_message() is not None:
                init_Flag = True
                break
            time.sleep(0.001)
        

        #------ Set Defaults ------
        #Check if user has intialised with defaults, if defaults fail then init fails
        if defaults is not None:
            inti_Flag = self.Defaults(defaults)


        return init_Flag
    

    def Defaults(self,defaults):

        defaults_Flag = False

        return defaults_Flag
    

    def Read(self):

        #read all recent data on the canbus
        message = 0

        while message is not None:
            message = self.buffered_bus.get_message()
            #set the cached data to the most recent data recieved by the bus
            self.data[self.dbc.get_message_by_frame_id(message.arbitration_id)] = self.dbc.decode_message(message.arbitration_id, message.data)

        return self.data
    

    def Write(self,data):

        

        return
    

    def Close(self):

        self.bus.shutdown()

        return
    

    #-=-=-=-=-=-=-=-=-=-=-=-=-=- PRIVATES -=-=-=-=-=-=-=-=-=-=-=-=-=-

    def _GenerateDefaultData(self):
        
        # Note to self - should probably do something in here to make this use the Tx Rx properties in the dbc but oh well

        # Create a dictionary to store the JSON representation
        dbc_dict = {}

        # Iterate through messages and add them to the JSON dictionary
        for message in self.dbc.messages:
            message_info = {}
            
            # Iterate through signals within the message and add them to the message dictionary with initial value 0
            for signal in message.signals:
                message_info[signal.name] = 0
            
            # Add the message dictionary to the JSON data
            dbc_dict[message.name] = message_info

        self.data = dbc_dict



