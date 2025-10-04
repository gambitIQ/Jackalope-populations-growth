#Jackalope Populations by Zamambo Y Mkhize
    
repeat = "y"
while repeat != 'n':        #condition for repeat
        #get population and generation counts
        population = int(input("\nHow many Jackalopes do you have? "))
        generations = int(input("How many generations do you want to wait? "))
        population_new = population
        
        
        for i in range (generations):  # loop for the number of generations
            #births and mortality 
            births = round(population_new*0.1)
            deaths = round((population_new + births)*(0.02)) 
            population_growth = (births - deaths)
            population_new = population_new + population_growth
        
      
        #expected output 
        print(f"If you start with {population} jackalopes and wait {generations} generations")
        print(f"you'll end up with a total of {population_new} of them.")
        repeat = input("\nDo you want to calculate another population? (y/n) ")

'''Sample Output:

How many Jackalopes do you have? 200
How many generations do you want to wait? 1
If you start with 200 jackalopes and wait 1 generations
you'll end up with a total of 216 of them.

Do you want to calculate another population? (y/n) y

How many Jackalopes do you have? 132
How many generations do you want to wait? 2
If you start with 132 jackalopes and wait 2 generations
you'll end up with a total of 153 of them.

Do you want to calculate another population? (y/n) y

How many Jackalopes do you have? 100
How many generations do you want to wait? 10
If you start with 100 jackalopes and wait 10 generations
you'll end up with a total of 214 of them. '''
