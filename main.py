import tkinter as tk
import pygame
import tkvideo
from pygame import mixer
import webbrowser as web
from tkVideoPlayer import TkinterVideo
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt


pc = tk.Tk()
pc.geometry("1000x500")
pc.title("potifey")
videoplayer = TkinterVideo(master=pc, scaled=True, width=500, height=500)
videoplayer.load("ast.mp4")
sism = tk.Label(text="dcaf")
c = 0.5
pygame.init()
mixer.init()
hghg = tk.Label(text="           ")
gr = tk.Button(text="Girişi onayla")

l1 = tk.Label(text="Kullanıcı Adı:")

l2 = tk.Label(text="Şifre:")

l3 = tk.Label(text="Gmail:")

l4 = tk.Label(text="Şifreyi onayla:")

a1 = tk.Entry()

a2 = tk.Entry()

a3 = tk.Entry()

a4 = tk.Entry()

q1 = tk.Label(text="")

q2 = tk.Label(text="")

q3 = tk.Label(text="")

q4 = tk.Label(text="")

q5 = tk.Label(text="")

q6 = tk.Label(text="")

q7 = tk.Label(text="")

q8 = tk.Label(text="Giriş bilgileri")

r1 = tk.Label(text="Lütfen tüm işlemleri yapınız", fg="red")

secs = ["Cinsiyet seçiniz", "Savaş heelikopteri", "Bim poşeti", "Belirtmek istemiyorum", "Erkek", "Kadın"]
secilis = tk.StringVar(pc)
secilis.set(secs[0])
om2s = tk.OptionMenu(pc, secilis, *secs)

lbkl = tk.Label(text="Kullancı Adı:")

lbsf = tk.Label(text="Şifre:")

ote = tk.Entry()

otes = tk.Entry()

a = True
sf2 = tk.Frame(pc, bg="#4C2A85")
sf2.pack(side="left", fill="y")


def giris():
    print("giriş")

    l4.config(text="                              ")
    hghg.place(x=10, y=0)
    prr2.place(x=100, y=30)
    bst1.place(x=52131250, y=50)
    pr1.place(x=100, y=0)
    bot.place(x=452228, y=300)
    bhs.place(x=533330, y=250)
    lbkl.place(x=33330, y=30)
    lbsf.place(x=33370, y=70)
    ote.place(x=133300, y=30)
    otes.place(x=102220, y=70)
    otgr.place(x=103330, y=130)
    l1.place(x=33232313, y=50)
    l1.place(x=3323131320, y=52132130)
    l2.place(x=523132131230, y=80)
    l3.place(x=231323140, y=110)
    l4.place(x=22213132314, y=50)
    a1.place(x=1021313230, y=50)
    a2.place(x=1231232100, y=80)
    a3.place(x=1023123120, y=110)
    q8.place(x=23350, y=200)
    bot.place(x=45228, y=300)
    bhs.place(x=452220, y=250)
    q1.place(x=333300, y=250)
    q2.place(x=3033330, y=270)
    q3.place(x=30333330, y=290)
    q4.place(x=3333300, y=310)
    q5.place(x=3333300, y=330)
    q6.place(x=3333333, y=350)
    b1s.place(x=3522220, y=150)
    b2s.place(x=3522220, y=150)
    om2s.place(x=322200, y=75)
    q7.place(x=333333300, y=370)
    b2s.place(x=1212, y=223232)
    a4.place(x=302131230, y=50)
    gr.place(x=123123, y=132131)


def otac():
    print("oturum aç")
    bot.place(x=452228, y=300)
    bhs.place(x=50, y=250)
    lbkl.place(x=30, y=30)
    lbsf.place(x=70, y=70)
    ote.place(x=100, y=30)
    otes.place(x=100, y=70)
    otgr.place(x=100, y=130)
    # -----------------------

    l1.place(x=33320, y=50)
    l2.place(x=53330, y=80)
    l3.place(x=433330, y=110)
    l4.place(x=233324, y=50)
    a1.place(x=103330, y=50)
    a2.place(x=133300, y=80)
    a3.place(x=100333333, y=110)
    a4.place(x=30333330, y=50)
    b1s.place(x=3333350, y=150)
    om2s.place(x=3333300, y=75)


bst1 = tk.Button(text="AMONG SUS", command=giris)
bst1.place(x=550, y=50)


def otac1():
    s = otes.get()
    k = ote.get()

    if k == "Alpash":
        print("Kullanıcı girişi başarılı")
        if s == "1234":
            print("Şifre girşi başarılı")
            giris()
    elif k == "Admin":
        print("Admin girşi başarılı")
        if s == "Y":
            giris()


def hspo():
    bot.place(x=50, y=250)
    bhs.place(x=453330, y=250)
    print("Hesap oluştur")
    l1.place(x=20, y=50)
    l2.place(x=50, y=80)
    l3.place(x=40, y=110)
    l4.place(x=224, y=50)
    a1.place(x=100, y=50)
    a2.place(x=100, y=80)
    a3.place(x=100, y=110)
    a4.place(x=300, y=50)
    b1s.place(x=350, y=150)
    om2s.place(x=300, y=75)
    # ---------------------
    lbkl.place(x=333330, y=30)
    lbsf.place(x=733330, y=70)
    ote.place(x=1333300, y=30)
    otes.place(x=1333300, y=70)
    otgr.place(x=13333300, y=130)


def d1():
    w = a
    s2 = secilis.get()
    w1 = a1.get()
    w2 = a2.get()
    w3 = a3.get()
    w4 = a4.get()
    if w:
        print("w giriş başarılı")
        if s2 != "Cinsiyet seçiniz":
            print("Cinsiyet girişi başarılı")
            if w:
                print("Kullanıcı adı girişi başarılı")
                if len(w1) >= 4:
                    print("w1 girişi başarılı")
                    if len(w2) >= 4:
                        print("w2 girişi başarılı")
                        if w3.__contains__("@") and w3.__contains__("gmail.com") and len(str(w3)) >= 11:
                            print("Kullanıcı adı" + str(w1))
                            print("ŞİFRE onay" + str(w4))
                            print("Gmail" + str(w3))
                            print("şifre " + str(w2))
                            print("w3 girişi başarılı")
                            if w4 == w2:
                                print("w4 girişi başarılı")
                                q1.config(text="Kullanıcı adınız: " + w1)
                                q2.config(text="Şifreniz: " + w2)
                                q3.config(text="Gmail: " + w3)
                                q6.config(text="Cinsiyet: " + s2)
                                q1.place(x=200, y=250)
                                gr.place(x=420, y=350)
                                gr.config(command=giris)
                                q2.place(x=200, y=270)
                                q3.place(x=200, y=290)
                                q6.place(x=200, y=350)
                                q8.place(x=200, y=210)
                                b2s.place(x=350, y=310)
                                r1.place(x=3322333331334, y=111111)
                                b2s.config(text="Girşi sil", command=sil2)
                            else:
                                r1.config(text="Şifreniz 1 inci girlen şifre ile eşleşmiyor", fg="red")
                                r1.place(x=300, y=280)
                                b2s.place(x=400, y=310)
                                b2s.config(text="Uyarıyı sil", command=sil)
                                b2s.place(x=400, y=450)
                        else:
                            r1.config(text="Geçerli bir gmail girniz", fg="red")
                            r1.place(x=300, y=280)
                            b2s.place(x=400, y=310)
                            b2s.config(text="Uyarıyı sil", command=sil)
                            b2s.place(x=400, y=450)
                    else:
                        r1.config(text="Şifre minimum 4 haneli olabilir", fg="red")
                        r1.place(x=300, y=280)
                        b2s.place(x=400, y=310)
                        b2s.config(text="Uyarıyı sil", command=sil)
                        b2s.place(x=400, y=450)
                else:
                    r1.config(text="Kullanıcı adı Minimum 4 harfli olabilir", fg="red")
                    r1.place(x=300, y=280)
                    b2s.place(x=400, y=310)
                    b2s.config(text="Uyarıyı sil", command=sil)
                    b2s.place(x=400, y=450)
            else:
                r1.place(x=300, y=280)
                b2s.place(x=400, y=310)
                b2s.config(text="Uyarıyı sil", command=sil)
                b2s.place(x=400, y=450)
        else:
            r1.config(text="Lütfen Cinsiyet seçiniz", fg="red")
            r1.place(x=300, y=280)
            b2s.place(x=400, y=310)
            b2s.config(text="Uyarıyı sil", command=sil)
            b2s.place(x=400, y=450)
    else:
        r1.place(x=300, y=280)
        b2s.place(x=400, y=310)
        b2s.config(text="Uyarıyı sil", command=sil)


def sil():
    r1.place(x=33221334, y=111111)
    b2s.place(x=1212, y=223232)


def pl2():
    videoplayer.place(x=15, y=30)
    videoplayer.config(width=830, height=415)


def pl():
    videoplayer.play()
    videoplayer.place(x=15, y=30)
    videoplayer.config(width=830, height=415)
    fto6.place(x=231123, y=2131234)
    pc.after(1, lambda: pl2())


def sil2():
    gr.place(x=423330, y=350)
    q8.place(x=23350, y=200)
    q1.place(x=333300, y=250)
    q2.place(x=3033330, y=270)
    q3.place(x=30333330, y=290)
    q4.place(x=3333300, y=310)
    q5.place(x=3333300, y=330)
    q6.place(x=3333333, y=350)
    q7.place(x=333333300, y=370)
    b2s.place(x=1212, y=223232)


