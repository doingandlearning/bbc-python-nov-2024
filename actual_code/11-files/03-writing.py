try:
    with open("file3.txt", mode="w") as f:  # write mode erases the current contents!
        f.write("Hello, how are you?\n")
        f.write("Python is fun!\n")
        f.write("Writing to files looks okay\n")
        f.write(f"1 + 1 = {1+1}")
except Exception as e:
    print(f"Problem creating the file: {e}")
