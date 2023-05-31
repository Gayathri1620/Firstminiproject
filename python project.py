import sys
prod=[]
qty=[]
rate=[]
def bill( item,  qt, r):
    prod.append(item)
    qty.append(qt)
    rate.append(r)
    
def total():
    price=[]
    for i in range(len(prod)):
        price.append(qty[i]*rate[i])
    
    print("               AVATAR RESTAURANT")
    print("        No:7/4, 6th mainroad,nanganallur")
    print("                  044 6542321")
    print("Date:02/01/2023                         Time:2pm")
    print("     Item                    Quantity      Price")

    for i in range(len(prod)):
        print("{}{}            {}".format(prod[i],qty[i],price[i]))

    cost=0
    for i in range(len(price)):
        cost+=price[i]
    print("Total cost=Rs.",cost)

    
def indiandes():
    print("INDIAN DESSERTS                    Rs.")
    print("1.Rasmalai                         60")
    print("2.Gulab jamun                      80")
    print("3.Kaju katli                       150")
    print("4.Kulfi                            80")
    print("5.Falooda                          120")
    print("6.Exit")
    rg=int(input("What kind of dessert do you prefer? "))
    if rg==1:
        qt=int(input("How many do you want? "))
        bill("Rasmalai                        ",qt,60)
    elif rg==2:
        qt=int(input("How many do you want? "))
        bill("Gulab jamun                     ",qt,80)
    elif rg==3:
        qt=int(input("How many do you want? "))
        bill("Kaju katli                      ",qt,150)
    elif rg==4:
        qt=int(input("How many do you want? "))
        bill("Kulfi                           ",qt,80)
    elif rg==5:
        qt=int(input("How many do you want? "))
        bill("Falooda                         ",qt,120)
    elif rg==6:
        bvgdes()
    else:
        print("Invalid input")
    indiandes()

def indianbvg():
    print("INDIAN BEVERAGES                   Rs.")
    print("1.Goli soda                        30")
    print("2.Masala chai                      60")
    print("3.Mojito                           100")
    print("4.Butter milk                      50")
    print("5.Fresh lime juice                 40")
    print("6.Exit")
    fb=int(input("Which kind of beverage you prefer? "))
    if fb==1:
        qt=int(input("How many do you want? "))
        bill("Goli soda                       ",qt,30)
    elif fb==2:
        qt=int(input("How many do you want? "))
        bill("Masala chai                     ",qt,60)
    elif fb==3:
        qt=int(input("How many do you want? "))
        bill("Mojito                          ",qt,100)
    elif fb==4:
        qt=int(input("How many do you want? "))
        bill("Butter milk                     ",qt,50)
    elif fb==5:
        qt=int(input("How many do you want? "))
        bill("Fresh lime juice                ",qt,40)
    elif fb==6:
        indiandes()
    else:
        print("Invalid input")
    indianbvg()

def bvgdes():
    print("BEVERAGES OR DESSERTS")
    print("1.Beverages")
    print("2.Desserts")
    print("3.Exit")
    bd=int(input("What do you want to prefer Beverage or Dessert? "))
    if bd==1:
        indianbvg()
    elif bd==2:
        indiandes()
    elif bd==3:
        indian()
    else:
        print("Invalid input")
    bvgdes()


def invmaindish():
    print("INDIAN NON VEG MAINDISH            Rs.")
    print("1.Chicken biriyani                 220")
    print("2.Mutton biriyani                  270") 
    print("3.Prawn fried rice                 150") 
    print("4.Fish fried rice                  250")
    print("5.Mixed fried rice                 300")
    print("6.Exit")
    cf=int(input("What kind of Main dish you prefer? "))
    if cf==1:
        qt=int(input("How many do you want? "))
        bill("Chicken biriyani                ",qt,220)
    elif cf==2:
        qt=int(input("How many do you want? "))
        bill("Mutton biriyani                 ",qt,270)
    elif cf==3:
        qt=int(input("How many do you want? "))
        bill("Prawn fried rice                ",qt,150)
    elif cf==4:
        qt=int(input("How many do you want? "))
        bill("Fish fried rice                 ",qt,250)
    elif cf==5:
        qt=int(input("How many do you want? "))
        bill("Mixed fried rice                ",qt,300)
    elif cf==6:
        bvgdes()
    else:
        print("Invalid input")
    invmaindish()