b2s = tk.Button(text="Uyarıyı sil", command=sil)
b1s = tk.Button(text="Kaydet", command=d1, fg="white", bg="green")
ft = tk.PhotoImage(file="pn1.png")
fto = tk.Label(image=ft, height=3, width=3)
ft2 = tk.PhotoImage(file="pn2.png")
fto2 = tk.Label(image=ft2, height=1, width=1)
ft3 = tk.PhotoImage(file="pn3.png")
fto3 = tk.Label(image=ft3, height=1, width=1)
ft4 = tk.PhotoImage(file="pn6.png")
fto4 = tk.Label(image=ft4, height=3, width=3)
ft5 = tk.PhotoImage(file="pn5.png")
ft6 = tk.PhotoImage(file="pn4.png")
fto6 = tk.Label(image=ft6, height=3, width=3)
fto5 = tk.Label(image=ft5, height=3, width=3)
ft7 = tk.PhotoImage(file="pngoz.png")
fto7 = tk.Label(image=ft7, height=1, width=1)
ft8 = tk.PhotoImage(file="png8.png")
fto8 = tk.Label(image=ft8, height=3, width=3)
ft9 = tk.PhotoImage(file="png9.png")
fto9 = tk.Label(image=ft9, height=3, width=3)
ft10 = tk.PhotoImage(file="png10.png")
fto10 = tk.Label(image=ft10, height=3, width=3)
ft11 = tk.PhotoImage(file="png11.png")
fto11 = tk.Label(image=ft11, height=3, width=3)
ft12 = tk.PhotoImage(file="png12.png")
fto12 = tk.Label(image=ft12, height=3, width=3)
ft13 = tk.PhotoImage(file="pn13.png")
fto13 = tk.Label(image=ft13, height=3, width=3)
ftecho1 = tk.PhotoImage(file="pngecho1.png")
ftoecho1 = tk.Label(image=ftecho1, height=3, width=3)
ftecho = tk.PhotoImage(file="pngecho.png")
ftoecho = tk.Label(image=ftecho, height=3, width=3)
ftrickroll = tk.PhotoImage(file="pngrickrolled.png")
ftorickrolled = tk.Label(image=ftrickroll, height=3, width=3)
fta = tk.PhotoImage(file="pnga.png")
ftoa = tk.Label(image=fta, height=3, width=3)
fts = tk.PhotoImage(file="sngerpng.png")
ftos = tk.Label(image=fts, height=3, width=3)
ftompk = tk.PhotoImage(file="MPKDR.png")
ftompkr = tk.Label(image=ftompk, height=3, width=3)
ftmc = tk.PhotoImage(file="pngmc.png")
ftomc = tk.Label(image=ftmc, height=3, width=3)
ftbc = tk.PhotoImage(file="bc.png")
ftobc = tk.Label(image=ftbc, height=3, width=3)
ftas = tk.PhotoImage(file="asiye.png")
ftoas = tk.Label(image=ftas, height=3, width=3)
ftot = tk.PhotoImage(file="othersidepng.png")
ftoot = tk.Label(image=ftot, height=3, width=3)
snm3 = tk.Label(text="𝙎𝙚𝙥𝙩𝙚𝙢𝙗𝙚𝙧 - 𝙎𝙥𝙖𝙧𝙠𝙮 𝙙𝙚𝙖𝙩𝙝𝙘𝙖𝙥")
snm2 = tk.Label(text="Unutulanlar")
snm = tk.Label(text="Miki Matsubara - Stay With Mea")
volume2 = tk.Entry()
alt = tk.Label()
ses = tk.Label(text="Ses Düzeyi")
test = "A1"
mixer.music.set_volume(c)
uyari = tk.Label(text="0-10 arası sayılar ile ses düzeyini ayarlaya bilirsiniz", fg="red")
syf = tk.Label(text="Giriş Sayafası")
syf.place(x=830, y=0)
dz = tk.Label(text="/ Ses düzeyi " + str(c))
dz.place(x=910, y=0)
altl = tk.Label()
uyar = tk.Label(text="")
sec3 = ["Kapalı", "Speed up", "Lycris"]
sec2 = ["Kapalı", "Türkce Seslendirme", "Orginal Seslendirme"]
sec = ["Kapalı", "Türkce Alt yazı", "Orginal Alt yazı"]
secili = tk.StringVar(pc)
secili.set(sec[0])
secili2 = tk.StringVar(pc)
secili2.set(sec2[0])
secili3 = tk.StringVar(pc)
secili3.set(sec3[0])
altayar = tk.Label(text="Alt yazı")
sesayar = tk.Label(text="Seslendirme")
sesayar2 = tk.Label(text="Ses düzeni")

om = tk.OptionMenu(pc, secili, *sec)
om2 = tk.OptionMenu(pc, secili2, *sec2)
om3 = tk.OptionMenu(pc, secili3, *sec3)

g = True
sarkiisim = ""
sf = 1
youtube = ""


# ------------------------------------------------------#

def ayrkap():
    om3.place(x=8222280, y=360)
    ses.place(x=82222293, y=50)
    sesayar.place(x=8222280, y=250)
    altayar.place(x=8222220, y=170)
    sesayar2.place(x=8222280, y=330)
    om2.place(x=8222250, y=280)
    om.place(x=2222880, y=200)
    btvolume.place(x=8222295, y=110)
    volume2.place(x=862220, y=80)
    bayr.config(text="Ses Ayarları", command=ayarlar)


def ayarlar():
    print("ayarlar")
    om3.place(x=880, y=360)
    ses.place(x=893, y=50)
    sesayar.place(x=880, y=250)
    altayar.place(x=890, y=170)
    sesayar2.place(x=880, y=330)
    om2.place(x=880, y=280)
    om.place(x=880, y=200)
    btvolume.place(x=895, y=110)
    volume2.place(x=860, y=80)
    bayr.config(text="Ses Ayarlarını kapat", command=ayrkap)


def altyazi2():
    global sarkiisim
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 1")
            altl.config(text=tralt1)
            altl.place(x=320, y=420)
            pc.after(4140, lambda: altyazi3())
        elif s == "Kapalı":
            altl.place(x=383330, y=420)
            print("Alt yazı kapalı")
        elif s == "Orginal Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 1")
            altl.config(text=alt1)
            altl.place(x=320, y=420)
            pc.after(4140, lambda: altyazi3())
    elif not g:
        print("g GİRİŞL BAŞARISIZ")


def altyazi3():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 2")
            altl.config(text=tralt2)

            pc.after(1300, lambda: altyazi4())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 2")
            altl.config(text=alt2)
            pc.after(1300, lambda: altyazi4())


def altyazi4():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 3")
            altl.config(text=tralt3)

            pc.after(3660, lambda: altyazi5())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 3")
            altl.config(text=alt3)
            pc.after(3660, lambda: altyazi5())


def altyazi5():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 4")
            altl.config(text=tralt4)

            pc.after(1160, lambda: altyazi6())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 4")
            altl.config(text=alt4)

            pc.after(1160, lambda: altyazi6())


def altyazi6():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 5")
            altl.config(text=tralt5)

            pc.after(4030, lambda: altyazi7())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 5")
            altl.config(text=alt5)

            pc.after(4030, lambda: altyazi7())


def altyazi7():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 6")
            altl.config(text=tralt6)

            pc.after(4570, lambda: altyazi8())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 6")
            altl.config(text=alt6)
            pc.after(4570, lambda: altyazi8())


def altyazi8():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 7")
            altl.config(text=tralt7)

            pc.after(2500, lambda: altyazi9())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 7")
            altl.config(text=alt7)

            pc.after(2500, lambda: altyazi9())


def altyazi9():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 8")
            altl.config(text=tralt8)

            pc.after(2150, lambda: altyazi10())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)

        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 8")
            altl.config(text=alt8)

            pc.after(2150, lambda: altyazi10())


def altyazi10():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 9")
            altl.config(text=tralt9)

            pc.after(2540, lambda: altyazi11())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 9")
            altl.config(text=alt9)

            pc.after(2540, lambda: altyazi11())


def altyazi11():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 10")
            altl.config(text=tralt10)

            pc.after(2540, lambda: altyazi12())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)

        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 10")
            altl.config(text=alt10)

            pc.after(2540, lambda: altyazi12())


def altyazibonus():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 11")
            altl.config(text=tralt12)

            pc.after(2140, lambda: altyazi13())
        elif s == "Kapalı":
            print("Alt yazı kapalı")
            altl.place(x=383330, y=420)
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 11")
            altl.config(text=alt12)

            pc.after(2140, lambda: altyazi13())


def altyazi12():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 12")
            altl.config(text=tralt11)

            pc.after(2510, lambda: altyazibonus())
        elif s == "Kapalı":
            altl.place(x=383330, y=420)
            print("Alt yazı kapalı")
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 12")
            altl.config(text=alt11)

            pc.after(2510, lambda: altyazibonus())


def altyazi13():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 13")
            altl.config(text=tralt13)

            pc.after(2740, lambda: altyazi14())
        elif s == "Kapalı":
            altl.place(x=383330, y=420)
            print("Alt yazı kapalı")
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 13")
            altl.config(text=alt13)

            pc.after(2740, lambda: altyazi14())


def altyazi14():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 14")
            altl.config(text=tralt14)

            pc.after(2860, lambda: altyazi15())
        elif s == "Kapalı":
            altl.place(x=383330, y=420)
            print("Alt yazı kapalı")
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 14")
            altl.config(text=alt14)

            pc.after(2860, lambda: altyazi15())


def altyazi15():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 15")
            altl.config(text=tralt4)

        elif s == "Kapalı":
            altl.place(x=383330, y=420)
            print("Alt yazı kapalı")
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı 15")

            altl.config(text=alt4)
            pc.after(1500, lambda: altyazi16())


def altyazi16():
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 16")
            altl.config(text=tralt4)
            altl.place(x=38330, y=420)
        elif s == "Kapalı":
            altl.place(x=383330, y=420)
            print("Alt yazı kapalı")
        elif s == "Türkce Alt yazı" and sarkiisim == "Twotime":
            print("Alt yazı grş başarılı 16")
            altl.place(x=38330, y=420)
            altl.config(text=alt4)
        if sarkiisim == "Sungerbob":
            altl.place(x=38330, y=420)


def unpsu():
    print("unpasue")
    mixer.music.unpause()
    pause.config(text="Şarkıyı durdur", command=psu)


def psu():
    print("pause")
    mixer.music.pause()
    pause.config(text="Şarkıyı oynat", command=unpsu)


def yeniden():
    global g
    print("yeniden 1")
    g = False
    global test
    if not g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 3")
            altl.config(text="Lütfen 5 saniye bekleyin...")
            pc.after(1000, lambda: sayac())

        elif s == "Kapalı":
            altl.config(text="Lütfen 5 saniye bekleyin...")
            if test == "A1":
                altl.place(x=370, y=430)
            elif test != "A1":
                altl.place(x=320, y=420)
            print("Alt yazı kapalı")
            pc.after(1000, lambda: sayac())
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı")
            altl.config(text="Please wait 5 seconds...")
            pc.after(1000, lambda: sayac())
    mixer.music.stop()


def sayac():
    global g
    print("sayac 1")
    g = False
    if not g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 3")
            altl.config(text="Lütfen 4 saniye bekleyin...")
            pc.after(1000, lambda: sayac2())
        elif s == "Kapalı":
            altl.config(text="Lütfen 4 saniye bekleyin...")
            print("Alt yazı kapalı")
            pc.after(1000, lambda: sayac2())
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı")
            altl.config(text="Please wait 4 seconds...")
            pc.after(1000, lambda: sayac2())


def sayac2():
    global g
    g = False
    print("sayac 2")
    if not g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 3")
            altl.config(text="Lütfen 3 saniye bekleyin...")
            pc.after(1000, lambda: sayac3())
        elif s == "Kapalı":
            altl.config(text="Lütfen 3 saniye bekleyin...")
            print("Alt yazı kapalı")
            pc.after(1000, lambda: sayac3())
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı")
            altl.config(text="Please wait 3 seconds...")
            pc.after(1000, lambda: sayac3())


def sayac3():
    global g
    print("sayac 3")
    g = False
    if not g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("Alt yazı grş başarılı 3")
            altl.config(text="Lütfen 2 saniye bekleyin...")
            pc.after(1000, lambda: sayac4())
        elif s == "Kapalı":
            altl.config(text="Lütfen 2 saniye bekleyin...")
            print("Alt yazı kapalı")
            pc.after(1000, lambda: sayac4())
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı")
            altl.config(text="Please wait 2 seconds...")
            pc.after(1000, lambda: sayac4())


