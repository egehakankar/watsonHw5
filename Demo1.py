# coding=utf-8
# This is the submission of the project group named WATSON for Homework 5.
# To run normally: python main.py

# Members:
#           Mehmet Berk Şahin (CONTACT)
#           Balaj Saleem
#           Mehmet Alper Genç
#           Ege Hakan Karaağaç
#           Fırat Yönak

'''
In this program BACKWARD CHAIN algorithm is implemented. 

Until all hypotheses have been tried and none have been supported or until the
animal is identified program does the following for each hypotheses:

For each rule whose consequent matches the current hypothesis,

Try to support each of the rule's antecedents by matching it to assertions in working
memory or by backward chaining through another rule, creating new hypotheses. Program checks
all matching and instantiation alternatives. 

If all the rule's antecedents are supported, program announces success and its concludes
that the hypothesis is true. 
'''
from PyQt5 import QtWidgets
import window
import sys

class ContentWrapper:
    def __init__(self, content):
        self.content = content
    def getContent(self):
        return self.content
    def setContent(self, content):
        self.content= content

output = []

ruleList = [
    "Z1: if ?x has hair,\n then ?x is a mammal\n", 

    "Z2: if ?x gives milk,\n then ?x is a mammal\n",

    "Z3: if ?x has feathers,\n then ?x is a bird\n",

    "Z4: if ?x flies,\n ?x lays eggs,\n then ?x is a bird\n",

    "Z5: if ?x eats meat,\n ?x is a mammal,\n then ?x is a carnivore\n",

    "Z6: if ?x has pointed teeth,\n ?x has claws ,\n ?x has forward-pointing eyes ,\n ?x is a mammal,\n then ?x is a carnivore\n",

    "Z7: if ?x has hoofs ,\n ?x is a mammal,\n then ?x is an ungulate\n",

    "Z8: if ?x chews cud ,\n ?x is a mammal,\n then ?x is an ungulate\n",

    "Z9: if ?x has tawny color ,\n ?x has dark spots ,\n ?x is a carnivore,\n then ?x is a cheetah\n",

    "Z10: if ?x has tawny color ,\n ?x has black stripes ,\n ?x is a carnivore,\n then ?x is a tiger\n",

    "Z11: if ?x has long legs ,\n ?x has a long neck ,\n ?x has a tawny color ,\n ?x has dark spots ,\n ?x is an ungulate,\n then ?x is a giraffe\n",

    "Z12: if ?x has white color ,\n ?x has black stripes ,\n ?x is an ungulate,\n then ?x is a zebra\n",

    "Z13: if ?x does not fly ,\n ?x has long legs ,\n ?x has a long neck ,\n ?x is black and white ,\n ?x is a bird,\n then ?x is an ostrich\n",

    "Z14: if ?x does not fly ,\n ?x swims ,\n ?x is black and white ,\n ?x is a bird,\n then ?x is a penguin\n",

    "Z15: if ?x is a good flyer ,\n ?x is a bird,\n then ?x is an albatross\n"

]
#These are rules specialized to ZOOKEEPER scenario
animals = ["Albatross", "Penguin", "Ostrich", "Zebra", "Giraffe", "Tiger", "Cheetah"]
hypothesis = animals[0]

