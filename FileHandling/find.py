book = open("C:\\Users\\skshu\\OneDrive\\Desktop\\new.txt", "r")
content = book.read()
if "Hello" in content:
    print("Text 'Hello' is available")
book.close()
