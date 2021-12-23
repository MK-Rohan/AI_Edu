data = input("Give your string: ")
print("upper:", data.upper())
print("lower:", data.lower())
if data.isalpha:
    print("Your input data is alphabet.")
else:
    print("Your input data is not alphabet.")
print()
digit = input("Give your number: ")
if digit.isdigit:
    print("Your input data is number.")
else:
    print("Your input data is not number.")
print()
sentence = input("Give your sentence: ")
sentence2 = sentence.split()
third = sentence2[2]
fifth = sentence2[4]
print("third word: ", third[0])
print("fifth word: ",  fifth[-1])
print("sentence length: ", len(sentence))
if "test" in sentence:
    print('The sentence contains "test".')
else:
    print('The sentence don\'t contains "test".')
print()
numbers = input("Give your numbers: ")
numbers2 = numbers.split()
fir = numbers2[0]
sec = numbers2[1]
thi = numbers2[2]
print("The sum of the first and last number is ", int(fir) + int(thi))
print("The product of the second and last number is ", int(sec)*int(thi))
