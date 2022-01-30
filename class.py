class Tree:
    height=5
    def pramod (self):
        print(id(self))
        print('height is {}'.format(self.height))

Elm=Tree()
print(id(Elm))
print(Elm.height)
Elm.pramod()
id(Elm)