def rules(ruleNo, workMem):
    check = 0
    global hypothesis
    global animals
    #STEP-BY-STEP

    if (ruleNo >= 10):
        hypothesis = animals[15-ruleNo]
        output.append("\n")
        output.append("Hypothesis is " + hypothesis)

    output.append("\n")
    output.append("Working Memory:")
    for assertion in workMem:
        output.append(assertion)
    output.append("\n")
    output.append("Rule is Z" + str(ruleNo))


    if ruleNo == 1:
        output.append("?x has hair")
        for feature in workMem:
            if feature == "?x has hair":
                check += 1
        if check == 1:
            return 2
        return 0

    elif ruleNo == 2:
        output.append("?x gives milk")
        for feature in workMem:
            if feature == "?x gives milk":
                check += 1
        if check == 1:
            return 2
        return 0

    elif ruleNo == 3:
        output.append("?x has feathers")
        for feature in workMem:
            if feature == "?x has feathers":
                check += 1
        if check == 1:
            return 2
        return 0

    elif ruleNo == 4:
        output.append("?x flies")
        output.append("?x lays eggs")
        for feature in workMem:
            if feature == "?x flies":
                check += 1
            elif feature == "?x lays eggs":
                check += 1
        if check == 2:
            return 2
        return 0

    elif ruleNo == 5:
        mammalCheck = False
        output.append("?x eats meat")
        output.append("?x is a mammal")
        for feature in workMem:
            if feature == "?x eats meat":
                check += 1
            elif feature == "?x is a mammal":
                mammalCheck = True
        if check == 1:
            if mammalCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 6:
        mammalCheck = False
        output.append("?x has pointed teeth")
        output.append("?x has claws")
        output.append("?x has forward-pointing eyes")
        output.append("?x is a mammal")
        for feature in workMem:
            if feature == "?x has pointed teeth":
                check += 1
            elif feature == "?x has claws":
                check += 1
            elif feature == "?x has forward-pointing eyes":
                check += 1
            elif feature == "?x is a mammal":
                mammalCheck = True
        if check == 3:
            if mammalCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 7:
        mammalCheck = False
        output.append("?x has hoofs")
        output.append("?x is a mammal")
        for feature in workMem:
            if feature == "?x has hoofs":
                check += 1
            elif feature == "?x is a mammal":
                mammalCheck = True
        if check == 1:
            if mammalCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 8:
        mammalCheck = False
        output.append("?x chews cud")
        output.append("?x is a mammal")
        for feature in workMem:
            if feature == "?x chews cud":
                check += 1
            elif feature == "?x is a mammal":
                mammalCheck = True
        if check == 1:
            if mammalCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 9:
        carnivoreCheck = False
        output.append("?x has tawny color")
        output.append("?x has dark spots")
        output.append("?x is a carnivore")
        for feature in workMem:
            if feature == "?x has tawny color":
                check += 1
            elif feature == "?x has dark spots":
                check += 1
            elif feature == "?x is a carnivore":
                carnivoreCheck = True
        if check == 2:
            if carnivoreCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 10:
        carnivoreCheck = False
        output.append("?x has tawny color")
        output.append("?x has black stripes")
        output.append("?x is a carnivore")
        for feature in workMem:
            if feature == "?x has tawny color":
                check += 1
            elif feature == "?x has black stripes":
                check += 1
            elif feature == "?x is a carnivore":
                carnivoreCheck = True
        if check == 2:
            if carnivoreCheck:
                return 2
            return 1
        return 0


    elif ruleNo == 11:
        ungulateCheck = False
        output.append("?x has long legs")
        output.append("?x has a long neck")
        output.append("?x has a tawny color")
        output.append("?x has dark spots")
        output.append("?x is an ungulate")
        for feature in workMem:
            if feature == "?x has long legs":
                check += 1
            elif feature == "?x has a long neck":
                check += 1
            elif feature == "?x has tawny color":
                check += 1
            elif feature == "?x has dark spots":
                check += 1
            elif feature == "?x is an ungulate":
                ungulateCheck = True
        if check == 4:
            if ungulateCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 12:
        ungulateCheck = False
        output.append("?x has white color")
        output.append("?x has black stripes")
        output.append("?x is an ungulate")
        for feature in workMem:
            if feature == "?x has white color":
                check += 1
            elif feature == "?x has black stripes":
                check += 1
            elif feature == "?x is an ungulate":
                ungulateCheck = True
        if check == 2:
            if ungulateCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 13:
        birdCheck = False
        output.append("?x does not fly")
        output.append("?x has long legs")
        output.append("?x has a long neck")
        output.append("?x is black and white")
        output.append("?x is a bird")
        for feature in workMem:
            if feature == "?x does not fly":
                check += 1
            elif feature == "?x has long legs":
                check += 1
            elif feature == "?x has a long neck":
                check += 1
            elif feature == "?x is black and white":
                check += 1
            elif feature == "?x is a bird":
                birdCheck = True
        if check == 4:
            if birdCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 14:
        birdCheck = False
        output.append("?x does not fly")
        output.append("?x swims")
        output.append("?x is black and white")
        output.append("?x is a bird")
        for feature in workMem:
            if feature == "?x does not fly":
                check += 1
            elif feature == "?x swims":
                check += 1
            elif feature == "?x is black and white":
                check += 1
            elif feature == "?x is a bird":
                birdCheck = True
        if check == 3:
            if birdCheck:
                return 2
            return 1
        return 0

    elif ruleNo == 15:
        birdCheck = False
        output.append("?x is a good flyer")
        output.append("?x is a bird")
        for feature in workMem:
            if feature == "?x is a good flyer":
                check += 1
            elif feature == "?x is a bird":
                birdCheck = True
        if check == 1:
            if birdCheck:
                return 2
            return 1
        return 0

