def fayyaz(*listOfFoodItems,mobileCard):
    """This funtion is to prepare Tea"""
    #Modificaiton in tuple is not allowed
    #listOfFoodItems[1]="Roll"
    print("Mobile Card value "+ str(mobileCard))
    for food in listOfFoodItems:
        print("Purchaing " + str(food) + " from Market");


# Will give error of multiple value
#fayyaz("Biryani", "Keema", "Sendwich", "Nihari",mobileCard=500)
fayyaz("Biryani", "Keema", "Sendwich", "Nihari",mobileCard=500)





