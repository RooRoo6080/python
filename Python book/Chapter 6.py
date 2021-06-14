import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?", choices = ["Vanilla", "Strawberry", "Chocolate"])
easygui.msgbox("You picked " + flavor)
