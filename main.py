import PySimpleGUI as sg
import random

class account:
    def __init__(self, id, name, surname, p_number, cardNo, password, balance):
        self.id = id
        self.name = name
        self.surname = surname
        self.p_number = p_number
        self.cardNo = cardNo
        self.password = password
        self.balance = balance

userDetails = {}

def screenDisplay(scr):
    screens = {
        "logIn" : [ [sg.Text('Bank', size=(600,1), font=('Arial, 35'), justification='c')],
                    [sg.Text('Log In', size=(600,1), font=('Arial, 25'), text_color = 'Red', justification='c')],
                    [sg.Text('', size = (1,3), key = 'fill')],
                    [sg.Text('Card Number : ', size = (20, 1), justification = 'c'), sg.InputText(key = 'cardInputLogIn')],
                    [sg.Text('Password :', size = (20, 1), justification = 'c'), sg.InputText(key = 'passInputLogIn')],
                    [sg.Text('', size = (1,3), key = 'fill')],
                    [sg.Text('', key = 'fill', size = (27, 1)), sg.Button('Log In', font=('Arial, 12'), auto_size_button=True, use_ttk_buttons = True), sg.Button('Sign In', font=('Arial, 12'), auto_size_button=True, use_ttk_buttons = True)]
                ],
        "signIn" : [[sg.Text('Bank', size=(600,1), font=('Arial, 35'), justification='c')],
                    [sg.Text('Sign In', size=(600,1), font=('Arial, 25'), text_color = 'Red', justification='c')],
                    [sg.Text('', size = (1,1), key = 'fill')],
                    [sg.Text('Id Number : ', size=(20, 1), justification = 'c'), sg.InputText(key = 'idInput')],
                    [sg.Text('Name : ', size=(20, 1), justification = 'c'), sg.InputText(key = 'nameInput')],
                    [sg.Text('Surname : ', size=(20, 1), justification = 'c'), sg.InputText(key = 'surnameInput')],
                    [sg.Text('Phone Number : ', size=(20, 1), justification = 'c'), sg.InputText(key = 'phoneInput')],
                    [sg.Text('Password : ', size=(20, 1), justification = 'c'), sg.InputText(key = 'passInput')],
                    [sg.Text('', size = (1,1), key = 'fill')],
                    [sg.Text('', key = 'fill', size = (27, 1)), sg.Button("Done", font=('Arial, 12'), auto_size_button=True, use_ttk_buttons = True), sg.Button("Back", font=('Arial, 12'), auto_size_button=True, use_ttk_buttons = True)]
                ],
        "mainScreen" : [
            [sg.Text('Welcome,', size=(300,1), font=('Arial, 20'), justification='c'), sg.Text(f'.', size=(300,1), font=('Arial, 15'))]
        ]
    }
    return screens[scr]


def idChecker(idInput): #Tamamlandı
    sum = 0
    try:
        for i in idInput[0 : len(idInput) - 1]:
            sum += int(i)
        if(not(len(idInput) == 11 and idInput[-1] == str(sum)[-1])):
            sg.popup("Invalid ID")
            return False
        return True
    except:
        sg.popup("Invalid ID")
        return False

def phoneChecker(phoneInput):
    try:
        int(phoneInput)    
        if(len(phoneInput) == 11):
            return True
        else:
            sg.popup("Invalid Phone Number.")
            return False
    except:
        sg.popup("Invalid Phone Number.")
        return False

def cardNumberChecker(cardInput): #Tamamlandı
    stDigits = cardInput[-1::-2]
    ndDigits = cardInput[-2::-2]
    sum = 0
    try:
        if(len(cardInput) == 16):
            for i in stDigits:
                sum += int(i)
            for i in ndDigits:
                num = int(i) * 2
                if(num > 9):
                    sum += int(str(num)[0]) + int(str(num)[1])
                else:
                    sum += num
            if(sum % 10 == 0):
                return True
            return False
    except:
        sg.popup("Invalid Card Number.")
        return False

def logInDataChecker(num):
    try:
        if(userDetails[keyFinder(num)]["cardNo"] == window['cardInputLogIn'].get() and userDetails[keyFinder(num)]["password"] == window['passInputLogIn'].get()):
            sg.popup("Logged In Successfully!")
            return True
        sg.popup("Invalid Card Number Or Password.")
        return False
    except:
        sg.popup("Invalid Card Number Or Password.")
        return False

def createCardNumber(): #Tamamlandı
    generatedNumbers = ""
    sum = 0
    for i in range(15):
        generatedNumbers += str(random.randint(0,9))
    stDigits = generatedNumbers[-1::-2]
    ndDigits = generatedNumbers[-2::-2]
    try:
        for i in stDigits:
            num = int(i) * 2
            if(num > 9):
                sum += int(str(num)[0]) + int(str(num)[1])
            else:
                sum += num
        for i in ndDigits:
            sum += int(i)
        generatedNumbers += str(sum * 9)[-1]
        sg.popup("Your Card Number Sent As a Output.")
        print(f'Your Generated Card Number is \'{generatedNumbers}\'')
        return generatedNumbers
    except:
        print("Card Number Can Not Generated.")
        return False

def keyFinder(val):
    for i in userDetails:
        for value in userDetails.values():
            if val == value:
                print(value)
                return i
        else:
            return False

sg.theme('TealMono')
layout = [[sg.Column(screenDisplay("logIn"), key = 'logInScreen', justification = 'c'), sg.Column(screenDisplay("signIn"), key = 'signInScreen', justification = 'c', visible = False), sg.Column(screenDisplay("mainScreen"), key = 'mainScreen', justification = 'c', visible = False)]]

window = sg.Window('ATM App', layout, size=(600, 400), element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Sign In':
        window['logInScreen'].update(visible = False)
        window['signInScreen'].update(visible = True)
    elif event == 'Log In':
        if(logInDataChecker(window['cardInputLogIn'].get())):
            window['logInScreen'].update(visible = False)
            window['mainScreen'].update(visible = True)
    elif event == 'Back':
        window['signInScreen'].update(visible = False)
        window['logInScreen'].update(visible = True)
    elif event == 'Done':
        if(idChecker(window['idInput'].get()) and phoneChecker(window['phoneInput'].get())):
            cardNumber = createCardNumber()
            user = account(window['idInput'].get(), window['nameInput'].get(), window['surnameInput'].get(), window['phoneInput'].get(), cardNumber, window['passInput'].get(), 500)
            userDetails[len(userDetails)] = {
                "id" : window['idInput'].get(),
                "name" : window['nameInput'].get(),
                "surname" : window['surnameInput'].get(),
                "p_number" : window['phoneInput'].get(),
                "cardNo" : cardNumber,
                "password" : window['passInput'].get(),
                "balance" : 500
            }


window.close()
