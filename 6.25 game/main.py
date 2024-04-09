"""
1950 : 정지
메인 코드 파일
"""


import sys
import pygame
import pygame as pg
import data.code.map as Map
from data.code.textinputbox import Textinput_box
import data.code.save as Save
import data.code.msgbox as msg

S_FIRST = Save.Save()
S_INI = Save.Save_Ini()

width = 640  # 가로 길이 설정
height = 480  # 세로 길이 설정
fps = 30
game_name = "찌찌우 "
speed = 10
BLACK = (0, 0, 0)

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')

WHITE = (255, 255, 255)


# class Save:
#     def __init__(self):
#         self.file0 = open(r"data\save\file0", "r", encoding="cp949")
#         self.file0_r = self.file0.readlines()
#         print(self.file0_r)
#         self.file0.close()
#         self.file0 = open(r"data\save\file0", "w", encoding="cp949")
#
#     def edit(self, line, r):
#         self.file0_r[line] = str(r) + "\n"
#
#     def write(self):
#         for i in self.file0_r:
#             print(i)
#             self.file0.write(str(i))
#         self.file0.close()
#
#
# # noinspection PyUnresolvedReferences
# S = Save()


class Selsect_cousor:
    def __init__(self, screen, cousor_type=1):
        self.s = screen

        self.c_img = pygame.image.load(r"data\img\cousor\cousor1.png")
        self.c_img = pygame.transform.scale(self.c_img, (117.5, 25))
        self.cousor_sprite = [self.c_img]

        print(self.c_img.get_size())

    def cousor_show(self, cousor_pos, size):
        self.s.blit(pygame.transform.scale(self.c_img, (117.5 * size, 25 * size)), cousor_pos)


