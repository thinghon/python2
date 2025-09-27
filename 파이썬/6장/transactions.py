def save_transaction(price,credit_card,description):
    file=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\transaction.txt","a")
    file.write("%16s%07d%16s\n"%(credit_card,price*100,description))
    file.close()