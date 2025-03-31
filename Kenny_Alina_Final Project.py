# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 19:29:00 2022

@author: Alina
"""
while True:

    import pandas as pd
    from Garage import Garage
    from spaces import Spaces
    
    #read the excel file of parking lot details
    data = pd.read_excel(r'Final_Project_ParkingLotDetail.xlsx')
    
    print("Welcome to the parking app! \nBuildings are grouped into five lists.")
    
    purpose = input("Would you like to see a list of: \n- Schools & Colleges \n- Campus Life \n- Major Residences\n- Buildings & Services \n- Special Attractions \n\nPlease type one of the options (type 'and' as '&'): ")
    purpose = purpose.lower() #for case insensitive
    
    #for loop for keep asking if they found what they were looking for
    #use definition and raise exception for these if/else
    def choose_list(user_input):
        if user_input == "schools & colleges":
            building_list = data['Schools & Colleges'].tolist()
            print()
            print("Here is the list of building for schools & colleges:")
            print()
            for i in building_list:
                print(i)
        elif user_input == "campus life":
            building_list = data['Campus Life'].tolist()
            print()
            print("Here is the list of buildings for campus life:")
            print*()
            for i in building_list:
                print(i)
        elif user_input == "major residence":
            building_list = data['Major Residence'].tolist()
            print()
            print("Here is the list of buildings for major residence:")
            print()
            for i in building_list:
                print(i)
        elif user_input == "buildings & services":
            building_list = data['Buildings & Services'].tolist()
            print()
            print("Here is the list of buildings for buildings & services:")
            print()
            for i in building_list:
                print(i)
        else:
            print()
            print("Did you type the name correctly? Please type exactly as one of the options.")
            purpose = input("Would you like to see a list of the 'Schools & Colleges', 'Campus Life', 'Major Residences','Buildings & Services', or 'Special Attractions'? ")
            purpose = purpose.lower() #for case insensitive 
            
        #there are some issues with nan that I was not sure how to figure out
    
            
    choose = choose_list(purpose)
    print(choose)
    
    #try else statement to check the input validity
    def try_except():
        try: 
            purpose = input("Would you like to see a list of: \n- Schools & Colleges \n- Campus Life \n- Major Residences\n- Buildings & Services \n- Special Attractions \nPlease type one of the options (type 'and' as '&'): ")
            purpose = purpose.lower() #for case insensitive
        except:
            if purpose is int:
                print("Enter valid input")
        else: 
            #choose = choose_list(purpose)
            print(choose_list(purpose))       
    
       # problem with nan in lists
    
    user_building = input("Please choose a building: ")
    print()
    
    #dictionary of building and their corresponding number on the BU campus map
    buildings = {
        16: 'boston university academy',
        25: 'college of arts & science',
        33: 'college of communications',
        32: 'college of engineering',
        14: 'college of fine arts',
        13: 'college of general studies',
        27: 'graduate school of arts & sciences',
        20: 'metropolitan college & extended education',
        35: 'sargent college of health & rehabilitation sciences',
        36: 'school of education',
        7: 'school of hospitality administration',
        19: 'school of law',
        41: 'school of management',
        26: 'school of social work',
        21: 'school of theology',
        21.5: 'university professor programs',
        6: 'agganis arena',
        48: 'barnes & noble at boston university',
        3: 'case athletic center',
        8: 'fitness & recreation center',
        17: 'george sherman union',
        22: 'marsh chapel',
        18: 'mugar memorial library',
        16.5: 'student activities center',
        1: 'track & tennis center',
        28: 'tsai performance center',
        9: '10 buick street', 
        44: '575 commonwelath avenue',
        2: '1019 commonwealth avenue danielsen hall',
        50: 'myles standish hall', 
        45: 'shelton hall',
        24: 'south campus',
        39: 'the towers',
        30: 'warren towers',
        4: 'west campus',
        43: 'admissions reception center',
        5: 'boston university police',
        12: 'center for english language and orientation programs',
        11: 'comptroller',
        17.5: 'dean of students',
        11.5: 'financal assistance',
        49: 'hotel commonwalth',
        10: 'housing office',
        31: 'information technology',
        46: 'international students & scholars office',
        34: 'life science & engineering',
        42: 'metcalf science center',
        40: 'presidents office',
        11.1: 'registrar',
        11.2: 'student health services',
        47: 'university computers',
        11.3: 'university service center',
        14.1: 'bu art gallery at the stone gallery',
        37: 'boston university experiences',
        37.1: 'boston unviersity theatre',
        29: 'the catsle',
        51: 'dewolfe boathouse',
        18.1: 'gotlieb archibal research center',
        23: 'photonics center'
        }
    
    #dictionary for lots and their areas
    garage_area = dict(zip(data.Lot, data.Area))
    
    
    #tuple as it should not be changed
    area_1 = (50, 46, 47, 48, 45, 43, 39, 40, 41, 44, 49)
    area_2 = (36, 35, 37, 37.1, 42, 38, 33, 34, 32, 31, 30)
    area_3 = (28, 27, 25, 26, 22, 21, 21.5, 20, 29)
    area_4 = (23, 16, 16.5, 17, 17.5, 18, 18.1, 19)
    area_5 = (15, 14, 14.1, 13, 11, 11.1, 11.2, 11.3, 11.5, 10, 12)
    area_6 = (6, 8, 9, 7, 5)
    area_7 = (2, 4, 3, 1)
    
    
    
    #dictionary for lot and permit types
    permit_lot = dict(zip(data.Lot, data.Permits))
    
        
    print("Here are the permit options from the university:")
    print()
    print("Blue = student commuter permit")
    print("White = student evening commuter permit")
    print("Flex = pay only when you park")
        
    user_permit = input("What kind of permit do you hold: ")
    print()
    user_permit = user_permit.lower()
    
    
        
    #to print list of garages closest to building
    user_garage = Garage()
    
    print(f"The area of your building is {user_garage.get_area(buildings, user_building)}")
    print()
    print(f"The garages in that area are {user_garage.get_garages(garage_area)}")
    print()
    
    #user_garage.get_area(buildings, user_building)
    #user_garage.get_garages(garage_area)
    
    #dictionary for lot and time it is open
    lot_time = dict(zip(data.Lot, data.Time))
    
    permitLot = []
    
    #to check which garage each permit is allowed
    def permit(userPermit):
        
        for i in permit_lot:
            if str(userPermit) in str(permit_lot[i]):
                permitLot.append(i)
            else:
                continue
        
        return permitLot
    
    permit_check = permit(user_permit)   
    
    #dictionary for lot and time it is open
    lot_time = dict(zip(data.Lot, data.Time))
    
    user_time = input("What time do you need to park? \nPlease use military time and format at quarter of hour (ex. 15:00, 15:15, 15:30, or 15:45): ")
    print()
    
    time_lot = []
    
    #check lots with corresponsing time regulations
    def time(input_time):
        for i in lot_time:
            if str(input_time) in str(lot_time[i]):
                time_lot.append(i)
            else:
                continue
        return time_lot
    
    time_check = time(user_time)
    
    
    
    a = set(permit_check)
    b = set(user_garage.get_garages(garage_area))
    #c = set(time_check)
    
    lots_accessiblePermit = [i for i in a if i in b]
    print(f"The lots you can park with your permit type are: {lots_accessiblePermit}")
    print()
    
    lots_accessible = []
    
    #check lots that match both permit and time regulations
    def timeMatch():
        for i in lots_accessiblePermit:
            if i in time_lot:
                lots_accessible.append(i)
            else:
                continue
        return lots_accessible
    
    user_lotAccessible = timeMatch()
    
    print(f"The lots you can park at {user_time} with your permit are: {user_lotAccessible}")
    
    
    user_lot = input("Which lot would you like to choose? Format Answer (ex.Lot G): ")
    print()
    space = Spaces(user_lot)
    space.get_spaceNumber()
    
    print("Your parking information:")
    print()
    print(space.__str__())
    space.enter_lot()
    
    #try function to check if user input is yes or no typed correctly
    def main(u_input):
        try:
            u_input == "yes" or "no"
        except: 
            print("Try again.")
    
    main(user_lot)
    
    #dictionary for lot and lot name
    lot_name = dict(zip(data.Lot, data.Name))
    
    print(f"The name of {user_lot} is {user_garage.get_name(lot_name, user_lot)}.")
    
    #dictionary for lot and address
    lot_address = dict(zip(data.Lot, data.Address))
    
    #print the address of the lot using class method
    print(f"The address of {user_lot} is {user_garage.get_address(lot_address, user_lot)}.")
    
    user_status = input("Would your like to stay or leave? Yes or No: ")
    user_status = user_status.lower()
    
    #to see if continue the program or not
    if user_status == "yes":
        continue
    else:
        break










