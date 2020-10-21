from venmo_api import Client
import emoji
import regex
import string
import sys
from unicodedata import category
import json
from venmo_api.models.exception import HttpCodeError
import time

# friends = venmo.user.get_user_friends_list(user = user)
venmo = None
venmo_config = None
user = None


def read_config():
    with open("sensitive.txt", "r") as handle:
        data = handle.read()

    # reconstructing the data as dictionary
    global venmo_config
    venmo_config = json.loads(data)
    handle.close()

    if venmo_config.get("access_token") is None:
        if venmo_config.get("username") is None or venmo_config.get("password") is None:
            print("USERNAME AND PASSWORD MUST BE SET")
            sys.exit()
        access_token = Client.get_access_token(
            username=venmo_config["username"], password=venmo_config["password"]
        )
        venmo_config["access_token"] = access_token
        with open("sensitive.txt", "w") as handle:
            json.dump(venmo_config, handle)
        handle.close()
    print(venmo_config)


def set_user():
    print(venmo_config)
    global venmo
    venmo = Client(access_token=venmo_config["access_token"])
    global user
    user = venmo.user.get_my_profile()


def all_words():
    phrase_list = []
    print(f"***{user.username}***")
    phrase_list.extend(words_for_user(user.id))
    friends = venmo.user.get_user_friends_list(user=user)
    for friend in friends[:10]:
        print(f"***{friend.username}***")
        phrase_list.extend(words_for_user(friend.id))
    return phrase_list


def words_for_user(user_id, limit=51):
    phrase_list = []
    try:
        count = 0
        before_id = None
        while count < limit:
            fetch_size = limit - count
            if fetch_size > 50:
                fetch_size = 50
            print(f"fetching {count + 1} to {count + fetch_size}")

            transactions = venmo.user.get_user_transactions(
                user_id=user_id, count=fetch_size, before_id=before_id
            )

            for transaction in transactions:
                count += 1
                print(transaction.note)
                split_transaction = transaction.note.split(" ")
                for word in split_transaction:
                    phrase_list.append(word)
                before_id = transaction.id

            if len(transactions) < fetch_size:
                break
    except HttpCodeError as e:
        print(f"{user.username} Error processing transaction info: {str(e)}")
    return phrase_list


def process_text_to_dict(arr):
    most_common = dict()
    for word in arr:
        most_common[word] = most_common.get(word, 0) + 1
    return most_common


def sort_most_common(text_dict):
    common_sorted = sorted(
        text_dict.items(), key=lambda item: item[1], reverse=True
    )  # add on [:10] if you want short list
    common_list = []
    for k, v in common_sorted:
        print(f"{k}:{v}")
        common_list.append([k, v * 20])
    return common_list


def split_count(text):
    emoji_list = []
    data = regex.findall(r"\X", text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    return emoji_list


def create_emoji_dict(count_dict):
    # go to dictionary key
    # parse out emojis from dictionary key and add them to new dict
    # add count from original dictionary to new emoji dictionary for each emoji
    emoji_dict = dict()
    for word in count_dict.keys():
        # print(word, end="    , data: ")
        data = regex.findall(r"\X", word)
        # print(data, end=",   graphemes: ")
        for grapheme in data:
            # print(grapheme, end=", encoding: ")
            # print(grapheme.encode("raw_unicode_escape"), end=",  ")
            if any(char in emoji.UNICODE_EMOJI for char in grapheme):
                emoji_dict[grapheme] = emoji_dict.get(grapheme, 0) + count_dict[word]
        # print()
    return emoji_dict


def execute_most_common():
    read_config()
    set_user()

    word_list = all_words()
    word_count_dict = process_text_to_dict(word_list)
    common_list = sort_most_common(word_count_dict)
    return common_list


def execute_emoji_list():
    read_config()
    set_user()

    word_list = all_words()
    # word_list = words_for_user(user.id)
    word_count_dict = process_text_to_dict(word_list)
    emoji_dict = create_emoji_dict(word_count_dict)
    sorted_emoji_list = sort_most_common(emoji_dict)
    return sorted_emoji_list


def execute():
    read_config()
    set_user()

    word_list = all_words()
    # word_list = words_for_user(user.id)
    word_count_dict = process_text_to_dict(word_list)
    sorted_count_list = sort_most_common(word_count_dict)
    emoji_dict = create_emoji_dict(word_count_dict)
    sorted_emoji_list = sort_most_common(emoji_dict)


if __name__ == "__main__":
    execute_most_common()
    # execute()


# most common word (kinda complete, need to add skip phrases)
# most common emoji (complete)
# 5 most common words not in dictionary
# Those 5 words defined by urban dictionary

# IF TIME:
# average transaction size
# most active transaction day of the week
# "Venmo best friend" and total # of transactions w this person


# def print_transactions(transactions_list):
#     for transaction in transactions_list:
#         print(f"{friends[0].first_name} said this in a note: {transaction.note}")

# # callback is optional. Max number of transactions per request is 50.
# venmo.user.get_user_transactions(user_id=friends[0].id,
#                                      callback=print_transactions)
