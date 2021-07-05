# Pre-installed libraries
import os
import time
import msvcrt as m
import re
import random
import sys
import shutil
import threading as thrd
import json as jl
from volume import Volume
import bitly
import subprocess
import pyHook
import pyttsx3
from mega import Mega

# Must be installed
import keyboard as kl
import mouse as ml
import pyperclip
import win32gui
import win32api
import win32ui
import win32con
import datetime
import randstr
import colorama
from pytube import YouTube
import youtubesearchpython as ys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from base64 import b64encode, b64decode
from google_trans_new import google_translator
import speech_recognition as sr
from fuzzywuzzy import fuzz
import webbrowser
import convertapi
import pygame

colorama.init(autoreset=True)
convertapi.api_secret = 'QRttNaCK0tXSOHeY'
speak_engine = pyttsx3.init()
os.system('cls')

def removeAllExceptNumbers(stringg):
    return re.sub("\D", "", stringg)
def removePrefix(stringg, value):
    if len(value) != int:
        if not stringg.startswith(value):
            raise KeyError(f"'{stringg}' doesn't start with '{value}'")
        value = len(value)
    full_string_without_prefix = ''
    i = 1
    for valuee in list(stringg):
        if i <= value:
            time.sleep(0)
        else:
            full_string_without_prefix += valuee
        i += 1
    return full_string_without_prefix
def removeSuffix(stringg, value):
    if len(value) != int:
        if not stringg.endswith(value):
            raise KeyError(f"'{stringg}' doesn't end with '{value}'")
        value = len(value)
    full_string_without_suffix = ''
    i = 0
    for valuee in list(stringg):
        if i != len(stringg) - value:
            full_string_without_suffix += valuee
        else:
            break
        i += 1
    return full_string_without_suffix
_typeReal = type
def _type(var):
    global typeReal
    return removeSuffix(removePrefix(str(_typeReal(var)), "<class '"), '>')
