'''Create an html document for the purpose of visualizing the logfile. Not the most optimized thing ever but it does the job.'''

import json
import os

import ao3downloader.strings as strings

def action():

    keys = ['timestamp'] # always put timestamp first
    data = []

    logfile = os.path.join(strings.LOG_FOLDER_NAME, strings.READINGLOG_FILE_NAME) # mkp - use different logfile
    visfile = os.path.join(strings.LOG_FOLDER_NAME, strings.READINGLOG_VISUALIZATION_FILE_NAME) # mkp - create different logfile

    if not os.path.exists(logfile):
        print(strings.INFO_NO_LOG_FILE)
        return

    with open(logfile, 'r', encoding='utf-8') as f:
        for line in f:
            js = json.loads(line)
            if 'starting' not in js:
                for key in js:
                    if key not in keys:
                        keys.append(key)
                data.append(js)

    for item in data:
        for key in keys:
            if key not in item:
                item[key] = ''

    thead = '<thead><tr>'
    for key in keys:
        thead += '<th>' + key + '</th>'
    thead += '</tr></thead>'

    tbody = '<tbody>'
    for item in data:
        tr = '<tr>'
        for key in keys:
            key_item = str(item[key])
            tr += '<td>' + key_item + '</td>'
        tr += '</tr>'
        tbody += tr
    tbody += '</tbody>'

    table = thead + tbody

    with open(os.path.join(strings.HTML_FOLDER_NAME, strings.TEMPLATE_FILE_NAME), encoding='utf-8') as f:
        template = f.read()

    logvisualization = template.replace('%TABLE%', table)

    with open (visfile, 'w', encoding='utf-8') as f:
        f.write(logvisualization)
