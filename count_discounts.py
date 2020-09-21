# Coding question:
# Count the Discounts
# You receive two structures as an input:
#  - A set/list of products, e.g. products = ["car", "burger", "phone"]
#  - A list of transactions, e.g. transactions =
# ["car", "car", "burger", "phone", "car", "phone", "phone", "burger"]
# Imagine a shop selling products given above. That shop has a rule that products having
# the lowest number of sold items at a given point in time are sold with a discount.
# Having a full history of sold items in transactions, calculate the total count of discounts
# that were applied.
#
# Example:
# products: ["car", "burger", "phone"]
# transactions: [*"car", "car", *"burger", *"phone", "car", *"phone", "phone", *"burger"]
# Discounts count = 5

def count_discounts (products, transactions=()):
    count = 0

    prod_dict = dict.fromkeys(products , 0)

    for t in transactions:         
        print(prod_dict)
        if( prod_dict[t] == min(prod_dict.values()) ):
            count += 1            
            print("**** count : " + str(count))

        prod_dict[t] += 1   

    return count

products = ["car", "burger", "phone"]
transactions = ["car", "car", "burger", "phone", "car", "phone", "phone", "burger"]

print("Total discounts: " + str(count_discounts(products, transactions)))
