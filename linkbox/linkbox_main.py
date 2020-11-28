import sys
import tkinter
import create_html

class linkbox:
    def __init__(self):
        #とりあえずGUI作成
        self.text = ''
        self.root = tkinter.Tk()
        root = self.root
        root.title(u"書籍リンクボックス作成")
        root.geometry('500x250')
        
        #
        # UI作成
        #
        #rakuten
        label_rakuten = tkinter.Label(text='楽天のテキストのみリンク')
        label_rakuten.place(x=10, y=10)
        label_rakuten.pack()

        self.editbox_rakuten = tkinter.Entry(width=50)
        editbox_rakuten = self.editbox_rakuten
        editbox_rakuten.place(x=10, y=30)
        editbox_rakuten.pack()

        #amazon
        label_amazon = tkinter.Label(text='Amazonの画像のみリンク')
        label_amazon.place(x=10, y=40)
        label_amazon.pack()

        self.editbox_amazon = tkinter.Entry(width=50)
        editbox_amazon = self.editbox_amazon
        editbox_amazon.place(x=10, y=60)
        editbox_amazon.pack()

        #kindle
        # label_amazon = tkinter.Label(text='Kindle')
        # label_amazon.place(x=10, y=70)
        # label_amazon.pack()

        # editbox_kindle = tkinter.Entry(width=50)
        # editbox_kindle.place(x=10, y=90)
        # editbox_kindle.pack()

        #7net
        label_seven = tkinter.Label(text='7netの商品ページのリンク')
        label_seven.place(x=10, y=100)
        label_seven.pack()

        self.editbox_7net = tkinter.Entry(width=50)
        editbox_7net = self.editbox_7net
        editbox_7net.place(x=10, y=120)
        editbox_7net.pack()

        #submit button
        button_enter = tkinter.Button(text=u'決定')
        button_enter.bind("<Button-1>", self.parseAdLink)
        button_enter.pack()

        #copy button
        button_copy = tkinter.Button(text=u'コピー')
        button_copy.bind("<Button-1>", self.copy_clipboard)
        button_copy.pack()

        #描画
        root.mainloop()


    # ボタン押下時のイベント
    def parseAdLink(self, *args):
        rak = self.editbox_rakuten.get()
        ama = self.editbox_amazon.get()
        sev = self.editbox_7net.get()
        self.text = create_html.createHTML(rak, ama, sev)
    
    def copy_clipboard(self, *args):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text)

if __name__ == "__main__":
    box = linkbox()