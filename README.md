Online Etymology Dictionary Scraper
===================================

A spider that crawls [etymonline.com](https://www.etymonline.com).

forked from @kyleroot

```
class Etymology(Item):
    word = Field()
    origin = Field()
``` 

Example usage with [Scrapy](https://docs.scrapy.org/en/latest/topics/commands.html#command-line-tool):
```
python3 -m venv etymonline
. bin/activate.fish
pip install -r requirements.txt
scrapy crawl etymonline.com -o data.json -t json
```
