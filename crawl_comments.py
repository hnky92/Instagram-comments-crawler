import requests, json
import sys, time
from tqdm import tqdm

SHORTCODE = sys.argv[1]

QUERY_HASH = "bc3296d1ce80a24b1b6e40b1e72903f5"
WAIT = 3
CRAWL_SIZE = 50

cursor = ''
has_next_page = True
comments =[]
while True:
    variables = {"shortcode":SHORTCODE, "first":CRAWL_SIZE, "after":cursor}
    query = 'https://www.instagram.com/graphql/query/?query_hash='+QUERY_HASH+'&variables='+json.dumps(variables)
    
    ## req 
    res = requests.get(query).json()
    
    ## update page info
    page_info = res['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']
    tot = res['data']['shortcode_media']['edge_media_to_parent_comment']['count']
    cursor = page_info['end_cursor']
    has_next_page = page_info['has_next_page']

    ## iterate edge
    for edge in tqdm(res['data']['shortcode_media']['edge_media_to_parent_comment']['edges']):
        comments.append((edge['node']['owner']['username'],edge['node']['text']))
	
    print('total crawled : ', str(len(comments)), '  remain:',str(tot-len(comments)))
	
    if has_next_page == False:
	    break

    ## prevent DDoS
    time.sleep(WAIT)
    

with open('out.tsv','w',encoding='utf-8') as f_out:	
    for comment in comments:
        f_out.write(comment[0] + '\t' + comment[1].replace('\n','') +'\n')

