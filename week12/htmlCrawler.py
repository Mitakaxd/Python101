import requests
from collections.abc import Iterable
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from collections import deque
from sqlalchemy import Table, Column, create_engine, String, MetaData
from sqlalchemy.sql import insert, select
metadata = MetaData()
engine = create_engine('sqlite:///:domainservers:', echo=False)


def get_links_from_site(site):
    q = deque()
    q.append(site)
    links = Table('links', metadata, Column('domain', String, primary_key=True),
                  Column('server', String))
    metadata.create_all(engine)
    conn = engine.connect()
    flag = False
    while len(q) > 0:
        site = q[0]
        q.popleft()
        # get site from queue
        try:
            response = requests.get(site)
            server = response.headers['Server']
        except:
            continue
        # get server for site
        if flag == True:
            insert_query = links.insert()
            conn.execute(insert_query, domain=site, server=server)
        else:
            flag = True
        # insert site in db

        soup = BeautifulSoup(response.text, 'html.parser')
        # beautify

        for link in soup.find_all('a'):  # find a tags in there
            link_to_check = link.get('href')  # get links
            # get only bulgarian links
            if isinstance(link_to_check, Iterable) and 'bg' in link_to_check:
                # strip it of /../..
                final_link = link_to_check.split('.bg')[0] + '.bg/'
               # todo  if final_link not in db
                if 'www.bg' in final_link:
                    continue
                # print(final_link)
                
                s = select([links.c.domain]).where(links.c.domain == final_link)
                result = conn.execute(s)
                site_in_db = result.fetchone()
                print(site_in_db, final_link)
                if (site_in_db == None or site_in_db[0]!=final_link) and (final_link not in q):
                    
                    q.append(final_link)
    #getting everything from DB
    sel_query = select([links])
    result = conn.execute(sel_query)
    result = result.fetchall()
    #Formatting dict style
    data = {}
    for domain, server in result:
        server = server.split('/')[0]
        if server in data.keys():
            data[server] += 1
        else:
            data[server] = 1
    #plotting
    keys = data.keys()
    values = data.values()
    X = list(range(len(keys)))
    plt.rcParams.update({'font.size': 13})
    plt.bar(X, values, align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")
    plt.show()
    plt.savefig("histogram.png")
    

if __name__ == '__main__':
    get_links_from_site('http://www.register.start.bg/')
