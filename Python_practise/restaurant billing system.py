"""
user :- name
Total number of items
find total
add discount
grand total
"""
# This dictionary contains user information
"""
 => Name
 => Total Number of Items
 => Item details 
 => total Amount
 => Discount Amount
 => Grand Total
"""
user_record = {}

name = input("Enter Your Name : ")
items_list = []

def display():
    print("""
    ================= Food Items =======================
        1. Paneer Tikka ------------------ 199
        2. Paneer Butter Masala ---------- 199
        3. Roti -------------------------- 20
        4. Chole Bhature ----------------- 100
        5. Biryani ----------------------- 90
        6. Masala Dosa ------------------- 110
        7. Gulab Jamun ------------------- 30
    =====================================================
    \n""")

    number_items = int(input("Enter Number of Items : "))
    print()

    for i in range(1,number_items+1):
        choice = int(input(f"Please enter the item number {i} displayed above: "))
        if(choice==1):
            items_list.append(("Paneer Tikka\t",199))
        elif(choice==2):
            items_list.append(("Paneer Butter Masala",199))
        elif(choice==3):
            items_list.append(("Roti\t\t",20))
        elif(choice==4):
            items_list.append(("Chole Bhature\t",100))
        elif(choice==5):
            items_list.append(("Biryani\t",90))
        elif(choice==6):
            items_list.append(("Masala Dosa\t",110))
        elif(choice==7):
            items_list.append(("Gulab Jamun\t",30))
        else:
            print("\nGiven number is Not valid")


    print("\nYour Selected Items : ")
    print("------------------------------\n")
    # print(items_list)
    for i in items_list:
        print("\t*",i[0])

    print()

display()

confirm = input("To confirm enter y : ")

if(confirm == "y"):
    user_record.update({"Name":name ,"Items":items_list})
else:
    display()

print(user_record)

def bill_using_print():
    print(f"""
                        IITM Restaurant
        -----------------------------------------------
        Near New Bus Stant Mathura
        GSTIN  : 21902120G3893H378
        Phone  : +913273989332  
        ------------------------------------------------\n
            Item                         Amt.
        .................................................""")

    total_amount = 0

    for key in user_record:
        if(key=="Items"):
            for item in user_record[key]:
                print("\t",item[0],"\t\t",item[1])
                total_amount += item[1]

    discount_amount = (total_amount*10)/100
    grand_total = total_amount - discount_amount

    print("   .................................................")
    print("\tTotal Amount  \t:\t\t",total_amount)
    print("\tDiscount 10%  \t:\t\t",discount_amount)
    print("\tGrand Total   \t:\t\t",grand_total)
    print("   .................................................")

    print(end="\n\n")

# Handle file using with statement
"""
Syntax:-
---------
with open("fileName.extension" ,"Mode") as filehandler :
    statement
    statement
"""
def bill():
    bill_text = f"""
                    IITM Restaurant
    -----------------------------------------------
    Near New Bus Stant Mathura
    GSTIN  : 21902120G3893H378
    Phone  : +913273989332  
    ------------------------------------------------

        Item                         Amt.
    .................................................
"""

    total_amount = 0

    for key in user_record:
        if key == "Items":
            for item in user_record[key]:
                bill_text += f"\n\t{item[0]}\t\t{item[1]}"
                total_amount += item[1]

    discount_amount = (total_amount * 10) / 100
    grand_total = total_amount - discount_amount

    bill_text += f"""

   .................................................
    Total Amount   \t:      {total_amount}
    Discount 10%   \t:      {discount_amount}
    Grand Total    \t:      {grand_total}
   .................................................

"""

    print(bill_text)
    return bill_text

bill()

bill_data = bill()

with open("customers.txt", "a") as file:
    file.write(bill_data)

