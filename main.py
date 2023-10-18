from threading import Thread, Event
import time
from SharedContext import SharedContext
from Limitless_class import Limitless
import json


#------ Define Constants ------
WRITE_PERIOD = 5     #write period in seconds
CONTROL_JSON_PATH = "control.json"


# class Limits:

#     def __init__(self):

#         self.alarm = Limitless("alarm.json")
#         self.error = Limitless("critical.json")

#         return 
    
#     def CheckLimits(self,data):
        
#         alarm_flag = self.alarm.checkLimits(data)
#         error_flag = self.error.checkLimits(data)

#         return alarm_flag, error_flag


class DataTransfer:
    def __init__(self):

        self.read_data = SharedContext()
        self.control = SharedContext()
        self.status = SharedContext()

        return 
    
    def ReadRead(self):
        
        data = self.read_data.read()

        return data
    
    def ReadControl(self):

        data = self.control.read()

        return data
    
    def ReadStatus(self):

        data = self.status.read()

        return data

    def WriteRead(self, data):

        self.read_data.write(data)

        return
    
    def WriteControl(self, data):

        self.control.write(data)

        return
    
    def WriteStatus(self,key,value):

        self.status.write_specific(key,value)

        return


class Main:
    def __init__ (self):

        self.data_transfer = DataTransfer() #this is SharedContext class by Melissa
        #self.limits = Limits()
        main.InitEvents()

        return

    def InitEvents(self):

        self.write_event = Event()
        self.shutdown_event = Event()

        return 


    def StartThreads(self):
        self.comms, self.data_connectivity = main.InitThreads()
        return 

    def InitThreads(self):
        self.comms = threading.Thread(target=CommsThread, args=(self.data_transfer,self.shutdown_event) )
        self.data_connectivity = threading.Thread(target=DataConnectivityThread, args=(self.write_event,self.data_transfer,self.shutdown_event) )
        return


    def InitSharedContext(self):

        data_socket = DataTransfer()

        return data_socket


    def ReadWriteComms(self,data_socket,data):

        data_socket.WriteWrite(data)
        data = data_socket.ReadRead()

        return data


    def Connect(self):
        
        connected = False

        #Turn on Sequence
        #Connect Bat Interlock, Enable battery CAN, wait for voltage & status
        #Close precharge, wait till voltage hits Vchrg, Close inverter_rly, wait for voltage hits Vchrg 
        #Close batt_rly, Open Precharge, Check voltage stability, close AC Relay

        #between eaxh state once battery is connected ensure battery contactors dicharge can signal is ok

        control["batt_interlock"] = 1
        self.ReadWriteComms(control)

        control["batt_enable"] = 1
        self.ReadWriteComms(control)



        control[""]



        return connected 


    def Disconnect(self):

        #follow disconnect procedure - eg everything off

        return


    def Shutdown(self):

        #send out shutdown event. wait for rondevous, die :)

        return
    
    def GetStatus(self):
        return self.data_transfer.ReadStatus()
    
    def GetData(self):
        return self.data_transfer.ReadRead
    




#####=====----- Main Begins Here -----=====#####

#---- Setup Main Class ----
main = Main()

#---- Setup Variables -----
control = json.load(CONTROL_JSON_PATH)
read_data = {}
status = {"DataHandler":0,"Comms":0}

#---- Setup Threads ----
main.StartThreads()

#Wait till all threads threads have started
while status["DataHandler"] is 0 or status["Comms"] is 0:
    status = main.GetStatus()
    time.sleep(0.1)


#---- Connect Procedure ----
connected = main.Connect()
if connected is not True:
    main.Disconnect()
    main.Shutdown()
    exit()


#---- Main Loop ----
#set initial time
t0 = time.time()

while True:

    read_data = main.ReadWriteComms(control)
    #error, warn = limits.CheckLimits(read_data)

    # Check if write time has elapsed
    if (time.time() - t0) > WRITE_PERIOD:
        write_event.set
        t0 = time.time()

    # if doing some debug then just stick print suff in here - threadding means keep alive will be unaffectert


    #instead of limits if battery contactors dicharge can signal goes false then shutdown

    # if error is True:
    #     Disconnect()
    #     Shutdown()
    #     break

    # elif warn is True:
    #     #Do Something
    #     control["led_amber"] = True

exit()