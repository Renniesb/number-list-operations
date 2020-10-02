def main():
    #Rennie Bevineau
    
    values = [1,2,3]

    for i in range(3): #iterates a key so we can get each value within the array
        values[i] = int(input("Please provide a number[%1.0f]"%i))

    total = sum(values)
    average = total/len(values)

    product = 1
    for i in range(3): #iterates a key so we can multiply each value within the array
        product = product * values[i]

    largest_number = max(values)
    smallest_number = min(values)

    print("\nSum is:",
          total,
          "\nAverage is: %.2f"%average,
          "\nProduct is:",
          product,
          "\nLargest Number is:",largest_number,
          "\nSmallest Number is:", smallest_number)    

main()

    
    
