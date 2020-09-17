course = 'Python for Beginners'
print(len(course))
#Will count and let you print out the amout of characters in a message or string. In this case 20 characters.

print(course.upper()) 
#Will print course in uppercase letters, .uppper is the method that makes this function able to do that. 

print(course.lower())
#Will print course in lowercase letters, .lower is the method that makes this function able to do that. 

print(course.find('Beginners'))
#Will find the index of the first character of the string. 

print(course.replace('Beginners', 'Absolute Beginners'))
#Will replace Beginners string with string: Absolute Beginners. 

print(course.replace('P', 'J'))
#Will replace the first P with J in the string that is chosen. 

print('Python' in course) 
#Will look for the exact word 'Python' in the cosen string. If found it will print a bolean value; true, if not false. 