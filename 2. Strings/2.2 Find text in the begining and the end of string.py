filename = "spam.txt"
print(filename.startswith("file:"))
print(filename.endswith(".txt"))

url = "http://www.python.org"
print("1: {}".format(url.startswith("http://")))
print("2: {}".format(url.endswith(".org")))
choices_1 = (".com", ".ua", ".org")
choices_2 = (".com", ".ua", ".org")
print("3: {}".format(url.endswith(choices_1)))
print("4: {}".format(url.endswith(choices_2)))
