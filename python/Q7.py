'''7 . Write all content of a given list into a new list by skipping item number 5 and 9
	UseList = [21,5,4,3,21,78,7,12,34,26,51,71,19]'''
 
a = [21,5,4,3,21,78,7,12,34,26,51,71,19]

for x in a:
    if x == a[5] :
        continue
    elif x == a[9] :
        continue
    print(x)
       
