# Instagram-comments-crawler
## description
Crawl Instagram comments using GET request.

Without Selenium, it uses the way browser requests to get comments. --> fast, simple and stable.

It crawls no reply. Crawl 'comments' ONLY

## usage

```bash
## give "postfix URL" of your target post as python arg
## if URL of your post is "https://www.instagram.com/p/B-TvKr_gHNm/"
python3 crawl_comments.py B-TvKr_gHNm
```
## output
TSV format with columns of user-ID and comment.
