import pyautogui
import time
import clipboard
WIDTH=1400

def findmark(mark):
    try:
        left,top,width,height = pyautogui.locateOnScreen(mark)
        center=pyautogui.center((left,top,width,height))
        return center
    except:
        print(f"{mark} not found")
        return None

def choose(center):
    if center:
        pyautogui.click(center)

def getqueston(start,end):
    if start and end:
        question=pyautogui.screenshot(region=(int(start[0]-100),int(start[1]-50),WIDTH,int(end[1]-start[1]+100)))
        return question
    else:
        print("Question not found")
        return None

def type(text):
    pyautogui.typewrite(text)

while True:
    center = findmark('ProblemKindA.png')
    CenterOfA = findmark('AnswerMarkA.png')
    CenterOfB = findmark('AnswerMarkB.png')
    CenterOfC = findmark('AnswerMarkC.png')
    CenterOfD = findmark('AnswerMarkD.png')
    choose(center)
    if not (center and CenterOfA and CenterOfB and CenterOfC and CenterOfD):
        pyautogui.scroll(-100)
        continue
    question = getqueston(center, CenterOfD)
    question.save('question.png')
    CenterOfUpload = findmark('Upload.png')
    choose(CenterOfUpload)
    time.sleep(1)
    type('question.png')
    type('\n')
    time.sleep(10)
    type('please answer it with only a mark from A,B,C,D')
    type('\n')
    time.sleep(20)
    CenterOfCopy = findmark('TagOfCopy.png')
    choose(CenterOfCopy)
    answer = clipboard.paste()
    if answer == 'A':
        choose(CenterOfA)
    elif answer == 'B':
        choose(CenterOfB)
    elif answer == 'C':
        choose(CenterOfC)
    elif answer == 'D':
        choose(CenterOfD)
    else:
        print("Invalid answer")
    pyautogui.scroll(-100)
'''
def answerKindB():
    center = findmark('ProblemKindB.png')
    CenterOfA = findmark('AnswerMarkA.png')
    CenterOfB = findmark('AnswerMarkB.png')
    choose(center)
    question = getqueston(center, CenterOfB)
    question.save('question.png')
    CenterOfUpload = findmark('Upload.png')
    choose(CenterOfUpload)
    time.sleep(1)
    type('question.png')
    type('\n')
    time.sleep(10)
    type('please answer it with only a mark from A,B,C,D')
    type('\n')
    time.sleep(10)
    CenterOfCopy = findmark('TagOfCopy.png')
    choose(CenterOfCopy)
    answer = clipboard.paste()
    if answer == 'A':
        choose(CenterOfA)
    elif answer == 'B':
        choose(CenterOfB)
    else:
        print("Invalid answer")
    return center, CenterOfB
'''







