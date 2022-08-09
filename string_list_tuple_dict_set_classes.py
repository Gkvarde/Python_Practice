#***************************************
#*           String Class             **
#***************************************


# Try to extract data from index one to index 300 with a jump of 3
# Try to reverse a string without using reverse function
# Try to split a string after conversion of entire string in uppercase
# Try to convert the whole string into lower case
# Try to capitalize the whole string
# Try to give an example of expand tab
# Give an example of strip, lstrip and rstrip
# Replace a string character by another character by taking your own example
# String center function with an example
# Try to filter out all the string data
# Try to Find  out alphanum in data

import logging
logging.basicConfig(filename="string_list_tuple_dict_set_classes.txt", level=logging.DEBUG,
                    format='%(asctime)s || %(name)s || %(levelname)s || %(message)s')

class string_s():

    def in_dex(self, s):
        try:
            result = s[0:300:3]
            logging.info("The original string is: %s", s)
            logging.info("The result from index one to index 300 with a jump of 3 of the string is: %s", result)
        except Exception as e:
            logging.exception(e)

    def reverse_s(self, s):
        try:
            result = s[::-1]
            logging.info("The original string is: %s", s)
            logging.info("The result of reversed string is: %s", result)
        except Exception as e:
            logging.exception(e)

    def split_up(self, s):
        try:
            result = s.upper().split()
            logging.info("The original string is: %s", s)
            logging.info("The result of splitting a string after conversion in uppercase is: %s", result)
        except Exception as e:
            logging.exception(e)

    def lower_case(self, s):
        try:
            result = s.lower()
            logging.info("The original string is: %s", s)
            logging.info("The result of lower case of the string is: %s", result)
        except Exception as e:
            logging.exception(e)

    def capitalization(self, s):
        try:
            result = s.capitalize()
            logging.info("The original string is: %s", s)
            logging.info("The result of capitalization of the string is: %s", result)
        except Exception as e:
            logging.exception(e)

    def expand_tab(self, s):
        try:
            result = s.expandtabs()
            logging.info("The original string is: %s", s)
            logging.info("The result of expand tab is: %s", result)
        except Exception as e:
            logging.exception(e)

    def all_strips(self, s):
        try:
            result_strip = s.strip('-')
            result_lstrip = s.lstrip('-')
            result_rstrip = s.rstrip('-')
            logging.info("The original string is: %s", s)
            logging.info("The result of strip of the string is: %s", result_strip)
            logging.info("The result of left strip of the string is: %s", result_lstrip)
            logging.info("The result of right strip of the string is: %s", result_rstrip)
        except Exception as e:
            logging.exception(e)

    def replace_char(self, s):
        try:
            result = s.replace('AI/ML','DS')
            logging.info("The original string is: %s", s)
            logging.info("The result of replace method is: %s", result)
        except Exception as e:
            logging.exception(e)

    def string_center(self, s):
        try:
            result = s.center(30, '*')
            logging.info("The original string is: %s", s)
            logging.info("The result of string center is: %s", result)
        except Exception as e:
            logging.exception(e)

    def extract_string(self, l):
        try:
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            logging.info("Extraction of string from the data: %s", j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str:
                            logging.info("Extraction of string from the data: %s", k)
                        if type(v) == str:
                            logging.info("Extraction of string from the data: %s", v)
        except Exception as e:
            logging.exception(e)

    def al_num(self, l):
        try:
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            if j.isalnum():
                                logging.info("Extrection of alpha-numeric from data: %s", j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str:
                            if k.isalnum():
                                logging.info("Extrection of alpha-numeric from data: %s", k)
                        if type(v) == str:
                            if v.isalnum():
                                logging.info("Extrection of alpha-numeric from data: %s", v)
        except Exception as e:
            logging.exception(e)




s = "this is My First Python programming class and i am learNING python string and its function"
s1 = "AI\tML\tis\tthe\tfuture"
s2 = "-----AI/ML is the future-----"
s3 = "AI/ML is the future"
s4 = "Data is the new oil"
strings = string_s()
strings.in_dex(s)
strings.reverse_s(s)
strings.split_up(s)
strings.lower_case(s)
strings.capitalization(s)
strings.expand_tab(s1)
strings.all_strips(s2)
strings.replace_char(s3)
strings.string_center(s4)

l5 = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
      {'k1' :"AI" , "k2" : "machine learning","k3": "maths" , 3:6 , 7:8} , ["machine learning", "data science"]]
strings.extract_string(l5)
strings.al_num(l5)

#***************************************
#*           List Class               **
#***************************************

#Try to reverse a list l
#Try to access 234 out of this list l
#Try to access 456 from list l
#Try to extract only a list collection form list l
#Try to extract all the list entity from l1 list
#Try to extract all the numerical data it may be a part of dict key and values from list l1
#Try to unwrape all the collection inside collection from l1 and create a flat list
#Try to filter out all the odd values out all numeric data which is a part of a list l1
#Try to find out multiplication of all numeric value inside list from list l1

class list_l():

    def reverse_list(self, l):
        try:
            result = l[::-1]
            logging.info("The original list is: %s", l)
            logging.info("The result of reverse list method is: %s", result)
        except Exception as e:
            logging.exception(e)

    def access_234(self, l):
        try:
            result1 = l[7][0]
            result2 = list(l[8].keys())[1]
            logging.info("The original list is: %s", l)
            logging.info("234 has been accessed from list of main list: %s", result1)
            logging.info("234 has been accessed from dictionary of main list: %s", result2)
        except Exception as e:
            logging.exception(e)

    def access_456(self, l):
        try:
            result = l[5][1]
            logging.info("The original list is: %s", l)
            logging.info("456 has been accessed from list of main list: %s", result)
        except Exception as e:
            logging.exception(e)

    def list_collection(self, l):
        try:
            result = l[5:7]
            logging.info("The original list is: %s", l)
            logging.info("List collection fetched from main list: %s", result)
        except Exception as e:
            logging.exception(e)

    def list_entities(self,l):
        try:
            logging.info("The original list is: %s", l)
            for i in l:
                if type(i) == list:
                    logging.info("List entities from main list: %s", i)
        except Exception as e:
            logging.exception(e)

    def number_entities_list(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            list_of_numbers.append(j)
            logging.info("List of all numbers, part of lists: %s", list_of_numbers)
        except Exception as e:
            logging.exception(e)

    def sum_list(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            list_of_numbers.append(j)
            sum_ = sum(list_of_numbers)
            logging.info("Sum of all numbers, part of list: %s", sum_)
        except Exception as e:
                logging.exception(e)

    def unwrapped_all(self, l):
        try:
            list_of_all = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        list_of_all.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        list_of_all.append(k)
                        list_of_all.append(v)
            logging.info("Unwrapped all collections from main list: %s", list_of_all)
        except Exception as e:
            logging.exception(e)


    def odd_values(self, l):
        try:
            list_all_int = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            list_all_int.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                list_all_int.append(g)
            list_of_odd = []
            for i in list_all_int:
                if i % 2 == 0:
                    pass
                else:
                    list_of_odd.append(i)
            logging.info("Odd values of all numeric data: %s", list_of_odd)
        except Exception as e:
            logging.exception(e)

    def mul_list(self, l):
        try:
            for i in l:
                m = 1
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            m = m * j
                    logging.info("Multiplication of all values inside list: %s", m)
        except Exception as e:
            logging.exception(e)




l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) ,
     {"key1" :"data science" , 234:[23,45,656]}]
list_var = list_l()
list_var.reverse_list(l)
list_var.access_234(l)
list_var.access_456(l)
list_var.list_collection(l)


l1 = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
      {'k1' :"AI" , "k2" : "machine learning","k3": "maths" , 3:6 , 7:8} , ["machine learning", "data science"]]
