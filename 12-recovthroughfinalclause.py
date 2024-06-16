def readFile(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        if file:
            file.close()
            print("File closed successfully.")
readFile("example.txt")
readFile("kou")