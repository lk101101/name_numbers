import os
import csv
import random
import matplotlib.pyplot as plt

class NameReader():
    def __init__(self, filename, name, gender):
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.full_path = os.path.join(self.base_path, filename)
        self.file_obj = open(self.full_path, 'r')
        self.raw_data = self.file_obj.readlines()
        self.file_obj.close()

        self.name = name
        self.gender = gender

    # iterate through list
    # if specified name matches a name from the list, return its ranking
    def ranking_of_name(self):
        for i in self.raw_data:
            separated = i.split(',')
            if separated[1].lower() == self.gender.lower() and separated[0].lower() == self.name.lower():
                return separated[2].strip('\n')

# create line graph to display change in ranking of name over time
def viz(year_list, rank_list, name, year):
    # change color of line here 
    plt.plot(year_list, rank_list, color = 'deepskyblue', marker = 'o')
    plt.ylabel('Popularity')
    plt.xlabel('Years')
    plt.title('Popularity of Name {} from {} to 2020'.format(name.upper(), year))
    
    # add ranking labels to points on graph
    for x, y in zip(year_list, rank_list):
        plt.annotate(y, (x,y))   
    plt.grid(True)
    plt.show()

def main():
    answer = input("Select an option: r to return a random name or p to return the popularity ranking of a name: ")

    if answer.lower() == 'p':
        name, gender, year = input("Find out how many babies are named a certain name in a specific year. Format as 'name gender (m/f) year': ").split()

        current_file = 'yob2020.txt'
        past_file = 'yob' + year + '.txt'

        full_gender = ""
        if (gender.lower() == 'f'):
            full_gender = "girls'"
        else:
            full_gender = "boys'"
    
        # create instances of NameReader class
        current_name = NameReader(current_file, name, gender)
        past_name = NameReader(past_file, name, gender)
    
        # get ranks from current and specified year
        cur_rank = current_name.ranking_of_name()
        past_rank = past_name.ranking_of_name()

        print("The {} name {} was used {} times in 2020 and {} times in {}".format(full_gender, name.upper(), cur_rank, past_rank, year))

        # visualization code

        years = []
        ranks = []
        # gather the ranks for each year between the specified and current year
        for i in range(int(year), 2021):
            years.append(str(i))
            new_file = 'yob' + str(i) + '.txt'
            new_name = NameReader(new_file, name, gender)
            new_rank = new_name.ranking_of_name()

        # if name isn't in file, use 0 as rank
        if (new_rank == None):
            ranks.append(0)
        else:
            ranks.append(int(new_rank))

        viz(years, ranks, name, year)

    # random name generator
    else:
        # TO DO: 
            # implement way to specify gender and rank

        # get random year + file
        year = random.randrange(1880, 2020)
        file_name = 'yob' + str(year) + '.txt'

        # get random line
        line = random.choice(open(file_name).readlines())
        # split line into words
        line = line.split(',')

        # print year + name
        print(str(year) + " : " + line[0])
    
if __name__ == '__main__':
    main()