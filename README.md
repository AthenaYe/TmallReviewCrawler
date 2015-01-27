# TmallReviewCrawler
A small product review crawler, taking thoughts from lidongone/Spider_on_Tianmao_and_Taobao.git

## Dependencies

`pip install requests`

## Usage

```
./main.py -h
usage: main.py [-h] [--debug] {get-proxies,tmall} ...

Crawl comments from Tmall

optional arguments:
  -h, --help           show this help message and exit
  --debug              Print debug info

Subcommands:
  {get-proxies,tmall}
    get-proxies        Get proxy list
    tmall              Get tmall comments for a item
```

### Get proxy list

```
./main.py get-proxies
```

### Crawl Tmall comments

```
./main.py tmall <item_id>
```
