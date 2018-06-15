page = open('HTML_TWP415.htm', encoding='utf-8')
print(page.read())
page.close()
import urllib.request

site = 'http://www.afterfest.com.br/'
tag = 'wp-content/uploads/2017/09/'

k = page.find(tag)
while k != -1:
    j = k + len(tag)
    if page[j] != 'm':
        f = page.find('"', j)
        print(page[k+30:f])
        foto = 