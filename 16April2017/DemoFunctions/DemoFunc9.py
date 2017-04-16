def fayyaz(type,noOfSugarSpoon=0):
    """This funtion is to prepare Tea"""
    if noOfSugarSpoon >0:
        print("Preparing "+type +" with "+str(noOfSugarSpoon) +" spoon of Sugar")
    else:
        print("Preparing " + type + " without Sugar")
    print("cleaning cups")
    print("filling cups")
    return type+" Hazir Hai"

myCup = fayyaz("Tea",2)



