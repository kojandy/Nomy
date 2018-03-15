#!/usr/bin/env python
import yaml
from lxml import etree
import requests
import sqlite3
import time

with open('settings.yml') as f:
    settings = yaml.load(f)

def get_prev(conn, url):
    prev = conn.execute('select response from snapshot where url=? order by time desc limit 1', (url,)).fetchone()
    if not prev:
        return None
    else:
        return prev[0]

def notify(msg):
    requests.get(settings['notify']['url'].format(msg=msg))

with sqlite3.connect('data.db') as conn:
    conn.execute('create table if not exists snapshot (id integer primary key, time numeric not null, url text not null, response text)')

    for item in settings['check']:
        re = requests.get(item['url'])
        curr = re.text
        prev = get_prev(conn, item['url'])
        conn.execute('insert into snapshot (time, url, response) values (?, ?, ?)', (time.time(), item['url'], curr))
        exam = [prev, curr]
        exam = [etree.tostring(etree.HTML(x).xpath(item['xpath'])[0]) for x in exam if x]
        if len(exam) == 1:
            notify(settings['notify']['message']['registered'].format(**item))
        else:
            if exam[0] != exam[1]:
                notify(settings['notify']['message']['updated'].format(**item))
