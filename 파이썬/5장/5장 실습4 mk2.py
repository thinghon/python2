print("20224016-박소호")
def find_details(id2find):
    surfer_f=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\surfing_data.csv")
    for eachline in surfer_f:
        s={}
        (s['id'],s['name'],s['country'],s['average'],s['board'],s['age'])=eachline.split(";")
        if id2find == int(s['id']):
            surfer_f.close()
            return(s)
    surfer_f.close
    return({})
running = True
while running:
    lookup_id = int(input("Enter the if of the surfer:"))
    surfer=find_details(lookup_id)
    if lookup_id == -1:
        break;
    else:
        if surfer:
            print("ID:          "+surfer['id'])
            print("Name:        "+surfer['name'])
            print("Country:     "+surfer['country'])
            print("Average:     "+surfer['average'])
            print("Board type:  "+surfer['board'])
            print("Age:         "+surfer['age'])
