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
def price_point(entry,leverage,rr,label):
    pop  = round(float("{:.2f}".format(rr/leverage)), 2)
    if label == 'TP':
        out = entry + ((entry*float(pop))/100)
    elif label == 'SL' :
        out = entry - ((entry*float(pop))/100)
    

    return out

def process():
    leverage = int(os.environ.get("DEF_LEV"))
    tp = float(os.environ.get("REWARD"))
    sl = float(os.environ.get("RISK"))
    entry = float(input("Enter entry price - "))

    print(f"""
    LEVERAGE - {leverage}
    
    TP - {price_point(entry,leverage,tp,'TP')}
    SL - {price_point(entry,leverage,tp,'SL')}

    """)

    print("Press anything to copy tp.",end='')
    input()
    pyperclip.copy(price_point(entry,leverage,tp,'TP'))
    print("Copied !")
    input()
    print("Press anything to copy sl.",end='')
    input()
    pyperclip.copy(price_point(entry,leverage,tp,'SL'))
    print("Copied !")
    input()

while True:
    clear()
    process()