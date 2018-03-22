time_spend = []
answer = ""
x = 0
while True:
  if x == 5:
    break
  print ("adding arive and leave date")
  print ("arive date")
  arive = int(input())
  print ("leave date")
  leave = int(input())
  time_in_eu = leave - arive + 1
  time_spend.append(time_in_eu)
  print ("add more data?")
  answer = input()
  if answer == "no":
    break
  elif answer == "yes":
    continue
  else: 
    while answer != "no" or answer != "yes":
      print ("Print Yes or No")
      answer = input()
      if answer == "no":
        x = 5
        break
      elif answer == "yes":
        break
print ("yspex")
print (time_spend)