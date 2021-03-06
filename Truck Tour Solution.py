"""
Problem Description: 
Suppose there is a circle. 
There are N petrol pumps on that circle. 
Petrol pumps are numbered 0 to N-1 (both inclusive). 
You have two pieces of information corresponding to each of the petrol pump: 
(1) the amount of petrol that particular petrol pump will give, and 
(2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol.
You can start the tour at any of the petrol pumps. Calculate the first point from
where the truck will be able to complete the circle. Consider that the truck will 
stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
Description: 
The function receives a matrix type list, where in the first column is the gasoline provided by 
the gas station and in the second column is the distance between that gas station and the following one.
It returns a int with position for the starting point that wil allow to complete the cycle. 
"""
def truckTour(petrolpumps):
    for i in range(len(petrolpumps)):
        if petrolpumps[i][0]>=petrolpumps[i][1]: #This makes the first comparison, if the gas quantity is bigger/equal than the distance to the next station it will proceed
            j = (i+1)%len(petrolpumps) #Since we need to complete the cicle, the module sum is ued to avoid out of lenght pointing. 
            gas = petrolpumps[i][0] - petrolpumps[i][1] #Here we save the reamining gas after arriving to the next station. 
            while j != i:
                if  gas+ petrolpumps[j][0] < petrolpumps[j][1]: #This compares if the gas that have in addition to the provided if enough to arrivo to next station.
                    break
                else: 
                    gas = gas -petrolpumps[j][1] + petrolpumps[j][0] #Here we save, again, the remaining gas. and them we move to the following station till we 
                    j+=1                                             # Complete the cycle. 
                    j%= len(petrolpumps)
            if j== i:
                    return i