def invstarter():
    print("INDIAN NON VEG STARTER             Rs.")
    print("1.Chicken manchurian               200")
    print("2.Crab gravy                       180")
    print("3.Prawn tikka                      150")
    print("4.Chicken lollipop                 140")
    print("5.Mutton fry                       250")
    print("6.Exit")
    cp=int(input("Which kind of starter you prefer? "))
    if cp==1:
        qt=int(input("How many do you want? "))
        bill("Chicken manchurian              ",qt,200)
    elif cp==2:
        qt=int(input("How many do you want? "))
        bill("Crab gravy                      ",qt,180)
    elif cp==3:
        qt=int(input("How many do you want? "))
        bill("Prawn tikka                     ",qt,150)
    elif cp==4:
        qt=int(input("How many do you want? "))
        bill("Chicken lollipop                ",qt,140)
    elif cp==5:
        qt=int(input("How many do you want? "))
        bill("Mutton fry                      ",qt,250)
    elif cp==6:
        invmaindish()
    else:
        print("Invalid input")
    invstarter()


def invsoup():
    print("INDIAN NON VEG SOUP                Rs.")
    print("1.Mutton soup                      100")
    print("2.Chicken soup                     80")
    print("3.Beef soup                        90")
    print("4.Exit")
    mc=int(input("Which kind of soup you prefer? "))
    if mc==1:
        qt=int(input("How many do you want? "))
        bill("Mutton soup                     ",qt,100)
    elif mc==2:
        qt=int(input("How many do you want? "))
        bill("Chicken soup                    ",qt,80)
    elif mc==3:
        qt=int(input("How many do you want? "))
        bill("Beef soup                       ",qt,90)
    elif mc==4:
        invstarter()
    else:
        print("Invalid input")
    invsoup()
    

def indiannonveg():
    print("INDIAN NON VEGETARIAN")
    print("1.Soup")
    print("2.Starter")
    print("3.Main dish")
    print("4.Exit")
    inv=int(input("What do you prefer? "))
    if inv==1:
        invsoup()
    elif inv==2:
        invstarter()
    elif inv==3:
        invmaindish()
    elif inv==4:

        indian()
    else:
        print("Invalid input")



def indianmaindish():
    print("INDIAN VEG MAINDISH                Rs.")
    print("1.Veg biriyani                     140")
    print("2.Veg tomato rice                  80")
    print("3.Curd rice                        60")
    print("4.Paneer rice                      150")
    print("5.Mushroom rice                    160")
    print("6.Exit")
    im=int(input("What kind of maindish you prefer? "))
    if im==1:
        qt=int(input("How many do you want? "))
        bill("Veg biriyani                    ",qt,140)
    elif im==2:
        qt=int(input("How many do you want? "))
        bill("Veg tomato rice                 ",qt,80)
    elif im==3:
        qt=int(input("How many do you want? "))
        bill("Curd rice                       ",qt,60)
    elif im==4:
        qt=int(input("How many do you want? "))
        bill("Paneer rice                     ",qt,150)
    elif im==5:
        qt=int(input("How many do you want? "))
        bill("Mushroom rice                   ",qt,160)
    elif im==6:
        bvgdes()
    else:
        print("Invalid input")
    indianmaindish()