type = _type
def hex2rgb(hex):
    hex = removePrefix(hex, '#')
    lv = len(hex)
    return tuple(int(hex[i:i+lv//3], 16) for i in range(0, lv, lv//3))
def rgb2hex(rgb):
    return '%02x%02x%02x' % rgb
class blockInput():
    def OnKeyboardEvent(self, event):
        return False
    def OnMouseEvent(self, event):
        return False
    def unblock(self, kl=True, mouse=True):
        try:
            if self.t.is_alive():
                self.t.cancel()
        except: pass
        if kl:
            try: self.hm.UnhookKeyboard()
            except: pass
        if mouse:
            try: self.hm.UnhookMouse()
            except: pass
    def block(self, timeout = None, kl = True, mouse = True):
        self.t = thrd.Timer(timeout, self.unblock(kl = kl, mouse = mouse))
        self.t.start()
        if timeout == None:
            self.t.cancel()
        if mouse:
            self.hm.MouseAll = self.OnMouseEvent
            self.hm.HookMouse()
        if kl:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()
        win32gui.PumpWaitingMessages()
    def __init__(self):
        self.hm = pyHook.HookManager()
blockObj = blockInput()
class keyClass:
    global blockObj
    __block = blockObj
    # keys = ['Ctrl', 'Shift', 'Alt', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\\', '!', '%', '^', '&', '\\', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', '/', '?', '.', '>', ',', '<', 'Escape', 'Space', 'BackSpace', 'Tab', 'Linefeed', 'Clear', 'Return', 'Pause', 'Scroll_Lock', 'Sys_Req', 'Delete', 'Home', 'Left', 'Up', 'Right', 'Down', 'Page_Up', 'Page_Down', 'End', 'Select', 'Print', 'Execute', 'Insert', 'Num_Lock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']
    def press(self, key):
        kl.press(key)
    def release(self, key):
        kl.release(key)
    def click(self, key, delay=0):
        if delay/1000 == 0:
            kl.send(key)
        else:
            kl.press(key)
            time.sleep(delay/1000)
            kl.release(key)
    def write(self, keys, delay=100):
        kl.write(keys, delay=delay/1000)
    def isPressed(self, key):
        return kl.is_pressed(key)
    def wait(self, key=None):
        if key == None:
            while 1:
                for value in self.keys:
                    if self.isPressed(value):
                        return value
        elif type(key) == 'list':
            while 1:
                for value in key:
                    if self.isPressed(value):
                        return value
        else:
            while 1:
                if self.isPressed(key):
                    return key
    def block(self, timeout=None):
        self.__block.block(timeout=timeout, kl=True, mouse=False)
    def unblock(self):
        self.__block.unblock(kl=True, mouse=False)
keys = keyClass()
keyboard = keyClass()
del keyClass
class mouseClass:
    global blockObj
    __block = blockObj
    def scroll(self, x):
        ml.wheel(x)
    def click(self, side):
        ml.click(button = side)
    @property
    def position(self):
        class positionMouseClass:
            x = ml.get_position()[0]
            y = ml.get_position()[1]
            def __repr__(self):
                return ml.get_position()
        return positionMouseClass()
    def move(self, x, y, absolute=True, delay=100):
        ml.move(x, y, absolute=absolute, duration=delay/1000)
    def isPressed(self, side):
        return ml.is_pressed(button = side)
    def wait(self, side=None):
        if side == None:
            while 1:
                if self.isPressed('left'):
                    return 'left'
                elif self.isPressed('right'):
                    return 'right'
                elif self.isPressed('middle'):
                    return 'middle'
        elif type(side) == 'list':
            while 1:
                for value in side:
                    if self.isPressed(value):
                        return value
        else:
            while 1:
                if self.isPressed(side):
                    return side
    def block(self, timeout=None):
        self.__block.block(timeout=timeout, kl=False, mouse=True)
    def unblock(self):
        self.__block.unblock(kl=False, mouse=True)
mouse = mouseClass()
del mouseClass
del blockObj
class colorsClass:
    class textClass:
        black = colorama.Fore.BLACK
        red = colorama.Fore.RED
        green = colorama.Fore.GREEN
        yellow = colorama.Fore.YELLOW
        blue = colorama.Fore.BLUE
        magenta = colorama.Fore.MAGENTA
        cyan = colorama.Fore.CYAN
        white = colorama.Fore.WHITE
    text = textClass()
    del textClass
    class bgClass:
        black = colorama.Back.BLACK
        red = colorama.Back.RED
        green = colorama.Back.GREEN
        yellow = colorama.Back.YELLOW
        blue = colorama.Back.BLUE
        magenta = colorama.Back.MAGENTA
        cyan = colorama.Back.CYAN
        white = colorama.Back.WHITE
    bg = bgClass()
    del bgClass
    class styleClass:
        dim = colorama.Style.DIM
        normal = colorama.Style.NORMAL
        bright = colorama.Style.BRIGHT
    style = styleClass()
    del styleClass
color = colorsClass()
del colorsClass

class consoleClass:
    __printed = ''
    @property
    def printed(self):
        return self.__printed.split('\n')
    def input(self, *string, anim=False, center=False, animDelay=10, color=color.text.white, newLine=True):
        string0 = ''
        for value in string:
            string0 += str(value)
        string = string0
        del string0
        beforePrint = self.__printed
        if not center:
            if not anim:
                if newLine:
                    self.__printed += '\n' + color + str(string)
                    return input(color + str(string))
                else:
                    self.__printed += color + str(string)
                    os.system('cls')
                    return input(self.__printed)
            else:
                string = str(string)
                no_full_str = ''
                for value in list(string):
                    no_full_str += value
                    time.sleep(animDelay / 1000)
                    os.system('cls')
                    print(self.__printed)
                    print(color + no_full_str)
                os.system('cls')
                print(self.__printed)
                self.__printed += '\n' + color + str(string)
                return input(color + no_full_str)
        else:
            if not anim:
                line = [str(string)]
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, line))) // 2
                self.__printed += '\n' + color + str(line[0].center(width))
                return input(color + str(line[0].center(width)))
            else:
                lines = str(string)
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, lines))) // 2
                no_full_str = ''
                for value in list(string):
                    os.system('cls')
                    print(self.__printed)
                    time.sleep(animDelay / 1000)
                    print(color + no_full_str.center(width))
                    no_full_str += value
                self.__printed += '\n' + str(color + no_full_str.center(width))
                return input(color + no_full_str.center(width))
    def print(self, *string, anim=False, center=False, animDelay=10, color=color.text.white, newLine=True, msBeforeDelete=None):
        string0 = ''
        for value in string:
            string0 += str(value)
        string = string0
        del string0
        beforePrint = self.__printed
        if not center:
            if not anim:
                if newLine:
                    print(color + str(string))
                    self.__printed += '\n' + color + str(string)
                else:
                    self.__printed += color + str(string)
                    os.system('cls')
                    print(self.__printed)
            else:
                string = str(string)
                no_full_str = ''
                for value in list(string):
                    no_full_str += value
                    time.sleep(animDelay / 1000)
                    os.system('cls')
                    print(self.__printed)
                    print(color + no_full_str)
                self.__printed += '\n' + color + str(string)
        else:
            if not anim:
                if type(string) == 'list':
                    lines = str(string)
                else:
                    lines = [string]
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, lines))) // 2
                for line in lines:
                    print(color + line.center(width))
                    self.__printed += '\n' + color + str(line.center(width))
            else:
                if type(string) == 'list':
                    lines = str(string)
                else:
                    lines = [string]
                width = shutil.get_terminal_size().columns
                position = (width - max(map(len, lines))) // 2
                for line in lines:
                    no_full_str = ''
                    for value in list(string):
                        os.system('cls')
                        print(self.__printed)
                        time.sleep(animDelay / 1000)
                        print(color + no_full_str.center(width))
                        no_full_str += value
                    self.__printed += '\n' + str(color + no_full_str.center(width))
        if msBeforeDelete != None:
            def deleteDef():
                nonlocal beforePrint, msBeforeDelete
                time.sleep(msBeforeDelete/1000)
                os.system('cls')
                self.__printed = beforePrint
                return
            deleteThread = thrd.Thread(target=deleteDef)
            deleteThread.start()
    def clear(self, lines=0):
        if lines == 0:
            os.system('cls')
            self.__printed = ''
        else:
            splitLines = self.__printed.split('\n')
            fixedLines = ''
            i = 0
            for value in splitLines:
                if i == len(splitLines) - lines:
                    break
                else:
                    fixedLines += value
                    if i != len(splitLines):
                        fixedLines += '\n'
                i += 1
            os.system('cls')
            print(fixedLines)
            self.__printed = fixedLines
    def run(self, cmd, show=False):
        if show:
            subprocess.check_call(cmd, shell=True)
        returnedText = subprocess.check_output(cmd, shell=True).decode()
        try:
            returnedText = removeSuffix(returnedText, '\r\n')
        except:
            pass
        return returnedText
