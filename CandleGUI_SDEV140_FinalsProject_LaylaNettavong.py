'''Layla Nettavong    10/12/2021
Professor Traecy    SDEV140
Finals Project GUI    Candle store
A series of candle options that can be placed in a cart and purchased
'''
from tkinter import* 
root = Tk()
root.configure(bg = 'lawn green')
#The 'title' of page
title = Label(root, text = "Abunscents", bg = 'lawn green')
title.grid(row = 0, column = 3)

#candle scent choice buttons
'''I wanted all the candle buttons to be same size or atleast close
'''

#Food scnet buttons and relations
foodCandles = Label(root, text = 'Food Scents', bg = 'lawn green')
foodCandles.grid(row = 1, column = 3)

vanillaButton = Button(root, text = "Vanilla", padx = 14, pady = 0)
vanillaButton.grid(row = 2, column = 3)
cookiesButton = Button(root, text = "Cookies", padx = 10, pady = 0)
cookiesButton.grid(row = 3, column = 3)
applesButton = Button(root, text = "Apples", padx = 13, pady = 0)
applesButton.grid(row = 4, column = 3)

#Special scent buttons and relations
specialCandles = Label(root, text = 'Special Scents', bg = 'lawn green')
specialCandles.grid(row = 1, column = 4)

nightButton = Button(root, text = 'Night', padx = 22, pady = 0)
nightButton.grid(row = 2, column = 4)
romanceButton = Button(root, text = 'Romance', padx = 12, pady = 0)
romanceButton.grid(row = 3, column = 4)
pumpkinButton = Button(root, text = 'Pumpkin', padx = 13, pady = 0)
pumpkinButton.grid(row = 4, column = 4)

#Outdoor scent buttons and relations
outdoorCandles = Label(root, text = 'Outdoor Scents', bg = 'lawn green')
outdoorCandles.grid(row = 1, column = 1)

flowersButton = Button(root, text = 'Flowers', padx = 9, pady = 0)
flowersButton.grid(row = 2, column = 1)
oceanButton = Button(root, text = 'Ocean', padx = 12, pady = 0)
oceanButton.grid(row = 3, column = 1)
forestButton = Button(root, text = 'Forest', padx = 13, pady = 0)
forestButton.grid(row = 4, column = 1)

#Cart button and relations to cart
cartButton = Button(root, text = 'Cart')
cartButton.grid(row = 0, column = 5)
    #This is cart window
cart = Toplevel(bg = 'lawn green')
cartLabel = Label(cart, text = 'Cart', bg = 'lawn green')
cartLabel.grid(row =0, column = 3)
    #Cart buttons operations
leaveCartButton = Button(cart, text = 'Leave', padx = 10, pady = 0)
leaveCartButton.grid(row = 1, column = 3)
purchaseCartButton = Button(cart, text = "Purchase Cart", padx = 12, pady = 0)
purchaseCartButton.grid(row = 1, column = 2)

#contact info
contact = Label(root, text = 'Have questions? Call us at (574)000-1234', bg = 'lawn green')
contact.grid(row = 6, column = 3)