def indianstarter():
    print("INDIAN VEG STARTER                 Rs.")
    print("1.Paneer tikka                     100")
    print("2.Gobi manchurian                  130")
    print("3.Mushroom fry                     65")
    print("4.Veg cutlet                       50")
    print("5.Veg momos                        120")
    print("6.Exit")
    ist=int(input("What kind of starter do you prefer? "))
    if ist==1:
        qt=int(input("How many do you want? "))
        bill("Paneer tikka                    ",qt,100)
    elif ist==2:
        qt=int(input("How many do you want? "))
        bill("Gobi manchurian                 ",qt,130)
    elif ist==3:
        qt=int(input("How many do you want? "))
        bill("Mushroom fry                    ",qt,65)
    elif ist==4:
        qt=int(input("How many do you want? "))
        bill("Veg cutlet                      ",qt,50)
    elif ist==5:
        qt=int(input("How many do you want? "))
        bill("Veg momos                       ",qt,120)
    elif ist==6:
        indianmaindish()
    else:
        print("Invalid input")
    indianstarter()

def indiansoup():
    print("INDIAN VEG SOUP                   Rs.")
    print("1.Vegetable soup                  30")
    print("2.Sweet corn soup                 35")
    print("3.Mushroom soup                   40")
    print("4.Thoothuvalai soup               45")
    print("5.Tomato soup                     50")
    print("6.Exit")
    iss=int(input("What kind of soup you prefer? "))
    if iss==1:
        qt=int(input("How many do you want? "))
        bill("Vegetable soup                  ",qt,30)
    elif iss==2:
        qt=int(input("How many do you want? "))
        bill("Sweet corn soup                 ",qt,35)
    elif iss==3:
        qt=int(input("How many do you want? "))
        bill("Mushroom soup                   ",qt,40)
    elif iss==4:
        qt=int(input("How many do you want? "))
        bill("Thoothuvalai                    ",qt,45)
    elif iss==5:
        qt=int(input("How many do you want? "))
        bill("Tomato soup                     ",qt,50)
    elif iss==6:
        indianstarter()
    else:
        print("Invalid input")
    indiansoup()

    
def indianveg():
    print("INDIAN VEGETARIAN")
    print("1.Soup")
    print("2.Starter")
    print("3.Maindish")
    print("4.Exit")
    iv=int(input("what do you prefer? "))
    if iv==1:
        indiansoup()
    elif iv==2:
        indianstarter()
    elif iv==3:
        indianmaindish()
    elif iv==4:
        bvgdes()
    else:
        print("invalid input")
        indianveg()

def indian():
    print("INDIAN")
    print("1.Vegetarian")
    print("2.Non-Vegetarian")
    print("3.Beverages or desserts ")
    print("4.Exit")
    vn=int(input("what do you like to have? "))
    if vn==1:
        indianveg()
    elif vn==2:
        indiannonveg()
    elif vn==3:
        bvgdes()
    elif vn==4:
        main()
    else:
        print("Invalid input")
        indian()
def cdes():
    print("CHINESE DESSERTS                  Rs.")
    print("1.Rice dumplings                  40")
    print("2.Sugarcoated haws on a stick     80")
    print("3.Dragon's beard candy            100")
    print("4.Water chestnut cake             330")
    print("5.Tangyuan                        240")
    print("6.Exit")
    dt=int(input("What kind of dessert do you prefer? "))
    if dt==1:
        qt=int(input("How many do you want? "))
        bill("Rice dumplings                  ",qt,40)
    elif dt==2:
        qt=int(input("How many do you want? "))
        bill("Sugarcoated haws                ",qt,80)
    elif dt==3:
        qt=int(input("How many do you want? "))
        bill("Dragon's beard candy            ",qt,100)
    elif dt==4:
        qt=int(input("How many do you want? "))
        bill("Water chestnut cake             ",qt,330)
    elif dt==5:
        qt=int(input("How many do you want? "))
        bill("Tangyuan                        ",qt,240)
    elif dt==6:
        cbvgdes()
    else:
        print("Invalid input")
    cdes()
