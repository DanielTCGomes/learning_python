name = "abc xyz"
name1 = name.split(" ")[0]
name2 = name.split(" ")[1]
name3 = name1.replace(name1[0:2], name2[0:2])
name4 = name2.replace(name2[0:2], name1[0:2])
print(name3 +" "+ name4)


"""
st1 = 'abc'
st2 = 'xyz'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")
"""