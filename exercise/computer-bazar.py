print("======================================================")
print("====================Computer Bazar====================")
print("1.Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:50000)")
print("======================================================")
product_name = ''
dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
deliver_price = 0
packing_price = 0
tax_amount = 0
option = int(input("Enter your option:"))
if option == 1:
    product_name = "Dell"
    quantity = int(input("Enter quantity:"))
    dell_price = quantity * 20000
elif option == 2:
    product_name = "Toshiba"
    quantity = int(input("Enter quantity:"))
    toshiba_price = quantity * 30000
elif option == 3:
    product_name = "Mac"
    quantity = int(input("Enter quantity:"))
    mac_price = quantity * 50000
else:
    print("Invalid option")
    exit()

print("========Delivery Option========")
print("1.Home Delivery(Rs:1000) 2.Pickup(Free)")

delivery_option = int(input("Enter your option:"))
if delivery_option == 1:
    deliver_price = 1000

print("====Packing Option====")
print("1.Plastic Bag(Rs:1000) 2.Bag(Rs:2000) 3.Gift Box(Rs:5000) 4.No Packing(Free)")
packing_option = int(input("Enter your option:"))
if packing_option == 1:
    packing_price = 1000
elif packing_option == 2:
    packing_price = 2000
elif packing_option == 3:
    packing_price = 5000

total_price = dell_price + toshiba_price + mac_price
print("==============Location==============")
print("1.Kathmandu(13% tax) 2.Lalitpur(free) 3.Bhaktapur(free)")
location = int(input("Enter your option:"))
if location == 1:
    tax_amount = total_price * 0.13

grand_total = total_price + deliver_price + packing_price + tax_amount

print("==============Bill==============")
print("Product Name:", product_name)
print("Quantity:", quantity)
print("Total Price:", total_price)
print("Tax Amount:", tax_amount)
print("Grand Total:", grand_total)
