print("Welcome to Disaster Prep! \n Disaster Prep alerts users when a natural disaster has been predicted in their area and provides users with a personalized plan and check list of necessary items to keep users safe.")
def firstaid():
    print("First Aid Kit:")
    print("Flashlight and Extra Batteries \n Nonperishable food to last 3 days (for each person) (purification tablets) \n 1 gallon of water per person per day (3 Days) \n Plates, Cutlery, and, of course, a manual Can Opener \n 3 days worth of Clothing for everyone in your family \n Eyeglasses/Contacts and Contact Solution \n Necessary Medicines \n Electronics and Chargers \n For Infants: diapers, formula, etc. \n Waterproof Matches, a Whistle, and Strong Tape \n Battery operated or Crank Radio")

def flood():
    print("How to protect your home:")
    print("Board up windows \n All circuit breakers, switches, sockets, etc. should be a foot above water \n Anchor or disassemble outdoor equipment \n Clear gutters, downspouts, and drains \n Shut off electricity")
    print("Never drive on flooded roads \n Drive slowly and steadily \n Don’t drive over bridges over fast moving water unless absolutely necessary \n Watch out for downed power lines.")
    print("Check with your local council about local flood plans or records which detail problem areas \n Ask authorities about relocation routes and centers \n If your area is flood prone, consider alternatives to carpets \n Prepare an emergency kit \n Prepare a household flood plan \n Keep a list of emergency telephone numbers on display \n Check your insurance policy to see if you are covered for flood damage \n Secure hazardous items \n Roll up rugs, move furniture, electrical items and valuables to a higher level \n Place important personal documents, valuables and vital medical supplies into a waterproof case in an accessible location \n If you are relocating, take your pets with you if it is safe to do so. If not provide adequate food and water and move them to a safer place \n Monitor Bureau of Meteorology (BoM) forecasts and warnings online and listen to your local ABC Radio \n If rising waters threaten your home and you decide to move to a safer location, tell the police, your nearest State Emergency Service (SES) unit or your neighbors of your plans to move \n Monitor your local radio for warnings and advice \n Pack warm clothing, essential medication, valuables and personal papers in waterproof bags along with your emergency kit. \n Raise furniture, clothing and valuables onto beds, tables and into roof space place electrical items in the highest place \n Empty freezers and refrigerators, leaving doors open to avoid damage or loss if they float. \n Turn off power, water and gas and take your mobile phone \n Whether you leave or stay, put sand bags in the toilet bowl and over all laundry/bathroom drain holes to prevent sewage backflow \n Lock your home and take recommended relocation routes for your area \n Do not drive into water of unknown depth and current \n Monitor your local radio for warnings and advice \n Get to higher ground \n Switch off electricity and gas supplies to your home \n Prepare to move vehicles, outdoor equipment, garbage, chemical and poisons to higher locations \n Prepare for the well-being of pets \n Raise furniture above likely flood levels \n Check your emergency kit \n Do not allow children to play in or near floodwaters \n Avoid entering floodwaters. If you must do so, wear solid shoes and check depth and current with a stick \n Stay away from drains, culverts and water over knee deep. \n Do not use gas or electrical appliances that have been in floodwater until checked for safety \n Do not eat food that has been in floodwaters \n Boil tap water until supplies have been declared safe \n Secure hazardous items \n Roll up rugs, move furniture, electrical items and valuables to a higher level \n Place important personal documents, valuables and vital medical supplies into a waterproof case in an accessible location \n If you are relocating, take your pets with you if it is safe to do so. If not provide adequate food and water and move them to a safer place \n Monitor Bureau of Meteorology (BoM) forecasts and warnings online and listen to your local ABC Radio \n If rising waters threaten your home and you decide to move to a safer location, tell the police, your nearest State Emergency Service (SES) unit or your neighbors of your plans to move. \n Monitor your local radio for warnings and advice \n Pack warm clothing, essential medication, valuables and personal papers in waterproof bags along with your emergency kit. \n Raise furniture, clothing and valuables onto beds, tables and into roof space place electrical items in the highest place \n Empty freezers and refrigerators, leaving doors open to avoid damage or loss if they float. \n Turn off power, water and gas and take your mobile phone \n Whether you leave or stay, put sand bags in the toilet bowl and over all laundry/bathroom drain holes to prevent sewage backflow \n Lock your home and take recommended relocation routes for your area \n Do not drive into water of unknown depth and current")

