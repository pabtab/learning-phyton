numbers = (1, 2, 4)
# numbers[0] = 10 # error
print(numbers[0])

coord = (11, 12, 13) # also works with []
x, y, z = coord

print(x, y , z)


#Dictionaries
customer = {
    "name": "pabtab",
    "age": 27
}

print(customer['name'])
print(customer.get('burth')) #to know if the value exist and no error
print(customer.get('adiciona', 'defaultval')) #no adiciona al obj

message = input(">")
words = message.split(' ')

emojis = {
    ':)': '😃',
    ':(': '😞'
}

output = ''

for word in words:
    output += emojis.get(word, word) +  ' '

print(output)

