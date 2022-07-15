file = open('sample.txt')
# print(file.read())
# file.seek(0)
print(file.readlines())

file.close()
print(file.closed)

with open('sample.txt') as sample_file:
    sample_file = sample_file.read()
    print(sample_file)