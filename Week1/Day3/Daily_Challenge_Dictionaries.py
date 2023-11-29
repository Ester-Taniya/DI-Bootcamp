'''____________Daily Challenge: Dictionaries_____________________________________________________________'''

#_______Challenge 1 ______________
word = input("Enter a word: ")

letter_indexes = {}
for index, letter in enumerate(word):
    letter = str(letter)
    letter_indexes.setdefault(letter, [])
    letter_indexes[letter].append(index)

print(letter_indexes)

#______________________


#______Challenge 2____
#1
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
can_afford = []


wallet = "$300"
wallet_amount = int(wallet.replace('$', '').replace(',', ''))

for item, price in items_purchase.items():
    price_amount = int(price.replace('$', '').replace(',', ''))

    if price_amount <= wallet_amount :
        can_afford.append(item)
        wallet_amount -= price_amount

print(can_afford)
#2
can_afford.sort()
print(can_afford)

 #3
if len(can_afford) == 0:
    print('Nothing')
else: print(can_afford)


