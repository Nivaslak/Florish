# To calculate the total stock worth in the cafe

menu=['bread','egg','cake','muffin'] 
stock={'bread':5,                       
        'egg':8,
        'cake':3,
        'muffin':4
      }
price={'bread':3.00,
       'egg':1.00,
       'cake':2.00,
       'muffin':0.75
}
Tot_stock_val=0
for items in menu:
    Tot_stock_val=Tot_stock_val+stock[items]*price[items]
print("Total worth of the cafe stock=" , "£",Tot_stock_val)    