def cbvg():
    print("CHINESE BEVERAGES                 Rs.")
    print("1.Hot tea                         50")
    print("2.Ice tea                         100")
    print("3.Kiddie cocktail                 300")
    print("4.Ginger ale                      250")
    print("5.yanjing                         85")
    print("6.Exit")
    kg=int(input("What kind of beverage do you prefer? "))
    if kg==1:
        qt=int(input("How many do you want? "))
        bill("Hot tea                         ",qt,50)
    elif kg==2:
        qt=int(input("How many do you want? "))
        bill("Ice tea                         ",qt,100)
    elif kg==3:
        qt=int(input("How many do you want? "))
        bill("Kiddie cocktail                 ",qt,300)
    elif kg==4:
        qt=int(input("How many do you want? "))
        bill("Ginger ale                      ",qt,250)
    elif kg==5:
        qt=int(input("How many do you want? "))
        bill("Yanjing                         ",qt,85)
    elif kg==6:
        cdes()
    else:
        print("Invalid input")
    cbvg()

def cbvgdes():
    print("BEVERAGES OR DESSERTS")
    print("1.Beverages")
    print("2.Desserts")
    print("3.Exit")
    db=int(input("what do you prefer? "))
    if db==1:
        cbvg()
    elif db==2:
        cdes()
    elif db==3:
        chinese()
    else:
        print("Invalid input")
        cbvgdes()

def chineserice():
    print("CHINESE VEG RICE                  Rs.")
    print("1.Veg soybean rice                160")
    print("2.Veg triple schezwan rice        350")
    print("3.Stewed rice & manchurian gravy  150")
    print("4.Spice tofu & bean sprouts rice  300")
    print("5.Burnt ginger fried rice         200")
    print("6.Exit")
    cr=int(input("What kind of rice do you prefer? "))
    if cr==1:
        qt=int(input("How many do you want? "))
        bill("Veg soybean rice                ",qt,160)
    elif cr==2:
        qt=int(input("How many do you want? "))
        bill("Veg triple schezwan rice        ",qt,350)
    elif cr==3:
        qt=int(input("How many do you want? "))
        bill("Stewed rice & manchurian gravy  ",qt,150)
    elif cr==4:
        qt=int(input("How many do you want? "))
        bill("Spice tofu & bean sprouts rice  ",qt,300)
    elif cr==5:
        qt=int(input("How many do you want? "))
        bill("Burnt ginger fried rice         ",qt,200)
    elif cr==6:
        cbvgdes()
    else:
        print("Invalid input")
    chineserice()

def chinesenoodles():
    print("CHINESE VEG NOODLES               Rs.")
    print("1.Veg hakka noodles               60")
    print("2.Veg hong kong noodles           70")
    print("3.veg pakoda noodles              100")
    print("4.Rice noodles                    210")
    print("5.Peking noodles                  199")
    print("6.Exit")
    cp=int(input("What kind of noodles do you want? "))
    if cp==1:
        qt=int(input("How many do you want? "))
        bill("Veg hakka noodles               ",qt,60)
    elif cp==2:
        qt=int(input("How many do you want? "))
        bill("Veg hong kong noodles           ",qt,70)
    elif cp==3:
        qt=int(input("How many do you want? "))
        bill("Veg pakoda noodles              ",qt,100)
    elif cp==4:
        qt=int(input("How many do you want? "))
        bill("Rice noodles                    ",qt,210)
    elif cp==5:
        qt=int(input("How many do you want? "))
        bill("Peking noodles                  ",qt,199)
    elif cp==6:
        chineserice()
    else:
        print("Invalid input")
    chinesenoodles()

def chinesestarter():
    print("CHINESE VEG STARTER               Rs.")
    print("1.Crispy cheese balls             80")
    print("2.Veg spring roll                 190")
    print("3.Golden fry baby corn            120")
    print("4.Veg paneer and noodle balls     130")
    print("5.Mushroom mangolian              140")
    print("6.Exit")
    ct=int(input("What kind of starter do you prefer? "))
    if ct==1:
        qt=int(input("How many do you want? "))
        bill("Crispy cheese balls             ",qt,80)
    elif ct==2:
        qt=int(input("How many do you want? "))
        bill("Veg spring rolls                ",qt,190)
    elif ct==3:
        qt=int(input("How many do you want? "))
        bill("Golden fry baby corn            ",qt,120)
    elif ct==4:
        qt=int(input("How many do you want? "))
        bill("Veg paneer and noodle balls     ",qt,130)
    elif ct==5:
        qt=int(input("How many do you want? "))
        bill("Mushroom mangolian              ",qt,140)
    elif ct==6:
        chinesenoodles()
    else:
        print("Invalid input")
    chinesestarter()



