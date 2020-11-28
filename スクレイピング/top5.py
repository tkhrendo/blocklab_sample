import requests, re, lxml, sys, urllib.parse
from bs4 import BeautifulSoup

def requestGoogleSearch(query):
    print(query)
    res = requests.get('http://www.google.co.jp/search?hl=jp&gl=JP&num=6&q='+query)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    classes = soup.find_all('div', class_="ZINbbc xpd O9g5cc uUPGi")

    for idx, item in enumerate(classes):
        if idx >= 5: 
            break
        else:
            arr = []
            title = classes[idx].find('h3').find('div').text
            arr.append("# "+ title)
            link = classes[idx].find('a').get('href').split("/url?q=")[1]
            link = link.split("&")[0]

            res = parseItem(link)
            if res is not None:
                arr.append(('\n'.join(res)))
                print(arr)
                print('')

def parseItem(url):
    arr = []

    res = requests.get(url)

    try:
        res.raise_for_status()
    except:
        print('HTTPError')
        return None
    
    soup = BeautifulSoup(res.text, "lxml")
    [tag.extract() for tag in soup(string='\n')]
    main = soup.find('main')
    if main is not None:
        h23 = main.find_all(['h2','h3'])
    else:
        h23 = soup.find_all(['h2','h3'])

    for headline in h23:
        if 'h2' in str(headline):
            arr.append("## "+ headline.text.replace('\xa0||\xe3', ''))
        else:
            arr.append("### "+ headline.text.replace('\xa0||\xe3', ''))

    return arr

if __name__ == "__main__":
    args = sys.argv
    # requestGoogleSearch(urllib.parse.quote(args[1]))
    requestGoogleSearch("ブログ 始め方")