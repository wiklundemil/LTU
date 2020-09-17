course = 'Python for beginners'
another = course[:]
#another is the whole course message
print(course[-3]) 
#prints de first character in course. 01234... Is how python counts characters in strings. If 0 is P in the string then -1 will be s. It counts backwards when value is negative.
print(course[0:3])
#prints character 0 to index 3 all but index 3 will be printed that will say 0 1 2.  
print(course[1:])
#prints all characters from start index 1 to the end 
print(course[:5])
#prints all characters from 0 to 5 
print(another)

print()
name = 'Jennifer'
print(name[1:-1])
#Will probably print out from index 1 and to index -1. Index -1 is the 1st character in the name starting backwards. It will print ennife