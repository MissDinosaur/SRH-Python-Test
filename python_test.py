import numpy as np
import csv
import pandas as pd
import random
random.seed(42)

"""
# Q1: What is the main difference between the list and Tuple?
# A1: Elements in List are mutable while elements in Tuple are immutable. 
"""

"""
# Q2: why should list indexing be used Python?
# A2: Because elements in list are ordered and we need list indexing to slice the list, selecting the elements we need.
"""

"""
Write a function of a name count_car. The function returns a dictionary.
The expected return of the function should print out this dictionary:
    {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]
"""

def generate_dictionary_1():
    car_name = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

    value = [2, 4, 5, 7, 2]
    distinct_car_name = []
    for x in car_name:
        if x not in distinct_car_name:
             distinct_car_name.append(x)
    
    output_dict = {}
    i = 0
    for x in distinct_car_name:
        output_dict[x] =  value[i]
        i+=1
    return output_dict

def double_even_numbers():
    input = np.random.randint(0, 10, 100)
    output = [x**2 for x in input if x%2 == 0]
    output[0] = input[0]
    return output

def read_and_write_func():
    data = pd.read_csv("movies.csv")
    data = data[data["score"] >= 7]
    data = data.iloc[0:2000, :]
    rows = list(data)
    output_file = "dest_csv.csv"
    with open(output_file, mode='w', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerows(rows)

def div_func(input):
    size = len(input)
    output = []
    i = 0
    while size >= 1:
        if size == 1:
            output.append(input[0])
        else:
            if input[size - 2] == 0:
                output.append("NAN")
            else:
                output.append(input[size - 1] / input[size - 2])
            i = i + 1
            size = size -1 
    return output





if __name__ == "__main__":
    #string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
    #           'BMW_720', 'VW_passat']
#
    #value_list = [2, 4, 5, 7, 2]
    #dict_out = generate_dictionary(string_list, value_list)
    #for x in dict_out:
    #    print(f"{x}, {dict_out[x]}")
        
    short_list = [1, 0, 2, 2, 20]
    long_list = [random.randrange(0, 10, 1) for i in range(15)]

    output = div_func(short_list)
    for x in output:
        print(x)
    print("I'm a module")