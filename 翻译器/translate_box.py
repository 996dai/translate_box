import requests
import tkinter as t


class Dcc:
    def __init__(self):
        self.s = None
        self.tk = t.Tk()
        self.tk.title('翻译器')
        self.en1 = t.Entry(self.tk, bd=5, font=('楷体', 25), width=30)
        self.en1.pack()
        self.en1.insert('end', '你好')
        t.Label(self.tk, text='输入⬆' + '-' * 25 + '输出⬇', font=('正楷', 18)).pack()

        self.en2 = t.Text(self.tk, width=30, height=6, font=('楷体', 25))
        self.en2.pack()
        self.button = t.Button(self.tk, text="翻译", command=self.translate, font=('正楷', 15), activebackground='blue',
                               overrelief='sunken')
        self.button.pack()
        self.en1.bind('<Return>', self.translate)
        self.tk.mainloop()

    def translate(self, *kk):
        self.s = self.en1.get()
        url = 'https://fanyi.qq.com/api/translate'
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        data = {
            'sourceText': self.s
        }
        resp = requests.post(url=url, data=data, headers=headers)
        a = resp.json()
        dat = a['translate']['records'][0]['targetText']
        self.en2.delete('1.0', 'end')
        if len(dat) > 0:
            self.en2.insert('end', dat)
        else:
            self.en2.insert('end', '抱歉，没找到')


A = Dcc()
