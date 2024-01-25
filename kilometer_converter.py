"""we want to convert miles into kilometers and print the result"""

### Constants
FACTOR = 1.609344  #this is the factor
                   #to calculate kilometers from miles

### Variables
miles = 500
miles_2 = 600

### code
kilometers = miles * FACTOR #calculate the kilometers
print(kilometers)

kilometers_2 = miles_2 * FACTOR #calculate the kilometers 2
print(kilometers_2)
