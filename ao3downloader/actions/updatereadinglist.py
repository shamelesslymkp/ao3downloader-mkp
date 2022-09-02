import itertools
import os
import requests
import traceback

import ao3downloader.actions.shared as shared
import ao3downloader.ao3 as ao3
import ao3downloader.fileio as fileio
import ao3downloader.strings as strings
import ao3downloader.update as update

from tqdm import tqdm


def action():

    folder = fileio.setting(
        strings.UPDATE_PROMPT_INPUT, 
        strings.SETTINGS_FILE_NAME, 
        strings.SETTING_UPDATE_FOLDER)

    update_filetypes = shared.get_update_types()
    download_filetypes = shared.get_download_types()

    print(strings.AO3_PROMPT_IMAGES)
    images = True if input() == strings.PROMPT_YES else False

    session = requests.sessions.Session()
    shared.ao3_login(session)    

    print(strings.UPDATE_INFO_FILES)

    fics = shared.get_files_of_type(folder, update_filetypes)
    
    print(strings.UPDATE_INFO_NUM_RETURNED.format(len(fics)))

    print(strings.UPDATE_INFO_URLS)

    logfile = shared.get_readinglogfile() # mkp - use reading list log file instead of general log file

    works = []
    for fic in tqdm(fics):
        try:
            work = update.process_file(fic['path'], fic['filetype'])
            if work:
                works.append(work)
                fileio.write_log(logfile, {'message': strings.MESSAGE_INCOMPLETE_FIC, 'path': fic['path'], 'link': work['link']})
        except Exception as e:
            fileio.write_log(logfile, {'message': strings.ERROR_INCOMPLETE_FIC, 'path': fic['path'], 'error': str(e), 'stacktrace': traceback.format_exc()})    

    # remove duplicate work links. take lowest number of chapters.
    works_cleaned = []
    works_sorted = sorted(works, key=lambda x: x['link'])
    for link, group in itertools.groupby(works_sorted, lambda x: x['link']):
        chapters = min(group, key=lambda x: x['chapters'])['chapters']
        works_cleaned.append({'link': link, 'chapters': chapters})

    print(strings.UPDATE_INFO_URLS_DONE)

    print(strings.UPDATE_INFO_DOWNLOADING)

    fileio.make_dir(strings.READING_LIST_FOLDER_NAME) # mkp - use reading list downloads folder instead of general downloads folder

    for work in tqdm(works_cleaned):
        ao3.update(work['link'], download_filetypes, strings.READING_LIST_FOLDER_NAME, logfile, session, work['chapters'], images) # mkp - use reading list downloads folder instead of general downloads folder

    session.close()
