
import pyautogui as pygui
import keyboard as kb
import pygame as pg
import datetime
import time
import asyncio

class console:
    pg.init()
    # Setting some default colors
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    color_maize = (231, 210, 190)
    color_lblue = (157, 189, 241)
    color_dorange = (211, 143, 93)
    color_dkorange = (180, 150, 60)
    colors = [color_black, color_maize, color_lblue, color_dkorange]
    font = pg.font.SysFont("SimHei", 48)
    # font_l = pg.font.Font('D:\\tech\python\\game\\shaweima\\font\\ZhouZiSongTi7000Zi-2.otf', 40)
    titles = ['橙汁', '可乐', '削土豆', '烤架', '薯条机', '双刃刀', '配料', '石榴糖浆', '克比', '包装', '培训', '法薯', '面饼', '装杯']
    tools_lv = {'橙汁': 2, '可乐':3, '削土豆':3, '烤架':4, '薯条机':3,
                '双刃刀':3, '配料':3, '石榴糖浆':3, '克比':2, '包装':3,
                '培训':2, '法薯': 4, '面饼':2, '装杯': 3}

    def __init__(self):
        self.win = pg.display.set_mode((800, 800))

        self.win.fill(self.color_white)
        self.buttons = {}
        self.button_info = {}
        self.button_loc = {}

        l = len(self.titles)
        for i, j in enumerate(self.titles):
            words = self.font.render(j, True, self.color_black)
            loc = words.get_rect()
            loc.x += i * 200 % 800
            loc.y += i * 200 // 800 * 150
            self.win.blit(words, loc)

            self.buttons[j] = words
            self.button_info[j] = False
            self.button_loc[j] = loc

        pg.display.flip()