def sayac4():
    global g
    g = False
    print("sayac 4")
    if not g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("sayac 4")
            altl.config(text="Lütfen 1 saniye bekleyin...")
            pc.after(1000, lambda: yeniden2())
        elif s == "Kapalı":
            altl.config(text="Lütfen 1 saniye bekleyin...")
            print("Alt yazı kapalı")
            pc.after(1000, lambda: yeniden2())
        elif s == "Orginal Alt yazı":
            print("Alt yazı grş başarılı")
            altl.config(text="Please wait 1 seconds...")
            pc.after(1000, lambda: yeniden2())


def yeniden2():
    global g
    g = True
    if g:
        s = str(secili.get())
        if s == "Türkce Alt yazı":
            print("yeniden 2")
            altl.config(text="")
            pc.after(2730, lambda: altyazi2())
        elif s == "Kapalı":
            altl.config(text="")
            print("Alt yazı kapalı")
            print("yeniden 2")
            altl.place(x=323220, y=420)
        elif s == "Orginal Alt yazı":
            print("yeniden 2")
            altl.config(text="")
            pc.after(2730, lambda: altyazi2())
    mixer.music.play()


def volume1():
    global c

    a9 = str(volume2.get())
    if a9 == "0":
        mixer.music.set_volume(0)
        c = 0
    elif a9 == "1":
        mixer.music.set_volume(0.1)
        c = 0.1
    elif a9 == "2":
        mixer.music.set_volume(0.2)
        c = 0.2
    elif a9 == "3":
        mixer.music.set_volume(0.3)
        c = 0.3
    elif a9 == "4":
        mixer.music.set_volume(0.4)
        c = 0.4
    elif a9 == "5":
        mixer.music.set_volume(0.5)
        c = 0.5
    elif a9 == "6":
        mixer.music.set_volume(0.6)
        c = 0.6
    elif a9 == "7":
        mixer.music.set_volume(0.7)
        c = 0.7
    elif a9 == "8":
        mixer.music.set_volume(0.8)
        c = 0.8
    elif a9 == "9":
        mixer.music.set_volume(0.9)
        c = 0.9
    elif a9 == "10":
        mixer.music.set_volume(1)
        c = 1
    elif a9 == "Allahıma Şükür":
        sukur()
    elif a9 == "Please rickrolled me":
        sukur()
    elif a9 == "ECHO":
        sukur()
    elif a9 == "oy asiye":
        sukur()
    elif a9 == "The Other Side":
        sukur()
    else:
        uyari.place(x=535, y=0)
        temizle.place(x=920, y=25)
    dz.config(text="/ Ses düzeyi " + str(c))


def siluyari():
    temizle.place(x=384782509, y=7)
    uyari.place(x=9485, y=7)


def syf1():
    pr1.place(x=132200, y=0)
    pr2.place(x=231231100, y=30)
    hghg.place(x=0, y=0)
    bayr.place(x=870, y=450)
    fto3.place(x=0, y=320, relheight=0.3, relwidth=0.3)
    fto2.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    fto.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    btsyf.config(text="Sayfa 2", command=syf2)
    snm3.place(x=350, y=340)
    snm.place(x=350, y=10)
    snm2.place(x=390, y=170)
    bt1.config(command=oynat1)
    bt2.config(command=oynat2)
    bt3.config(command=oynat3)
    bt2.place(x=390, y=270)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    snm3.place(x=350, y=340)
    snm.place(x=350, y=10)
    snm2.place(x=390, y=170)
    # ---------------------------------------------------------#
    fto6.place(x=23131231, y=320, relheight=0.3, relwidth=0.3)
    fto4.place(x=3231320, y=160, relheight=0.3, relwidth=0.3)
    fto5.place(x=23131230, y=0, relwidth=0.3, relheight=0.3)
    snm.config(text="Miki Matsubara - Stay With Mea")
    snm2.config(text="Unutulanlar")
    snm3.config(text="𝙎𝙚𝙥𝙩𝙚𝙢𝙗𝙚𝙧 - 𝙎𝙥𝙖𝙧𝙠𝙮 𝙙𝙚𝙖𝙩𝙝𝙘𝙖𝙥")
    syf.config(text="Sayfa 1`desiniz")
    bt2.place(x=390, y=270)
    bt1.place(x=390, y=100)
    btsyf.place(x=800, y=400)
    bt3.place(x=390, y=440)
    btsyf3.place(x=83300, y=400)
    btsyf.place(x=800, y=400)
    global sf
    sf = 1


def syf2():
    bayr.place(x=870, y=450)
    fto3.place(x=222220, y=320, relheight=0.3, relwidth=0.3)
    fto2.place(x=2222220, y=160, relheight=0.3, relwidth=0.3)
    fto8.place(x=333330, y=200, relheight=0.3, relwidth=0.3)
    fto9.place(x=-133300, y=10, relheight=0.4, relwidth=0.4)
    fto.place(x=222222, y=0, relwidth=0.3, relheight=0.3)
    btsyf.config(text="Sayfa 1", command=syf1)
    # ---------------------------------------------------#
    fto4.place(x=0, y=0, relheight=0.3, relwidth=0.3)
    fto6.place(x=0, y=320, relheight=0.4, relwidth=0.3)
    fto5.place(x=0, y=160, relwidth=0.3, relheight=0.3)
    snm.config(text="Daft Punk-Get Lucky(sped up) ☆ ")
    snm3.config(text="Two Time")
    snm2.config(text="Adele - Rolling in the Deep")
    bt1.config(command=oynat4)
    bt2.config(command=oynat5)
    bt3.config(command=oynat6)
    bt2.place(x=390, y=270)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    btsyf.place(x=700, y=400)
    btsyf3.place(x=800, y=400)
    snm3.place(x=390, y=340)
    btsyf3.config(text="Sayfa 3", command=syf3)
    snm.place(x=350, y=10)
    snm2.place(x=370, y=170)
    fto7.place(x=0, y=333220, relheight=0.5, relwidth=0.3)
    syf.config(text="Sayfa 2`desiniz")
    global sf
    sf = 2


def syf3():
    bayr.place(x=870, y=450)
    fto10.place(x=23220, y=350, relheight=0.5, relwidth=0.3)
    fto3.place(x=222220, y=320, relheight=0.3, relwidth=0.3)
    fto2.place(x=2222220, y=160, relheight=0.3, relwidth=0.3)
    fto.place(x=222222, y=0, relwidth=0.3, relheight=0.3)
    btsyf3.config(text="Sayfa 4", command=syf4)
    fto4.place(x=676760, y=0, relheight=0.3, relwidth=0.3)
    fto6.place(x=657750, y=320, relheight=0.4, relwidth=0.3)
    fto5.place(x=5670, y=160, relwidth=0.3, relheight=0.3)
    snm.config(text="rei sings u fly me to the moon")
    snm2.config(text="🖇 system of a down - lonely day ")
    snm3.config(text="LEGION")
    fto12.place(x=1221210, y=320, relheight=0.3, relwidth=0.3)
    fto11.place(x=1221210, y=320, relheight=0.3, relwidth=0.3)
    bt1.config(command=oynt9)
    snm3.place(x=410, y=340)
    snm.place(x=350, y=10)
    snm2.place(x=350, y=170)
    bt2.config(command=oynt8)
    btsyf.place(x=700, y=400)
    bt3.config(command=oyntozl)
    btsyf.config(text="Sayfa 2", command=syf2)
    bt2.place(x=390, y=270)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    btsyf3.place(x=800, y=400)
    fto7.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    fto8.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    fto9.place(x=-100, y=10, relheight=0.4, relwidth=0.4)
    syf.config(text="Sayfa 3`desiniz")
    global sf
    sf = 3


def syf4():
    bayr.place(x=870, y=450)
    bt3.config(command=oynat10)
    btsyf3.place(x=800, y=400)
    btsyf.place(x=700, y=400)
    bt1.config(text="Şarkıyı Başlat", command=oynat12)
    bt2.config(text="Şarkıyı Başlat", command=oynat11)
    bt3.config(text="Şarkıyı Başlat", command=oynat10)
    bt2.place(x=390, y=270)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    ftobc.place(x=0, y=2131231320, relheight=0.3, relwidth=0.3)
    btsyf.config(text="Sayfa 3", command=syf3)
    btsyf3.config(text="Sayfa 5", command=syf5)
    bt2.config(command=oynat11)
    bt1.config(command=oynat12)
    fto9.place(x=676760, y=0, relheight=0.3, relwidth=0.3)
    fto8.place(x=657750, y=320, relheight=0.4, relwidth=0.3)
    fto7.place(x=5670, y=160, relwidth=0.3, relheight=0.3)
    snm3.place(x=370, y=340)
    snm2.place(x=320, y=170)
    snm.place(x=350, y=10)
    ftomc.place(x=33330, y=170, relheight=0.3, relwidth=0.3)
    snm.config(text="Suzume · Suzume no Tojimari Theme OST Version [Sub Español]")
    snm2.config(text="Bay city - Junko Yagami Japanesse City Pop")
    snm3.config(text="Roar - Christmas Kids (Lyrics)s")
    fto12.place(x=0, y=10, relheight=0.4, relwidth=0.3)
    fto11.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    fto10.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    ftompkr.place(x=33333330, y=350, relheight=0.5, relwidth=0.3)
    syf.config(text="Sayfa 4`desiniz")
    global sf
    sf = 4


def syf5():
    bayr.place(x=870, y=450)
    btsyf3.place(x=800, y=400)
    syf.config(text="Sayfa 5`desiniz")
    ftoa.place(x=2222222222222220, y=222222225)
    fto12.place(x=333330, y=10, relheight=0.4, relwidth=0.3)
    fto11.place(x=333330, y=200, relheight=0.3, relwidth=0.3)
    fto10.place(x=333330, y=350, relheight=0.5, relwidth=0.3)
    ftompkr.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    ftomc.place(x=0, y=170, relheight=0.3, relwidth=0.3)
    fto13.place(x=1231312313120, y=0, relheight=0.3, relwidth=0.3)
    ftobc.place(x=0, y=0, relheight=0.3, relwidth=0.3)
    snm.config(text="Bella Ciao")
    snm2.config(text="Mice On Venus but make it extra nostalgic")
    snm3.config(text="kardaşlar - çökertme ")
    snm3.place(x=360, y=340)
    snm.place(x=390, y=10)
    snm2.place(x=360, y=170)
    bt1.config(text="Şarkıyı Başlat", command=oynt13)
    bt2.config(text="Şarkıyı Başlat", command=mc)
    bt3.config(text="Şarkıyı Başlat", command=seryoz)
    bt2.place(x=390, y=270)
    btsyf.config(text="Sayfa 4", command=syf4)
    btsyf3.config(text="Sayfa 6", command=syf6)
    btsyf.place(x=700, y=400)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    global sf
    sf = 5