console = consoleClass()
cnsl = consoleClass()
cmd = consoleClass()
del consoleClass
def wait(ms):
    time.sleep(ms/1000)
def rand(x=0, y=0):
    if type(x) != list:
        return random.randint(x, y)
    else:
        return random.randint(0, len(x)-1)
def randStr(countKeysfff):
    return randstr.randstr(countKeysfff)
def copied():
    return pyperclip.paste()
class base64Class:
    def encode(self, string):
        string = str(string)
        return b64encode(string.encode('ascii')).decode('utf8')
    def decode(self, string):
        string = str(string)
        return b64decode(string).decode('utf8')
base64 = base64Class()
del base64Class
class thread:
    def __init__(self, func, name=None, daemon=None, group=None):
        self.function = func
        self.name = name
        self.daemon = daemon
        self.group = group
        self.isStarted = False
        self.thread = thrd.Thread(target=self.function,
                                        name=self.name,
                                        daemon=self.daemon,
                                        group=self.group)
    def start(self):
        self.thread.start()
        self.isStarted = True
    def stop(self):
        self.thread.join()
        self.isStarted = False
threading = thread
class timer:
    def __init__(self, func, interval):
        self.function = func
        self.interval = interval
        self.thread = thrd.Timer(self.interval, self.function)
    def start(self):
        self.thread.start()
    def stop(self):
        self.thread.cancel()
    @property
    def isStarted(self):
        return self.thread.isAlive()
class fileClass:
    def read(self, file):
        file_ = open(file, 'rb')
        read_ = file_.read()
        file_.close()
        return read_.encode()
    def write(self, file, strrrr):
        file_ = open(file, 'w')
        file_.write(strrrr)
        file_.close()
    def create(self, file):
        open(file, 'w').close()
    def remove(self, file):
        os.remove(file)
    def exists(self, file):
        return os.path.isfile(file)
    def local(self):
        try:
            return sys._MEIPASS
        except Exception:
            return os.path.abspath(".")
    def files(self, src):
        return os.listdir(src)
    def run(self, args):
        subprocess.run(args)
    def convert(self, file, to_format):
        format_ = file.split('.')[-1]
        outfile = removeSuffix(file, format_)
        convertapi.convert(format_, { 'File': file }).file.save(f'{outfile}.{to_format}')
    def createDir(self, dir):
        os.mkdir(dir)
    def removeDir(self, dir):
        shutil.rmtree(dir)
    def localFile(self, path_string):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, path_string)
file = fileClass()
files = fileClass()
del fileClass
def copy(strr):
    pyperclip.copy(strr)
