import random
import clipboard as clipboard
from selenium import webdriver
import time
import pyautogui
import pytesseract

captchaImage=[1000, 600]    #coordinates of captcha
saveImageRel=[20, 60]       #relative coordinates for saving image
locationPath=[160, 70]      #coordinates for location entry
saveImage=[300, 200]        #coordinates to save button
overWrite=[1000, 540]       #overwriting the captcha image
searchBar=[532,64]          #search bar coordinates
reloadIcon=[105, 65]        #coordinates for reload button

myfile = open('rockyou.txt', encoding='cp437')    #open the rockyou.txt as a list
content=myfile.read()
content_list=content.split('\n')


safe_list=[]

passwordfile=open('passwords.txt','r')          #opens the input passwords set as a list
passcontent=passwordfile.read()
pass_list=passcontent.split('\n')

for n in pass_list:
    if n not in content_list:
        safe_list.append(n)                #safe list is prepared eith passwords not included in rockyou.txt

def inputCaptcha():                                                                                     #Function to input captcha
    time.sleep(1)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'                 #importing pytesseract. User should install this on the PC
    captcha = pytesseract.image_to_string(r'captcha/captcha.gif')                                       #obtaining the saved captcha image
    captcha = captcha.lower()                                                                           #GX router only uses lower case captcha
    driver.find_element_by_xpath("/html/body/div/form/table/tbody/tr[5]/td[3]/input").send_keys(captcha)#Send decoded captcha to the login page

def getBarElement():                                    #search bar status reader
    time.sleep(1)
    pyautogui.moveTo(searchBar[0],searchBar[1])         #select search bar url
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl','c')                        #copies the selected url
    text=clipboard.paste()                              #pasting it as a string for decision making
    if(text==r"http://192.168.1.1/cgi-bin/login.asp"):
        pyautogui.moveTo(reloadIcon[0],reloadIcon[1])   #if captcha bypass failed reload and try the same agaim
        pyautogui.click()
        start()
    else:                                               #if successfully logged in, display tha msg and continue with password changing
        print("logged in")
        changePass()                                    #function to change password

def first():
    global newPass
    global encodedPass
    newPass = random.choice(safe_list)          #new password is chosen randomly from safe list.
    encodedPass = newPass[::-1]                 #password is encrypted by string reversal
    print(encodedPass)
    global captchaPath
    captchaPath = r'C:\Users\USER\Desktop\Good Scholars Project\SmartPasswordAssistant\captcha'     #path where captcha image is saved for captcha bypass using pytesseract
    pyautogui.moveTo(1775, 15)
    pyautogui.click()
    global driver
    driver = webdriver.Chrome()                #selenium webdriver to open google chrome
    driver.maximize_window()                    # window maximzing
    driver.get("http://192.168.1.1/cgi-bin/login.asp")               #login page of router
    start()                                     #starting automation

def start():
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("BC62D269DAD8")       #Enter password of the router
    pyautogui.moveTo(captchaImage[0],captchaImage[1])                                   #Saving the captcha image for decryption
    pyautogui.rightClick()
    pyautogui.moveRel(saveImageRel[0],saveImageRel[1])
    pyautogui.click()
    while True:
        pointer=None
        pointer=pyautogui.locateOnScreen(r'photos/saveas.png')
        if pointer:
            pyautogui.moveTo(locationPath[0], locationPath[1])
            pyautogui.click()
            pyautogui.write(captchaPath)                                                 #Enter captcha image where to be saved
            pyautogui.press('enter')
            while True:
                pointer=None
                pointer=pyautogui.locateOnScreen(r'photos/confirmcaptcha.png')           #waiting for path selection complete
                if pointer:
                    pyautogui.moveTo(saveImage[0],saveImage[1])
                    pyautogui.doubleClick()
                    while True:
                        pointer=None
                        pointer=pyautogui.locateOnScreen(r'photos/overwrite.png')       #to overwrite previous captch to avoid space consumption
                        if pointer:
                            pyautogui.moveTo(overWrite[0],overWrite[1])
                            pyautogui.click()
                            inputCaptcha()                                              #captcha inputing function
                            getBarElement()                                             #function to obain success login status


def changePass():                                                                           #function used to change the passsword of the wifi
    while True:
        pointer=None
        pointer=pyautogui.locateOnScreen(r'photos/net.png')
        if pointer:
            pyautogui.moveTo(809,336)
            pyautogui.click()                                                               #all these are directed to select the password changing option. All GX server works on these.
            while True:
                pointer=None
                pointer=pyautogui.locateOnScreen(r'photos/wlan.png')
                if pointer:
                    pyautogui.moveTo(827,369)
                    pyautogui.click()
                    while True:
                        pointer=None
                        pointer=pyautogui.locateOnScreen(r'photos/enablewireless.png')
                        if pointer:
                            pyautogui.scroll(-1000)
                            while True:
                                pointer=None
                                pointer=pyautogui.locateOnScreen(r'photos/password.png')
                                if pointer:
                                    pyautogui.moveTo(915, 259)
                                    pyautogui.doubleClick()
                                    pyautogui.write(newPass)
                                    while True:
                                        pointer=None
                                        pointer=pyautogui.locateOnScreen(r'photos/ok.png')
                                        if pointer:
                                            pyautogui.moveTo(1060,936)
                                            pyautogui.click()
                                            while True:
                                                pointer=None
                                                pointer=pyautogui.locateOnScreen(r'photos/logout.png')
                                                if pointer:
                                                    pyautogui.moveTo(1395,246)
                                                    pyautogui.click()
                                                    print("Password Changed Successfully")
                                                    while True:
                                                        pointer=None
                                                        pointer=pyautogui.locateOnScreen(r'photos/exitpage.png')
                                                        if pointer:
                                                            driver.close()
                                                            openWP()

