from pathlib import Path
import time
import json

import cv2
import easyocr
import matplotlib.pyplot as plt 

## Automation Steps
#       
#   Load Database
#   Read Card Text
#   Store Card Text + Confidence
#   Get Matching Field in DB with Card Text
#   Store Matching Field Data in DICT
#   Write to own DB
#

class ValidationError(Exception):
    pass

####################################################################
'''
Load and Read JSON Database
'''

# read DB
db_path = str(Path.cwd() / 'db' / 'scryfall-bulk-data.json')
print(db_path)

try:
    with open(db_path, "r", encoding='utf-8') as json_file:
        db_data = json.load(json_file)
    print(f"Success with reading file")

except (FileNotFoundError, json.decoder.JSONDecodeError):
    raise ValidationError(f'Unable to load the JSON file.')


# read scanned DB
scanned_card_db_path = str(Path.cwd() / 'db' / 'scanned_card_data.json')
print(scanned_card_db_path)

try:

    with open(scanned_card_db_path, "r") as scanned_card_json_file:
        scanned_card_data = json.load(scanned_card_json_file)
    print(f"Success with reading file")

except (FileNotFoundError, json.decoder.JSONDecodeError):
    raise ValidationError(f'Unable to load the JSON file.')





# ####################################################################
'''
Read Card Text
'''

'''
Store Card Text + Confidence
'''


# # Record the start time
# start_time = time.time()

# # read img
# img_name = "img_03.jpg"
# img_path = str(Path.cwd() / 'images' / img_name)

# # Read only a section of the image (you can adjust these values)
# x, y, w, h = 0, 0, 5000, 1000
# my_img = cv2.imread(img_path)[y:y+h, x:x+w]

# # instance text detector
# reader = easyocr.Reader(['en'], gpu=False)

# # detect text on img
# my_text = reader.readtext(my_img)

# threshold = 0.25

# # draw bbox and text
# for t in my_text:
#     print(t)

#     bbox, text, score =  t

# #     if score > threshold:
# #         cv2.rectangle(my_img, bbox[0], bbox[2], (0, 255, 0), 10)
# #         cv2.putText(my_img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 15)
# #         cv2.putText(my_img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)

# # plt.imshow(cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB))

# # Record the end time
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Time elapsed: {elapsed_time} seconds")

# # plt.show()



# ####################################################################
    
'''
Get Matching Field in DB with Card Text
'''

# Specify the variable name you are looking for
desired_variable_name = "Legolas's Quick Reflexes"  # Replace with the variable name you are looking for

# Find the card with the specified variable name
matching_card = None
for card_entry in db_data:
    card_name = card_entry.get("name", "").strip()
    if card_name == desired_variable_name:
        matching_card = card_entry
        break


'''
Store Matching Field Data in DICT
'''

DICT_card_info = {}

# Display the results
if matching_card:

    DICT_card_info[matching_card.get('name')] = {
        'USD Price': matching_card.get('prices', {}).get('usd'),
        'Rarity': matching_card.get("rarity"),
        'URL Link': matching_card.get("scryfall_uri"),
    }
    
else:
    print(f"No card found with the name: {desired_variable_name}")

print(DICT_card_info)



'''
Write to own DB
'''

# Update scanned_card_db_path in the JSON file

scanned_card_data.update(DICT_card_info)

with open(scanned_card_db_path, "w") as json_file:
        json.dump(scanned_card_data, json_file, indent=4)  # The indent parameter adds pretty-printing for better readability





