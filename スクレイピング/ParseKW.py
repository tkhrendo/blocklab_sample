import collections
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties


def parseKeywords():
    data = []
    d = []

    with open("KW_sampledata.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line.split())

    for item in data:
        for kw in item:
            d.append(kw)
    
    c = collections.Counter(d)
    showPlt(c.most_common())
    
def showPlt(c):
    fp = FontProperties(fname='C:\\Users\\tkhro\\AppData\\Local\\Microsoft\\Windows\\Fonts\\ipaexg.ttf', size=14)
    plt.rcdefaults()

    x = [x[1] for x in c]
    label = [label[0] for label in c]

    x_position = np.arange(len(x))

    fig, ax = plt.subplots(figsize=(7,4))
    plt.title("ぐらふ", fontname="MS Gothic")
    # plt.rcParams["font.family"] = "IPAexGothic"
    plt.barh(x_position, x, tick_label=label)
    plt.yticks(x_position, label, fontproperties=fp)
 
    plt.show()



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
    parseKeywords()