class Actions:
    win = pygui.getWindowsWithTitle('Shawarma Legend')

    region = pygui.getWindowsWithTitle('Shawarma Legend')[0]
    region.resizeTo(1920, 840)
    print(region)

    pygui.PAUSE = 0.05

    def __init__(self, path = 'D:\\tech\python\\game\\shaweima\\img\\'):
        self.mouse_loc = []
        self.path = path
        self.start = True
        self.sir = self.path + 'sir.png'
        self.cucumber = self.path + 'cucumber.png'
        self.sauce1 = self.path + 'sauce1.png'
        self.add_cucumber = self.path + 'add cucumber.png'
        self.add_sauce1 = self.path + 'add sauce1.png'
        self.end_sir = self.path + 'end sir.png'
        self.kobe = self.path + 'kobe.png'
        self.thief = self.path + 'thief.png'
        self.orange_juice = self.path + 'orangejuice.png'
        self.finda = self.path + 'finda.png'
        self.cola = self.path + 'cola.png'
        self.french_fries = self.path + 'frenchfries.png'
        self.cooked_fries = self.path + 'cooked fries.png'
        self.items = dict()
        self.items['sir'] = self.sir
        self.items['cucumber'] = self.cucumber
        self.items['sauce1.png'] = self.sauce1
        self.items['add cucumber'] = self.add_cucumber
        self.items['add sauce1'] = self.add_sauce1
        self.items['end sir'] = self.end_sir
        self.items['kobe'] = self.kobe
        self.items['thief'] = self.thief
        self.items['orange_juice'] = self.orange_juice
        self.items['finda'] = self.finda
        self.items['cola'] = self.cola
        self.items['french fries'] = self.french_fries
        self.num_kobes = 0
        self.num_orange_juice = 0
        self.num_french_fries = 0
        self.tasks = []
        self.shawarma_on_oven = 0
        self.c = console()
        asyncio.run(self.run())

    async def run(self):

        tasks = []
        while True:
            if kb.is_pressed('1'):
                print('Do shawarma')
                self.do_shawarma(1)
            elif kb.is_pressed('2'):
                print('Do shawarma')
                self.do_shawarma(2)
            elif kb.is_pressed('3'):
                print('Do shawarma')
                self.do_shawarma(3)
            elif kb.is_pressed('4'):
                print('Do shawarma')
                self.do_shawarma(4)
            elif kb.is_pressed('5'):
                print('Do shawarma')
                self.do_shawarma(5)
            elif kb.is_pressed('6'):
                print('Do shawarma')
                self.do_shawarma(6)
            elif kb.is_pressed('7'):
                print('Do shawarma')
                self.do_shawarma(7)
            elif kb.is_pressed('8'):
                print('Do shawarma')
                self.do_shawarma(8)
            elif kb.is_pressed('9'):
                print('Do shawarma')
                self.do_shawarma(9)
            elif kb.is_pressed('0'):
                print('Do shawarma')
                self.do_shawarma(0)


            elif kb.is_pressed('w'):
                print('Do shawarma')
                self.do_shawarma(-1)

            elif kb.is_pressed('s'):
                print('supply! sir')
                self.supply_sir()
            elif kb.is_pressed('c'):
                print('Chopping!!!')
                self.chop_meat()
            elif kb.is_pressed('f'):
                print('More chips!')
                self.cut_potatoes()

            elif kb.is_pressed('r'):
                print('restore!')
                self.num_french_fries = 0
                self.num_kobes = 0
                self.num_orange_juice = 0

            elif kb.is_pressed('o') and self.c.button_info['橙汁']:
                self.give_orange()

            elif kb.is_pressed('k') and self.c.button_info['克比']:
                self.give_kobe()

            elif kb.is_pressed(']') and self.c.button_info['可乐']:
                self.supply_cola()

            # elif kb.is_pressed('t') and self.c.button_info['小偷']:
            #     self.attack_thief()

            elif kb.is_pressed('g') and self.c.button_info['可乐']:
                self.give_soda()

            elif kb.is_pressed('m'):
                print('CHACHIN')
                self.cash_in()

            elif kb.is_pressed('/') and self.c.button_info['法薯']:
                print('French Fries!')
                self.give_french_fries()

            elif kb.is_pressed('esc'):
                break


            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    mouse = pg.mouse.get_pos()
                    for i in self.c.buttons:
                        loc = self.c.button_loc[i]

                        if loc.x <= mouse[0] <= loc.x + 45 *len(i) and loc.y <= mouse[1] <= loc.y + 40:
                            self.c.button_info[i] = (self.c.button_info[i] + 1) % self.c.tools_lv[i]
                            words = self.c.font.render(i, True, self.c.colors[self.c.button_info[i]])
                            self.c.win.blit(words, loc)
                            pg.display.flip()
                    # print(self.c.button_info)

            self.finish_task()




    def finish_task(self):
        for i, (t, interval, act, arg) in enumerate(self.tasks):
            if (datetime.datetime.now() - t).seconds >= interval:
                if arg != None:
                    act(arg)
                else:
                    act()
                self.tasks.pop(i)

    def supply_sir(self):
        print(self.region)
        # location = pygui.locateCenterOnScreen(self.items['sir'], grayscale=True, confidence=0.85)
        x = self.region.left + 0.15 * self.region.width
        y = self.region.top + 0.5 * self.region.height

        pygui.moveTo(x, y)
        pygui.mouseDown()
        pygui.mouseUp()

        if self.c.button_info['培训']:
            self.num_kobes = 8
            self.num_orange_juice = 4
            return

        time.sleep(0.7)

        pygui.moveTo(x + self.region.width / 15, y + self.region.height/80)

        for i in range(10):
            pygui.mouseDown()
            pygui.mouseUp()

        pygui.moveTo(x + self.region.width / 15, y - self.region.height/15)

        for i in range(10):
            pygui.mouseDown()
            pygui.mouseUp()

        pygui.moveTo(x, y)
        pygui.mouseDown()
        pygui.mouseUp()

    def suppply_french_fries(self):

        x = self.region.left + 0.8 * self.region.width
        y = self.region.top + 0.9 * self.region.height

        pygui.moveTo(x, y)
        for i in range(3):
            pygui.mouseDown()
            pygui.mouseUp()
        time.sleep(1)
        y -= 0.1 * self.region.height
        pygui.moveTo(x, y)
        for i in range(3):
            pygui.moveTo(x + i * 0.03 * self.region.width, y)
            pygui.mouseDown()
            if self.c.button_info['法薯'] == 1:
                pygui.moveTo(self.region.left + 0.5 * self.region.width, self.region.top + 0.65 * self.region.height, duration=0.2)
            pygui.mouseUp()
        self.num_french_fries = 3

    def give_french_fries(self):
        fries_item = self.items['french fries']

        try:
            if self.c.button_info['法薯'] < 3:

                if self.num_french_fries <= 0:
                    self.suppply_french_fries()
            else:
                self.num_french_fries = 3


            while self.num_french_fries > 0:

                region = pygui.locateCenterOnScreen(fries_item, grayscale=False, confidence=0.85)
                print('find cutomer', region)

                area = (int(self.region.left + 0.7 * self.region.width), int(self.region.top + 0.7 * self.region.height), 900, 450)
                print(area)
                find_fries = pygui.locateCenterOnScreen(self.cooked_fries,region= area, grayscale=False, confidence=0.95)
                print('find fries', find_fries)
                pygui.moveTo(find_fries.x, find_fries.y)
                pygui.mouseDown()
                pygui.moveTo(region.x, region.y, duration=0.15)
                pygui.mouseUp()
                pygui.moveTo(region.x, region.y - 0.3 * self.region.height)
                self.num_french_fries -= 1
        except:
            pass


    def give_kobe(self):
        item = self.items['kobe']

        try:
            if self.num_kobes <= 0:
                self.supply_kobe()
            while self.num_kobes > 0:
                region = pygui.locateCenterOnScreen(item, grayscale=False, confidence=0.96)

                x = self.region.left + 0.6 * self.region.width
                y = self.region.top + 0.6 * self.region.height
                pygui.moveTo(x, y)
                pygui.mouseDown()
                pygui.moveTo(region.x, region.y, duration=0.15)
                pygui.mouseUp()
                self.num_kobes -= 1
                pygui.moveTo(region.x, region.y - 0.3 * self.region.height)
        except:
            return

    def give_soda(self):
        cola = self.items['cola']
        finda = self.items['finda']
        x_cola = self.region.left + 0.67 * self.region.width
        y_cola = self.region.top + 0.6 * self.region.height
        try:
            region = pygui.locateCenterOnScreen(finda, grayscale=False, confidence=0.95)
            pygui.moveTo(x_cola, y_cola)
            pygui.mouseDown()
            pygui.moveTo(region.x, region.y,duration=0.15)
            pygui.mouseUp()
            pygui.moveTo(region.x, region.y - 0.3 * self.region.height)

        except:
            pass

        try:
            region = pygui.locateCenterOnScreen(cola, grayscale=False, confidence=0.95)
            pygui.moveTo(x_cola + 0.075 * self.region.width, y_cola)
            pygui.mouseDown()
            pygui.moveTo(region.x, region.y, duration=0.15)
            pygui.mouseUp()
            pygui.moveTo(region.x, region.y - 0.3 * self.region.height)

        except:
            pass

        self.supply_cola()
        return

    def give_orange(self):
        item = self.items['orange_juice']

        try:
            if self.num_orange_juice <= 0:
                self.supply_orange()
                time.sleep(0.3)
            while self.num_orange_juice > 0:
                region = pygui.locateCenterOnScreen(item, grayscale=False, confidence=0.83)

                x = self.region.left + 0.25 * self.region.width
                y = self.region.top + 0.8 * self.region.height

                pygui.moveTo(x, y)
                pygui.mouseDown()
                pygui.moveTo(region.x, region.y, duration=0.15)
                pygui.mouseUp()
                self.num_orange_juice -= 1
                pygui.moveTo(region.x, region.y - 0.3 * self.region.height)
        except:
            return



    # def attack_thief(self):
    #     item = self.items['thief']
    #
    #     try:
    #         while True:
    #             region = pygui.locateCenterOnScreen(item, grayscale=False, confidence=0.96)
    #             pygui.moveTo(region.x + 0.1 * self.region.width, region.y)
    #             for i in range(20):
    #                 pygui.mouseDown()
    #                 pygui.mouseUp()
    #     except:
    #         return

    def supply_kobe(self):
        x = self.region.left + 0.15 * self.region.width
        y = self.region.top + 0.5 * self.region.height

        pygui.moveTo(x, y)
        pygui.mouseDown()
        pygui.mouseUp()

        if not self.c.button_info['培训']:

            time.sleep(0.85)

            pygui.moveTo(x + self.region.width / 15, y + self.region.height / 4)
            for i in range(8):
                pygui.mouseDown()
                pygui.mouseUp()
            pygui.moveTo(x, y)
            pygui.mouseDown()
            pygui.mouseUp()
        self.num_kobes = 8

    def supply_orange(self):
        x = self.region.left + 0.15 * self.region.width
        y = self.region.top + 0.5 * self.region.height

        pygui.moveTo(x, y)
        pygui.mouseDown()
        pygui.mouseUp()
        if not self.c.button_info['培训']:

            time.sleep(0.7)

            pygui.moveTo(x + self.region.width / 15, y + self.region.height / 7)
            for i in range(4):
                pygui.mouseDown()
                pygui.mouseUp()
            pygui.moveTo(x, y)
            pygui.mouseDown()
            pygui.mouseUp()
        self.num_orange_juice = 4


    def supply_cola(self):
        if self.c.button_info['可乐'] > 0:
            if self.c.button_info['装杯'] < 1:
                x = self.region.left + 0.85 * self.region.width
                y = self.region.top + 0.9 * self.region.height

                pygui.moveTo(x, y)
                pygui.mouseDown()
                pygui.mouseUp()
                pygui.mouseDown()
                pygui.mouseUp()
            if self.c.button_info['装杯'] < 2:
                x_cola = self.region.left + 0.67 * self.region.width
                y_cola = self.region.top + 0.52 * self.region.height

                pygui.moveTo(x_cola, y_cola)
                pygui.mouseDown()
                pygui.mouseUp()
                pygui.moveTo(x_cola + 0.075 * self.region.width, y_cola)
                pygui.mouseDown()
                pygui.mouseUp()

    def cut_potatoes(self):
        if self.c.button_info['削土豆'] == 2:
            return
        if self.c.button_info['削土豆'] == 0:
            cutTime = 6
        elif self.c.button_info['削土豆'] == 1:
            cutTime = 3

        if self.c.button_info['薯条机'] == 0:
            friedTime = 15
        elif self.c.button_info['薯条机'] == 1:
            friedTime = 10

        x = self.region.left + 0.9 * self.region.width
        y = self.region.top + 0.6 * self.region.height

        pygui.moveTo(x, y)
        pygui.mouseDown()
        time.sleep(cutTime)
        pygui.mouseUp()

        self.tasks.append((datetime.datetime.now(), friedTime, self.fried_potatoes, None))

    def fried_potatoes(self):

        x = self.region.left + 0.9 * self.region.width
        y = self.region.top + 0.6 * self.region.height

        pygui.moveTo(x - self.region.width * 0.1, y - 0.1 * self.region.height)

        pygui.mouseDown()
        pygui.mouseUp()

    def chop_meat(self):
            if self.c.button_info['双刃刀'] == 2:
                return
            x = self.region.left + 0.2 * self.region.width
            y = self.region.top + 0.65 * self.region.height
            pygui.moveTo(x, y)
            pygui.mouseDown()

            if self.c.button_info['双刃刀'] == 1:
                for i in range(5):
                    pygui.moveTo(x + 0.05 * self.region.width, y - 0.4 * self.region.height, duration = 0.5)

                    pygui.moveTo(x + 0.05 * self.region.width, y - 0.09 * self.region.height, duration = 0.5)
            else:
                for i in range(10):
                    pygui.moveTo(x + 0.05 * self.region.width, y - 0.4 * self.region.height)

                    pygui.moveTo(x + 0.05 * self.region.width, y - 0.09 * self.region.height, duration = 0.5)

            pygui.mouseUp()

    def do_shawarma(self, type):
        x_wrap = self.region.left + 0.3 * self.region.width
        y_wrap = self.region.top + 0.8 * self.region.height

        if not self.c.button_info['面饼']:
            pygui.moveTo(x_wrap, y_wrap)
            pygui.mouseDown()
            pygui.mouseUp()

        x_ingred = self.region.left + 0.25 * self.region.width
        y_ingred = self.region.top + 0.65 * self.region.height
        time.sleep(0.5)

        if self.c.button_info['配料'] == 1:
            add_t = 2
        elif self.c.button_info['配料'] == 0:
            add_t = 3
        elif self.c.button_info['配料'] == 2:
            add_t = 1

        if 0 < type < 8 or type == -1:
            for i in range(4):
                if i != 0 and (i == type or i == type - 4):
                    continue
                pygui.moveTo(x_ingred + i * 0.085 * self.region.width, y_ingred)
                for i in range(add_t):
                    pygui.mouseDown()
                    pygui.mouseUp()
        else:
            choices = {8:(1, 2),
                       9:(1, 3),
                       0:(2,3)}

            for i in range(4):
                print(i, type, choices[type])
                if i in choices[type]:
                    continue
                pygui.moveTo(x_ingred + i * 0.085 * self.region.width, y_ingred)
                for i in range(add_t):
                    pygui.mouseDown()
                    pygui.mouseUp()

        if type not in (4,5,6,7):
            if self.c.button_info['石榴糖浆'] == 1:
                pygui.moveTo(self.region.left + 0.15 * self.region.width, y_wrap)
                pygui.mouseDown()
                pygui.moveTo(x_wrap + 0.2 * self.region.width, y_wrap, duration=0.15)
                pygui.mouseUp()
                time.sleep(1)
            elif self.c.button_info['石榴糖浆'] == 2:
                pygui.moveTo(self.region.left + 0.15 * self.region.width, y_wrap)
                pygui.mouseDown()
                pygui.mouseUp()
                time.sleep(1)

        pygui.moveTo(x_wrap + 0.2 * self.region.width, y_wrap + 0.05 * self.region.height)
        pygui.mouseDown()
        pygui.moveTo(x_wrap + 0.2 * self.region.width, y_wrap - 0.06 * self.region.height, duration=0.3)
        pygui.mouseUp()

        if self.c.button_info['包装'] == 2:
            return

        if self.c.button_info['烤架'] == 1:
            self.tasks.append((datetime.datetime.now(), 7.5, self.wrap_shawarma, self.shawarma_on_oven))
            self.shawarma_on_oven += 1
        elif self.c.button_info['烤架'] == 2:
            self.tasks.append((datetime.datetime.now(), 3.5, self.wrap_shawarma, self.shawarma_on_oven))
            self.shawarma_on_oven += 1
        elif self.c.button_info['烤架'] == 3:
            self.tasks.append((datetime.datetime.now(), 2.3, self.wrap_shawarma, self.shawarma_on_oven))
            self.shawarma_on_oven += 1
        elif self.c.button_info['烤架'] == 0:
            self.wrap_shawarma(self.shawarma_on_oven)
            self.shawarma_on_oven += 1




    def wrap_shawarma(self, loc):
        x_wrap = self.region.left + 0.3 * self.region.width
        y_wrap = self.region.top + 0.77 * self.region.height

        if 0 < self.c.button_info['烤架'] < 3:
            pygui.moveTo(x_wrap + 0.4 * self.region.width, y_wrap + loc * 0.065 * self.region.height)
            pygui.mouseDown()
            pygui.moveTo(x_wrap + 0.3 * self.region.width, y_wrap + loc * 0.065 * self.region.height)
            pygui.mouseUp()
            self.shawarma_on_oven -= 1
            time.sleep(0.5)
        else:
            self.shawarma_on_oven -= 1
            time.sleep(0.5)

        if self.c.button_info['包装'] < 2:
            pygui.moveTo(x_wrap + 0.1 * self.region.width, y_wrap)
            pygui.mouseDown()
            if self.c.button_info['包装'] < 1:
                pygui.moveTo(x_wrap + 0.3 * self.region.width, y_wrap + loc * 0.065 * self.region.height, duration=0.25)

            pygui.mouseUp()


    def cash_in(self):
            x = self.region.left + 0.3 * self.region.width
            y = self.region.top + 0.5 * self.region.height

            pygui.moveTo(x, y)
            pygui.mouseDown()
            pygui.moveTo(self.region.left + 0.9 * self.region.width, y, duration=0.75)
            pygui.mouseUp()

    # async def orange_juice(self):
    #         if not self.c.button_info['橙汁']:
    #             return
    #
    #         x = self.region.left + 0.25 * self.region.width
    #         y = self.region.top + 0.85 * self.region.height
    #
    #         pygui.moveTo(x, y)
    #         pygui.mouseDown()
    #         pygui.mouseUp()