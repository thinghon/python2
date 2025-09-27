print("20224016-박소호")
def save_transaction(price,credit_card,description):
    file=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\transaction.txt","a")
    file.write("%16s%07d%16s/n"%(credit_card,price*100,description))
    file.close()

items = ["DONUT","LATTE","FILTER","MUFFIN"]
prices=[1.50,2.20,1.80,1.20]
running=True

while running:
    option=1
    for choice in items:
        print(str(option)+"."+choice)
        option=option+1
    print(str(option)+".Quit")
    choice=int(input("Choose an option"))
    if choice==option:
        running=False
    else:
        credit_card=input("Credit card number:")
        save_transaction(prices[choice-1],credit_card,items[choice-1])
