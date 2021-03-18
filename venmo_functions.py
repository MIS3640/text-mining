from venmo_api import Client
import emoji
import regex
import string
import sys
from unicodedata import category
import json
from venmo_api.models.exception import HttpCodeError
from venmo_api.models.transaction import Transaction
import time
import pickle

# friends = venmo.user.get_user_friends_list(user = user)
venmo = None
venmo_config = None
user = None
transcations = None

# word cloud lists
wc_word_list = None
wc_emoji_list = None


def read_config():
    """
    Opens sensitive.txt and reads it to data,
    Checks to see if access token already exists, if it does, it does nothing
    If access token does not exist, it generates an access token using username/password credentials (Prompts 2 factor authentication)
    """
    with open("sensitive.txt", "r") as handle:
        data = handle.read()

    # reconstructing the data as dictionary
    global venmo_config
    venmo_config = json.loads(data)

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
    """
    Creates venmo object using access token
    stores user info inside of global variable user
    """
    print(venmo_config)
    global venmo
    venmo = Client(access_token=venmo_config["access_token"])
    global user
    user = venmo.user.get_my_profile()


def get_data():
    """
    Function is currently a work in progress,
    it is supposed to fetch stored data from a
    .txt file
    """
    print("Getting data")
    return fetch_data()
    # saved_data = read_dict("venmo_data.json")

    # if saved_data is None:
    #     saved_data = fetch_data()
    #     print(saved_data)
    #     save_dict(saved_data, "venmo_data.json")

    # return saved_data


def get_users(account_user):
    """
    Creates a dict called users,
    Adds main user to users dict,
    Gets all of main user's friends
    For all key value pairs it sets userid:user(object)
    returns users dict
    """
    # put users in dict  user.id : user
    # return dict
    users = dict()
    users[account_user.id] = account_user
    # add all of the user's friends as key:value (userid:user) to this same dictionary
    for user in venmo.user.get_user_friends_list(user=account_user):
        users[user.id] = user
    return users


def get_user_transcation_data(user_id, limit=50):
    """
    Fetches all transaction data for a specific user,
    takes in a user id and a limit for transactions to pull from account
    Has to take in limit because Venmo only sends back a max of 50
    transactions per request
    returns transactions data
    """
    transactions = None

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

            if len(transactions) < fetch_size:
                break

            count += len(transactions)
            before_id = transactions[-1].id

    except HttpCodeError as e:
        print(f"{user.username} Error processing transaction info: {str(e)}")

    return transactions


def fetch_data(user_limit=10):
    """
    fetches transaction data for each user and stores it in all_data dict
    {user_id:transactions}
    returns all_data
    """
    global user

    users = get_users(user)
    all_data = dict()
    count = 0
    for user_id in users:
        if count > user_limit:
            break
        transactions = get_user_transcation_data(user_id)
        all_data[user_id] = transactions
        count += 1
    return all_data


class TransactionEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def save_dict(data, filename):
    with open(filename, "w") as handle:
        json.dump(data, handle, cls=TransactionEncoder, sort_keys=True, indent=3)


def read_dict(filename):
    with open(filename, "r") as handle:
        data = handle.read()
        if data == "":
            return None
    return json.loads(
        data,
        object_hook=lambda d: Transaction(
            amount=d["amount"], date_created=d["date_created"], note=d["note"]
        ),
    )


def word_list_from_transactions(transactions):
    """
    Splits indiviudal transaction notes into single words
    Adds single words to a list (phrase_list)
    returns phrase_list
    """
    phrase_list = []
    for transaction in transactions:
        print(transaction.note)
        split_transaction = transaction.note.split(" ")
        for word in split_transaction:
            phrase_list.append(word)

    return phrase_list


def all_words(data):
    """
    Calls word_list_from_transactions on all users
    Adds each user's word list to phrase_list
    """
    phrase_list = []

    for user_id, transactions in data.items():
        phrase_list.extend(word_list_from_transactions(transactions))
    return phrase_list
    # for user, transactions in data.items():
    #     print(f"***{user.username}***")
    #     phrase_list.extend(word_list_from_transactions(transactions))
    # return phrase_list


def count_all_words(word_list):
    """
    Creates a dict (most_common) that stores word counts
    {word:# of times it appears}
    returns most_common
    """
    most_common = dict()
    for word in word_list:
        most_common[word] = most_common.get(word, 0) + 1
    return most_common


def sort_by_count(text_dict):
    """
    Takes in a count dictionary, with key value pairs of
    {word(str):count(int)}
    and sorts them in descending order based on count
    returns a sorted list of words
    """
    common_sorted = sorted(
        text_dict.items(), key=lambda item: item[1], reverse=True
    )  # add on [:10] if you want short list
    common_list = []
    for k, v in common_sorted:
        print(f"{k}:{v}")
        common_list.append([k, v * 20])
    return common_list


def split_count(text):
    """
    Finds words that contain emojis and appends the words to a list
    returns list of words that contian emojis
    """
    emoji_list = []
    data = regex.findall(r"\X", text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    return emoji_list


def create_emoji_dict(count_dict):
    """
    Creates a dictionary that counts frequency of each emoji
    Searches for emojis that are made up of multiple emojis (graphemes)
    Adds graphemes to emoji_dict instead of adding all of the separate emojis
    returns emoji_dict
    """
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
    data = get_data()
    word_list = all_words(data)
    word_count_dict = count_all_words(word_list)
    common_list = sort_by_count(word_count_dict)
    return common_list


def execute_emoji_list():
    data = get_data()
    word_list = all_words(data)
    word_count_dict = count_all_words(word_list)
    emoji_dict = create_emoji_dict(word_count_dict)
    sorted_emoji_list = sort_by_count(emoji_dict)
    return sorted_emoji_list


def get_user_info():
    return venmo.user.get_my_profile()


def execute():
    read_config()
    set_user()

    data = get_data()
    word_list = all_words(data)
    word_count_dict = count_all_words(word_list)

    # generate most common word list for word cloud
    global wc_word_list
    wc_word_list = sort_by_count(word_count_dict)

    # generat most common emoji list
    emoji_dict = create_emoji_dict(word_count_dict)
    global wc_emoji_list
    wc_emoji_list = sort_by_count(emoji_dict)


if __name__ == "__main__":
    # execute_most_common()
    execute()
