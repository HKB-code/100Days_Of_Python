from logo import logo

def ceaser(original_text,shift_amount,encode_or_decode):
    alpha_list = [ chr(i) for i in range(ord("a") ,ord("z")+1)]
    if encode_or_decode =="decode":
        shift_amount*=-1
    shift_text = ""
    for letter in original_text:
        if letter in alpha_list:
             ind = alpha_list.index(letter)
             shift_position = shift_amount + ind
             shift_position%=len(alpha_list)
             shift_text += alpha_list[shift_position]
        else:
            shift_text+=letter
    print(f"Here is the {encode_or_decode}d message is : {shift_text}")

should_continue = True

while should_continue:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your Message...\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)
  
  restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
  if restart =='no':
    should_continue=False
    print("Bye..")
