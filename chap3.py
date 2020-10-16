#Try it yourself - guest list page 46
name = ['olivia', 'sophie', 'amanda', 'mia', 'maris']
message = name[0].title() + "," + "come and join our dinner, please!"
message1 = name[1].title() + "," + "come and join our dinner, please!"
message2 = name[2].title() + "," + "come and join our dinner, please!"
message3 = name[3].title() + "," + "come and join our dinner, please!"
message4 = name[4].title() + "," + "come and join our dinner, please!"
print(message1)
print(message2)
print(message3)
print(message4)
print(message)
name.append('John')
print(name)
name[2] = 'Tom'
print(name)
message = name[0].title() + "," + "come and join our dinner, please!"
message1 = name[1].title() + "," + "come and join our dinner, please!"
message2 = name[2].title() + "," + "come and join our dinner, please!"
message3 = name[3].title() + "," + "come and join our dinner, please!"
message4 = name[4].title() + "," + "come and join our dinner, please!"
message5 = name[5].title() + "," + "come and join our dinner, please!"
print(message1)
print(message2)
print(message3)
print(message4)
print(message)
print(message5)
name.insert(0, 'momo')
name.insert(2, 'phung')
print(name)
urgent = "I can invite only two people for dinner"
print(urgent)
del name[2]
print(name)
travel = ['new zealand', 'japan', 'korea', 'america', 'england']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel, reverse=True))
travel.reverse()
print(travel)
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)
print(len(travel))
