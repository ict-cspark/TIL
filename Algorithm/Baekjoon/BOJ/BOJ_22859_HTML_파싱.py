# Baekjoon Online Judge - HTML 파싱

import re

html = input()

html = html[len('<main>'):-len('</main>')]

html = re.sub(r'<div title="([\w ]+)">', r'title : \1\n', html)
html = re.sub(r'</div>', '', html)

html = re.sub(r'<p>', '', html)
html = re.sub(r'</p>', '\n', html)

html = re.sub(r'</?([\w ]+)>', '', html)
html = re.sub(r' *\n *', '\n', html)
html = re.sub(r' +', ' ', html)

print(html)