#  {"object":"card","id":"07c42262-6291-43df-ba34-83e462ab56b6","oracle_id":"c65ba242-3369-48a9-864f-1b1f85238f67","multiverse_ids":[],"tcgplayer_id":496186,"name":"Emmara, Soul of the Accord","lang":"en","released_at":"2020-09-26","uri":"https://api.scryfall.com/cards/07c42262-6291-43df-ba34-83e462ab56b6","scryfall_uri":"https://scryfall.com/card/plst/GRN-168/emmara-soul-of-the-accord?utm_source=api","layout":"normal","highres_image":true,"image_status":"highres_scan","image_uris":{"small":"https://cards.scryfall.io/small/front/0/7/07c42262-6291-43df-ba34-83e462ab56b6.jpg?1684198134","normal":"https://cards.scryfall.io/normal/front/0/7/07c42262-6291-43df-ba34-83e462ab56b6.jpg?1684198134","large":"https://cards.scryfall.io/large/front/0/7/07c42262-6291-43df-ba34-83e462ab56b6.jpg?1684198134","png":"https://cards.scryfall.io/png/front/0/7/07c42262-6291-43df-ba34-83e462ab56b6.png?1684198134","art_crop":"https://cards.scryfall.io/art_crop/front/0/7/07c42262-6291-43df-ba34-83e462ab56b6.jpg?1684198134","border_crop":"https://cards.scryfall.io/border_crop/front/0/7/07c42262-6291-43df-ba34-83e462ab56b6.jpg?1684198134"},"mana_cost":"{G}{W}","cmc":2.0,"type_line":"Legendary Creature — Elf Cleric","oracle_text":"Whenever Emmara, Soul of the Accord becomes tapped, create a 1/1 white Soldier creature token with lifelink.","power":"2","toughness":"2","colors":["G","W"],"color_identity":["G","W"],"keywords":[],"all_parts":[{"object":"related_card","id":"20a9bda0-5673-4071-9201-83670a317f8a","component":"token","name":"Soldier","type_line":"Token Creature — Soldier","uri":"https://api.scryfall.com/cards/20a9bda0-5673-4071-9201-83670a317f8a"},{"object":"related_card","id":"07c42262-6291-43df-ba34-83e462ab56b6","component":"combo_piece","name":"Emmara, Soul of the Accord","type_line":"Legendary Creature — Elf Cleric","uri":"https://api.scryfall.com/cards/07c42262-6291-43df-ba34-83e462ab56b6"}],"legalities":{"standard":"not_legal","future":"not_legal","historic":"legal","timeless":"legal","gladiator":"legal","pioneer":"legal","explorer":"legal","modern":"legal","legacy":"legal","pauper":"not_legal","vintage":"legal","penny":"legal","commander":"legal","oathbreaker":"legal","standardbrawl":"not_legal","brawl":"legal","alchemy":"not_legal","paupercommander":"not_legal","duel":"legal","oldschool":"not_legal","premodern":"not_legal","predh":"not_legal"},"games":["paper"],"reserved":false,"foil":false,"nonfoil":true,"finishes":["nonfoil"],"oversized":false,"promo":false,"reprint":true,"variation":false,"set_id":"67e47ba2-b019-4181-9005-fe9fc021de44","set":"plst","set_name":"The List","set_type":"masters","set_uri":"https://api.scryfall.com/sets/67e47ba2-b019-4181-9005-fe9fc021de44","set_search_uri":"https://api.scryfall.com/cards/search?order=set&q=e%3Aplst&unique=prints","scryfall_set_uri":"https://scryfall.com/sets/plst?utm_source=api","rulings_uri":"https://api.scryfall.com/cards/07c42262-6291-43df-ba34-83e462ab56b6/rulings","prints_search_uri":"https://api.scryfall.com/cards/search?order=released&q=oracleid%3Ac65ba242-3369-48a9-864f-1b1f85238f67&unique=prints","collector_number":"GRN-168","digital":false,"rarity":"rare","watermark":"selesnya","flavor_text":"\"Whatever hatred destroys, a single act of trust can revive.\"","card_back_id":"0aeebaf5-8c7d-4636-9e82-8c27447861f7","artist":"Mark Winters","artist_ids":["3d8a379d-f4e8-440d-99d5-5ec107757348"],"illustration_id":"c9286244-cb23-44a0-bfd3-f44351516def","border_color":"black","frame":"2015","frame_effects":["legendary"],"security_stamp":"oval","full_art":false,"textless":false,"booster":false,"story_spotlight":false,"edhrec_rank":5246,"penny_rank":2728,"prices":{"usd":"0.37","usd_foil":null,"usd_etched":null,"eur":null,"eur_foil":null,"tix":null},"related_uris":{"tcgplayer_infinite_articles":"https://tcgplayer.pxf.io/c/4931599/1830156/21018?subId1=api&trafcat=infinite&u=https%3A%2F%2Finfinite.tcgplayer.com%2Fsearch%3FcontentMode%3Darticle%26game%3Dmagic%26partner%3Dscryfall%26q%3DEmmara%252C%2BSoul%2Bof%2Bthe%2BAccord","tcgplayer_infinite_decks":"https://tcgplayer.pxf.io/c/4931599/1830156/21018?subId1=api&trafcat=infinite&u=https%3A%2F%2Finfinite.tcgplayer.com%2Fsearch%3FcontentMode%3Ddeck%26game%3Dmagic%26partner%3Dscryfall%26q%3DEmmara%252C%2BSoul%2Bof%2Bthe%2BAccord","edhrec":"https://edhrec.com/route/?cc=Emmara%2C+Soul+of+the+Accord"},"purchase_uris":{"tcgplayer":"https://tcgplayer.pxf.io/c/4931599/1830156/21018?subId1=api&u=https%3A%2F%2Fwww.tcgplayer.com%2Fproduct%2F496186%3Fpage%3D1","cardmarket":"https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Emmara%2C+Soul+of+the+Accord&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall","cardhoarder":"https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Emmara%2C+Soul+of+the+Accord&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"}},
