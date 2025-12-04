# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/awk/awk_print/test/macos/execute-article-code.py


import time
from lxml import html
import subprocess
from datetime import datetime


start_time=time.time()

target_os = "macos"
repository_name = "awk_print"
now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
latest_html = "test/html/"+subprocess.run("ls -1t test/html | head -1", shell=True, capture_output=True, text=True).stdout.strip()
print("latest_html:"+latest_html)
search_quickstart_code = '(//code[@class="code-flex"])[2]'
search_procedure_code = '(//code[@class="code-flex"])[10]'
output_quickstart_name = f"auto_quickstart_output{now}.txt"
output_procedure_name = f"auto_procedure_output{now}.txt"

# 1. 保存しておいたHTMLファイルを読み込む
with open(latest_html, "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
quickstart_code = tree.xpath(search_quickstart_code)
quickstart_code_array = quickstart_code[0].text_content().split("\n")
quickstart_cmd = f"""rm -rf test/{target_os}/{repository_name}
i=0
target_directory="test/{target_os}/"
output_file_name={output_quickstart_name}
while IFS= read -r keyword; do
    bash -c "$keyword >> $target_directory/compare-auto/\"$output_file_name\""
    echo >> $target_directory/compare-auto/"$output_file_name"
       
    echo
    i=$(($i+1))
done << 'EOF'
""" + "\n".join(quickstart_code_array) + "\nEOF"
subprocess.run(quickstart_cmd, shell=True)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
procedure_code = tree.xpath(search_procedure_code)
procedure_code_array = procedure_code[0].text_content().split("\n")
procedure_cmd = f"""rm -rf test/{target_os}/{repository_name}
i=0
target_directory="test/{target_os}/"
output_file_name={output_procedure_name}
while IFS= read -r keyword; do
    bash -c "$keyword >> $target_directory/compare-auto/\"$output_file_name\""
    echo >> "$target_directory/compare-auto/$output_file_name"
       
    echo
    i=$(($i+1))
done << 'EOF'
""" + "\n".join(procedure_code_array) + "\nEOF"
subprocess.run(procedure_cmd, shell=True)

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



