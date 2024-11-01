
import pyautogui as pygui
import keyboard as kb
import pygame as pg
import sys
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
    font = pg.font.SysFont("SimHei", 48)
    # font_l = pg.font.Font('D:\\tech\python\\game\\shaweima\\font\\ZhouZiSongTi7000Zi-2.otf', 40)
    titles = ['橙汁', '削土豆', '烤架1']

    def __init__(self):
        self.win = pg.display.set_mode((800, 600))

        self.win.fill(self.color_white)
        self.buttons = {}
        self.button_info = {}
        self.button_loc = {}

        l = len(self.titles)
        for i, j in enumerate(self.titles):
            words = self.font.render(j, True, self.color_black)
            loc = words.get_rect()
            loc.x += i * 200 % 600
            loc.y += i * 200 // 600 * 150
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
        self.items = dict()
        self.items['sir'] = self.sir
        self.items['cucumber'] = self.cucumber
        self.items['sauce1.png'] = self.sauce1
        self.items['add cucumber'] = self.add_cucumber
        self.items['add sauce1'] = self.add_sauce1
        self.items['end sir'] = self.end_sir
        self.c = console()
        asyncio.run(self.run())

    async def run(self):

        tasks = []
        while True:
            if kb.is_pressed('w'):
                print('Do shawarma')
                await self.do_shawarma()
            elif kb.is_pressed('s'):
                print('supply! sir')
                await self.supply_sir()
            elif kb.is_pressed('c'):
                print('Chopping!!!')
                await self.chop_meat()
            elif kb.is_pressed('f'):
                print('More chips!')
                await self.cut_potatoes()

            elif kb.is_pressed('m'):
                print('CHACHIN')
                await self.cash_in()
            elif kb.is_pressed('esc'):
                break

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    mouse = pg.mouse.get_pos()
                    for i in self.c.buttons:
                        loc = self.c.button_loc[i]
                        print(loc.x, loc.y)
                        if loc.x <= mouse[0] <= loc.x + 45 *len(i) and loc.y <= mouse[1] <= loc.y + 40:
                            self.c.button_info[i] = not self.c.button_info[i]
                            if self.c.button_info[i]:
                                words = self.c.font.render(i, True, self.c.color_maize)
                            else:
                                words = self.c.font.render(i, True, self.c.color_black)
                            self.c.win.blit(words, loc)
                            pg.display.flip()

            # for t in tasks:
            #     asyncio.run(t)
            # tasks = []

    async def terminate(self):
        return

    async def supply_sir(self):
        print(self.region)
        # location = pygui.locateCenterOnScreen(self.items['sir'], grayscale=True, confidence=0.85)
        x = self.region.left + 0.15 * self.region.width
        y = self.region.top + 0.5 * self.region.height
        # sir_loc = self.locate('sir')
        #
        pygui.moveTo(x, y)
        pygui.mouseDown()
        pygui.mouseUp()

        await asyncio.sleep(0.7)

        if self.c.button_info['橙汁']:
            pygui.moveTo(x + self.region.width / 15 , y + self.region.height / 7)

            for i in range(4):
                pygui.mouseDown()
                pygui.mouseUp()


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

    async def cut_potatoes(self):

        if not self.c.button_info['削土豆']:
            cutTime = 6
        else:
            cutTime = 3
        friedTime = 14

        x = self.region.left + 0.9 * self.region.width
        y = self.region.top + 0.6 * self.region.height

        pygui.moveTo(x, y)
        pygui.mouseDown()
        await asyncio.sleep(cutTime)
        pygui.mouseUp()

        # if self.start:
        #     await self.supply_sir()
        #     await asyncio.sleep(0.5)
        #     await self.chop_meat()
        #     await asyncio.sleep(friedTime - 7)
        #     self.start = False
        # else:
        await asyncio.sleep(friedTime)

        pygui.moveTo(x - self.region.width * 0.1, y - 0.1 * self.region.height)

        pygui.mouseDown()
        pygui.mouseUp()


    async def chop_meat(self):
            x = self.region.left + 0.2 * self.region.width
            y = self.region.top + 0.65 * self.region.height

            pygui.moveTo(x, y)
            pygui.mouseDown()

            for i in range(10):
                pygui.moveTo(x + 0.05 * self.region.width, y - 0.4 * self.region.height)

                pygui.moveTo(x + 0.05 * self.region.width, y - 0.09 * self.region.height, duration = 0.5)

            pygui.mouseUp()

    async def do_shawarma(self):
            x_wrap = self.region.left + 0.3 * self.region.width
            y_wrap = self.region.top + 0.8 * self.region.height

            pygui.moveTo(x_wrap, y_wrap)
            pygui.mouseDown()
            pygui.mouseUp()

            x_ingred = self.region.left + 0.25 * self.region.width
            y_ingred = self.region.top + 0.65 * self.region.height
            await asyncio.sleep(0.5)

            for i in range(4):
                pygui.moveTo(x_ingred + i * 0.085 * self.region.width, y_ingred)
                for i in range(3):
                    pygui.mouseDown()
                    pygui.mouseUp()



            pygui.moveTo(x_wrap + 0.2 * self.region.width, y_wrap + 0.05 * self.region.height)
            pygui.mouseDown()
            pygui.moveTo(x_wrap + 0.2 * self.region.width, y_wrap - 0.06 * self.region.height, duration=0.3)
            pygui.mouseUp()

            pygui.moveTo(x_wrap + 0.1 * self.region.width, y_wrap)
            pygui.mouseDown()
            pygui.moveTo(x_wrap + 0.3 * self.region.width, y_wrap - 0.05 * self.region.height, duration=0.3)
            pygui.mouseUp()

    async def cash_in(self):
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