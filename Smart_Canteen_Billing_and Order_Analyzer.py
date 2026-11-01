#Smart Canteen Billing and Order Analyzer
print("======SMART CANTEEN======")
Veg_Sandwich=60
Masala_Dosa=80
Chole_Rice=85
Paneer_Roll=100
Tea=20
#display menu
print("\n1.Veg Sandwich-Rs.60")
print("2.Masala Dosa-Rs.80")
print("3.Chole Rice-Rs.85")
print("4.Paneer Roll-Rs.100") 
print("5.Tea-Rs.20")
total_price=0
count=0
receipt=" "
while True:
  choice=int(input("choose item number:"))
  if  choice==1:
        item="Veg Sandwich"
        price=60
  elif choice==2:
        item="Masala Dosa"
        price=80
  elif choice==3:
        item="Chole Rice"
        price=85
  elif choice==4:
        item="Paneer Roll"
        price=100
  elif choice==5:
        item="Tea"
        price=20
  else:
       print("invalid choice!")
       continue
  quantity=int(input("enter the quantity:"))
  if quantity<=0:
      print("invalid quantity!")
      continue

  cost=price*quantity
  total_price+=cost
  count+=1
 
  receipt+=f"{item}X{quantity}:Rs{cost:.2f}\n"
  print(f"Added:{item}X{quantity}:Rs.{cost:.2f}")
  again=input("add another item? (yes/no):").lower() 
  if again=="no":
      break
if total_price==0:
       print("no order placed:")
else:

   if total_price>=500:
        discount=total_price*0.10
   elif total_price>=250:
        discount=total_price*0.05
   else:
        discount=0                                                  
   final_total=total_price-discount
   #display receipt
   print("\n=======RECEIPT=======")
   print(receipt,end="")

   print(f"total_price:Rs{total_price:.2f}")
   print(f"Discount:Rs{discount:.2f}")    
   print(f"Final total:Rs{final_total:.2f}")
   print("Thank you!")