# Instagram-comments-crawler
## description
Crawl Instagram comments using GET request.

Without Selenium, it uses the way browser requests to get comments. 

--> fast, simple and stable.

It does not crawl reply. Crawl "comments" ONLY

(개발목적: 인스타그램 댓글 이벤트 추첨)

## prerequisites
- python 3.8
- requests
- tqdm

## changeable parameters
```
# Seconds to sleep btw each crawling iteration (to prevent DDoS) 
WAIT = 3
# Batch size of crawling (Max 50)
CRAWL_SIZE = 50
```

## usage

```bash
## give "postfix URL" of your target post as python arg
## if URL of your post is "https://www.instagram.com/p/B-TvKr_gHNm/"
python3 crawl_comments.py B-TvKr_gHNm
```
## output
TSV format with columns of user-ID and comment.

```
id1 comment1
id2 comment2
id3 comment3
id4 commnet4
...
```
