from tabulate import tabulate

products = {
    "milk":40,
    "coffee":50,
    "tea":120,
    "bread":30,
    "chocolate":200
}

def is_expensive (item):
    name,price = item
    if(price > 100):
        return True
    else:
        return False


def apply_discount(item):
    name,price = item
    discounted_price = price*0.8
    return (name,round(discounted_price,2))

exp_tems= filter(is_expensive,products.items())

disc_prices = map(apply_discount,exp_tems)
final_result  = list(disc_prices)
final_result2  = dict(disc_prices)

print (disc_prices)
print (type(disc_prices))
print(dict(disc_prices))
print(list(disc_prices))
print("-------------")
print(final_result)
print(final_result2)


print("------------------")
print(tabulate(final_result,headers=["Product","Price"], tablefmt='github'))