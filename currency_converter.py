import tkinter as tk
import webbrowser as web
import json

__version__ = '1.1.0'
__home__    = 'https://github.com/TJ20201/CurrencyConverter'

datajson = json.load(open('currency_data.json'))
rates = datajson['rates']
currencies = []
for rate in rates:
 if not rate.split("_")[0] in currencies: currencies.append(rate.split("_")[0])
 if not rate.split("_")[1] in currencies: currencies.append(rate.split("_")[1])
currencies = sorted(currencies)

colours = {
 'BLACK': '#28282B',
 'BLACM': '#18171B',
 'BLACD': '#17171A',
 'WHITE': '#FDFBF9',
 'GREEN': '#48A14D',
 'GREED': '#37903C',
 'RED':   '#AB7473'
}

width, height = 350, 200

def stringToNumber(string: str) -> float:
 try: return float(string.replace(',',''))
 except ValueError:return 0.0

root = tk.Tk()
# Move Window
mwcx,mwcy = 0,0
mwcxl,mwcyl = 0,0
def move_window_cacheclick(event):
 global mwcx, mwcy
 mwcx = event.x
 mwcy = event.y
def move_window(event):
 global mwcxl,mwcyl
 restrict = 25
 skiplen = 55
 nx = event.x - mwcx + root.winfo_x()
 ny = event.y - mwcy + root.winfo_y()
 if nx > mwcxl+restrict: nx = mwcxl+restrict
 if nx < mwcxl-restrict: nx = mwcxl-restrict
 if ny > mwcyl+restrict: ny = mwcyl+restrict
 if ny < mwcyl-restrict: ny = mwcyl-restrict
 if nx > mwcxl-skiplen or nx < mwcxl+skiplen: nx = event.x - mwcx + root.winfo_x()
 if ny > mwcyl-skiplen or ny < mwcyl+skiplen: ny = event.y - mwcy + root.winfo_y()
 mwcxl,mwcyl = nx, ny
 root.geometry('+{0}+{1}'.format(mwcxl,mwcyl))
root.overrideredirect(True)
# Title Bar
titleBarHeight = 25
titleBar = tk.Frame(root, bg=colours['BLACM'])
titleBarLabel = tk.Label(titleBar, bg=colours['BLACM'],fg=colours['WHITE'],text='Currency Converter')
buttonClose = tk.Button(titleBar, width=int(titleBarHeight/8), height=titleBarHeight, text='X', bg=colours['RED'], activebackground='#9A6362', fg=colours['WHITE'], activeforeground=colours['BLACK'], command=root.destroy)
titleBar.bind('<Button-1>', move_window_cacheclick);titleBarLabel.bind('<Button-1>', move_window_cacheclick)
titleBar.bind('<B1-Motion>', move_window);titleBarLabel.bind('<B1-Motion>', move_window);
titleBar.place(height=titleBarHeight,width=width)
titleBarLabel.place(height=titleBarHeight, width=105,x=titleBarHeight)
buttonClose.pack(side=tk.RIGHT)

root.geometry(f"{width}x{height+titleBarHeight}")
root.geometry(f"+50+50")

main = tk.Frame(bg=colours['BLACK'])
main.place(height=height,width=width,y=titleBarHeight)

intype = tk.StringVar();intype.set("GBP")
outype = tk.StringVar();outype.set("USD")
output = tk.StringVar()

curin = tk.Entry(root,bg=colours['BLACD'],fg=colours['WHITE']) 
curin.place(width=width-75,x=5,y=5+titleBarHeight)

valin = tk.OptionMenu(root, intype, *currencies)
valin.config(highlightthickness=0,bg=colours['BLACD'],fg=colours['WHITE'],activebackground=colours['BLACM'])
valin["menu"].config(bg=colours['BLACD'],fg=colours['WHITE'],activebackground=colours['BLACM'])
valin["menu"]["borderwidth"] = valin["borderwidth"] = 0
valin.place(x=width-65,y=5+titleBarHeight, height=20)
valou = tk.OptionMenu(root, outype, *currencies)
valou.config(highlightthickness=0,bg=colours['BLACD'],fg=colours['WHITE'],activebackground=colours['BLACM'])
valou["menu"].config(bg=colours['BLACD'],fg=colours['WHITE'],activebackground=colours['BLACM'])
valou["menu"]["borderwidth"] = valou["borderwidth"] = 0
valou.place(x=5,y=35+titleBarHeight, height=20,width=width-10)
final = tk.Text(root,state='disabled',fg=colours['WHITE'],relief='flat',bg=colours['BLACD'])
final.place(x=5, y=105+titleBarHeight, width=width-10,height=height-165)

def openSite():web.open(__home__, new=2)

verLabel = tk.Label(root, fg='#DBDBD7', bg=colours['BLACK'],text=f"Version v{__version__}")
verLabel.place(y=height-5,x=width-105)
webLabel = tk.Button(root, fg='#9A9AD7',activeforeground='#8989C6', activebackground=colours['BLACK'],bg=colours['BLACK'],relief='flat',text="Website",command=openSite)
webLabel.place(y=height-5,x=5)

def convertMoney():
 if not intype.get() == outype.get():
  try:rate = rates[f'{intype.get()}_{outype.get()}']
  except KeyError:rate = rates[f'{outype.get()}_{intype.get()}']
 else: rate = 1.0000
 output.set(f"~{round(stringToNumber(curin.get()),2)} {intype.get()}\n~{round(stringToNumber(curin.get())*rate,2)} {outype.get()}")
 lineOne = output.get().split("\n")[0]
 lineTwo = output.get().split("\n")[1]
 final.configure(state='normal')
 final.delete(1.0,"end");final.delete(2.0,"end")
 final.insert(1.0,lineOne+"\n");final.insert(2.0,lineTwo)
 final.configure(state='disabled')

convert = tk.Button(root,fg=colours['WHITE'],activeforeground=colours['WHITE'],bg=colours['GREEN'],activebackground=colours['GREED'],text=f"Convert currency",command=convertMoney)
convert.place(x=width/4+5,y=75+titleBarHeight,width=width/2-5)

root.mainloop()