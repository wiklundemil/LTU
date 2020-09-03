def greet(name):
    print(f"Hi {name}") #Here with this function we are locked to print it to the terminal.


def get_greeting(name):
    return f"hi {name}" #We can print it on the terminal, write it to a file and email it. Return ger oss dessa möjligheter.


message = get_greeting("Emil") #With function with a return value you can create variables like message to use later in code. 