#Animals specific to ZOOKEEPER scenario

def cheetah(workMem):
    rule9 = rules(9, workMem)
    if rule9 != 0:
        if rule9 == 1:
            rule5 = rules(5, workMem)
            if rule5 != 0:
                if rule5 == 1:
                    if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                        return True
                    else:
                        rule6 = rules(6, workMem)
                        if rule6 != 0:
                            if rule6 == 2:
                                return True
                            elif rule6 == 1:
                                if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                                    return True
                                else:
                                    return False
                        else:
                            return False
                elif rule5 == 2:
                    return True
            else:
                rule6 = rules(6, workMem)
                if rule6 != 0:
                    if rule6 == 2:
                        return True
                    elif rule6 == 1:
                        if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                            return True
                        else:
                            return False
                else:
                    return False
        elif rule9 == 2:
            return True
    else:
        return False

def tiger(workMem):
    rule10 = rules(10, workMem)
    if rule10 != 0:
        if rule10 == 1:
            rule5 = rules(5, workMem)
            if rule5 != 0:
                if rule5 == 1:
                    if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                        return True
                    else:
                        rule6 = rules(6, workMem)
                        if rule6 != 0:
                            if rule6 == 2:
                                return True
                            elif rule6 == 1:
                                if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                                    return True
                                else:
                                    return False
                        else:
                            return False
                elif rule5 == 2:
                    return True
            else:
                rule6 = rules(6, workMem)
                if rule6 != 0:
                    if rule6 == 2:
                        return True
                    elif rule6 == 1:
                        if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                            return True
                        else:
                            return False
                else:
                    return False
        elif rule10 == 2:
            return True
    else:
        return False

def giraffe(workMem):
    rule11 = rules(11, workMem)
    if rule11 != 0:
        if rule11 == 1:
            rule7 = rules(7, workMem)
            if rule7 != 0:
                if rule7 == 1:
                    if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                        return True
                    else:
                        rule8 = rules(8, workMem)
                        if rule8 != 0:
                            if rule8== 2:
                                return True
                            elif rule8 == 1:
                                if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                                    return True
                                else:
                                    return False
                        else:
                            return False
                elif rule7 == 2:
                    return True
            else:
                rule8 = rules(8, workMem)
                if rule8 != 0:
                    if rule8 == 2:
                        return True
                    elif rule8 == 1:
                        if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                            return True
                        else:
                            return False
                else:
                    return False
        elif rule11 == 2:
            return True
    else:
        return False

