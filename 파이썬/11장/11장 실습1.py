#20224016-박소호
class Address():
    name=""
    line1=""
    line2=""
    city=""
    state=""
    zip=""


homeAddress=Address()

homeAddress.name="John Smith"
homeAddress.line1="701 N. C Street"
homeAddress.line2="Carver Science Building"
homeAddress.city="Indianola"
homeAddress.state="IA"
homeAddress.zip="50125"

vacationHomeAddress=Address()

vacationHomeAddress.name="John Smith"
vacationHomeAddressline1="1122 Main Street"
vacationHomeAddress.line2=""
vacationHomeAddress.city="Panama City Beach"
vacationHomeAddress.state="FL"
vacationHomeAddress.zip="32407"

def printAddress(address):
    print(address.name)

    if(len(address.line1)>0):
        print(address.line1)

    if(len(address.line2)>0):
        print(address.line2)
    print(address.city+","+address.state+""+address.zip)

printAddress(homeAddress)
print()
printAddress(vacationHomeAddress)