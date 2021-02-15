
import requests
from bs4 import BeautifulSoup as BS
from wordcloud import WordCloud

#jsのチュートリアルサイトのテキストを形態素解析
res = requests.get('https://javascript.info')
soup = BS(res.text, 'html.parser')

title_sub_elms = soup.find_all('a', {'class':'list-sub__link'})

#URLに追加する用のhref取得
js_urls = []
for title_sub_elm in title_sub_elms:
    
    js_urls.append(title_sub_elm.get('href', 'nothing'))

js_text_all = str()
for js_url in js_urls:
    res = requests.get('https://javascript.info' + js_url)
    js_text_all += res.text

jssoup = BS(js_text_all, 'html.parser')

#wordcloudで抽出、図示化
#pytermextractのライブラリも試してみたがwordcloudの方がまだ綺麗に結果が出たように見えた
wordcloud = WordCloud(width=1200, height=600, max_words=600).generate(jssoup.get_text())
wordcloud.to_file("wordcloud_jsterm.png")


#pythonチュートリアルサイトのテキストを形態素解析
res = requests.get('https://docs.python.org/3/tutorial/index.html')
soup = BS(res.text, 'html.parser')

url_elms = soup.find_all('a', {'class':'reference internal'})

#URLに追加する用のhref取得
py_urls = []
for url_elm in url_elms:
    
    py_urls.append(url_elm.get('href', 'nothing'))

py_text_all = str()
for py_url in py_urls:
    res = requests.get('https://docs.python.org/3/tutorial/' + py_url)
    py_text_all += res.text

pysoup = BS(py_text_all, 'html.parser')

wordcloud = WordCloud(width=1200, height=600, max_words=600).generate(pysoup.get_text())
wordcloud.to_file("wordcloud_pyterm.png")