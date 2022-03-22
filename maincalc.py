import os
try:
    import dotenv
except:
    os.system('pip install python-dotenv')
    import dotenv
try:
    import pyperclip
except:
    os.system('pip install pyperclip')
    import pyperclip

#Calulator
dotenv.load_dotenv()

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

#lev calc
def long(entry,leverage,rr,label):
    pop  = round(float("{:.2f}".format(rr/leverage)), 2)
    if label == 'TP':
        out = entry + ((entry*float(pop))/100)
    elif label == 'SL' :
        out = entry - ((entry*float(pop))/100)
    

    return out

def short(entry,leverage,rr,label):
    pop  = round(float("{:.2f}".format(rr/leverage)), 2)
    if label == 'TP':
        out = entry - ((entry*float(pop))/100)
    elif label == 'SL' :
        out = entry + ((entry*float(pop))/100)
    

    return out


def process():
    leverage = int(os.environ.get("DEF_LEV"))
    tp = float(os.environ.get("REWARD"))
    sl = float(os.environ.get("RISK"))
    entry = float(input("Enter entry price - "))
    choice = input("Long or Short (l/s) - ")

    if choice == 'l':
        print(f"""
        LEVERAGE - {leverage}
        Direction - LONG
        
        TP - {long(entry,leverage,tp,'TP')}
        SL - {long(entry,leverage,sl,'SL')}

        """)

        print("Press anything to copy tp.",end='')
        input()
        pyperclip.copy(long(entry,leverage,tp,'TP'))
        print("Copied !")
        input()
        print("Press anything to copy sl.",end='')
        input()
        pyperclip.copy(long(entry,leverage,tp,'SL'))
        print("Copied !")
        input()

    elif choice == 's':
        print(f"""
        LEVERAGE - {leverage}
        Direction - SHORT
        
        TP - {short(entry,leverage,tp,'TP')}
        SL - {short(entry,leverage,sl,'SL')}

        """)

        print("Press anything to copy tp.",end='')
        input()
        pyperclip.copy(short(entry,leverage,tp,'TP'))
        print("Copied !")
        input()
        print("Press anything to copy sl.",end='')
        input()
        pyperclip.copy(short(entry,leverage,tp,'SL'))
        print("Copied !")
        input()




while True:
    clear()
    process()