class Game:

    def __init__(self):
        # 메인 셋팅
        self.fullscreen = False
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(game_name)
        self.screen = pygame.display.set_mode((width, height))  # 창 설정
        # DISPLAYSURF = pygame.display.set_mode((400, 300), FULLSCREEN)
        self.clock = pygame.time.Clock()  # 시간 설정
        self.M = False

        self.menunext = 0
        self.interaction_menu = False
        self.menupage = 0
        self.filenumber = 1

        # Key DEFINE
        self.KDOWN = False
        self.z_key = False
        self.down = False
        self.up = False
        self.left = False
        self.right = False
        self.interaction = False

        self.CO = Selsect_cousor(self.screen)
        self.reload = False

        self.COpos_index = 0

        # 플레이어 설정
        self.mapfile = Map.Map(self.screen)
        self.p_pos = [160, 260]  # 좌표
        self.movement = [True, False]
        self.font = pygame.font.SysFont("malgungothic", 50)

        # 이스터에그
        self.scroll_menu_E_count = 0
        self.E_text_M = 0
        self.IsterEgg_M = False
        self.IsterEgg_MM = False

        # 음악 , 소리 설정
        self.IntroBgm = pygame.mixer.Sound(r"data\sound\music\mus_IntroBGM.ogg")
        self.collect = pygame.mixer.Sound(r"data\sound\effect\A Piano.wav")
        self.typing_sound = pygame.mixer.Sound(r"data\sound\effect\Typing.wav")
        self.connect = pygame.mixer.Sound(r"data\sound\effect\Connect.wav")
        self.text = lambda size, text, color=WHITE: pygame.font.SysFont("malgungothic", size).render(text, 1, color)
        pygame.mouse.set_visible(False)

    def title(self):
        self.typing_sound.play()

        self.IntroBgm.set_volume(5)
        self.interaction_menu = True
        font = pygame.font.SysFont("malgungothic", 50)
        text1 = font.render("B", 1, WHITE)
        text2 = font.render("By ", 1, WHITE)
        text3 = font.render("By Y", 1, WHITE)
        text4 = font.render("By YJ", 1, WHITE)
        title_lines = [text1, text2, text3, text4]
        title_pos = [[270, 190], [270, 190], [270, 190], [270, 190]]

        title_delay = 1000  # Milliseconds between title advances
        title_count = 4  # How many titles are in the animation
        title_index = 0  # what is the currently displayed title
        title_next_time = title_delay  # clock starts at 0, time for first title
        skip = 0
        while True:

            pygame.display.flip()
            clock = pygame.time.get_ticks()  # time now

            self.pressed_key = pygame.key.get_pressed()
            # Handle events
            for event in pygame.event.get():
                self.event(event=event)
            if self.pressed_key[pygame.K_z] or self.pressed_key[pygame.K_RETURN]:
                skip = 1
                print("skip")

            # paint the screen
            self.screen.fill(BLACK)  # paint it black

            # Write the current title, unless we've seen them all
            if title_index < title_count:
                self.screen.blit(title_lines[title_index], (title_pos[title_index][0], title_pos[title_index][1]))
            # Is it time to update to the next title?
            if clock > title_next_time:
                title_next_time = clock + title_delay  # some seconds in the future
                title_index += 1  # advance to next title-image
                if title_index != 4: self.typing_sound.play()
                print(title_index)

            if title_index == 5 or skip == 1:
                self.IntroBgm.play(-1)
                print("break")
                break

    def menu(self):
        font = pygame.font.SysFont("malgungothic", 25)
        t = pygame.time.get_ticks()
        print("M")
        print(t)
        self.screen.fill(WHITE)
        while True:
            pygame.display.update()
            self.pressed_key = pygame.key.get_pressed()
            self.screen.fill(BLACK)
            self.screen.blit(self.text(50, "1 9 5 0: 정지"), (0, 0))
            self.screen.blit(self.text(20, "Press Z key to start"), (240, 120))
            for event in pygame.event.get():
                self.event(event=event)
            if self.pressed_key[pygame.K_z]:  # and pygame.time.get_ticks() > t + 3000:
                print(pygame.time.get_ticks(), t + 3000)
                self.menupage += 1
                break
        # 파트 2 - 세이브 데이터 설정
        w = width - width / 1.15
        h = height - height / 1.2
        w1 = width - width / 1.17
        h1 = height - height / 1.23
        s1_size = (480, 100)
        self.COpos_index = 0
        save1_rect = pygame.Rect(w, h, s1_size[0], s1_size[1])
        save1_rect_second = pygame.Rect(w1, h1, s1_size[0] - 20, s1_size[1] - 20)

        def menu_first():
            print("t")
            self.menupage = 1
            while True:
                self.M = True
                self.pressed_key = pygame.key.get_pressed()
                # self.screen.fill((200, 100, 200))
                self.screen.fill(BLACK)
                self.screen.blit(self.text(30, "플레이할 파일을 선택하세요."), (0, 0))

                # File1 칸 드로우
                pygame.draw.rect(self.screen, WHITE, save1_rect)  # 메뉴 사각형 각각 3개중 하나생성
                pygame.draw.rect(self.screen, BLACK, save1_rect_second)  # 메뉴 사각형 각각 3개중 하나생성
                self.screen.blit(self.text(20, "파일 1"), (w + 15, h + 10))
                self.screen.blit(self.text(20, "내용 없음"), (w + 15, h + 40))
                # File2 칸 드로우
                pygame.draw.rect(self.screen, WHITE,
                                 pygame.Rect(w, h + 130, s1_size[0], s1_size[1]))  # 메뉴 사각형 각각 3개중 하나생성
                pygame.draw.rect(self.screen, BLACK,
                                 pygame.Rect(w1, h1 + 130, s1_size[0] - 20, s1_size[1] - 20))  # 메뉴 사각형 각각 3개중 하나생성
                self.screen.blit(self.text(20, "파일 2"), (w + 15, h + 140))
                self.screen.blit(self.text(20, "내용 없음"), (w + 15, h + 170))

                # File3 칸 드로우
                pygame.draw.rect(self.screen, WHITE,
                                 pygame.Rect(w, h + 260, s1_size[0], s1_size[1]))  # 메뉴 사각형 각각 3개중 하나생성
                pygame.draw.rect(self.screen, BLACK,
                                 pygame.Rect(w1, h1 + 260, s1_size[0] - 20, s1_size[1] - 20))  # 메뉴 사각형 각각 3개중 하나생성
                self.screen.blit(self.text(20, "파일 3"), (w + 15, h + 270))
                self.screen.blit(self.text(20, "내용 없음"), (w + 15, h + 300))

                self.screen.blit(self.text(20, "설정"), (w, 440))

                # 디스플레이 업데이트, 이벤트 설정

                self.COpos = [80, 210, 340, 415]

                for event in pygame.event.get():
                    self.event(event=event)
                if self.COpos_index > 3:
                    self.COpos_index = 0
                if self.COpos_index < 0:
                    self.COpos_index = 3
                self.CO.cousor_show((0, h * 0.5 + self.COpos[self.COpos_index]), size=0.6)  # 130
                if self.IsterEgg_MM and not self.E_text_M + 5000 < pygame.time.get_ticks():
                    self.screen.blit(self.text(20, "업적 달성: 이럴 바에 게임을 좀 시작해"), (220, 440))
                    S_INI.edit_ini("Achievement", "_m_isteregg", "1")

                pygame.display.update()
                if self.menupage == 2:
                    menu_second()
                    break

        def menu_second():
            self.screen.fill(BLACK)
            print("성공", self.COpos_index)
            # self.COpos_index = 0
            self.filenumber = self.COpos_index + 1
            self.COpos_index = 0
            while True:
                pygame.display.update()  # 디스플레이 없데이트하기

                self.M = True
                pos = 270, 300, 330

                self.screen.fill(BLACK)
                self.screen.blit(self.text(30, "파일 {} 을 플레이 하시겠습니까?".format(self.filenumber)), (110, 210))
                self.screen.blit(self.text(20, "네"), (110, 270))
                self.screen.blit(self.text(20, "아니오"), (110, 300))
                self.screen.blit(self.text(20, "삭제"), (110, 330))

                if self.COpos_index > 2:
                    self.COpos_index = 0

                if self.COpos_index < 0:
                    self.COpos_index = 2

                self.CO.cousor_show((30, pos[self.COpos_index]), size=0.6)
                if self.menupage == 3:
                    if self.COpos_index == 0:
                        print("ED")
                        self.menupage = 0
                        self.M = False
                        break
                    if self.COpos_index == 1:
                        menu_first()
                        self.menupage = 0
                        self.COpos_index = 0
                        break
                for event in pygame.event.get():
                    self.event(event=event)

        print("t")
        self.menupage = 0

        # if self.COpos_index == 3:  # 설정 메뉴
        #     print("선수 입장")
        #     self.event()
        #     self.screen.fill(BLACK)
        #     self.screen.blit(self.text(20, "설정"), (0, 0))

        menu_first()




    def event(self, event, more=0):
        # 이스터에그들..

        if self.scroll_menu_E_count >9 and not self.IsterEgg_M and not self.IsterEgg_MM:
            if S_INI.get_ini("E_M") == "0" and self.menupage == 1:
                self.E_text_M = pygame.time.get_ticks()
                self.IsterEgg_M = True
                self.IsterEgg_MM = True
                self.IsterEgg_M = False
                self.connect.play()


        self.pressed_key = pygame.key.get_pressed()  # 키 인식

        if event.type == pygame.QUIT or self.pressed_key[pygame.K_ESCAPE] or more==1:  # 게임 종료, or more값이 1일떄
            print("GAME END")
            if not S_FIRST.is_none(self.filenumber-1): S_FIRST.write()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            self.KDOWN = True
            if event.key == pygame.K_LEFT:
                self.left = True

            if event.key == pygame.K_RIGHT:
                self.right = True

            if event.key == (pygame.K_z or pygame.K_RETURN):
                if self.M:
                    self.menupage += 1
                if self.menupage == 4:
                    self.interaction = True
                self.interaction = True


            if event.key == pygame.K_UP:
                self.up = True
                if self.M:
                    self.COpos_index -= 1  # 메뉴전용 커서이동
                    self.scroll_menu_E_count += 1  # 이숫터에그
                    self.collect.play()

                # print(self.COpos_index)

            if event.key == pygame.K_DOWN:
                print(self.COpos_index)
                self.down = True
                if self.M:
                    self.COpos_index += 1  # 메뉴전용 커서이동
                    self.scroll_menu_E_count += 1  # 이숫터에그
                    self.collect.play()

                    # print(self.COpos_index)
                    self.collect.play()

            # 키가 떼졌을 때
            if event.type == pygame.KEYUP:
                # print(self.COpos_index)
                self.KDOWN = False
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False

                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                if event.key == pygame.K_z or pygame.K_RETURN and self.menupage == 0:
                    self.interaction = False

            if self.pressed_key[pygame.K_z]:  # 만약 Z키를 눌렀는가?
                self.z_key = True
            if self.pressed_key[pygame.K_w]:  # W키를 눌렀는가
                pass

    def file_start(self):
        if S_FIRST.is_none(self.filenumber-1):
            print("이름 존재 X")
            T = Textinput_box((280, 80), self.screen, 6)
            tim = pygame.time.get_ticks()
            while True:
                p = pygame.key.get_pressed()
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.text(30, "군인의 이름은? (ENTER키로 이름 완성)"), (0, 0))
                self.screen.blit(self.text(30, "나중에 변경이 불가하니 신중히 생각하세요."), (0, 40))

                T.draw()
                for event in pygame.event.get():
                    self.event(event=event)
                    T.event(event)
                if tim+1000 < pygame.time.get_ticks() and p[pygame.K_RETURN] and len(T.get()) > 2:
                    # save file edit
                    S_FIRST.edit("name", T.get(), self.filenumber-1)
                    self.interaction = False
                    break


    def run(self):  # 쌈1뽕한 매인
        print("Game Run successfully")
        self.title()
        self.menu()
        print(" MAINRUN ")
        self.file_start()




        self.IntroBgm.stop()
        self.screen.fill(0)
        msg.eventset(self.event)
        while True:
            a = msg.MsgBox(self.screen, "* 어둡다.. 아무것도 볼 수 없다", 20, 0, 25).draw()
            if a == "END1":
                pygame.quit()
                sys.exit()
            elif a == "END2":
                print("성공")
                break

        while True:
            a = msg.MsgBox(self.screen, "* 차갑다.. 아무것도 알 수 없다", 20, 0, 25).draw()
            if a == "END1":
                for event in pygame.event.get():
                    self.event(event=event)
            elif a == "END2":
                print("성공")
                break

        while True:
            a = msg.MsgBox(self.screen, "* 차가운 물이 한 방울 떨어졌다.", 20, 0, 25).draw()
            for event in pygame.event.get():
                self.event(event=event)
            if a == "END2": break

        Screen = self.screen
        M = self.mapfile
        Clock = pygame.time.Clock()
        M._load(2)
        M.draw_set()
        while True:
            self.screen.fill(0)
            M.draw()
            M.event()
            Screen.blit(M.assets["Player1"], (287, 215))
            pygame.display.update()
            for event in pygame.event.get():
                self.event(event)
            Clock.tick(60)


Game().run()
