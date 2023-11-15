import json
import random

from dataLists import *


# generate 2000 random data entries
data = []
for i in range(1, 10001):
    name = random.choice(male_names + female_names) + " " + random.choice(last_names) + " " + random.choice(last_names)
    sex = "varon" if name.split()[0] in male_names else "mujer"
    city = random.choice(cities)
    k = min(random.randint(2, 5), len(interests))
    interests_list = random.sample(interests, k=k)
    image = random.choice(image_man) if name.split()[0] in male_names else random.choice(image_woman)
    data.append({
        "id": i,
        "name": name,
        "sex": sex,
        "city": city,
        "interests": interests_list,
        "imgUrl": image
    })

# write the data to a JSON file
with open("../data/data.json", "w") as f:
    json.dump(data, f)