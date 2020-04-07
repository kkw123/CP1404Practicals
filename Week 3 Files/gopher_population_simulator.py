"""
CP1404 Practicals

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""
import random


def main():
    population = 1000
    max_year = 10
    current_year = 1
    min_birth_rate = 0.1
    max_birth_rate = 0.2
    min_death_rate = 0.05
    max_death_rate = 0.25
    print('Welcome to the Gopher Population Simulator!\nStarting population: {}\n'.format(population))
    while current_year < max_year + 1:
        births = calculate_births(min_birth_rate,max_birth_rate,population)
        deaths = calculate_deaths(min_death_rate,max_death_rate,population)
        population += births
        population -= deaths
        print('Year {}'.format(current_year))
        print('*****')
        print('{} gophers were born. {} died'.format(births,deaths))
        print('Population: {}\n'.format(population))
        current_year += 1


def calculate_births(min, max, population):
    birth_rate = random.uniform(min, max)
    births = population * birth_rate
    return int(births)

def calculate_deaths(min, max, population):
    death_rate = random.uniform(min,max)
    deaths = population * death_rate
    return int(deaths)

main()