def wildfire():
    print("How to evacuate a building:")
    print("Check if doors handles are hot. If they are, chances are the next room has fire \n Avoid large rooms, as the oxygen will fuel the fire \n Do not use elevators.")
    print("Fire Plan:")
    print("Shut all windows and doors, leaving them unlocked \n Remove flammable window shades, curtains and close metal shutters \n Remove lightweight curtains \n Move flammable furniture to the center of the room, away from windows and doors \n Shut off gas at the meter; turn off pilot lights \n Leave your lights on so firefighters can see your house under smoky conditions \n Shut off the air conditioning")
    print("Outside:")
    print("Gather up flammable items from the exterior of the house and bring them inside (patio furniture, children’s toys, door mats, trash cans, etc.) or place them in your pool \nTurn off propane tanks \n Move propane BBQ appliances away from structures \n Connect garden hoses to outside water valves or spigots for use by firefighters. Fill water buckets and place them around the house \n Don’t leave sprinklers on or water running, they can affect critical water pressure \n Leave exterior lights on so your home is visible to firefighters in the smoke or darkness of night \n Put your Emergency Supply Kit in your vehicle \n Back your car into the driveway with vehicle loaded and all doors and windows closed. Carry your car keys with you \n Have a ladder available and place it at the corner of the house for firefighters to quickly access your roof \n Seal attic and ground vents with pre-cut plywood or commercial seals \n Patrol your property and monitor the fire situation. Don’t wait for an evacuation order if you feel threatened \n Check on neighbors and make sure they are preparing to leave")
    print("Animals:")
    print("Locate your pets and keep them nearby \n Prepare farm animals for transport and think about moving them to a safe location early.")

def yesno(question, yess, nos):
    result = input(question)
    while (not ( result in yess)) and (not (result in nos)):
        result = input(question)

    if result in yess:
        return(True)
    else:
        return(False)


def pets(question, dog, cat, other):
    result = input(question)
    while not((result in dog) or (result in cat) or (result in other)):
        result = input(question)

    if result in dog:
        return("dog")
    elif result in cat:
        return("cat")
    elif result in other:
        return ("other")
    else:
        return(result)

def questionnaire():
    print("Collect these items listed below to prepare beforehand for the natural disaster:")
    print("Water - one gallon of water per person per day for at least three days, for drinking and sanitation")
    print("Food - at least a three-day supply of non-perishable food")
    print("Battery-powered or hand crank radio and a NOAA Weather Radio with tone alert \n Flashlight \n First aid kit")
    print("Extra batteries \n Whistle to signal for help")
    print("Dust mask to help filter contaminated air and plastic sheeting and duct tape to shelter-in-place")
    print(" Moist towelettes, garbage bags and plastic ties for personal sanitation \n Wrench or pliers to turn off utilities")
    print("Manual can opener for food \n Local maps \n Cell phone with chargers and a backup battery")
    print("Please answer the following questionnaire to customize supplies needed.")

    yess = ("yes", "Yes", "Y", "y", "ye", "Ye", "YES", "YE")
    nos  = ("No", "no", "N", "n", "naw")
    dog = ("dog")
    cat = ("cat")
    other = ("other")
    
    if yesno("Do you have an infant?(yes or no)", yess, nos):
        print("Bring: \n diapers \n formula \n other baby necessities.")
    if yesno("Do you have kids in your household under the age of 13?(yes or no)", yess, nos):
        print("Bring: \n games \n snacks.")
    if yesno("Do you take any necessary medicine?(yes or no)", yess, nos):
        meds = input("What medication do you take?")
        print("Bring: \n seven day supply of", meds)
    if yesno("Any additional supplies for your family's special needs?(yes or no)", yess, nos):
        stuff = input("What extra supplies do you think is necessary to bring?")
        print("Bring: \n ", stuff)
    if yesno("Are there any girls/women in your household?(yes or no)", yess, nos):
        print("Bring feminine supplies (ex. tampons, pads, and etc.)")
    if yesno("Do you have a pet?(yes or no)",yess, nos):
        animal = pets("Is your animal a dog, cat, or other?", dog, cat, other)
        if animal == "dog":
            print('Bring: \n dog food \n leash and/or harness \n pet carrier \n extra water \n trash bags')
        elif animal == "cat":
            print ('Bring: \n cat food \n litter box \n pet carrier \n water')
        elif animal == "other":
            other = input("What supplies does your other animal need?")
            print("Bring: \n", other)
        else:
            print("")
    rendezvous = input("Where is your safe rendezvous meeting place?")
    people_string = input("How many people are in your household?")
    while not people_string.isdigit(): 
        people_string = input("How many people are in your household?")
    people = int(people_string)
    print("Bring enough supplies for", people)
    print("Meet at the", rendezvous) 

valid_disaster = ('wildfire', 'flood')
disaster = input("What is your disaster? (wildfire or flood)")
while not disaster in valid_disaster: 
    disaster = input("What is your disaster? (wildfire or flood)")
if disaster == "flood":
    flood()
if disaster == "wildfire":
    wildfire()
firstaid()
questionnaire()
print("And don't forget the can opener!")