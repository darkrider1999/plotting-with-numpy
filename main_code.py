# code.py
# A terminal-based application to process and plot data based on given user input and provided csv files.

#importing all the python libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.lib.shape_base import row_stack

#Creates an user-defined class.
class Country:
    """A class used to create a School object.

        Attributes:
            country (str): String that represents the school's name
            un_region (str): String that represents the country's UN region
            sub_reg (str): String that represents the country's UN sub-region
            sqkm (str): String that representsthe country's area in square kilometers
    """

    def __init__(self, country, un_region, sub_reg, sqkm):
        self.country = country 
        self.un_region = un_region
        self.sub_reg = sub_reg
        self.sqkm = sqkm

    def print_all_stats(self):
        """A function that prints the country's UN Region, UN Sub-Region, and area.

        Parameters: None
        Return: None

        """
        print("UN Region: {0}\nUN Sub-Region: {1}\nCountry Area: {2} ".format(self.un_region, self.sub_reg, self.sqkm))



#validates if user input is inside the csv
def validation(user_input, list):
    if user_input in list:
        return True
    else:
        return False

#validates if user input is inside the csv
def number_validation(user_input, list):
    if user_input in list:
        return True
    else:
        return False


#main function
def main():
    
    #importing data from csv files
    country_data = pd.read_csv('Country_Data.csv')
    population = pd.read_csv('Population_Data.csv')
    species = pd.read_csv('Threatened_Species.csv')

    #putting pandas data into an array
    data_query_country = country_data.to_numpy().tolist()
    data_query_population = population.to_numpy().tolist()
    data_query_species = species.to_numpy().tolist()
    country_csv_array = country_data.to_numpy()
    population_csv_array = population.to_numpy()
    species_csv_array = species.to_numpy()
    #print(data_query_population)

    #lists for the all user_defined variables
    country_list = list(country_csv_array[:,0])
    numbers_list = [1,2,3,0]

    #print(population_csv_array)
    print('Welcome. Please select one of the countries below to analyze.')
    print(country_list)
    user_input = input('Enter a country or enter \'quit\' to quit program: ')

    #generates data from user input
    while user_input != 'quit':
        if validation(user_input, country_list) != True:
            print('Country is not in data. Please enter another country.')
            user_input = input('Enter a country or enter \'quit\' to quit program: ')
        else:
            position = country_list.index(user_input)
            user_country = Country(user_input, country_csv_array[position][1], country_csv_array[position][2], country_csv_array[position][3])
            user_country.print_all_stats()
            while True:
                selection = int(input('Select an action: 1 - view max/min/mean of population, 2 - view population change over time, 3 - access endangered species info: , 0 - Return to the main menu: '))
                if number_validation(selection, numbers_list) == True:
                #if user wants to receive country data

                    if selection == 1:
                        mean_population_2010 = 0
                        mean_population_2020 = 0
                        highest_population = 0
                        lowest_population = 0

                        for i in range(len(data_query_population)):
                            if user_input == data_query_population[i][0]:
                                mean_population_2010 += (data_query_population[i][1] + data_query_population[i][2] + data_query_population[i][3] + data_query_population[i][4] + data_query_population[i][5] + data_query_population[i][6] + data_query_population[i][7] + data_query_population[i][8] + data_query_population[i][9] + data_query_population[i][10] + data_query_population[i][11]) / 11
                        for i in range(len(data_query_population)):
                            if user_input == data_query_population[i][0]:
                                mean_population_2020 += (data_query_population[i][12] + data_query_population[i][13] + data_query_population[i][14] + data_query_population[i][15] + data_query_population[i][16] + data_query_population[i][17] + data_query_population[i][18] + data_query_population[i][19] + data_query_population[i][20] + data_query_population[i][21]) / 10
                
                        pop_years_list = list(range(2000, 2021))
                        imported_population_list = list(population_csv_array[position])
                        population_list = imported_population_list[1:]
                        highest_population = max(population_list)
                        highest_pop_pos = population_list.index(highest_population)
                        highest_pop_year = pop_years_list[highest_pop_pos]
                        lowest_population = min(population_list)
                        lowest_pop_pos = population_list.index(lowest_population)
                        lowest_pop_year = pop_years_list[lowest_pop_pos]

                        print("Highest population in country:", (highest_population), "in the year", highest_pop_year)
                        print("Lowest population in country:", (lowest_population), "in the year", lowest_pop_year)
                        print('Mean Population From 2000-2010: ' ,int(mean_population_2010))
                        print('Mean Population From 2011-2020: ' ,int(mean_population_2020))

                    #if user wants to get population graph
                    elif selection == 2:
                        imported_population_list = list(population_csv_array[position])
                        population_list = imported_population_list[1:]
                        years = list(range(2000, 2021))
                        plt.plot(years, population_list, 'b')
                        plt.xticks([2000, 2005, 2010, 2015, 2021])
                        plt.title("Country Population by Year")
                        plt.xlabel("Year")
                        plt.ylabel("Population")
                        plt.show()

                    #if user wants to receive species data and graph.
                    elif selection == 3:
                        imported_species_list = list(species_csv_array[position])
                        species_list = imported_species_list[1:]
                        overall_total = np.sum(species_list)
                        
                        species_list1 = list(species_csv_array[:,0])
                        position2 = species_list1.index(user_input)
                        plants = species_csv_array[position2][1]
                        fish = species_csv_array[position2][2]
                        birds = species_csv_array[position2][3]
                        animals = species_csv_array[position2][4]
                        total_species_plants = np.sum(species_csv_array[:,1],axis=0)
                        total_species_fish = np.sum(species_csv_array[:,2],axis=0)
                        total_species_birds = np.sum(species_csv_array[:,3],axis=0)
                        total_species_animals = np.sum(species_csv_array[:,4],axis=0)
                        print("Total Threatened Species in", user_input, "are", overall_total, "\nPlants:", plants, ", Fishes:", fish, ", Birds:", birds,", Mammals:", animals)
                        print("Total Number of Threatened Species In The World: ""Plants:", total_species_plants, ", Fishes:", total_species_fish, ", Birds:", total_species_birds,", Mammals:", total_species_animals)
                        families = ['Plants', 'Fish', 'Birds', 'Animals'] 
                        imported_species_list = list(species_csv_array[position])
                        species_list = imported_species_list[1:]
            
                        plt.subplot(2, 1, 1)
                        plt.bar(families, species_list)
                        plt.title("Total Number of Threatened Species")
                        plt.subplot(2,1,2)
                        plt.pie(species_list, labels = families)
                        plt.show()

                    elif selection == 0:
                        break

                
            user_input = input('Enter a country or enter \'quit\' to quit program: ')

    print('Thank you for using our program.')


if __name__ == '__main__':
    main()
