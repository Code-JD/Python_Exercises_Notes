sentence = 'The quick brown fox jumped over the lazy dog.'

# query = sentence.find('oops')
# query_two = sentence.index('oops')

# print(query)
# print(query_two)

# query = 'fox' in sentence <---- True
query = 'oops' in sentence

if 'oops' in sentence:
	

# print(query)

# to search in a string
# start with the variable sentence with a string with a sentence
# start with a query you first call the senetence then in parens type quick-which will return the index where quick is (this a a substring)
# NEXT
# the index function returns the similar finding of using find-BUT index will throw and error if it can't find
# if value is not contained in the string INDEX will throw an error while FIND will show an -1
#NEXT
# for the in operator- pass in the fox word to start which will display TRUE if you pass in oops it will return FALSE


# EXTRA NOTES TO HOLD ON TO

# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments >start and end are interpreted as in slice notation. Return -1 if sub is not found

# Note
# The find() method should be used only if you need to know the position of sub. To check if sub is a substring or >not, use the in operator

# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.