def zebra (workMem):
    rule12 = rules(12, workMem)
    if rule12 != 0:
        if rule12 == 1:
            rule7 = rules(7, workMem)
            if rule7 != 0:
                if rule7 == 1:
                    if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                        return True
                    else:
                        rule8 = rules(8, workMem)
                        if rule8 != 0:
                            if rule8 == 2:
                                return True
                            elif rule8 == 1:
                                if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                                    return True
                                else:
                                    return False
                        else:
                            return False
                elif rule7 == 2:
                    return True
            else:
                rule8 = rules(8, workMem)
                if rule8 != 0:
                    if rule8 == 2:
                        return True
                    elif rule8 == 1:
                        if rules(2, workMem) == 2 or rules(1, workMem) == 2:
                            return True
                        else:
                            return False
                else:
                    return False
        elif rule12 == 2:
            return True
    else:
        return False

def ostrich(workMem):
    rule13 = rules(13, workMem)
    if rule13 != 0:
        if rule13 == 1:
            if rules(3, workMem) == 2 or rules(4, workMem) == 2:
                return True
            else:
                return False
        elif rules(12, workMem) == 2:
            return True
    else:
        return False

def penguin(workMem):
    rule14 = rules(14, workMem)
    if rule14 != 0:
        if rule14 == 1:
            if rules(3, workMem) == 2 or rules(4, workMem) == 2:
                return True
            else:
                return False
        elif rule14 == 2:
            return True
    else:
        return False

#add prints here for single stepping

def albatross(workMem):
    rule15 = rules(15, workMem)
    if rule15 != 0:
        if rule15 == 1:
            if rules(3, workMem) == 2 or rules(4, workMem) == 2:
                return True
            else:
                return False
        elif rule15 == 2:
            return True
    else:
        return False



#Here is the working memory, you can put any assertion as you want.

# workMem = [
#     "?x has tawny color",
#     "?x has black stripes",
#     "?x has pointed teeth",
#     "?x has claws",
#     "?x has forward-pointing eyes",
#     "?x gives milk",
# ]

workMem = [
    "Splashy has feathers.",
    "Splashy lays eggs.",
    "Splashy swims.",
    "Splashy does not fly.",
    "Splashy is black and white.",
    "Splashy has tawny color.",
]


#cleans up the WorkMem
for i in range(len(workMem)):
    s = workMem[i]
    s = s.replace('.', '')
    replacement = '?x'
    s = s.split()
    s[0] = replacement
    workMem[i] = ' '.join(s)

print(workMem)

animals = ["Albatross", "Penguin", "Ostrich", "Zebra", "Giraffe", "Tiger", "Cheetah"]


#Create and test hypotheses, then display the result.

if albatross(workMem):
    output.append("The animal is Albatross")
elif penguin(workMem):
    output.append("The animal is Penguin")
elif ostrich(workMem):
    output.append("The animal is Ostrich")
elif zebra(workMem):
    output.append("The animal is Zebra")
elif giraffe(workMem):
    output.append("The animal is Giraffe")
elif tiger(workMem):
    output.append("The animal is Tiger")
elif cheetah(workMem):
    output.append("The animal is Cheetah")
else:
    output.append("The animal could not be identified.")

sep = "\n"
rulesString = sep.join(ruleList)
memString = sep.join(workMem)
outString = sep.join(output)

print(outString)

app = QtWidgets.QApplication(sys.argv)
MainWindow1 = QtWidgets.QMainWindow()
MainWindow2 = QtWidgets.QMainWindow()
ui = window.Ui_MainWindow()
ui2 = window.Ui_MainWindow()
c1 = ContentWrapper("RULES LIST: \n" + rulesString)
c2 = ContentWrapper("Working Memory: " + outString)
ui.setupUi(MainWindow1, "Rules", c1)
ui2.setupUi(MainWindow2, "Working Memory", c2, ui.refresh)
MainWindow1.show()
MainWindow2.show()
print("Displaying application UI.")
# c1.setContent("Test")
# c2.setContent("Test2")

app.exec_()
print("UI window closed. Program will now exit.")

#showWindows()