def checkTimer() :                                                                         #the function check for the timer to end or to get instruction from user to
    t=600                                                                                  #update the password or to display the current password
    while t:                                                                               #user can select the required time to reset the password
        newMessage=None
        newMessage=pyautogui.locateOnScreen(r'photos/newmessage.png' , confidence=0.9)     #System wait for instryction from users
        if newMessage:
            pyautogui.moveTo(newMessage[0],newMessage[1])
            pyautogui.click()

            while True:
                readPointer=None
                readPointer=pyautogui.locateOnScreen(r'photos/smiley.png', confidence=0.7 ) #System reads the message send by the user.

                if readPointer:
                    pyautogui.moveTo(readPointer[0],readPointer[1])
                    pyautogui.moveRel(20,-60)
                    pyautogui.tripleClick()
                    pyautogui.hotkey('ctrl', 'c')                                           #copies the instruction send
                    message=clipboard.paste()                                               #paste it as a string variable
                    message=message.lower()                                                 #Check accordingly with presaved instructions
                    if(message=='change password' or message=='update password' or message=='2'):   #System updates the password when a password instruction is given
                        pyautogui.moveTo(1890,10)                                                   #closes the whatsapp
                        first()                                                                     #Start passsword changing again
                    elif (message=='current password' or message=='present password' or message=='1'):  #Systwm provide the current key to obain password
                        while True:
                            pointer=None
                            pointer = pyautogui.locateOnScreen(r'photos/smiley.png', confidence=0.5)
                            if pointer:
                                pyautogui.moveTo(pointer[0], pointer[1])
                                pyautogui.moveRel(300, 20)
                                pyautogui.click()
                                pyautogui.write("Hi, Your assistant here, The current Wifi password is :- \n" + encodedPass + "\nKindly decrypt with our application. Be secure. Have a Good Day..!\n")
                                print("message send")
                                while True:
                                    newpointer=None
                                    newpointer=pyautogui.locateOnScreen(r'photos/broadcast.png',confidence=0.7)
                                    if newpointer:
                                        pyautogui.moveTo(newpointer[0],newpointer[1])
                                        pyautogui.click()
                                        checkTimer()
                    elif(len(message)>0):                                                                       #System detects an error message and display how the user can instruct the system
                        while True:
                            pointer=None
                            pointer = pyautogui.locateOnScreen(r'photos/smiley.png', confidence=0.5)
                            if pointer:
                                pyautogui.moveTo(pointer[0], pointer[1])
                                pyautogui.moveRel(300, 20)
                                pyautogui.click()
                                pyautogui.write("Sorry, Didn't understand..... Choose from below options:\n1.Current Password\n2.Update Password\n")
                                print("message send")
                                while True:
                                    newpointer = None
                                    newpointer = pyautogui.locateOnScreen(r'photos/broadcast.png', confidence=0.7)
                                    if newpointer:
                                        pyautogui.moveTo(newpointer[0], newpointer[1])
                                        pyautogui.click()
                                        checkTimer()
                message=''

        else:
            time.sleep(1)                               #Timer to check time
            t=t-1
    first()

def sndMsg():                                                                       #Function to send message to the users through whatsapp
    while True:
        pointer = None
        pointer = pyautogui.locateOnScreen(r'photos/broadcast.png',confidence=0.5)  #Check for the broadcastlist
        if pointer:
            pyautogui.moveTo(pointer[0], pointer[1])
            pyautogui.click()                                                       #Selects the broadcast list to send message to the intended users
            while True:
                poniter1 = None
                pointer1 = pyautogui.locateOnScreen(r'photos/smiley.png',confidence=0.5) #locatses the message writer
                if pointer1:
                    pyautogui.moveTo(pointer1[0], pointer1[1])
                    pyautogui.moveRel(300, 20)
                    pyautogui.click()
                    pyautogui.write("Hi, Your assistant just updated your wifi password. The new password is :- \n" + encodedPass + "\nKindly decrypt with our application. Be secure. Have a Good Day..!\n")
                    print("message send")    #Encoded message is send to the broadcast list and displays a success message on terminal
                    checkTimer()             #System starts a timer to initialise next password change

def openWP():                                                                           #Function to open whatsapp desktop
    while True:
        pointerwp=pyautogui.locateOnScreen(r'photos/whatsapp.png',confidence=0.9)       #Check for the whatsapp icon on the desktop
        if pointerwp:
            pyautogui.moveTo(pointerwp[0],pointerwp[1])                                 #Open the whatsapp by clicking on it
            pyautogui.moveRel(8,8)
            pyautogui.click()
            sndMsg()                                                                    #Function to send the message to the user

first()                                  #start of the program
