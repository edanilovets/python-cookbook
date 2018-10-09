# example 1
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)


# example 2
record = ("Dave", "dave@mail.com", "773-555-1212", "847-555-1212")
name, email, *phone_numbers = record
print(email)
print(phone_numbers)

# example 3
records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3, 4)
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)