def off():
    raise SystemExit
def screenshot(outfile):
    height = win32api.GetSystemMetrics(1)
    width = win32api.GetSystemMetrics(0)
    name = randStr(rand(1564, 7892))
    format_ = file.split('.')[-1]
    outfile_ = removeSuffix(outfile, format_)
    hwnd = win32gui.FindWindow(None, name)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0),(width, height), dcObj, (0, 0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, f'{outfile_}.bmp')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    file.convert(f'{outfile_}.bmp', format_)
    file.remove(f'{outfile_}.bmp')
class date:
    day = int(datetime.datetime.today().strftime('%d'))
    month = int(datetime.datetime.today().strftime('%m'))
    year = int(datetime.datetime.today().strftime('%y'))
    hour = int(datetime.datetime.today().strftime('%H'))
    minute = int(datetime.datetime.today().strftime('%M'))
    second = int(datetime.datetime.today().strftime('%S'))
    def __init__(self, str='%d.%m.%y %H:%M:%S'):
        self.__str = str
    def __repr__(self):
        return datetime.datetime.today().strftime(self.__str)
class sound:
    def __init__(self, pathsound):
        self.path = pathsound
        self.sound = pygame.mixer.Sound(self.path)
    def play(self):
        self.sound.play()
    def stop(self):
        self.sound.stop()
    @property
    def volume(self):
        return self.sound.get_volume()
    def setVolume(self, x):
        self.sound.set_volume(x)
    @property
    def length(self):
        return self.sound.get_length()
class voiceClass:
    def speak(self, text):
        speak_engine.say(text)
        speak_engine.runAndWait()
        speak_engine.stop()
    def listen(self, language="ru-RU"):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        while 1:
            try:
                with m as source:
                    audio = r.listen(source)
                return r.recognize_google(audio, language=language).lower()
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
    def save(self, text, filename, say=False):
        if say:
            speak_engine.save_to_file(text, filename)
            speak_engine.say(text)
            speak_engine.runAndWait()
            speak_engine.stop()
        else:
            speak_engine.save_to_file(text, filename)
            speak_engine.runAndWait()
voice = voiceClass()
del voiceClass
def short(linkkkk):
    c = bitly.Connection(access_token='ae0f0e3b0c2dc29bd0667787ccfc7cb39b25ad62')
    return c.shorten(linkkkk)[u'url']
class youtubeClass:
    class get:
        link = None
        def __init__(self, link):
            part = ys.Video.get(link)
            yt = YouTube(link)
            try:
                self.type = part['type']
            except:
                self.type = None
            self.link = part['link']
            self.shortLink = 'https://youtu.be/'+part['id']
            self.id = part['id']
            self.title = part['title']
            self.description = part['description']
            authorName = part['channel']['name']
            authorId = part['channel']['id']
            authorLink = part['channel']['link']
            try:
                authorAvatar = part['channel']['thumbnails'][-1]['url']
            except:
                authorAvatar = None
            self.author = self.__authorClass(authorName, authorId, authorLink, authorAvatar)
            self.preview = part['thumbnails'][-1]['url']
            try:
                self.views = yt.views
                self.duration = yt.length
                self.createdAt = yt.publish_date
                self.rating = yt.rating
            except:
                pass

        class __authorClass:
            def __init__(self, name, id, link, avatar):
                self.name = name
                self.id = id
                self.link = link
                self.avatar = avatar

        def getLastAuthorVideo(self):
            opts = Options()
            opts.headless = True
            opts.add_argument("--log-level=3")
            browser = Firefox(options=opts, executable_path='geckodriver.exe')
            browser.get(self.author.link)
            link = browser.find_elements_by_xpath("//a[@id='thumbnail']")[0].get_attribute('href')
            browser.close()
            return self.get(link)

        def download(self, on_progress_callback=lambda x: None,
                     on_complete_callback=None, proxies=None,
                     fps=None, res=None, resolution=None,
                     mime_type=None, type=None, subtype=None,
                     file_extension=None, abr=None, bitrate=None,
                     video_codec=None, audio_codec=None, only_audio=None,
                     only_video=None, progressive=None, adaptive=None,
                     is_dash=None, custom_filter_functions=None,
                     output_path=None, filename=None, filename_prefix=None,
                     skip_existing=True, timeout=None, max_retries=0):
            def on_progress_callback0(stream, _, bytes_remaining):
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                liveprogress = int(bytes_downloaded / total_size * 100)
                on_progress_callback(liveprogress)
            yt = YouTube(self.link, on_progress_callback=on_progress_callback0,
                         on_complete_callback=on_complete_callback, proxies=proxies)
            file = yt.streams.filter(fps=fps, res=res, resolution=resolution,
                     mime_type=mime_type, type=type, subtype=subtype,
                     file_extension=file_extension, abr=abr, bitrate=bitrate,
                     video_codec=video_codec, audio_codec=audio_codec, only_audio=only_audio,
                     only_video=only_video, progressive=progressive, adaptive=adaptive,
                     is_dash=is_dash, custom_filter_functions=custom_filter_functions).first()
            return file.download(output_path=output_path, filename=filename, filename_prefix=filename_prefix,
                                 skip_existing=skip_existing, timeout=timeout, max_retries=max_retries)

    def getLastAuthorVideo(self, authorLink):
        opts = Options()
        opts.headless = True
        opts.add_argument("--log-level=3")
        browser = Firefox(options=opts, executable_path='geckodriver.exe')
        browser.get(authorLink)
        link = browser.find_elements_by_xpath("//a[@id='thumbnail']")[0].get_attribute('href')
        browser.close()
        return self.get(link)

    def search(self, string, limit=15):
        part = ys.VideosSearch(string, limit=limit).result()['result']
        all = []
        for p in part:
            all.append(self.get(p['link']))
        return all

