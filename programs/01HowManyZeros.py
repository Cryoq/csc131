from time import time

class counting:
    # Initializes the target number
    def __init__(self,target):
        self.target = target
        
    # Calculates the number of zeros for a single number
    def singleNumZeros(self, a):
        while a > 1:
            if a % 10 == 0:
                self.numOfZeroes += 1
            a = int(a / 10)
    
    # Calculates the zeroes of all number from 1 to the target number.
    def calculateZeros(self):
        
        # Starts the time (uses self so it can be used in the getTime function)
        self.startTime = time()
        self.numOfZeroes = 0

        # Loops through all numbers from 1 to target number through the singleNumZeros function
        for i in range(1, self.target + 1):
            self.singleNumZeros(i)

        # Stops the time
        self.endTime = time()
    
    # Gets the time elapsed for the algorithm
    def getTimeElapsed(self):
        return self.endTime - self.startTime
            
# ----------Main----------

# Gets user input
numberInput = int(input("What number do you want to count zeros to? "))
zero = counting(numberInput)

#Runs the number of zeros algorithm
zero.calculateZeros()

# Outputs the number of zeros found and the time elapsed for the algorithm
print(f"The number of zeros written from 1 to {numberInput} is {zero.numOfZeroes}.")
print(f"This took {zero.getTimeElapsed()} seconds.")
