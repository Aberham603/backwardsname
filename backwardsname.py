for x in range(10):
    print("CGI is great.")
    

name = raw_input("What is your name?")
backwards = (name[::-1])

print "Hello", name,", please to meet you! Did you know your name backwards is", backwards
