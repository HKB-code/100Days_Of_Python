from logo import logo
print("Welcome to the secret blind auction")
print(logo)

# final_bid = {}
# def add_bid():
#     name = input("What is your name?")
#     bid = int(input("What is your bid?"))
#     final_bid[name] = bid





# should_continue = False
# add_bid()
# while not should_continue:
    
#     another_user = input("Are there any other bidders? Type 'yes' or 'no'")
#     if another_user == 'yes':
#         add_bid()
#     else:
#         high_bid = 0
#         key_name = ""
#         for key ,values in final_bid.items():
#             if final_bid[key]>high_bid:
#                 high_bid = final_bid[key]
#                 key_name = key
#         print(f"The winner is {key} with a bid of {high_bid}")
#         should_continue = True




# //////////////

final_bid = {}
should_continue=True
def add_Bid():
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  bid_data = {
      name:bid
     }
  final_bid.update(bid_data)

while should_continue:
  add_Bid()
  extra= input("Are there any other bidders? Type 'yes or 'no'.\n").lower() 
  if( extra=='no'):
     bidder_name=""
     max_bid = 0
     for key in final_bid:
       bid_amount = final_bid[key]
       if bid_amount>max_bid:
         max_bid=bid_amount
         bidder_name = key
         
     print(f"The winner is {bidder_name} with a bid of ${max_bid}")
    
     should_continue=False