youtube = youtubeClass()
yt = youtubeClass()
del youtubeClass

def exit(way='default'):
    if way == 'default':
        exit()
    elif way == 'raise':
        raise SystemExit
    else:
        print("TypeError: exit(), argument: 'way' must be 'default' or 'raise'")
        raise SystemExit

class json:
    def __init__(self, file):
        self.file = file
    def get(self, what=None):
        with open(self.file, encoding='utf-8') as file:
            data = jl.load(file)
        return data
    def set(self, to):
        with open(self.file, 'w', encoding='utf-8') as file:
            jl.dump(to, file, indent=4, sort_keys=True, ensure_ascii=False)

def title(name):
    os.system('title '+name)

def translate(text, from_, to_):
    translator = google_translator()
    return translator.translate(text, lang_src=from_, lang_tgt=to_)

class mega:
    def __init__(self, email=None, password=None):
        mega = Mega()
        self.__client = mega.login(email, password)
    @property
    def usedSize(self):
        return self.__client.get_storage_space()['used']
    @property
    def totalSize(self):
        return self.__client.get_storage_space()['total']
    @property
    def user(self):
        return self.__client.get_user()
    @property
    def quota(self):
        return self.__client.get_quota()
    @property
    def files(self):
        return self.__client.get_files()
    def rename(self, file):
        self.__client.rename(self.__client.find(file))
    def upload(self, file):
        self.__client.upload(file)
    def download(self, file, dest_path=None, dest_filename=None):
        temp = self.__client.download(self.__client.find(file), dest_path, dest_filename)
        if dest_filename == None:
            dest_filename = temp[1]
        if dest_path == None:
            dest_path = files.local()
        shutil.move(temp[0], os.path.join(dest_path, dest_filename))
        return os.path.join(dest_path, dest_filename)
    def getLink(self, file):
        return self.__client.get_link(self.__client.find(file))
    def delete(self, file):
        self.__client.delete_url(self.getLink(file))
    def remove(self, file):
        self.delete(file)
        self.clearTrash()
    def move(self, file, to):
        self.__client.move(self.__client.find(file), self.__client.find(file))
    def createDir(self, file):
        self.__client.create_folder(file)
    def downloadLink(self, link, dest_path=None, dest_filename=None):
        temp = self.__client.download_url(link, dest_path, dest_filename)
        if dest_filename == None:
            dest_filename = temp[1]
        if dest_path == None:
            dest_path = files.local()
        shutil.move(temp[0], os.path.join(dest_path, dest_filename))
        return os.path.join(dest_path, dest_filename)
    def clearTrash(self):
        self.__client.empty_trash()
    def read(self, file):
        self.download(file, files.local())
        name = os.path.basename(os.path.normpath(file))
        with open(files.localFile(name), 'r') as f:
            readen = f.read()
            f.close()
        files.remove(files.localFile(name))
        return readen
    def write(self, file, text):
        self.download(file, files.local())
        name = os.path.basename(os.path.normpath(file))
        with open(files.localFile(name), 'w') as f:
            f.write(text)
            f.close()
        self.remove(file)
        self.upload(files.localFile(name))
        files.remove(files.localFile(name))
