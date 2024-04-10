# Svirshch Daniil 
product_name_check = 0
product_price_check = 0

# import random??
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
Products = []

import json
Products_file = open('Products.json')
Products = json.load(Products_file)
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    print("1. Add a new product.")
    print("2. Clear your basket")
    print("3. Show your basket.")
    print("4. Discount")
    command = input("\nChoose command: ")
    if command == "1":
        product_name_check = 0
        product_price_check = 0
        product_name = ''
        product_price = ''
        while product_name_check == 0:
            product_name = input("Enter product name: ")
            if len(product_name) <= 2:
                print("Nope")
            elif len(product_name) >= 120:
                print("Nope")
            else:
                product_name_check =+ 1
        while product_price_check == 0:    
            product_price = input("Enter the price of product: ")
            if float(product_price) <= 0:
                print("Nope")
            elif float(product_price) >= 9999:
                print("Nope")
            else:
                product_price_check =+ 1
        dictionary = {
        "Name": product_name,
        "Price": product_price,
        }
        Products.append(dictionary)
        pass
    if command == "2":
        print("Do you want to clear it fully or only one product?")
        print("If fully type 0, else type 1")
        only_one = input()
        if float(only_one) == 0:
            Products.clear()
        elif float(only_one) == 1:
            indexx = input("Enter the index: ")
            del Products[int(indexx)]
            pass
    if command == "3":
      print([Products[0:20]])
      pass  
      if command == "4":
          pass

    with open("Products.json", "w") as outfile:
        json.dump(Products, outfile)
