import detail_info
import re
import bs4
import urllib.parse
from xml.sax.saxutils import unescape

#各種HTML
BOX_HEAD = '<div class="booklink-box" style="text-align: left; padding-bottom: 20px; font-size: 20px; zoom: 1; overflow: hidden;">'
IMAGE_HEAD = '<div class="booklink-image" style="float: left; margin: 0 15px 10px 0;">'
INFO_HEAD = '<div class="booklink-info" style="line-height: 120%; zoom: 1; overflow: hidden;"><div class="booklink-name" style="margin-bottom: 10px; line-height: 120%;">'
LINK_HEAD = '<div class="booklink-link2" style="margin-top: 10px;">'

#各種ID
AMAZON_KINDLE_ID = 'waublg-22'
SEVEN_ID = '3595KW+6G72PE+2N1Y+BW0YB'

#楽天サイトにリクエストして詳細な情報を引き出す
def getDetailsInfo(rakuten,seven):
    url_rakuten = re.search(r'pc=https.*book%2F(\d*)%2F&m=', rakuten)
    if url_rakuten is not None:
        data_details = detail_info.requestDetailsFromRakuten(rakuten)
    else:
        data_details = detail_info.requestDetailsFromSeven(seven)
    return data_details

#HTMLにまとめる
def createHTML(rakuten, amazon, seven):
    # details = getDetailsInfo(rakuten, seven)
    
    #header
    html_text = BOX_HEAD
    
    #画像領域
    html_text += IMAGE_HEAD
    
    # soup = bs4.BeautifulSoup(rakuten)
    # href = soup.find("a").get("href")
    # html_text += '<a href="' + href + '" target="_blank" rel="noopener noreferrer">'
    # html_text += '<img style="border: none;" src="' + details["imagePath"] + '?_ex=200x200"/></a></div>'
    
    #アマゾンの画像抽出
    if amazon != "":
        soup_ama = bs4.BeautifulSoup(amazon, "html.parser")
        image = soup_ama.find("img")
        image['src'] = re.sub('Format=_SL\d{3}', "Format=_SL200", image['src'])
        amazon = str(soup_ama) + "</div>"
        html_text += unescape(amazon)

        #INFO
        href_ama = soup_ama.a.get("href")
        html_text += INFO_HEAD
        html_text += '<a href="' + href_ama + '" style="font-size: 24px" target="_blank" rel="noopener noreferrer">' + details['title'] + '</a></div>'

        #Detail
        html_text += '<div class="detail" style="margin-bottom: 5px;">'
        if 'auther' in details:
            html_text += details['auther'] + " "
        if 'publisher' in details:
            html_text += details['publisher']
        html_text += '</div>'

    #リンク
    html_text += LINK_HEAD

    if rakuten != "":
        #楽天
        soup = bs4.BeautifulSoup(rakuten, "html.parser")
        href_raku = soup.find("a").get("href")
        html_text += '<div class="link_rakuten" style="display: inline-block; margin-right: 5px;"><a href="' + href_raku + '" target="_blank" rel="noopener noreferrer">楽天ブックス</a></div>'
    
    if amazon != "":
        #Amazon
        html_text += '<div class="link_amazon" style="display: inline-block; margin-right: 5px;"><a href="' + href_ama + '" target="_blank" rel="noopener noreferrer">Amazon</a></div>'
        
        #Kindle
        html_text += '<div class="link_kindle" style="display: inline-block; margin-right: 5px;"><a href="https://www.amazon.co.jp/s?k=' + urllib.parse.quote(details['title']) + '&i=digital-text&__mk_ja_JP=カタカナ&tag=' + AMAZON_KINDLE_ID + '&ref=nb_sb_noss_1" target="_blank" rel="noopener noreferrer">Kindle</a></div>'
    
    if seven != "":
        #7net
        url_seven = urllib.parse.quote(seven)
        html_text += '<div class="link_seven" style="display: inline-block; margin-right: 5px;"><a href="https://px.a8.net/svt/ejp?a8mat=' + SEVEN_ID + '&a8ejpredirect=' + url_seven + '" target="_blank" rel="noopener noreferrer">7net</a></div>'

    #リンクおしまい
    html_text += '</div></div></div>'

    print('parse complete')
    return html_text