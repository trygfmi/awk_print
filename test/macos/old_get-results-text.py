# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/macos/get-results-text.py


import time
from lxml import html
import subprocess


start_time=time.time()

search_details_code = '//details//code'
repository = "test/html/"+subprocess.run("ls -1t test/html | sed -n '1p'", shell=True, capture_output=True, text=True).stdout.strip()
# 1. 保存しておいたHTMLファイルを読み込む
with open(repository, "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
results = tree.xpath(search_details_code)

# 結果を確認
print(f"見つかった数: {len(results)}")
for i, el in enumerate(results, 1):
    print(f"{i}個目")
    print(f"{el.text_content()}")
    # print(el.text_content())
    # print(html.tostring(el, encoding="unicode"))
    print()

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



