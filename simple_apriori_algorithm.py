import itertools

# Accept input from the user and add it to a dictionary
def get_input():
    '''
    This will accept the number of records and the elements in each record
    
    Returns:
    --------
    A dictionary that holds the elements that the algorithm will be applied on
    
    '''
    dic={}
    n=int(input('Number of Records: '))
    #s=int(input('Sup: '))
    for i in range(n):
        key=input('ID=> ')
        value=input('Values=> ')
        dic[key]=value.replace(' ','')
    return dic    



# Extract the unique elements from the input that the user added
def create_unique_items(dic):
    '''
    This will extract the unique elements from all the elements that the user entered
    
    Args:
    ------
    dic: A dictionary containing the elments that the user entered with its ids (keys)
    
    Returns:
    -------
    All the unique sorted elements 
    
    '''
    items=''
    for k,v in dic.items():
        items+=v
    items=set(items) 
    items=list(items)
    return sorted(items)



# change the data type of dictionary values to be tuples
def change_type_dic(dic):
    '''
    change the dictionary values to be as a tuple data type
    
    Args:
    -------
    the dictionary that contains the original elements
    
    Returns:
    --------
    The dictionary with its values as tuples
    
    '''
    for i in dic:
        dic[i]=tuple(dic[i])

    return dic




# create combinations
def make_combinations(items):
    '''
    generate all possible combinations from the unique items that have been extracted before
    
    Args:
    -------
    items: the unique sorted
    
    Returns:
    --------
    All possible combinations from the unique items that provided as parameter
    
    '''
    all_combinations = []
    for r in range(len(items) + 1):
        combinations_object = itertools.combinations(items, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list

    return all_combinations


def make_comb_list(combinations):
    '''
    Add the resulted combinations to list

    Args:
    ------
    combinations: the combinations of elements that already generated
    
    Returns:
    ---------
    A list that contains each combination of elements as an item in the list 
    '''
    lis=[]
    for i in combinations:
        lis.append(list(i))
    return lis    


def make_tuple(lis):
    '''
    Transform the elements of the list to be tuples
    
    Args:
    ------
    lis: that contains the combinations of the items
    
    Returns:
    ---------
    the resulted tuple after transfroming the list elements into tuples
    '''
    
    t=[tuple(i) for i in lis]
    t=tuple(t)
    return t


#check if the subset exist in the superset 
def check_subset(bigger,smaller):
    '''
    check if there is subset of elements contained in another set of elements
    Args:
    -----
    bigger: A tuple that contain elements
    smaller: A tuple that contain elements 
    
    Returns:
    ---------
    A boolean value that equals true if one tuple contained in the other and false otherwise
    '''
    return all(i in bigger for i in smaller)




# Accept input from the user
dic=get_input()

# Accept the support from the user
sup=int(input('SUP => '))

#extract the unique elements
unique_items=create_unique_items(dic)

#change the type of dictionary values
dic=change_type_dic(dic)

#make all possible combinations of the unique elements
combinations=make_combinations(unique_items)

lis=make_comb_list(combinations)

# transform the list elements to be tuples
subsets=make_tuple(lis)





# new dictionary that will hold the final combinations of elements as keys with intial values 0 for each of them 
new_dic=dict.fromkeys(subsets,0)

# loop over the old dictionary 
for i,val in dic.items():
    
    # loop over the tuples
    for j in subsets:
        
        #check if there is one item contians another items as any subset of a frequent itemset must be frequent and if so increment it by 1
        if check_subset(val,j):
            new_dic[j]+=1

# create new dictionary that will hold only the elements that its value or its support will exceed the provided support by the user
new_data = {k: v for k, v in new_dic.items() if v >=sup }

data={}
for key,val in new_data.items():
    if key==():
        continue
    else:
        data[key]=val
print('items ==> Support')
for i,v in data.items():
    print(f'{i} ==> {v}')

stop=input("press close to exit") 