# this takes in a keyword list as an argument (combining names arguments) 

def greeting(**kw):     # 2 stars followed by kw-keyword arguments
      print(kw)


greeting()                  # this returns a dictionary with no arguments
greeting(first = 'Kristine', last = 'Hudgens')   # now insert named arguments (this returns a dictionary)

def greeting1(**kw):
  if kw:              # implementing a conditional starting--check if kw were set or not
    print(f"Hi {kw['first']} {kw['last']}, have a great day!") # for dictionary pass in bracket syntax using []
                                                                       # pass in bracket synatx pass in the first name and then same as last name
  else:                   # if no keyword  were given
    print('Hi Guest!')    # just say hi guest


greeting1()   # Hi guest have a great day
greeting(first = 'Kristine', last = 'Hudgens')
