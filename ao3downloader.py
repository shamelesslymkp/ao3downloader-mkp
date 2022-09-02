import ao3downloader.strings as strings

from ao3downloader.actions import ao3download
from ao3downloader.actions import pinboarddownload
from ao3downloader.actions import updatefics
from ao3downloader.actions import ao3readinglist # mkp - add reading list action
from ao3downloader.actions import updatereadinglist # mkp - add update reading list action
from ao3downloader.actions import ao3bookmarks # mkp - add bookmarks action
from ao3downloader.actions import ao3subscriptions # mkp - add subscriptions action
from ao3downloader.actions import redownload
from ao3downloader.actions import logvisualization
from ao3downloader.actions import readinglogvisualization # mkp - add reading log visualization action
from ao3downloader.actions import updateseries
from ao3downloader.actions import getlinks


def ao3_download_action():
    ao3download.action()


def links_only_action():
    getlinks.action()


def update_epubs_action():
    updatefics.action()


def update_readinglist_action(): # mkp - add update reading list definitions
	updatereadinglist.action()
	
def ao3_readinglist_action(): # mkp - add reading list definitions
	ao3readinglist.action()

def ao3_bookmarks_action(): # mkp - add bookmarks definition
	ao3bookmarks.action()
	
def ao3_subscriptions_action(): # mkp - add subscriptions definition
	ao3subscriptions.action()


def update_series_action():
    updateseries.action()
    

def re_download_action():
    redownload.action()


def pinboard_download_action():
    pinboarddownload.action()


def log_visualization_action():
    logvisualization.action()

def readinglog_visualization_action(): # mkp - add reading log visualization definition
	readinglogvisualization.action()

def display_menu():
    print(strings.PROMPT_OPTIONS)
    for key, value in actions.items():
        try:
            desc = value.description
        except AttributeError:
            desc = value.__name__
        print(' {}: {}'.format(key, desc))


def choose(choice):
    try:
        function = actions[choice]
        try:
            function()
        except Exception as e:
            print(str(e))
    except KeyError as e:
        print(strings.PROMPT_INVALID_ACTION)


display_menu.description = strings.ACTION_DESCRIPTION_DISPLAY_MENU
ao3_download_action.description = strings.ACTION_DESCRIPTION_AO3
update_epubs_action.description = strings.ACTION_DESCRIPTION_UPDATE
ao3_readinglist_action.description = strings.ACTION_DESCRIPTION_READINGLIST # mkp - add reading list action description
update_readinglist_action.description = strings.ACTION_DESCRIPTION_UPDATE_READINGLIST # mkp - add update reading list action description
ao3_bookmarks_action.description = strings.ACTION_DESCRIPTION_BOOKMARKS # mkp - add bookmarks action description
ao3_subscriptions_action.description = strings.ACTION_DESCRIPTION_SUBSCRIPTIONS # mkp - add subscriptions action description
pinboard_download_action.description = strings.ACTION_DESCRIPTION_PINBOARD
log_visualization_action.description = strings.ACTION_DESCRIPTION_VISUALIZATION
readinglog_visualization_action.description = strings.ACTION_DESCRIPTION_READINGLOG_VISUALIZATION # mkp - add reading log visualization description
re_download_action.description = strings.ACTION_DESCRIPTION_REDOWNLOAD
update_series_action.description = strings.ACTION_DESCRIPTION_UPDATE_SERIES
links_only_action.description = strings.ACTION_DESCRIPTION_LINKS_ONLY

QUIT_ACTION = 'q'
MENU_ACTION = 'd'

actions = {
    MENU_ACTION: display_menu,
    'a': ao3_download_action,	
	'h': ao3_readinglist_action, # mkp - add download reading list action
	'x': ao3_subscriptions_action, # mkp - add download subscriptions action
	'b': ao3_bookmarks_action, # mkp - add download bookmarks action
    'l': links_only_action,
    'u': update_epubs_action,
	'w': update_readinglist_action, # mkp - add update reading list action
    's': update_series_action,
    'r': re_download_action,
    'p': pinboard_download_action,
    'v': log_visualization_action,
	'z': readinglog_visualization_action # mkp - add reading log visualization action
    }

display_menu()

while True:
    print('\'{}\' to display the menu again'.format(MENU_ACTION))
    print('please enter your choice, or \'{}\' to quit:'.format(QUIT_ACTION))
    choice = input()
    if choice == QUIT_ACTION: break
    choose(choice)
