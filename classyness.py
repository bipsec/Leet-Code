class Classy(object):
    def __init__(self):
        self.items = []

    def getClassiness(self):

        for i in self.items:
            # print(i)
            if i == "tophat":
                return 2
            elif i == "bowtie":
                return 4
            elif i == "monocle":
                return 5
            return str(0)

    def addItem(self, class_type):
        self.items.append(class_type)



# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# # Should be 2
print(me.getClassiness())

# me.addItem("bowtie")
# me.addItem("jacket")
# me.addItem("monocle")
# # Should be 11
# print(me.getClassiness())

# me.addItem("bowtie")
# # Should be 15
# print(me.getClassiness())
