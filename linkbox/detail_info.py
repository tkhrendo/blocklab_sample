import requests, bs4, re

def requestDetailsFromSeven(url):
    print(url)
    if url is not None:
        res = requests.get(url)
        #sample: https://7net.omni7.jp/detail/1106840356

        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        data = {}
        data['title'] = soup.find("h1", "h1ProductName").string

        li = soup.find("li", "basic-information-0100")
        
        data['auther'] = li.find("a", "productDetailsLink").string

        li = soup.find("li", "basic-information-0170")
        data['publisher'] = li.find("a", "productDetailsLink").string
        
        return data
# <a href="https://hb.afl.rakuten.co.jp/hgc/18266142.692bb8cc.18266143.7d289bee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbook%2F15614409%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbook%2Fi%2F19300560%2F&link_type=text&ut=eyJwYWdlIjoiaXRlbSIsInR5cGUiOiJ0ZXh0Iiwic2l6ZSI6IjI0MHgyNDAiLCJuYW0iOjEsIm5hbXAiOiJyaWdodCIsImNvbSI6MSwiY29tcCI6ImRvd24iLCJwcmljZSI6MCwiYm9yIjoxLCJjb2wiOjEsImJidG4iOjF9" target="_blank" rel="nofollow noopener noreferrer" style="word-wrap:break-word;"  >即効！成果が上がる　文章の技術 [ 尾藤　克之 ]</a>

def requestDetailsFromRakuten(rakuten):
    #id抽出
    url_rakuten = re.search(r'pc=https.*book%2F(\d*)%2F&m=', rakuten)
    id = url_rakuten.group(1)
    print("id: " + id)
    print("start request")


    #リクエスト前にタイトルだけ取っておく
    data = {}
    soup = bs4.BeautifulSoup(rakuten, "html.parser")
    #タイトルは楽天で入力したテキストから
    title = soup.find("a")
    data['title'] = title.text

    #リクエスト開始
    res = requests.get("https://books.rakuten.co.jp/rb/" + id)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elements = soup.find_all("li", "productInfo")
    print("elements: " + str(len(elements)))
    for li in elements:
        category = li.find("span", "category").string
        span = li.find("span", "categoryValue")
        if span.find("a") is not None:
            categoryValue = span.find("a").string
        else:
            categoryValue = span.string
        
        if category == '著者／編集':
            data['auther'] = categoryValue
        elif category == '出版社':
            data['publisher'] = categoryValue
        
        print("category: " + category)
        print("categoryValue: " + categoryValue)
        
        # title = soup.find("h1", =itemprop"name")
        # title.find(class_="authorLink").extract()
        # data['title'] = title.text
        
    return data

if __name__ == "__main__":
    requestDetailsFromRakuten('15614409')
    # https://books.rakuten.co.jp/rb/15614409/