list_var.list_entities(l1)
list_var.number_entities_list(l1)
list_var.sum_list(l1)
list_var.unwrapped_all(l1)
list_var.odd_values(l1)
list_var.mul_list(l1)

#***************************************
#*           Dictionary Class         **
#***************************************

#Try to extract "data science" from list l
#Try to list all the key in dict element available in list l
#Try to extract all the value element form dict available in list l
#Try to extract all the dict entities from list l2
#Try to extract all the numerical data it may be a part of dict key and values from list l2
#Try to find out multiplication of all numeric value inside dictionary from list l2

class dict_class():

    def extract_string(self, l):
        try:
            logging.info("The original list is: %s", l)
            result = l[8]['key1']
            logging.info("'data science' extracted from dictionary of main list: %s", result)
        except Exception as e:
            logging.exception(e)

    def list_of_keys(self, l):
        try:
            logging.info("The original list is: %s", l)
            result = list(l[8].keys())
            logging.info("List of all keys extracted from dictionary of main list: %s", result)
        except Exception as e:
            logging.exception(e)

    def list_of_values(self, l):
        try:
            logging.info("The original list is: %s", l)
            result = list(l[8].values())
            logging.info("List of all value elements available in dictionary of main list: %s", result)
        except Exception as e:
            logging.exception(e)


    def dict_entities(self, l):
        try:
            logging.info("The original list is: %s", l)
            for i in l:
                if type(i) == dict:
                    logging.info("Dictionaries from main list: %s", i)
        except Exception as e:
            logging.exception(e)

    def number_entities_dict(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            list_of_numbers.append(k)
                            list_of_numbers.append(v)
            logging.info("List of all numbers, part of key value pairs from dictionary: %s", list_of_numbers)
        except Exception as e:
            logging.exception(e)

    def sum_dict(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            list_of_numbers.append(k)
                            list_of_numbers.append(v)
            sum_ = sum(list_of_numbers)
            logging.info("Sum of all numbers, part of key value pairs from dictionary: %s", sum_)
        except Exception as e:
                logging.exception(e)

    def mul_dict(self, l):
        try:
            for i in l:
                m = 1
                if type(i) == dict:
                    for k in i.items():
                        for n in k:
                            if type(n) == int:
                                m = m * n
                    logging.info("Multiplication of all values inside dictionary: %s", m)
        except Exception as e:
            logging.exception(e)



dict_var = dict_class()

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) ,
     {"key1" :"data science" , 234:[23,45,656]}]

