#Flattening a list

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = []
def flatten(n):
    for item in n:
        if type(item) == list:
            flatten(item)
        else:
            flat_list.append(item)
    return flat_list
  
  
 #Nested Lists
l = [[1, 2], [3, 4], [5, 6, 7]]
l2 = []
def nest(l):
    for i in l:
        if type(i) == list:
            l2.append(list(reversed(i)))
    return sorted(l2,reverse=True)