def chinesesoup():
    print("CHINESE VEG SOUP                  Rs.")
    print("1.Winter melon soup               50")
    print("2.Veg lung-fung soup              170")
    print("3.Veg wonton soup                 145")
    print("4.Veg com soup                    120")
    print("5.Veg manchow soup                50")
    print("6.Exit")
    cs=int(input("What kind of soup do you prefer? "))
    if cs==1:
        qt=int(input("How many do you want? "))
        bill("Winter melon soup               ",qt,50)
    elif cs==2:
        qt=int(input("How many do you want? "))
        bill("Veg lung-fung soup              ",qt,170)
    elif cs==3:
        qt=int(input("How many do you want? "))
        bill("Veg wonton soup                 ",qt,145)
    elif cs==4:
        qt=int(input("How many do you want? "))
        bill("Veg com soup                    ",qt,120)
    elif cs==5:
        qt=int(input("How many do you want? "))
        bill("Veg manchow soup                ",qt,50)
    elif cs==6:
        chinesestarter()
    else:
        print("Invalid input")
    chinesesoup()




def cnvrice():
    print("CHINESE NON VEG RICE              Rs.")
    print("1.Pork fried rice                 235")
    print("2.Shrimp fried rice               500")
    print("3.Yang chow fried rice            195")
    print("4.Ham and egg rice                200")
    print("5.Beef rice                       250")
    print("6.Exit")
    cr=int(input("What kind of rice do you prefer? "))
    if cr==1:
        qt=int(input("How many do you want? "))
        bill("Pork fried rice                 ",qt,235)
    elif cr==2:
        qt=int(input("How many do you want? "))
        bill("Shrimp fried rice               ",qt,500)
    elif cr==3:
        qt=int(input("How many do you want? "))
        bill("Yang chow fried rice            ",qt,195)
    elif cr==4:
        qt=int(input("How many do you want? "))
        bill("Ham & egg rice                  ",qt,200)
    elif cr==5:
        qt=int(input("How many do you want? "))
        bill("Beef rice                       ",qt,250)
    elif cr==6:
        cbvgdes()
    else:
        print("Invalid input")
    cnvrice()

def cnvnoodles():
    print("CHICKEN NON VEG NOODLES            Rs.")
    print("1.Chicken hakka noodles            300")
    print("2.Dandan noodles                   285")
    print("3.Shanghai fried noodles           310")
    print("4.Lanzhou hand pulled noodles      600")
    print("5.Xinjiang hand pulled noodles     800")
    print("6.Exit")
    lc=int(input("What kind of noodles do you prefer? "))
    if lc==1:
        qt=int(input("How many do you want? "))
        bill("Chicken hakka noodles           ",qt,300)
    elif lc==2:
        qt=int(input("How many do you want? "))
        bill("Dandan noodles                  ",qt,285)
    elif lc==3:
        qt=int(input("How many do you want? "))
        bill("Shanghai fried noodles          ",qt,310)
    elif lc==4:
        qt=int(input("How many do you want? "))
        bill("Lanzhou noodles                 ",qt,600)
    elif lc==5:
        qt=int(input("How many do you want? "))
        bill("Xinjiang noodles                ",qt,800)
    elif lc==6:
        cnvrice()
    else:
        print("Invalid input")
    cnvnoodles()

