import ao3downloader.fileio as fileio
import ao3downloader.strings as strings

username = fileio.get_setting(
    strings.SETTINGS_FILE_NAME, 
    strings.SETTING_USERNAME)

readinglist_url = f'https://archiveofourown.org/users/{username}/readings?show=to-read'
bookmarks_url = f'https://archiveofourown.org/users/{username}/bookmarks'
subscriptions_url = f'https://archiveofourown.org/users/{username}/subscriptions'