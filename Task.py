#1 List operations

# Create a list myNumbers with following elements [54,88,72,73,83,889,883,2284]:
myNumbers = [54,88,72,73,83,889,883,2284,0]
# print(myNumbers[2])

# function to check given number is prime or not
def check_prime(n):
    if n>1:
        for i in range(2, n):
            if (n % 2) == 0:
                return False
            else:
                return True
    else:
        return False
                
PrimeList = list(filter(check_prime,myNumbers))
print(PrimeList)

#2 Dictionary operations

# defining empty dictionary                                                 
# Capitals = {}   

# adding entries to dictionary 
# Capitals["Maharastra"] = "Mumbai"
# Capitals["Madhya_Pradesh"] = "Bhopal"
# Capitals["Uttar_Pradesh"] = "Lucknow"
# Capitals["Tamil_Nadu"] = "Chennai"

# print(Capitals)


# states list by extracting keys from Capitals dictionary
# States = []
# for keys in Capitals.keys():
#     States.append(keys)
# print(States)    
    

# # function to get capital by taking state as input
# def get_Capital(State):
#         if State in Capitals.keys():
#             print(Capitals[State])
#         else:
#             print("INVALID STATE")    
            
# get_Capital('maharastra')


#3 SET operations

# A = {44,4,5,6,77,855,445,667}
# B = {77,667,66,454,445,9902,560,235}
 

# # # common elements between set A and set B
# print(A.intersection(B))

# # # elements present between set A but not in set B
# print(A.difference(B))

# # # elements present in set A and set B
# print(A.union(B))










