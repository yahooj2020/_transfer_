
import requests
url = "https://github.com/scrapy/scrapy/blob/master/extras/qpsclient.py"

import re
res = requests.get(url)
# print(res.text)

pattern_str = '<div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  gist-border-0">(.*?)<details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">'

pattern  = re.compile(pattern_str,re.S)
items = re.findall(pattern,res.text)
print(items[0])
# <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  gist-border-0">(.*?)<details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">


