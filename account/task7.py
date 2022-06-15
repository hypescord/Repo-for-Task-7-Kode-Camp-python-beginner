from home.models import Product

'''Using commandprompt to modify the model:

>>> from account.task7 import Product'''
     
     
     
'''Inserting a new record into Product:

>>> Product1 = Post(product_name="Kitchen Faucet", Size=22, product_color="Grey", product_price=1500)
>>> Product1.save()'''


'''Getting all records from Product:

>>> Product.objects.all()'''

    
    
'''Filtering Products by name:

>>> Product.objects.filter(product_name="Product1")'''
    
    

'''Getting a single record from Products:

>>> Product.Size'''



'''Changing a Product price:
    
>>> Product!.product_price = 1400
>>> Product!.save()'''