string = """
John: Python is a high-level, general-purpose programming language. 

Its design philosophy emphasizes code readability with the use of significant indentation. 

Dave: Python is dynamically-typed and garbage-collected. 

It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. 

It is often described as a "batteries included" language due to its comprehensive standard library. 

John: Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. 

Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. 

Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. 

Python 2 was discontinued with version 2.7.18 in 2020. 

Dave: Python consistently ranks as one of the most popular programming languages.
"""

word = 'Python'
count = 0
lines = []
found = False
for item in string.splitlines():
    if item.find(word) != -1:
        if item.find('John:') != -1:
            lines.append(item)
            count += 1
            found = True
if found:
    print('Number of reputation: ' + str(count))
    for line in lines:
        print(line)
else:
    print('There are no result!')
