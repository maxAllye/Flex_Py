# Limitless Class
# Author: Melissa Patel MIET, Jacob Hopkins AMG 
# Date: 04/08/2023
# Version: 0.1
# Description: A class to check the limits of CAN Bus devices

# Import Libraries
import json

# Class
class Limitless:
    # Class Variables
    # None for now whilst in development

    # Class Initialisation
    def __init__(self, limits):
        #self.name = name
        #self.address = address
        # Dictionary to store the limits
        self.limits = {}
        # Load the limits from the JSON file
        self.loadLimits(limits)

    # Class Methods
    def loadLimits(self, filename):
        with open(filename) as f:
            data = json.load(f)
        # Store the limits in the dictionary
        self.limits = data
        
    def checkJson(self, json, limit_type, logger, *devices):

        #check the limit exists and pull the limit out
        if limit_type not in self.limits:
            return "not a valid limit not available"
        
        else:
            currentlimits = self.limits[limit_type]

        #iterrate through all devices passed to method
        for device in devices:

            #set flag to false 
            #flag is used to stop unessesary checks and speed up operation
            #all device variables appear in a block so once we start checking limits flag can be set
            limitscheckedflag = False

            #pull each key from the data json
            for key in json.keys():
                #split key to get device and the variable
                splitkeyarry = key.split("_")
                #check if the device is the requested device
                if splitkeyarry[0] == device:
                    #once we've started checking limits set flag to true
                    limitscheckedflag = True

                    #Check if the split key matches the limits - if it does then check against high and low limit
                    if splitkeyarry[1] in currentlimits:       
                        error = self.checkLimits(json[key], currentlimits[splitkeyarry[1]][0], currentlimits[splitkeyarry[1]][1])
                        #stick something in the logger if there has been a breach of limits
                        if error == True:
                            logger.critical(f"error has been raised in limits for {key} - lower and upper limits {currentlimits[splitkeyarry[1]][0]}, {currentlimits[splitkeyarry[1]][1]} with value {json[key]}")
                            return True
                
                #if we've already checked the limits then break out the for loop and continue to the next limit check (if applicable) 
                else:
                    if limitscheckedflag == True:
                        break

        return False

    def checkLimits(self, value, limit, limit_bound = False):
        # Check if there is an upper or lower limit
        #ignore all default values
        if value == -41173:
            return False
        
        if (limit_bound == False):
            # Check if the value is at or below the limit
            if (value <= limit):
                return False
            else:
                return True
        else:
            # Check if the value is within the limits
            if (value >= limit and value <= limit_bound):
                return False
            else:
                return True
         
            
    def checkLimitsAuto(self, canData):
        # This function is not yet implemented
        # This function will automatically check the limits of the device
        return False
    
    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                            Code Usage
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# testlimit = Limitless()
# json_string = '{"pack1":{"voltage":27,"poop":32}}'
# somejson = json.loads(json_string)
# error = testlimit.checkJson(somejson, "pack_NCM")
# print(error)
# anotherjson = '{"pack2":{"voltage":350, "current":-41173}}'
# somejson = json.loads(anotherjson)
# error = testlimit.checkJson(somejson, "pack_NCM")
# print(error)

