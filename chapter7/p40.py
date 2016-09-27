#/usr/bin/env python

import sys

dic = { 0:{'first_name':'Jonn', 'Last_name':'Johnson', 'position':'Manager', 'separation_date':'2016-12-31'}, \
        1:{'first_name':'Tou', 'Last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-15'}, \
        2:{'first_name':'Michaela', 'Last_name':'Michaelson', 'position':'District Manager', 'separation_date':'2015-12-19'}, \
        3:{'first_name':'Jake', 'Last_name':'Jacobson', 'position':'Programmer', 'separation_date':''}, \
        4:{'first_name':'Jacquelyn', 'Last_name':'Jackson', 'position':'DBA', 'separation_date':''}, \
        5:{'first_name':'sally', 'Last_name':'Weber', 'position':'Web Developer', 'separation_date':'2015-12-18'} 
        }

tuple_em = { 0:('Jonn', 'Johnson','Manager', '2016-12-31'), \
        1:('Tou', 'Xiong', 'Software Engineer', '2016-10-15'), \
        2:('Michaela', 'Michaelson', 'District Manager', '2015-12-19'), \
        3:('Jake', 'Jacobson', 'Programmer', ''), \
        4:('Jacquelyn', 'Jackson', 'DBA', ''), \
        5:('sally', 'Weber', 'Web Developer', '2015-12-18') 
        }

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def print_recode(data_list):
    print("Name\t\t\t|Position\t\t|Separation Date")
    print("--------------------------------------------------------")
    for info in data_list:
        if (len(info[0]) + len(info[1]) ) > 15:
            if sys.version_info > (3,0):
                print("%s %s \t|\r" % (info[0], info[1]))
            else:
                print("%s %s \t|" % (info[0], info[1])),
        else:
            if sys.version_info > (3,0):
                print("%s %s \t\t|\r" % (info[0], info[1]))
            else:
                print("%s %s \t\t|" % (info[0], info[1])),
        
        if len(info[2]) <= 5 and len(info[2]) > 0:
            print("%s\t\t\t|%s" % (info[2], info[3]))
        elif len(info[2]) > 5 and len(info[2]) <= 13:
            print("%s\t\t|%s" % (info[2], info[3]))
        else:
            print("%s\t|%s" % (info[2], info[3]))


if __name__ == "__main__":
    search_str = version_input("Enter a search string: ")
    employees_list=[]
    for key in tuple_em:
        if tuple_em[key][0].find(search_str) == 0 or tuple_em[key][1].find(search_str) == 0:
            map(employees_list.append(tuple_em[key]), tuple_em[key])
    
    print_recode(employees_list)
