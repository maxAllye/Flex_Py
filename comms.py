import CanDevice
import threading

#Define Constants

MAEVING_CAN = "can0"
MAEVING_DBC = ""
CONTROL_FRAME_PERIOD = 100

# Accesses CanDevice class and produces a Maeving instance
def Init():

    maeving = CanDevice(MAEVING_CAN, dbc=MAEVING_DBC)

    return maeving

# What is the point?
def Wait():

    return

def Run():
    
    if control["batt_rly"] is True
        #turn on battrly digi io

    etc 

    #every CONTROL_FRAME_PERIOD write the control frame

    return

def Close(maeving):

    meaving.close

    return


def CommsThread(data_transfer,shutdown_event):

    Init()

    while True:

        Run()

        if shutdown_event is set:
            Close()