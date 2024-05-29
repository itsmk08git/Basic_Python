"""
    ->Adding, Removing, Displaying & Querying the data of Dictionary.
"""
population = {
    "China" : 143,
    "India" : 136,
    "USA" : 32,
    "Pakistan" : 21
}
def print_all():
    for country, x in population.items():
        print(f"{country}==>{x}")
def add():
    country=input("Enter the name you want to add:")
    country=country.lower()
    if country in (x.lower() for x in population):
        print(f"Country Already exist in the database.")
        return
    p = input(f"Enter the Population for {country}:")
    population[country] = p
    print_all()

def remove():
    country=input("Enter the Country you want to remove:")
    lower_country=country.lower()

    if lower_country in (x.lower() for x in population):
        for country, popu in population.items():
            del population[country]
            print(f"{country} is removed.")
            print_all()
            return
    print(f"{country} doesn't exist in the database.")

def query():
    country=input("Enter the Country name:")
    low_country=country.lower()
    if low_country in (x.lower() for x in population):
        for country, popu in population.items() :
            print(f"The Population of {country} is {population[country]}.")
            return
    print("Country do not exist in the database.")


def main():
    user_input =input("Enter any one input(print/add/remove or query):")
    if user_input.lower() == "print" :
        print_all()
    elif user_input.lower() == "add" :
        add()
    elif user_input.lower() == "remove" :
        remove()
    elif user_input.lower() == "query" :
        query()

if  __name__ == '__main__' :
    main()