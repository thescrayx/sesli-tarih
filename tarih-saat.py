# MODÜLLER


###

from gtts import gTTS
from datetime import datetime
from pynput import keyboard
from pygame import mixer
from mutagen.mp3 import MP3
from colorama import init
from termcolor import colored
init()

###

import os
import time
import pygame
import locale

###

cls = lambda: os.system('cls')
cls()

print("Başlatıldı saati çağırmak için '-'(tire) tuşuna bas.")

if not os.path.isdir("Geçici_Dosya"):
   os.makedirs("Geçici_Dosya")

def get_date_in(loc, df):
    formats = ["%d-%b-%Y", "%d %b %Y"]

    for f in formats:
        if f == df:
            locale.setlocale(locale.LC_ALL, loc)
            loc_date = time.strftime(f)
            return loc_date

# TUŞA BASINCA TETİKLENEN SCRİPT
def on_activate():
    cls = lambda: os.system('cls')
    cls()
    print(colored("Saat çağırıldı dosya çalınıyor...", "green")) 
    
    try:
        now = datetime.now()
        saat = now.strftime("%H:%M")
        tarih = get_date_in('tr', "%d-%b-%Y")

        myobj = gTTS(text=tarih + " " + saat, lang='tr', slow=False)
        myobj.save("D:\pitonbitis\saat\Geçici_Dosya\sjwelcome.mp3")
    except OSError as err:
        print(colored("Bir Hata Oluştu | Detaylar:", 'red', 'on_white'))
        return print(err)
        try:
            os.remove("D:\pitonbitis\saat\Geçici_Dosya\sjwelcome.mp3")
        except OSError as err:
            print(colored('Dosya silinirken bir hata oluştu.(Uygulamanın konumundaki -Geçici_Dosya- adlı klasörü sil.)', 'red'))

    mixer.init()
    mixer.music.load("D:\pitonbitis\saat\Geçici_Dosya\sjwelcome.mp3")
    mp3 = MP3("D:\pitonbitis\saat\Geçici_Dosya\sjwelcome.mp3")
    mixer.music.play()

    time.sleep(mp3.info.length)
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

    mixer.quit()
    cls()
    print(colored("Dosya siliniyor...", "green"))  
    os.remove("D:\pitonbitis\saat\Geçici_Dosya\sjwelcome.mp3")
    time.sleep(3)
    cls()    
    print(colored("Tekrar çağırılmaya hazır...", "green")) 
    
def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('-'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
