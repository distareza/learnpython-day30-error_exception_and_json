"""
    Learn how to handle an Error or an Exception
"""
fruits = ["Apple", "Pear", "Orange"]


# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit Pie")


make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)

import json

new_data = {
    "Amazon": {
        "email": "my@email.com",
        "password": "K%4bB76&UOd#8)hp"
    }
}

with open("data_test.json", "w") as data_file:
    json.dump(new_data, data_file, indent=4)

with open("data_test.json", "r") as data_file:
    data = json.load(data_file)
    print(type(data))
    print(data)
