def unique_list(l):
    """return a list of unique from given list l"""
    x = []
    
    #iterate over provided list
    for a in l:
        #check if number is in new list
        if a not in x:
            #add it to new list
            x.append(a)
            
    return x

print (unique_list([1, 1, 2, 2, 2, 4, 4, 5, 5, 8, 9, 9, 22, 6]))