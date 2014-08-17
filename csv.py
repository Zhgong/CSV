

# IDs
ID={    'TAG' : 1,
            'FLAG': 4,

        }


# print ("IDs are: ", ID)
# print (" TAG:", ID['TAG'])
#print(type(ID['TAG']))

def genTagList(SubID):
    id =ID['TAG']
    return [id, SubID]



Taglist = genTagList(2)
print(Taglist, '\n', type(Taglist))
