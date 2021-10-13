'''Layla Nettavong    10/12/2021
Professor Traecy    SDEV140
Finals Project GUI    Candle store
A series of candle options that can be placed in a cart and purchased
This is all the buttons and functions
'''
#importing tkinter and making window
from tkinter import*
root = Tk()
root.configure(bg = 'lawn green')
root.geometry('450x150')

#The 'title' of page
title = Label(root, text = "Abunscents", bg = 'lawn green')
title.grid(row = 0, column = 3)

#This is cart window
cart = Toplevel(bg = 'lawn green')
cart.geometry('500x150')

#labels in cart window that are title and for a candle selected-reference list
cartLabel = Label(cart, text = 'Cart', bg = 'lawn green')
cartLabel.grid(row =0, column = 3)
candleSelect = Label(cart,text = 'You have selected :', bg = 'lawn green')
candleSelect.grid(row = 1, column = 0)

#function and button for buying candles from cart window
def purchaseDone():
    Done = Label(cart, text = 'Congrats! Your purchase was a success, you will never see these candles! :D',bg = 'lawn green')
    Done.grid(row = 6, column = 0)
purchaseCartButton = Button(cart, text = "Purchase Cart", padx = 12, pady = 0, command = purchaseDone)
purchaseCartButton.grid(row = 5, column = 3)


#candle scent choice buttons
'''I wanted all the candle buttons to be same size or atleast close'''

#Food scent buttons and relations
foodCandles = Label(root, text = 'Food Scents', bg = 'lawn green')
foodCandles.grid(row = 1, column = 3)
#all the functions for the food scented candles that show up in cart once selected
def addVanilla():
    pickVanilla = Label(cart, text = 'a vanilla candle!',bg = 'lawn green')
    pickVanilla.grid(row = 1, column = 3)
def addCookies():
    pickCookies = Label(cart, text = 'a cookie candle!',bg = 'lawn green')
    pickCookies.grid(row = 1, column = 2)
def addApples():
    pickApples = Label(cart, text = 'an apple candle!',bg = 'lawn green')
    pickApples.grid(row = 1, column = 4)

#Actual buttons of food scented candles
vanillaButton = Button(root, text = "Vanilla", padx = 14, pady = 0, command = addVanilla)
vanillaButton.grid(row = 2, column = 3)

cookiesButton = Button(root, text = "Cookies", padx = 10, pady = 0, command = addCookies)
cookiesButton.grid(row = 3, column = 3)

applesButton = Button(root, text = "Apples", padx = 13, pady = 0, command = addApples)
applesButton.grid(row = 4, column = 3)


#Special scent buttons and relations
#all the functions for the special scented candles that show up in cart once selected
def addNight():
    pickNight = Label(cart, text = 'a night candle!',bg = 'lawn green')
    pickNight.grid(row = 2, column = 3)
def addRomance():
    pickRomance = Label(cart, text = 'a romance candle!',bg = 'lawn green')
    pickRomance.grid(row = 2, column = 2)
def addPumpkin():
    pickPumpkin = Label(cart, text = 'a pumpkin candle!',bg = 'lawn green')
    pickPumpkin.grid(row = 2, column = 4)
    
specialCandles = Label(root, text = 'Special Scents', bg = 'lawn green')
specialCandles.grid(row = 1, column = 4)
#Actual buttons for special candles
nightButton = Button(root, text = 'Night', padx = 22, pady = 0, command = addNight)
nightButton.grid(row = 2, column = 4)

romanceButton = Button(root, text = 'Romance', padx = 12, pady = 0, command = addRomance)
romanceButton.grid(row = 3, column = 4)

pumpkinButton = Button(root, text = 'Pumpkin', padx = 13, pady = 0, command = addPumpkin)
pumpkinButton.grid(row = 4, column = 4)


#Outdoor scent buttons and relations
outdoorCandles = Label(root, text = 'Outdoor Scents', bg = 'lawn green')
outdoorCandles.grid(row = 1, column = 1)
#all the functions for the outdoor scented candles that show up in cart once selected
def addFlowers():
    pickFlowers = Label(cart, text = 'a flower candle!',bg = 'lawn green')
    pickFlowers.grid(row = 3, column = 3)
def addOcean():
    pickOcean = Label(cart, text = 'an ocean candle!',bg = 'lawn green')
    pickOcean.grid(row = 3, column = 2)
def addForest():
    pickForest = Label(cart, text = 'a forest candle!',bg = 'lawn green')
    pickForest.grid(row = 3, column = 4)
#Actual buttons for outdoor candles
flowersButton = Button(root, text = 'Flowers', padx = 9, pady = 0, command = addFlowers)
flowersButton.grid(row = 2, column = 1)

oceanButton = Button(root, text = 'Ocean', padx = 12, pady = 0, command = addOcean)
oceanButton.grid(row = 3, column = 1)

forestButton = Button(root, text = 'Forest', padx = 13, pady = 0, command = addForest)
forestButton.grid(row = 4, column = 1)


#contact info
contact = Label(root, text = 'Have questions? Call us at (574)000-1234', bg = 'lawn green')
contact.grid(row = 6, column = 3)
    
