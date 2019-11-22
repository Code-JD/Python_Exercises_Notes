post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from the end of a tuple
# post = post[:-1]
# print(post)

# Removing elements from the beginning of a tuple
# post = post[1:]
# print(post)

#Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)