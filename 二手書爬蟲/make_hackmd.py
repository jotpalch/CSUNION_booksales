# https://hackmd.io/@jotpac/rkGj6w-rF/edit

#顯示在imgur的圖片
import pyimgur
import os
from time import sleep

f = open("book.txt")
w = open("data.txt","a",encoding='utf-8')

CLIENT_ID = "2b7f0ebf5b7fe6c"

data = dict()

data = {'9781133953999\n': 'Physics for scientists and engineers with modern physics / Raymond A. Serway, John W. Jewett, Jr. ; with contributions from Vahé Peroomian', '9780132358811\n': 'Elementary differential equations with boundary value problems / C. Henry Edwards, David E. Penney with the assistance of David Calvis', '9781133187813\n': 'Introduction to the theory of computation / Michael Sipser', '9780132465403\n': 'C++ how to program / P.J. Deitel, H.M. Deitel', '9780071244749\n': 'Discrete mathematics and its applications / Kenneth H. Rosen', '9789867917461\n': '作業系統總整理(含系統程式) = Operating system / 程功編著', '9780387949031\n': 'Physics for computer science students : with emphasis on atomic and semiconductor physics / Narciso Garcia, Arthur Damask, Steven Schwarz', '9780321476173\n': 'Introduction to automata theory, languages, and computation / John E. Hopcroft, Rajeev Motwani, Jeffrey D. Ullman', '9780321509680\n': 'Concepts of programming languages / Robert W. Sebesta', '9789862366141\n': '電影鑑賞&創意 : 心理視覺線與轉化 / 張武恭著', '9780195142525\n': 'Microelectronic circuits / Adel S. Sedra, Kenneth C. Smith.', '9780929306377\n': 'Fundamentals of data structures in C++ / Ellis Horowitz, Sartaj Sahni, Dinesh P. Mehta', '9780137050512\n': 'Electric circuits / James W. Nilsson, Susan A. Riedel', '9780538498876\n': 'Calculus : early transcendentals / James Stewart', '9781449627324\n': 'An introduction to formal languages and automata / Peter Linz', '9789863471721\n': 'C++程式設計導論 / Y. Daniel Liang著; 蔡明志譯', '9789574424849\n': 'C語言教學手冊 = Programming language / 洪維恩作', '9789814336666\n': 'Principles of physics : a calculus approach / Raymond A. Serway ...[et al.]', '9780132067119\n': 'Logic and computer design fundamentals / M. Morris Mano, Charles R. Kime.', '9789864128549\n': 'VLSI設計概論/實習 / 唐經洲,李博明編著', '9789866482090\n': 'C/C+ + 入門進階 / 位元文化編著', '9780495382737\n': 'Calculus : early transcendentals / James Stewart', '9780132465588\n': 'Concepts of programming languages / Robert W. Sebesta', '9780273753728\n': 'Principles of economics / Karl E. Case, Ray C. Fair, Sharon M. Oster', '9789572145876\n': '訊號與系統 / Simon Haykin, Barry Van Veen原著; 洪惟堯等編譯', '9789579899109\n': '電磁學 / David k.Cheng原著; 李永勲譯', '9780132340434\n': 'Digital design / M. Morris Mano, Michael D. Ciletti', '9780131365841\n': 'Absolute C++ / Walter Savitch ; contributor, Kenrick Mock.', '9780470552001\n': 'Financial accounting / Jerry J. Weygandt, Paul D. Kimmel, Donald E. Kieso', '9780321544285\n': 'Computer science : an overview / J. Glenn Brookshear', '9780131377097\n': 'Assembly language for x86 processors / Kip R. Irvine', '9780131911659\n': 'Logic and computer design fundamentals / M. Morris Mano, Charles Kime.', '9789862263457\n': '離散數學 = Discrete mathematics / 黃子嘉編著', '9789862265109\n': '資料結構 : 含精選試題 / 洪逸編著', '9789862265116\n': '線性代數及其應用 / 黃子嘉編著', '9789862265123\n': '線性代數及其應用 / 黃子嘉編著', '9789862267950\n': '計算機組織與結構重點直擊 = Computer organization and architecture / 張凡編著', '9789862263211\n': '離散數學 = Discrete mathematics / 黃子嘉編著', '9789862268735\n': '線性代數決戰60天 / 周易編著', '9780534274092\n': 'Calculus : early transcendentals / James Stewart', '9789862263464\n': '離散數學分類題庫(離散數學習題詳解) = Discrete mathematics / 黃子嘉編著', '9789862265192\n': '線性代數分類題庫(線性代數及其應用習題詳解) = Linear algebra with applications / 黃子嘉編著', '9780132467162\n': "Summit 1 : English for today's world / Joan Saslow, Allen Ascher ; pronunciation booster by Bertha Chela-Flores", '9781259070365\n': 'Mosaic 1. Reading / Brenda Wegmann, Miki Knezevic', '9781424002511\n': 'Listening advantage / Tom Kenny, Tamami Wada, Colleen Sheils'}

img = os.listdir("ssimg")

for book in f.readlines():
    sleep(1)
    if data.get(book) :
        w.write("### "+data.get(book)+"\n")
    else :
        w.write("### "+book[:-1]+"\n")

    w.write("<details>\n"+"\n")

    if str(book[:-1])+"_.png" in img :
        PATH = os.getcwd() + "\\ssimg\\" + book[:-1] + "_.png" #A Filepath to an image on your computer"
        title = book[:-1]

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title=title)
        # print(uploaded_image.title)
        w.write("![]("+uploaded_image.link+")\n"+"\n")
        # print(uploaded_image.type)

    w.write("</details>\n"+"\n")

w.close()
f.close()