def syf6():
    btsyf3.place(x=802310, y=400)
    ftompkr.place(x=0, y=323242350, relheight=0.5, relwidth=0.3)
    ftomc.place(x=0, y=13423470, relheight=0.3, relwidth=0.3)
    ftobc.place(x=0, y=231231230, relheight=0.3, relwidth=0.3)
    sism.place(x=213123, y=23123)
    # ------#
    syf.config(text="Sayfa 6`dasınız")
    fto13.place(x=0, y=0, relheight=0.3, relwidth=0.3)
    snm.config(text="【Official】Uru 『紙一重』 TVアニメ「地獄楽」エンディングテーマ")
    snm2.config(text="...(2)")
    snm3.config(text="...(3) ")
    snm3.place(x=360, y=340)
    snm.place(x=330, y=10)
    snm2.place(x=360, y=170)
    bt1.config(text="Şarkıyı Başlat", command=oynt14)
    bt2.config(text="Şarkıyı Başlat", command=mc)
    bt3.config(text="Şarkıyı Başlat", command=seryoz)
    bt1.place(x=390, y=100)
    bt2.place(x=390, y=270)
    bt3.place(x=390, y=440)
    btsyf.config(text="Sayfa 5", command=syf5)
    btsyf.place(x=700, y=400)
    global sf
    sf = 6


def uyarsil():
    uyar.place(x=123123123, y=123)
    uyrsil.place(x=5333350, y=450)


def durdur1():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    pause.place(x=523330, y=470)
    fto.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    snm.place(x=350, y=10)
    yeniden1.place(x=5390, y=470)
    bt1.place(x=390, y=100)
    bt1.config(command=oynat1)
    fto2.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=390, y=170)
    bt2.place(x=390, y=270)
    bt1.config(text="Şarkıyı başlat", command=oynat1)
    fto3.place(x=0, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=390, y=440)
    snm3.place(x=350, y=340)
    btsyf.place(x=800, y=400)
    brw.place(x=9128, y=80)
    mixer.music.stop()


def yolla():
    global youtube
    web.open(youtube)


def oynat1():
    global sarkiisim
    sarkiisim = "Stay with me"
    mixer.music.load("mp1.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("stylc.mp3")
    if s == "Speed up" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Speed up yok, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
        uyar.place(x=330, y=450)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp1.mp3")
        if s == "Lycris":
            mixer.music.load("stylc.mp3")
    fto3.place(x=32323, y=320, relheight=0.3, relwidth=0.3)
    fto2.place(x=33333, y=160, relheight=0.3, relwidth=0.3)
    fto.place(x=10, y=0, relwidth=1, relheight=1)
    # ---------------------------
    bt3.place(x=39320, y=440)
    bt2.place(x=390333, y=270)
    snm3.place(x=35230, y=340)
    snm2.place(x=350333, y=170)
    # ---------------------------
    bt1.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=3700, y=400)
    snm.place(x=400, y=40)
    # ----------------------------
    bt1.config(text="Şarkıyı Kapat", command=durdur1)
    global youtube
    youtube = "https://www.youtube.com/watch?v=DXT9dF-WK-I"
    brw.config(command=yolla)
    mixer.music.play()


def durdur2():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    pause.place(x=52330, y=470)
    fto2.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=390, y=170)
    yeniden1.place(x=59033, y=470)
    bt2.place(x=390, y=270)
    bt2.config(text="Şarkıyı Başlat", command=oynat2)
    fto.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    snm.place(x=350, y=10)
    bt1.place(x=390, y=100)
    fto3.place(x=0, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=390, y=440)
    snm3.place(x=350, y=340)
    btsyf.place(x=800, y=400)
    brw.place(x=32220, y=470)
    mixer.music.stop()


def oynat2():
    global sarkiisim
    sarkiisim = "Unutulanlar"
    mixer.music.load("mp2.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp2lyc.mp3")
    if s == "Speed up":
        mixer.music.load("mp2spup.mp3")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=450)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp2.mp3")
        if s == "Lycris":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up seçebilrsin?", fg="red")
            mixer.music.load("mp2lyc.mp3")
        elif s == "Speed up":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
            mixer.music.load("mp2spup.mp3")
    fto.place(x=35032323, y=80, relwidth=0.3, relheight=0.3)
    bt1.place(x=460323, y=400)
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=3700, y=400)
    snm.place(x=4032332, y=40)
    fto2.place(x=10, y=0, relwidth=1, relheight=1)
    bt2.config(text="Şarkıyı Kapat", command=durdur2)
    snm2.place(x=468, y=40)
    fto3.place(x=32323, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=39320, y=440)
    snm3.place(x=35230, y=340)
    global youtube
    youtube = "https://www.youtube.com/watch?v=aqFoVhuG2ss"
    mixer.music.play()


def durdur3():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    pause.place(x=333520, y=470)
    fto2.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=390, y=170)
    bt2.place(x=390, y=270)
    bt2.config(text="Şarkıyı Başlat", command=oynat2)
    fto.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    snm.place(x=350, y=10)
    bt1.place(x=390, y=100)
    fto3.place(x=0, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=390, y=440)
    snm3.place(x=350, y=340)
    btsyf.place(x=800, y=400)
    yeniden1.place(x=59033, y=470)
    brw.place(x=32220, y=470)
    bt3.config(text="Şarkıyı Başlat", command=oynat3)
    mixer.music.stop()


def oynat3():
    global sarkiisim
    sarkiisim = "𝙎𝙚𝙥𝙩𝙚𝙢𝙗𝙚𝙧 - 𝙎𝙥𝙖𝙧𝙠𝙮 𝙙𝙚𝙖𝙩𝙝𝙘𝙖𝙥"
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris" or s == "Speed up" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Üzgünüm Bu Müzik`de Speed/Lycris ve Seslendirme yok :(", fg="red")
        uyar.place(x=300, y=430)
        uyrsil.place(x=700, y=430)
    fto.place(x=35032323, y=80, relwidth=0.3, relheight=0.3)
    bt1.place(x=460323, y=400)
    bt3.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    snm.place(x=4032332, y=40)
    mixer.music.load("mp3.mp3")
    fto2.place(x=350232, y=80, relwidth=0.3, relheight=0.3)
    bt2.place(x=460232, y=400)
    snm2.place(x=468232, y=40)
    fto3.place(x=250, y=80, relwidth=0.5, relheight=0.5)
    bt3.config(text="Şarkıyı Kapat", command=durdur3)
    snm3.place(x=400, y=40)
    btsyf.place(x=70033, y=400)
    global youtube
    youtube = "https://www.youtube.com/watch?v=bwoSjtjXK5U&t=4s"
    mixer.music.play()


def durdur4():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    pause.place(x=533320, y=470)
    fto4.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    snm.place(x=350, y=10)
    bt1.place(x=390, y=100)
    bt1.config(command=oynat4)
    fto5.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=390, y=170)
    bt2.place(x=390, y=270)
    btsyf3.place(x=800, y=400)
    bt1.config(text="Şarkıyı başlat", command=oynat4)
    fto6.place(x=0, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=390, y=440)
    snm3.place(x=390, y=340)
    btsyf.place(x=700, y=400)
    yeniden1.place(x=59330, y=470)
    brw.place(x=3320, y=470)
    mixer.music.stop()


def oynat4():
    mixer.music.load("mp5no.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp5lyc.mp3")
        print("lycr 1")
    if s == "Speed up":
        mixer.music.load("mp5.mp3")
        print("speed 1")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=280, y=420)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp5no.mp3")
        print("normalde kald")
        if s == "Lycris":
            print("lyc 2")
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up istersen seçebilrsin?", fg="red")
            mixer.music.load("mp5lyc.mp3")
        elif s == "Speed up":
            print("speed 2")
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris istersen seçebilrsin?",
                        fg="red")
            mixer.music.load("mp5.mp3")
    fto6.place(x=33350, y=80, relwidth=0.3, relheight=0.3)
    bt1.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf3.place(x=8321200, y=400)
    bt1.config(text="Şarkıyı Durdur", command=durdur4)
    snm.place(x=410, y=20)
    fto5.place(x=33333, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=350333, y=170)
    bt2.place(x=390333, y=270)
    fto4.place(x=10, y=-10, relheight=1, relwidth=1)
    bt3.place(x=39320, y=440)
    snm3.place(x=35230, y=340)
    btsyf.place(x=73300, y=400)
    global youtube
    youtube = "https://www.youtube.com/watch?v=lCv-XCbNiFU"
    global sarkiisim
    sarkiisim = "Daft punk"
    mixer.music.play()


def durdur5():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    pause.place(x=53333320, y=470)
    fto5.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=370, y=170)
    bt2.place(x=390, y=270)
    btsyf3.place(x=800, y=400)
    bt2.config(text="Şarkıyı Başlat", command=oynat5)
    fto4.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    snm.place(x=350, y=10)
    bt1.place(x=390, y=100)
    fto6.place(x=0, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=390, y=440)
    snm3.place(x=390, y=340)
    btsyf.place(x=700, y=400)
    yeniden1.place(x=59330, y=470)
    brw.place(x=23121, y=80)
    mixer.music.stop()


def oynat5():
    mixer.music.load("mp4.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp4lyc.mp3")
        print("lycr 1")
    if s == "Speed up":
        mixer.music.load("mp4speup.mp3"),
        print("speed 1")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=450)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp4.mp3")
        print("normalde kald")
        if s == "Lycris":
            print("lyc 2")
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up istersen seçebilrsin?", fg="red")
            mixer.music.load("mp4lyc.mp3")
        elif s == "Speed up":
            print("speed 2")
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris istersen seçebilrsin?",
                        fg="red")
            mixer.music.load("mp4speup.mp3")
    fto4.place(x=35032323, y=80, relwidth=0.3, relheight=0.3)
    bt1.place(x=460323, y=400)
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    snm.place(x=4032332, y=40)
    btsyf3.place(x=82131300, y=400)
    fto5.place(x=10, y=0, relwidth=1, relheight=1)
    bt2.config(text="Şarkıyı Kapat", command=durdur5)
    snm2.place(x=430, y=80)
    fto6.place(x=32323, y=320, relheight=0.3, relwidth=0.3)
    bt3.place(x=39320, y=440)
    snm3.place(x=35230, y=340)
    btsyf.place(x=70330, y=400)
    global youtube
    youtube = "https://www.youtube.com/watch?v=rYEDA3JcQqw"
    global sarkiisim
    sarkiisim = "Adele rolling"
    mixer.music.play()