dict_var.extract_string(l)
dict_var.list_of_keys(l)
dict_var.list_of_values(l)



l2 = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
      {'k1' :"AI" , "k2" : "machine learning","k3": "maths" , 3:6 , 7:8} , ["machine learning", "data science"]]

dict_var.dict_entities(l2)
dict_var.number_entities_dict(l2)
dict_var.sum_dict(l2)
dict_var.mul_dict(l2)

#***************************************
#*           Tuple Class              **
#***************************************

#Try to extract all the tuples entities
#Try to extract all the numerical data it may be a part of dict key and values from list l3
#Try to find out multiplication of all numeric value inside tuples from list l3

class tuple_class():

    def tuple_entities(self, l):
        try:
            logging.info("The original list is: %s", l)
            for i in l:
                if type(i) == tuple:
                    logging.info("Tuples from main list: %s", i)
        except Exception as e:
            logging.exception(e)

    def number_entities_tuple(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            list_of_numbers.append(j)
            logging.info("List of all numbers, part of tuples: %s", list_of_numbers)
        except Exception as e:
            logging.exception(e)

    def sum_tuple(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            list_of_numbers.append(j)
            sum_ = sum(list_of_numbers)
            logging.info("Sum of all numbers, part of tuple: %s", sum_)
        except Exception as e:
                logging.exception(e)

    def mul_tuple(self, l):
        try:
            for i in l:
                m = 1
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            m = m * j
                    logging.info("Multiplication of all values inside tuple: %s", m)
        except Exception as e:
            logging.exception(e)



l3 = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]) ,
      {'k1' :"AI" , "k2" : "machine learning","k3": "maths" , 3:6 , 7:8} , ["machine learning", "data science"]]

tuple_var = tuple_class()
tuple_var.tuple_entities(l3)
tuple_var.number_entities_tuple(l3)
tuple_var.sum_tuple(l3)
tuple_var.mul_tuple(l3)

#***************************************
#*           Set Class                **
#***************************************

#Try to extract all the numerical data it may be a part of dict key and values from list l4
#Try to find out multiplication of all numeric value inside set from list l4
#Try to extract "machine learning" out of this data
#Try to find out a number of occurances of all the data

class set_class():

    def number_entities_set(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            list_of_numbers.append(j)
            logging.info("List of all numbers, part of set: %s", list_of_numbers)
        except Exception as e:
                logging.exception(e)

    def sum_set(self, l):
        try:
            logging.info("The original list is: %s", l)
            list_of_numbers = []
            for i in l:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            list_of_numbers.append(j)
            sum_ = sum(list_of_numbers)
            logging.info("Sum of all numbers, part of set: %s", sum_)
        except Exception as e:
            logging.exception(e)

    def mul_set(self, l):
        try:
            for i in l:
                m = 1
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            m = m * j
                    logging.info("Multiplication of all values inside set: %s", m)
        except Exception as e:
            logging.exception(e)

    def extract_txt(self, l):
        try:
            list_txt = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == "machine learning":
                            list_txt.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == "machine learning":
                                list_txt.append(g)
            logging.info("Extraction of 'machine learning' from the data: %s", list_txt)
        except Exception as e:
            logging.exception(e)

    def occurances(self, l):
        try:
            l2 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l2.append(j)

                if type(i) == dict:
                    for k, v in i.items():
                        l2.append(k)
                        l2.append(v)
            s = set(l2)
            for i in set(l2):
                logging.info("Number of occurances for each element: %s", (i, l2.count(i)))
        except Exception as e:
            logging.exception(e)



l4 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
      {'k1': "AI", "k2": "machine learning", "k3": "maths", 3: 6, 7: 8}, ["machine learning", "data science"]]
set_var = set_class()
set_var.number_entities_set(l4)
set_var.sum_set(l4)
set_var.mul_set(l4)
set_var.extract_txt(l4)
set_var.occurances(l4)