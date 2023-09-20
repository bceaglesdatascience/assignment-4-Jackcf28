def add_tax(oldcosts,tax):
    for index,cost in enumerate(oldcosts):
        cost=cost*tax+cost
        cost=round(cost,1)
        oldcosts[index]=cost
    return oldcosts

number=int(input("Number of purchases: "))
sales=float(input("Sales tax: "))

customers=[]
costs=[]
for i in range(number):
    customers.append(input("Customer: "))
    costs.append(int(input("Cost: ")))

add_tax(costs,sales)

book={}
for i in range(len(customers)):
    if customers[i] not in book:  
        book[customers[i]]=costs[i]
    else:
        book[customers[i]]=costs[i]+book[customers[i]]

print(book)

