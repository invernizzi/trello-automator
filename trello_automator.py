from trello import TrelloApi
import sys

# You can use my API key, or get yours at https://trello.com/1/appKey/generate
API_KEY = 'b51d325ae73a0264377da49c031422cf'


# Initialize Trello
try:
    with open('token.txt') as f:
        TOKEN = f.readlines()[0].strip()
except IOError:
    TOKEN = None
trello = TrelloApi(API_KEY)
if not TOKEN:
    print 'Visit this, and save your token in token.txt'
    print trello.get_token_url('My App', expires='30days', write_access=True)
    sys.exit(0)
trello.set_token(TOKEN)


def get_list_id_from_name(name):
    return [
        l['id']
        for l in trello.boards.get_list('SkHEoGHF')
        if l['name'].startswith(name)][0]


def move_cards(from_list, to_list):
    for card in trello.lists.get_card(from_list):
        trello.cards.update_idList(card['id'], to_list)


later_list = get_list_id_from_name('Later This Week')
tomorrow_list = get_list_id_from_name('Tomorrow')
today_list = get_list_id_from_name('Today')
move_cards(tomorrow_list, today_list)
move_cards(later_list, tomorrow_list)
