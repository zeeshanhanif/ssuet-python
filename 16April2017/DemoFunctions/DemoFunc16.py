def fayyaz(*listOfFoodItems):
    """This funtion is to prepare Tea"""
    #Modificaiton in tuple is not allowed
    #listOfFoodItems[1]="Roll"
    for food in listOfFoodItems:
        print("Purchaing " + str(food) + " from Market");


fayyaz("Biryani", "Keema", "Sendwich", "Nihari",500,2.5)