def durdur6():
    videoplayer.place(x=212321313, y=13213132131231212312312)
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    fto5.place(x=0, y=160, relheight=0.3, relwidth=0.3)
    snm2.place(x=370, y=170)
    bt2.place(x=390, y=270)
    pause.place(x=533320, y=470)
    btsyf3.place(x=800, y=400)
    bt2.config(text="Şarkıyı Başlat")
    fto4.place(x=0, y=0, relwidth=0.3, relheight=0.3)
    snm.place(x=350, y=10)
    bt1.place(x=390, y=100)
    fto6.place(x=0, y=320, relheight=0.4, relwidth=0.3)
    bt3.place(x=390, y=440)
    snm3.place(x=390, y=340)
    bt3.config(text="Şarkıyı Başlat", command=oynat6)
    btsyf.place(x=700, y=400)
    yeniden1.place(x=59033, y=470)
    global g
    g = False
    bv.place(x=250, y=4231213231310)
    brw.place(x=33320, y=470)
    global sarkiisim
    sarkiisim = ""
    altl.place(x=111111, y=21323)
    mixer.music.stop()


def oynat6():
    global sarkiisim
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris" or s == "Speed up" or s2 == "Türkce Seslendirme" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı":
        uyar.config(text="Üzgünüm Bu Müzik`de Speed/Lycris, Seslendirme, :( (Alt yazı açıldığında durdurma tuşu "
                         "silinir)", fg="red")
        uyar.place(x=250, y=450)
        uyrsil.place(x=700, y=430)
    fto4.place(x=35032323, y=80, relwidth=0.3, relheight=0.3)
    bt1.place(x=460323, y=400)
    bt3.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    snm.place(x=4032332, y=40)
    mixer.music.load("mp6.mp3")
    btsyf3.place(x=12313800, y=400)
    fto5.place(x=350232, y=80, relwidth=0.3, relheight=0.3)
    bt2.place(x=460232, y=400)
    snm2.place(x=468232, y=40)
    fto6.place(x=-10, y=-50, relwidth=1, relheight=1)
    bt3.config(text="Şarkıyı Kapat", command=durdur6)
    snm3.place(x=470, y=10)
    btsyf.place(x=73300, y=400)
    global youtube
    youtube = "https://www.youtube.com/watch?v=BZk8UZ7a7uY"
    sarkiisim = "Twotime"
    bv.place(x=250, y=420)

    global g
    g = True
    if s1 == "Türkce Alt yazı":
        pause.place(x=54444420, y=470)
        print("Alt yazı grş başarılı")
        bt3.place(x=480, y=470)
        pc.after(2730, lambda: altyazi2())
    elif s1 == "Kapalı":
        pause.place(x=520, y=470)
        print("Alt yazı kapalı")
    elif s1 == "Orginal Alt yazı":
        pause.place(x=5244440, y=470)
        bt3.place(x=480, y=470)
        print("Alt yazı grş başarılı")
        altl.config(text=alt1)
        pc.after(2730, lambda: altyazi2())
    mixer.music.play()


def durozl():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    btsyf3.place(x=800, y=400)
    fto7.place(x=0, y=320, relheight=0.5, relwidth=0.3)
    bt1.place(x=410, y=100)
    bt2.place(x=410, y=270)
    bt3.place(x=410, y=460)
    pause.place(x=533320, y=470)
    snm3.place(x=420, y=340)
    snm.place(x=390, y=10)
    snm2.place(x=390, y=170)
    bt3.config(command=oyntozl, text="Şarkıyı Başlat")
    brw.place(x=23370, y=470)
    yeniden1.place(x=54033, y=470)
    fto8.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    fto9.place(x=-100, y=10, relheight=0.4, relwidth=0.4)
    btsyf.place(x=700, y=400)

    mixer.music.stop()