def cnvstarter():
    print("CHINESE NON VEG STARTER            Rs.")
    print("1.Sweet and sour chicken           590")
    print("2.Crispy chicken honey             250")
    print("3.Butter garlic prawns             320")
    print("4.Kung pao chicken                 285")
    print("5.Diced chicken in devil's sauce   210")
    print("6.Exit")
    nc=int(input("What kind of starter do you prefer? "))
    if nc==1:
        qt=int(input("How many do you want? "))
        bill("Sweet & sour chicken            ",qt,590)
    elif nc==2:
        qt=int(input("How many do you want? "))
        bill("Crispy chicken honey            ",qt,250)
    elif nc==3:
        qt=int(input("How many do you want? "))
        bill("Butter garlic prawns            ",qt,320)
    elif nc==4:
        qt=int(input("How many do you want? "))
        bill("Kung pao chicken                ",qt,285)
    elif nc==5:
        qt=int(input("How many do you want? "))
        bill("Diced chicken in devil's sauce  ",qt,210)
    elif nc==6:
        cnvnoodles()
    else:
        print("Invalid input")
    cnvstarter()

def cnvsoup():
    print("CHINESE NON VEG SOUP               Rs.")
    print("1.Duck's blood & vermicelli soup   500")
    print("2.Chicken Wonton soup              155")
    print("3.Imitation shark fin soup         1000")
    print("4.Tomato and egg soup              300")
    print("5.Snake soup                       1200")
    print("6.Exit")
    ns=int(input("What kind of soup do you prefer?"))
    if ns==1:
        qt=int(input("How many do you want? "))
        bill("Duck's blood & vermicelli soup  ",qt,500)
    elif ns==2:
        qt=int(input("How many do you want? "))
        bill("Chicken wanton soup             ",qt,155)
    elif ns==3:
        qt=int(input("How many do you want? "))
        bill("Imitation shark fin soup        ",qt,1000)
    elif ns==4:
        qt=int(input("How many do you want? "))
        bill("Tomato & egg soup               ",qt,300)
    elif ns==5:
        qt=int(input("How many do you want? "))
        bill("Snake soup                      ",qt,1200)
    elif ns==6:
        cnvstarter()
    else:
        print("Invalid input")
    cnvsoup()




def chineseveg():
    print("CHINESE VEGETARIAN")
    print("1.Soup")
    print("2.Starter")
    print("3.Noodles")
    print("4.Rice")
    print("5.Exit")
    cv=int(input("What do you prefer? "))
    if cv==1:
        chinesesoup()
    elif cv==2:
        chinesestarter()
    elif cv==3:
        chinesenoodles()
    elif cv==4:
        chineserice()
    elif cv==5:
        cbvgdes()
    else:
        print("Invalid input")
        chineseveg()

def chinesenonveg():
    print("CHINESE NON VEGETARIAN")
    print("1.Soup")
    print("2.Starter")
    print("3.Noodles")
    print("4.Rice")
    print("5.Exit")
    cnv=int(input("What do you prefer? "))
    if cnv==1:
          cnvsoup()
    elif cnv==2:
          cnvstarter()
    elif cnv==3:
          cnvnoodles()
    elif cnv==4:
          cnvrice()
    elif cnv==5:
          cbvgdes()
    else:
        print("Invalid input")
        chinesenonveg()

    
def chinese():
    print("CHINESE")
    print("1.Vegetarian")
    print("2.Non vegetarian")
    print("3.Beverages or Desserts")
    print("4.Exit")
    cn=int(input("What do you like to have? "))
    if cn==1:
          chineseveg()
    elif cn==2:
          chinesenonveg()
    elif cn==3:
           cbvgdes()
    elif cn==4:
        main()
    else:
        print("invalid input")
        chinese()
        

print("Welcome to our restaurant")
print("AVATAR RESTAURANT")
def main():
    while True:
        print("MAIN MENU")
        print("1.Indian")
        print("2.Chinese")
        print("3.Exit")
        cc=int(input("what kind of country cuisine you prefer? "))
        if cc==1:
                indian()
        elif cc==2:
                chinese()
        elif cc==3:
                total()
                print("THANK YOU VISIT AGAIN")
                sys.exit()
        else:
                print("Invalid input")
main()
        
