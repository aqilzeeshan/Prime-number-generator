
max = int(input("enter a number above 1 "))

def check(unchecked,max):
    decider = False
    for i in range(2,unchecked-1):
        if unchecked%i == 0:
            decider = True
            
    if decider == True:
        return(f"{unchecked} is not prime")
    else:
        return(f"{unchecked} is prime")


if max > 1:
    
  for i in range(2,max+1):
      print(check(i,max))
    
      