def oyntozl():
    btsyf3.place(x=83300, y=400)
    mixer.music.load("mpoz.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris" or s == "Speed up" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Üzgünüm Bu Müzik`de Speed/Lycris, Seslendirme, ve alt yazı yok :(", fg="red")
        uyar.place(x=300, y=430)
        uyrsil.place(x=700, y=430)
    fto7.place(x=0, y=25, relheight=0.8, relwidth=1)
    bt1.place(x=460323, y=400)
    bt2.place(x=460232, y=400)
    bt3.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=73300, y=400)
    bt3.config(command=durozl, text="Şarkıyı Kapat")
    snm3.place(x=470, y=0)
    snm2.place(x=33390, y=340)
    snm.place(x=39330, y=340)
    global youtube
    fto9.place(x=1231310, y=25, relheight=0.8, relwidth=0.8)
    youtube = "https://www.youtube.com/watch?v=JNwSOPLVkIc"
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Legion"
    fto8.place(x=323123120, y=25, relheight=0.8, relwidth=1)


def durdur8():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    btsyf3.place(x=800, y=400)
    fto7.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    bt1.place(x=410, y=100)
    bt2.place(x=410, y=270)
    pause.place(x=523330, y=470)
    bt3.place(x=410, y=460)
    btsyf.place(x=700, y=400)
    snm3.place(x=420, y=340)
    snm.place(x=390, y=10)
    snm2.place(x=390, y=170)
    bt3.config(command=oyntozl)
    brw.place(x=23370, y=470)
    yeniden1.place(x=54033, y=470)
    fto8.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    bt2.config(command=oynt8, text="Şarkıyı Başlat")
    yeniden1.place(x=5332310, y=470)
    fto9.place(x=-100, y=10, relheight=0.4, relwidth=0.4)
    mixer.music.stop()


def oynt8():
    btsyf3.place(x=80330, y=400)
    mixer.music.load("mp8.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp8lyc.mp3")
        print("lycr 1")
    if s == "Speed up":
        mixer.music.load("mp8speup.mp3")
        print("speed 1")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp8.mp3")
        print("normalde kald")
        if s == "Lycris":
            print("lyc 2")
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up istersen seçebilrsin?", fg="red")
            mixer.music.load("mp8lyc.mp3")
        elif s == "Speed up":
            print("speed 2")
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris istersen seçebilrsin?",
                        fg="red")
            mixer.music.load("mp8speup.mp3")
    snm3.place(x=444470, y=0)
    snm2.place(x=430, y=0)
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=73300, y=400)
    snm.place(x=39330, y=340)
    fto8.place(x=150, y=25, relheight=0.8, relwidth=0.7)
    global youtube
    youtube = "https://www.youtube.com/watch?v=37pGzZ6PZOY"
    bt1.place(x=460323, y=400)
    bt3.place(x=423420, y=460)
    fto7.place(x=3242432420, y=25, relheight=0.8, relwidth=1)
    bt2.config(command=durdur8, text="Şarkıyı Kapat")
    fto9.place(x=21313210, y=25, relheight=0.8, relwidth=1)
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Lonley day"


def durs():
    global sf
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    ftoot.place(x=4444440, y=25, relheight=0.8, relwidth=1)
    pause.place(x=5233330, y=470)
    ftoas.place(x=33333330, y=25, relheight=0.8, relwidth=0.9)
    ftoecho1.place(x=32323320, y=25, relheight=0.8, relwidth=1)
    mixer.music.stop()
    ftoecho.place(x=12233, y=22323)
    yeniden1.place(x=595430, y=470)
    brw.place(x=253350, y=470)
    ftorickrolled.place(x=2344242340, y=25, relheight=0, relwidth=0)
    sism.place(x=4213333333333333333, y=23424324)
    ftos.place(x=3213130, y=25, relheight=0.8, relwidth=0.9)
    ftoa.place(x=123132131313213131231310, y=2342423432423423432432432432424234234234234234343245, relheight=1,
               relwidth=1)
    if sf == 1:
        syf1()
    elif sf == 2:
        syf2()
    elif sf == 3:
        syf3()
    elif sf == 4:
        syf4()
    elif sf == 5:
        syf5()
    elif sf == 6:
        syf6()


def sukur():
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    global sf
    print("SUPRİZEE!")
    ftoot.place(x=4444440, y=25, relheight=0.8, relwidth=1)
    pause.place(x=5233330, y=470)
    ftoas.place(x=33333330, y=25, relheight=0.8, relwidth=0.9)
    ftoecho1.place(x=32323320, y=25, relheight=0.8, relwidth=1)
    mixer.music.stop()
    ftoecho.place(x=12233, y=22323)
    yeniden1.place(x=595430, y=470)
    brw.place(x=253350, y=470)
    ftorickrolled.place(x=2344242340, y=25, relheight=0, relwidth=0)
    sism.place(x=421333333333333333300, y=0)
    ftos.place(x=3213130, y=25, relheight=0.8, relwidth=0.9)
    ftoa.place(x=123132131313213131231310, y=2342423432423423432432432432424234234234234234343245, relheight=0.8,
               relwidth=1)
    yeniden1.place(x=590, y=470)
    btsyf3.place(x=83300, y=470)
    btsyf.place(x=83300, y=470)
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    bt2.config(text="Şarkıyı Kapat", command=durs)
    global g
    global sarkiisim
    g = True
    global youtube
    a87 = str(volume2.get())
    if sf == 1:
        ftoa.place(x=213120, y=25, relheight=0.8, relwidth=1)
        fto2.place(x=32130, y=160, relheight=0.3, relwidth=0.3)
        snm2.place(x=321390, y=170)
        sism.place(x=400, y=0)
        fto.place(x=2131313130, y=0, relwidth=0.3, relheight=0.3)
        snm.place(x=3213150, y=10)
        bt1.place(x=3123130, y=100)
        fto3.place(x=21310, y=320, relheight=0.3, relwidth=0.3)
        bt3.place(x=3123190, y=440)
        snm3.place(x=321312350, y=340)
        btsyf.place(x=23131700, y=400)
        print("El1")
        if a87 == "Allahıma Şükür":
            mixer.music.load("mpa.mp3")
            mixer.music.play()
            sism.config(text="Tayyip - Allahıma Şükür Bugün de Başkanım (TRAP Autotune UZUN VERSİYON)")
            youtube = "https://www.youtube.com/watch?v=1IYejfWvRk0"
            ftoa.place(x=0, y=25, relheight=0.8, relwidth=1)
        elif a87 == "The Other Side":
            sism.place(x=300, y=0)
            if s2 == "Türkce Seslendirme":
                sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                mixer.music.load("theothersidetr (1).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
            elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                sism.config(
                    text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                mixer.music.load("theothersideen (2).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s == "Lycris" or s == "Speed up":
                uyar.config(
                    text="Bu Müzik`de Lycris/Speed up, ve alt yazı yok :(, istersen Türkce seslendirem/Orginal seslendirme seçebilrsin?",
                    fg="red")
                uyar.place(x=330, y=430)
                uyrsil.place(x=270, y=430)
                mixer.music.load("theothersideen (2).mp3")
                print("normalde kald")
                sism.place(x=300, y=0)
                if s2 == "Türkce Seslendirme":
                    sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                    mixer.music.load("theothersidetr (1).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
                elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                    sism.config(
                        text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                    mixer.music.load("theothersideen (2).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            mixer.music.play()
        elif a87 == "ECHO":
            w = secili2.get()
            sism.config(text="【VOCALOID Orijinal】YANSIMA【Gumi İngilizce】")
            if s2 == "Türkce Seslendirme":
                ftoecho.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho.mp3")
                youtube = "https://www.youtube.com/watch?v=05Iw_jOxsuw"
                mixer.music.play()
            elif s2 == "Orginal Seslendirme" or "Kapalı":
                ftoecho1.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho1.mp3")
                youtube = "https://www.youtube.com/watch?v=cQKGUgOfD8U"
                mixer.music.play()
        elif a87 == "oy asiye":
            mixer.music.load("oysiye.mp3")
            mixer.music.play()
            sism.config(text="Oy asiye")
            ftoas.place(x=0, y=25, relheight=0.8, relwidth=0.9)
        elif a87 == "Please rickrolled me":
            mixer.music.load("mprickrolled.mp3")
            mixer.music.play()
            sism.config(text="Never Gonna Give You Up Opening ( Rickroll demon slayer op )")
            youtube = "https://www.youtube.com/watch?v=FmQbFdsngMA"
            ftorickrolled.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    elif sf == 2:
        print("El 2")
        ftoa.place(x=23120, y=25, relheight=0.8, relwidth=1)
        fto5.place(x=32130, y=16340, relheight=0, relwidth=0)
        snm2.place(x=321390, y=170)
        sism.place(x=400, y=0)
        fto4.place(x=2131313130, y=0, relwidth=0, relheight=0)
        snm.place(x=3213150, y=10)
        bt1.place(x=3123130, y=100)
        fto6.place(x=213310, y=320, relheight=0, relwidth=0)
        bt3.place(x=3123190, y=440)
        snm3.place(x=321312350, y=340)
        btsyf.place(x=23131700, y=400)
        if a87 == "Allahıma Şükür":
            mixer.music.load("mpa.mp3")
            mixer.music.play()
            sism.config(text="Tayyip - Allahıma Şükür Bugün de Başkanım (TRAP Autotune UZUN VERSİYON)")
            youtube = "https://www.youtube.com/watch?v=1IYejfWvRk0"
            ftoa.place(x=0, y=25, relheight=0.8, relwidth=1)
        elif a87 == "The Other Side":
            sism.place(x=300, y=0)
            if s2 == "Türkce Seslendirme":
                sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                mixer.music.load("theothersidetr (1).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
            elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                sism.config(
                    text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                mixer.music.load("theothersideen (2).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s == "Lycris" or s == "Speed up":
                uyar.config(
                    text="Bu Müzik`de Lycris/Speed up, ve alt yazı yok :(, istersen Türkce seslendirem/Orginal seslendirme seçebilrsin?",
                    fg="red")
                uyar.place(x=330, y=430)
                uyrsil.place(x=270, y=430)
                mixer.music.load("theothersideen (2).mp3")
                print("normalde kald")
                sism.place(x=300, y=0)
                if s2 == "Türkce Seslendirme":
                    sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                    mixer.music.load("theothersidetr (1).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
                elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                    sism.config(
                        text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                    mixer.music.load("theothersideen (2).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            mixer.music.play()
        elif a87 == "oy asiye":
            mixer.music.load("oysiye.mp3")
            mixer.music.play()
            sism.config(text="Oy asiye")
            ftoas.place(x=0, y=25, relheight=0.8, relwidth=0.9)
        elif a87 == "ECHO":
            sism.config(text="【VOCALOID Orijinal】YANSIMA【Gumi İngilizce】")
            if s2 == "Türkce Seslendirme" or "Kapalı":
                ftoecho.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho.mp3")
                youtube = "https://www.youtube.com/watch?v=05Iw_jOxsuw"
            elif s2 == "Orginal Seslendirme":
                ftoecho1.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho1.mp3")
                youtube = "https://www.youtube.com/watch?v=cQKGUgOfD8U"
            mixer.music.play()
        elif a87 == "Please rickrolled me":
            mixer.music.load("mprickrolled.mp3")
            mixer.music.play()
            youtube = "https://www.youtube.com/watch?v=FmQbFdsngMA"
            sism.config(text="Never Gonna Give You Up Opening ( Rickroll demon slayer op )")
            ftorickrolled.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    elif sf == 3:
        ftoa.place(x=121320, y=25, relheight=0.8, relwidth=1)
        fto8.place(x=32130, y=160, relheight=0.3, relwidth=0.3)
        snm2.place(x=321390, y=170)
        print("El 3")
        sism.place(x=400, y=0)
        fto9.place(x=2131313130, y=0, relwidth=0.3, relheight=0.3)
        snm.place(x=3213150, y=10)
        bt1.place(x=3123130, y=100)
        fto7.place(x=213310, y=320, relheight=0.3, relwidth=0.3)
        bt3.place(x=3123190, y=440)
        snm3.place(x=321312350, y=340)
        btsyf.place(x=23131700, y=400)
        if a87 == "Allahıma Şükür":
            mixer.music.load("mpa.mp3")
            mixer.music.play()
            youtube = "https://www.youtube.com/watch?v=1IYejfWvRk0"
            ftoa.place(x=0, y=25, relheight=0.8, relwidth=1)
        elif a87 == "The Other Side":
            sism.place(x=300, y=0)
            if s2 == "Türkce Seslendirme":
                sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                mixer.music.load("theothersidetr (1).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
            elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                sism.config(
                    text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                mixer.music.load("theothersideen (2).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s == "Lycris" or s == "Speed up":
                uyar.config(
                    text="Bu Müzik`de Lycris/Speed up, ve alt yazı yok :(, istersen Türkce seslendirem/Orginal seslendirme seçebilrsin?",
                    fg="red")
                uyar.place(x=330, y=430)
                uyrsil.place(x=270, y=430)
                mixer.music.load("theothersideen (2).mp3")
                print("normalde kald")
                sism.place(x=300, y=0)
                if s2 == "Türkce Seslendirme":
                    sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                    mixer.music.load("theothersidetr (1).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
                elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                    sism.config(
                        text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                    mixer.music.load("theothersideen (2).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            mixer.music.play()
        elif a87 == "oy asiye":
            mixer.music.load("oysiye.mp3")
            mixer.music.play()
            sism.config(text="Oy asiye")
            ftoas.place(x=0, y=25, relheight=0.8, relwidth=0.9)
        elif a87 == "ECHO":
            s2 = secili2.get()
            sism.config(text="【VOCALOID Orijinal】YANSIMA【Gumi İngilizce】")
            if s2 == "Türkce Seslendirme" or "Kapalı":
                ftoecho.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho.mp3")
                youtube = "https://www.youtube.com/watch?v=05Iw_jOxsuw"
            elif s2 == "Orginal Seslendirme":
                ftoecho1.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho1.mp3")
                youtube = "https://www.youtube.com/watch?v=cQKGUgOfD8U"
            mixer.music.play()
        elif a87 == "Please rickrolled me":
            mixer.music.load("mprickrolled.mp3")
            mixer.music.play()
            sism.config(text="Never Gonna Give You Up Opening ( Rickroll demon slayer op )")
            youtube = "https://www.youtube.com/watch?v=FmQbFdsngMA"
            ftorickrolled.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    elif sf == 4:
        ftoa.place(x=121320, y=25, relheight=0.8, relwidth=1)
        fto11.place(x=32130, y=160, relheight=0.3, relwidth=0.3)
        snm2.place(x=321390, y=170)
        print("El 4")
        sism.place(x=400, y=0)
        fto10.place(x=2131313130, y=0, relwidth=0.3, relheight=0.3)
        snm.place(x=3213150, y=10)
        bt1.place(x=3123130, y=100)
        fto12.place(x=213310, y=320, relheight=0.3, relwidth=0.3)
        bt3.place(x=3123190, y=440)
        snm3.place(x=321312350, y=340)
        btsyf.place(x=23131700, y=400)
        if a87 == "Allahıma Şükür":
            mixer.music.load("mpa.mp3")
            mixer.music.play()
            youtube = "https://www.youtube.com/watch?v=1IYejfWvRk0"
            ftoa.place(x=0, y=25, relheight=0.8, relwidth=1)
        elif a87 == "The Other Side":
            sism.place(x=300, y=0)
            if s2 == "Türkce Seslendirme":
                sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                mixer.music.load("theothersidetr (1).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
            elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                sism.config(
                    text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                mixer.music.load("theothersideen (2).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s == "Lycris" or s == "Speed up":
                uyar.config(
                    text="Bu Müzik`de Lycris/Speed up, ve alt yazı yok :(, istersen Türkce seslendirem/Orginal seslendirme seçebilrsin?",
                    fg="red")
                uyar.place(x=330, y=430)
                uyrsil.place(x=270, y=430)
                mixer.music.load("theothersideen (2).mp3")
                print("normalde kald")
                sism.place(x=300, y=0)
                if s2 == "Türkce Seslendirme":
                    sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                    mixer.music.load("theothersidetr (1).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
                elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                    sism.config(
                        text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                    mixer.music.load("theothersideen (2).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            mixer.music.play()
        elif a87 == "oy asiye":
            mixer.music.load("oysiye.mp3")
            mixer.music.play()
            sism.config(text="Oy asiye")
            ftoas.place(x=0, y=25, relheight=0.8, relwidth=0.9)
        elif a87 == "ECHO" or "Kapalı":
            w = secili2.get()
            sism.config(text="【VOCALOID Orijinal】YANSIMA【Gumi İngilizce】")
            if w == "Türkce Seslendirme":
                ftoecho.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho.mp3")
                youtube = "https://www.youtube.com/watch?v=05Iw_jOxsuw"
            elif w == "Orginal Seslendirme":
                ftoecho1.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho1.mp3")
                youtube = "https://www.youtube.com/watch?v=cQKGUgOfD8U"
            mixer.music.play()
        elif a87 == "Please rickrolled me":
            mixer.music.load("mprickrolled.mp3")
            mixer.music.play()
            sism.config(text="Never Gonna Give You Up Opening ( Rickroll demon slayer op )")
            youtube = "https://www.youtube.com/watch?v=FmQbFdsngMA"
            ftorickrolled.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    elif sf == 5:
        ftobc.place(x=-333333335, y=25, relheight=1, relwidth=1)
        ftompkr.place(x=3333330, y=350, relheight=0.5, relwidth=0.3)
        ftomc.place(x=33333330, y=170, relheight=0.3, relwidth=0.3)
        snm2.place(x=321390, y=170)
        sism.place(x=400, y=0)
        snm.place(x=3213150, y=10)
        bt1.place(x=3123130, y=100)
        bt3.place(x=3123190, y=440)
        snm3.place(x=321312350, y=340)
        btsyf.place(x=23131700, y=400)
        print("El 5")
        if a87 == "Allahıma Şükür":
            mixer.music.load("mpa.mp3")
            mixer.music.play()
            sism.config(text="Tayyip - Allahıma Şükür Bugün de Başkanım (TRAP Autotune UZUN VERSİYON)")
            youtube = "https://www.youtube.com/watch?v=1IYejfWvRk0"
            ftoa.place(x=0, y=25, relheight=0.8, relwidth=1)
        elif a87 == "The Other Side":
            sism.place(x=300, y=0)
            if s2 == "Türkce Seslendirme":
                sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                mixer.music.load("theothersidetr (1).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
            elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                sism.config(
                    text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                mixer.music.load("theothersideen (2).mp3")
                ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s == "Lycris" or s == "Speed up":
                uyar.config(
                    text="Bu Müzik`de Lycris/Speed up, ve alt yazı yok :(, istersen Türkce seslendirem/Orginal seslendirme seçebilrsin?",
                    fg="red")
                uyar.place(x=330, y=430)
                uyrsil.place(x=270, y=430)
                mixer.music.load("theothersideen (2).mp3")
                print("normalde kald")
                sism.place(x=300, y=0)
                if s2 == "Türkce Seslendirme":
                    sism.config(text="The Greatest Showman - The Other Side (Turkish Cover by @Minachua & @Miirai)")
                    mixer.music.load("theothersidetr (1).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=38lKn1z5n4Y"
                elif s2 == "Orginal Seslendirme" or s2 == "Kapalı":
                    sism.config(
                        text="The Other Side -- female ver. (from The Greatest Showman) 【covered by Anna ft. Cami-Cat】")
                    mixer.music.load("theothersideen (2).mp3")
                    ftoot.place(x=0, y=25, relheight=0.8, relwidth=1)
                    youtube = "https://www.youtube.com/watch?v=7jyuhwVSCks"
            mixer.music.play()
        elif a87 == "oy asiye":
            mixer.music.load("oysiye.mp3")
            mixer.music.play()
            sism.config(text="Oy asiye")
            ftoas.place(x=0, y=25, relheight=0.8, relwidth=0.9)
        elif a87 == "ECHO" or "Kapalı":
            s2 = secili2.get()
            sism.config(text="【VOCALOID Orijinal】YANSIMA【Gumi İngilizce】")
            if s2 == "Türkce Seslendirme":
                ftoecho.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho.mp3")
                youtube = "https://www.youtube.com/watch?v=05Iw_jOxsuw"
            elif s2 == "Orginal Seslendirme":
                ftoecho1.place(x=0, y=25, relheight=0.8, relwidth=1)
                mixer.music.load("mpecho1.mp3")
                youtube = "https://www.youtube.com/watch?v=cQKGUgOfD8U"
            mixer.music.play()
        elif a87 == "Please rickrolled me":
            mixer.music.load("mprickrolled.mp3")
            mixer.music.play()
            sism.config(text="Never Gonna Give You Up Opening ( Rickroll demon slayer op )")
            youtube = "https://www.youtube.com/watch?v=FmQbFdsngMA"
            ftorickrolled.place(x=0, y=25, relheight=0.8, relwidth=0.9)
            ftos.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    if s == "Türkce Alt yazı":
        print("Alt yazı grş başarılı")
        pc.after(0, lambda: altyazi2())
    elif s == "Kapalı":
        print("Alt yazı kapalı")
    elif s == "Orginal Alt yazı":
        print("Alt yazı grş başarılı")
        altl.config(text=alt1)
        pc.after(0, lambda: altyazi2())


def oynt9():
    mixer.music.load("mp9.mp3")
    btsyf3.place(x=83300, y=400)
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp9lyc.mp3")
    if s == "Speed up":
        mixer.music.load("mp9spep.mp3")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp9.mp3")
        if s == "Lycris":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up seçebilrsin?", fg="red")
            mixer.music.load("mp9lyc.mp3")
        elif s == "Speed up":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
            mixer.music.load("mp9spep.mp3")
    snm3.place(x=444470, y=0)
    snm.place(x=430, y=0)
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=73300, y=400)
    snm2.place(x=39330, y=340)
    fto9.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    global youtube
    youtube = "https://www.youtube.com/watch?v=FRo_9RMm5q8"
    bt1.place(x=460323, y=400)
    bt3.place(x=423420, y=460)
    fto7.place(x=3242432420, y=25, relheight=0.8, relwidth=1)
    bt2.config(command=durdur8, text="Şarkıyı Kapat")
    fto8.place(x=1534430, y=25, relheight=0.8, relwidth=0.7)
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Rei sing"


def durdur10():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    btsyf.place(x=700, y=400)
    fto11.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    fto12.place(x=0, y=10, relheight=0.4, relwidth=0.3)
    mixer.music.stop()
    fto10.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    yeniden1.place(x=543430, y=470)
    brw.place(x=223170, y=470)
    bt2.place(x=390, y=270)
    pause.place(x=523330, y=470)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    snm3.place(x=370, y=340)
    snm2.place(x=320, y=170)
    snm.place(x=350, y=10)
    btsyf.place(x=700, y=400)
    btsyf3.place(x=800, y=400)
    bt3.config(text="Şarkıyı Başlat", command=oynat10)


def oynat10():
    mixer.music.load("roarno.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp10.mp3")
    if s == "Speed up":
        mixer.music.load("raorspeup.mp3")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("roarno.mp3")
        if s == "Lycris":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up seçebilrsin?", fg="red")
            mixer.music.load("mp10.mp3")
        elif s == "Speed up":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
            mixer.music.load("raorspeup.mp3")
    fto11.place(x=23210, y=200, relheight=0.3, relwidth=0.3)
    fto12.place(x=21213210, y=10, relheight=0.4, relwidth=0.3)
    bt3.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=72300, y=400)
    btsyf3.place(x=833200, y=400)
    global youtube
    bt3.config(text="Şarkıyı Kapat", command=durdur10)
    snm3.place(x=400, y=0)
    snm.place(x=33350, y=10)
    snm2.place(x=33390, y=170)
    youtube = "https://www.youtube.com/watch?v=gGOcLcD0NqA"
    bt2.place(x=488820, y=460)
    bt1.place(x=43320, y=460)
    fto10.place(x=0, y=25, relheight=0.8, relwidth=0.9)
    mixer.music.play()
    global sarkiisim
    sarkiisim = "roar"


def durdur11():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)

    btsyf.place(x=700, y=400)
    mixer.music.stop()
    pause.place(x=523330, y=470)
    fto10.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    fto11.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    fto12.place(x=0, y=10, relheight=0.4, relwidth=0.3)
    yeniden1.place(x=543430, y=470)
    brw.place(x=223170, y=470)
    bt2.place(x=390, y=270)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    snm3.place(x=370, y=340)
    snm2.place(x=320, y=170)
    snm.place(x=350, y=10)
    btsyf.place(x=700, y=400)
    btsyf3.place(x=800, y=400)
    bt2.config(text="Şarkıyı Başlat", command=oynat11)


def oynat11():
    mixer.music.load("mp11.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("baylyc.mp3")
    if s == "Speed up":
        mixer.music.load("bayspd.mp3")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp11.mp3")
        if s == "Lycris":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up seçebilrsin?", fg="red")
            mixer.music.load("baylyc.mp3")
        elif s == "Speed up":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
            mixer.music.load("bayspd.mp3")
    btsyf.place(x=72300, y=400)
    btsyf3.place(x=833200, y=400)
    global youtube
    bt2.config(text="Şarkıyı Kapat", command=durdur11)
    snm2.place(x=350, y=0)
    snm3.place(x=33350, y=10)
    snm.place(x=33390, y=170)
    youtube = "https://www.youtube.com/watch?v=vPprOi4BB-4&list=RDvPprOi4BB-4&start_radio=1"
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    bt1.place(x=488820, y=460)
    bt3.place(x=43320, y=460)
    fto12.place(x=1322130, y=200, relheight=0.3, relwidth=0.3)
    fto10.place(x=32323223, y=25, relheight=0.8, relwidth=0.9)
    fto11.place(x=40, y=25, relheight=0.8, relwidth=0.8)
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Bay city"


def durdur12():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)
    mixer.music.stop()
    fto12.place(x=0, y=10, relheight=0.4, relwidth=0.3)
    fto10.place(x=0, y=350, relheight=0.5, relwidth=0.3)
    fto11.place(x=0, y=200, relheight=0.3, relwidth=0.3)
    yeniden1.place(x=543430, y=470)
    brw.place(x=223170, y=470)
    bt2.place(x=390, y=270)
    pause.place(x=533320, y=470)
    bt1.place(x=390, y=100)
    bt3.place(x=390, y=440)
    snm3.place(x=370, y=340)
    snm2.place(x=320, y=170)
    snm.place(x=350, y=10)
    btsyf.place(x=700, y=400)
    btsyf3.place(x=800, y=400)
    bt1.config(text="Şarkıyı Başlat", command=oynat12)


def oynat12():
    btsyf.place(x=72300, y=400)
    mixer.music.load("mp12.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris":
        mixer.music.load("mp12lyc.mp3")
    if s == "Speed up":
        mixer.music.load("mp12speup.mp3")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris/Speed up seçebilrsin?", fg="red")
        uyar.place(x=330, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp12.mp3")
        if s == "Lycris":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, Speed up seçebilrsin?", fg="red")
            mixer.music.load("mp12lyc.mp3")
        elif s == "Speed up":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
            mixer.music.load("mp12speup.mp3")
    btsyf3.place(x=833200, y=400)
    global youtube
    bt1.config(text="Şarkıyı Kapat", command=durdur12)
    snm.place(x=310, y=0)
    snm2.place(x=33350, y=10)
    snm3.place(x=33390, y=170)
    bt1.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    youtube = "https://www.youtube.com/watch?v=brmzZk87BoA"
    bt3.place(x=488820, y=460)
    bt2.place(x=43320, y=460)
    fto10.place(x=32323223, y=25, relheight=0.8, relwidth=0.9)
    fto11.place(x=42220, y=25, relheight=0.8, relwidth=0.8)
    fto12.place(x=40, y=25, relheight=0.8, relwidth=0.8)
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Suzume"


def srydur():
    uyrsil.place(x=32222230, y=430)
    uyar.place(x=33333330, y=430)

    mixer.music.stop()
    syf5()
    pause.place(x=53333320, y=470)
    brw.place(x=2733333330, y=470)
    yeniden1.place(x=5333340, y=470)


def mc():
    mixer.music.load("mpmc.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris" or s == "Speed up" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik kalitesini koruma amaçlı Speed/Lycris, seslendirme bulunmamaktadır :(", fg="red")
        uyar.place(x=270, y=430)
        mixer.music.load("mpmc.mp3")
        uyrsil.place(x=700, y=430)
    bt2.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    bt2.config(text="Şarkıyı Kapat", command=srydur)
    bt1.place(x=423330, y=460)
    bt3.place(x=43320, y=460)
    ftobc.place(x=-5555555, y=25, relheight=1, relwidth=1)
    snm2.place(x=350, y=0)
    snm3.place(x=33350, y=10)
    snm.place(x=33390, y=170)
    btsyf.place(x=72300, y=400)
    btsyf3.place(x=833200, y=400)
    ftompkr.place(x=4323332230, y=25, relheight=0.8, relwidth=0.8)
    ftomc.place(x=40, y=25, relheight=0.8, relwidth=0.8)
    global youtube
    youtube = "https://www.youtube.com/watch?v=dlNFhlbXWrU&t=30s"
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Mc"


def seryoz():
    mixer.music.load("MPKDR.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Speed up":
        mixer.music.load("mpsysp.mp3")
    if s == "Lycris" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, Lycris ve alt yazı yok :(, istersen Speed up seçebilrsin?", fg="red")
        uyar.place(x=290, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("MPKDR.mp3")
        if s == "Speed up":
            uyar.config(text="Bu Müzik`de Seslendirme, ve alt yazı yok :(, istersen Lycris seçebilrsin?", fg="red")
            mixer.music.load("mpsysp.mp3")
    ftobc.place(x=-5333333, y=25, relheight=1, relwidth=1)
    bt3.config(text="Şarkıyı Kapat", command=srydur)
    bt1.place(x=423330, y=460)
    bt3.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    bt2.place(x=43320, y=460)
    snm3.place(x=410, y=0)
    snm2.place(x=33350, y=10)
    snm.place(x=33390, y=170)
    btsyf.place(x=72300, y=400)
    btsyf3.place(x=833200, y=400)
    ftomc.place(x=4323332230, y=25, relheight=0.8, relwidth=0.8)
    ftompkr.place(x=40, y=25, relheight=0.8, relwidth=0.8)
    global youtube
    youtube = "https://www.youtube.com/watch?v=v9XHlDq8VGg&list=RDv9XHlDq8VGg&start_radio=1"
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Kardaşlar çökertme"


def oynt13():
    mixer.music.load("bcmp.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Speed up":
        mixer.music.load("bcspeup.mp3")
    if s == "Lycris":
        mixer.music.load("bclcy.mp3")
    if s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme":
        uyar.config(text="Bu Müzik`de Seslendirme, Lycris ve alt yazı yok :(, istersen Speed up seçebilrsin?", fg="red")
        uyar.place(x=310, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("bcmp.mp3")
        if s == "Speed up":
            mixer.music.load("bcspeup.mp3")
        elif s == "Lycris":
            mixer.music.load("bclcy.mp3")
    bt1.config(text="Şarkıyı Kapat", command=srydur)
    bt3.place(x=423330, y=460)
    bt1.place(x=420, y=460)
    bt2.place(x=43320, y=460)
    snm.place(x=430, y=0)
    snm3.place(x=33350, y=10)
    snm2.place(x=33390, y=170)
    bt1.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    btsyf.place(x=72300, y=400)
    btsyf3.place(x=833200, y=400)
    global youtube
    youtube = "https://www.youtube.com/watch?v=9ao4FEaDGhQ&list=RD9ao4FEaDGhQ&start_radio=1"
    ftomc.place(x=4323332230, y=25, relheight=0.8, relwidth=0.8)
    ftompkr.place(x=433330, y=25, relheight=0.8, relwidth=0.8)
    ftobc.place(x=-5, y=25, relheight=1, relwidth=1)
    mixer.music.play()
    global sarkiisim
    sarkiisim = "Bella ciao"


def oynt14():
    mixer.music.load("mp13.mp3")
    s = secili3.get()
    s1 = secili.get()
    s2 = secili2.get()
    if s == "Lycris" or s1 == "Türkce Alt yazı" or s1 == "Orginal Alt yazı" or s2 == "Türkce Seslendirme" or s == "Speed up":
        uyar.config(text="Bu Müzik`de Seslendirme,speed up, Lycris ve alt yazı yok :(", fg="red")
        uyar.place(x=290, y=430)
        uyrsil.place(x=700, y=430)
        mixer.music.load("mp13.mp3")
    bt3.config(text="Şarkıyı Kapat", command=durs)
    bt1.place(x=423330, y=460)
    bt3.place(x=440, y=470)
    brw.place(x=330, y=470)
    yeniden1.place(x=605, y=470)
    pause.place(x=520, y=470)
    bt2.place(x=43320, y=460)
    snm.place(x=340, y=0)
    snm2.place(x=33350, y=10)
    snm3.place(x=33390, y=170)
    btsyf.place(x=72300, y=400)
    btsyf3.place(x=833200, y=400)
    fto13.place(x=40, y=25, relheight=0.8, relwidth=0.8)
    global youtube
    youtube = "https://www.youtube.com/watch?v=x60xR0TEQ88"
    mixer.music.play()
    global sarkiisim
    sarkiisim = "kamihitoe"


tralt1 = "Işıkları açık bırakabiliriz, güneş bronzluğuna"
tralt2 = "(bo-bow-bo-bo)"
tralt3 = "Öğle yemeği yiyebiliriz, adamım (pa-pa-pa-pa-pa)"
tralt4 = "(müzik)"
tralt5 = "Sanırım senden hoşlanıyorum (seviyor musun?), Evet"
tralt6 = "Ama zarfları yalama şekliyle ilgili bir şey beni rahatsız ediyor, bu yüzden..."
tralt7 = "Tekrar bloktayım (pa-pa-pa-pa-pa)"
tralt8 = "O kadar zıpladım ki rol yapamam"
tralt9 = "İki kere!(pa-pa-pa-pa-pa), arkadaş kal"
tralt10 = "Savunamadığın sorun (oh)"
tralt11 = "Eller yukarı, iyi hisset (pa-pa-pa-pa-pa)"
tralt12 = "Bugün kimin kalbini kırabilirim?"
tralt13 = "İki kere! (pa-pa-pa-pa-pa), arkadaş kal!"
tralt14 = "Savunamadığın sorun"

sism = tk.Label(text="Tayyip - Allahıma Şükür Bugün de Başkanım")

alt1 = "We could leave the lights on, sun-tan"
alt2 = "(bo-bow-bo-bo)"
alt3 = "We could get lunch, aw, man (pa-pa-pa-pa-pa)"
alt4 = "(Music)"
alt5 = "I think that I like you (you do?), Yeah)"
alt6 = "But something bugs me 'bout the way you lick your envelopes, so-"
alt7 = "I'm out on the block again (pa-pa-pa-pa-pa)"
alt8 = "So hopped up that I can't pretend)"
alt9 = "Two time (pa-pa-pa-pa-pa), stay friends"
alt10 = "Problem that you can't defend (oh)"
alt11 = "Hands up, feel okay (pa-pa-pa-pa-pa)"
alt12 = "Whose heart could I break today?"
alt13 = "Two time (pa-pa-pa-pa-pa), stay friends"
alt14 = "Problem that you can't defend"

pr1 = tk.Button(text="Proje 1", command=syf1)
pause = tk.Button(text="Şarkıyı durdur", command=psu)
uyrsil = tk.Button(text="Uyarıyı sil", command=uyarsil)
bayr = tk.Button(text="Ses Ayarları", command=ayarlar)
bhs = tk.Button(text="Hesap oluştur", command=hspo)
bot = tk.Button(text="Oturum aç", command=otac)
bot.place(x=458, y=300)
bhs.place(x=450, y=250)
otgr = tk.Button(text="Oturum aç", command=otac1)
btsyf3 = tk.Button(text="Syafa 3", command=syf3)
btsyf = tk.Button(text="Sayfa 2", command=syf2)
bt1 = tk.Button(text="Şarkıyı Başlat", command=oynat1)
bt2 = tk.Button(text="Şarkıyı Başlat", command=oynat2)
bt3 = tk.Button(text="Şarkıyı Başlat", command=oynat3)
btvolume = tk.Button(text="Kaydet", command=volume1)
temizle = tk.Button(text="Uyarıyı sil", command=siluyari)
yeniden1 = tk.Button(text="Şarkıyı yeniden başlat", command=yeniden)
altyazi = tk.Button(text="Alt yazı")
brw = tk.Button(text="Youtubde`dan izle!", command=yolla)
btsp = tk.Button(text="Şarkıyı durdur")
bv = tk.Button(text="Video ile dinle!", command=pl)
# ---------------- #
ntp = 0
ntpo = 0
m1 = 80
f1 = 75
t1 = 100
k1 = 55
e1 = 100
b1 = 70
# -------------------#
l25 = tk.Label(sf2, text="A Okul", bg="#4C2A85", fg="#FFF", font=25)
l26 = tk.Label(sf2, text="Tam ad: Rya Gök ", bg="#4C2A85", fg="#FFF", font=25)

knt = ""
def dest():
    global l26
    l26 = tk.Label(sf2, text="Tam ad: Rya Gök ", bg="#4C2A85", fg="#FFF", font=25)
def pr2():
    print("Proje 2")
    l25 = tk.Label(sf2, text="A Okul", bg="#4C2A85", fg="#FFF", font=25)
    l25.pack(pady=60, padx=30)

    pr1.place(x=10213120, y=30)
    prr2.place(x=10213120, y=30)
    bst1.place(x=5503213213, y=50)
    ks1.place(x=100, y=50)


def pr2g():
    l23.place(x=23330, y=190)
    print("Proje 2")
    l25.config(text="A Okul", bg="#4C2A85", fg="#FFF", font=25)
    l26.destroy()
    dest()
    pr1.place(x=10213120, y=30)
    prr2.place(x=10213120, y=30)
    bst1.place(x=5503213213, y=50)
    ks1.place(x=100, y=50)
    ager.place(x=123232323200, y=250)


def alpc():
    pr2()


def alp():
    global knt
    knt = "alp"
    ks1.place(x=23432424, y=23432)
    not_data = {
        "Mat": m1,
        "Fizik": f1,
        "Tarih": t1,
        "Kimya": k1,
        "Edebiyat": e1,
        "Biyoloji": b1

    }
    ager.place(x=15, y=450)
    ntp = int(m1) + int(f1) + int(t1) + int(k1) + int(e1) + int(b1)
    ntpo = int(ntp) / 6
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

    fig2, ax2 = plt.subplots()
    ax2.barh(list(not_data.keys()), not_data.values())
    ax2.set_title("Kişi 1'in Not grafiği")
    ax2.set_xlabel("Kişinin Ortalaması " + str(ntpo))

    l26.pack()
    global l23
    l23 = tk.Label(sf2, text="Yaş: 15", bg="#4C2A85", fg="#FFF", font=25)
    l23.place(x=30, y=190)
    global cf
    cf = tk.Frame(pc)
    cf.pack()

    upper_frame = tk.Frame(cf)
    upper_frame.pack(fill="both", expand=True)
    global canvas2
    canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def adn():
    print("a okula dönüş")
    global knt
    pr2g()
    if knt == "alp":
        print("tk")

        for item in canvas2.get_tk_widget().find_all():
            canvas2.get_tk_widget().delete(item)
        cf.place(x=12332, y=132423)


ager = tk.Button(text="A okul'a dön", command=adn, bg="#4C2A85", fg="#FFF", font=25)
ks1 = tk.Button(text="Kişi 1", command=alp, bg="#4C2A85", fg="#FFF", font=25)
prr2 = tk.Button(text="proje 2", command=pr2)
# ----#
pc.mainloop()
