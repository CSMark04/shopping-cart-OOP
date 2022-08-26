class Cart:
    def __init__(self,cart):
        self.cart = cart

   

    def add(self):
        products = input('What would you like to add to the shopping cart? ')
        self.cart.append(products)


    def delt(self):
        print(self.cart)
        product_name = input('What would you like to take out? ')
        self.cart.remove(product_name)


    def show(self):
        for i in self.cart:
            print(f'You have {i} in your cart')


shopping = Cart([])

def run():
    while True:
        answer = input('What do you want to do? add/delt/show or quit? ')

        if answer.lower() == 'quit':
            shopping.show
            print('Thank you for shopping with us today!')
            break

        elif answer.lower() == 'add':

            shopping.add()

        elif answer.lower() == 'delt':
            shopping.delt()

        elif answer.lower() == 'show':
            shopping.show()



run()
