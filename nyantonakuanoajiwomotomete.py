import pygame
import sys
import random
import copy

#色
SGREEN = (164,213,189)
SBLUE = (165,189,214)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (252,157,184)
GRAY = (155,155,155)

#画像
img_title = pygame.image.load("./images/title.png")
img_typing = pygame.image.load("./images/typing.png")
img_neko_magao = pygame.image.load("./images/neko_magao.png")
img_neko_egao = pygame.image.load("./images/neko_egao.png")
img_neko_zannen = pygame.image.load("./images/neko_zannen.png")
img_nekokan_open = pygame.image.load("./images/nekokan_open.png")
img_nekokan = pygame.image.load("./images/nekokan.png")
img_nikukyu = pygame.image.load("./images/nikukyu.png")
img_title_logo = pygame.image.load("./images/title_logo.png")
img_dungeon_create = pygame.image.load("./images/dungeon_create.png")
img_dungeon_floor = pygame.image.load("./images/dungeon_floor.png")
img_muse_cry = pygame.image.load("./images/mouse_cry.png")
img_mouse_sleep = pygame.image.load("./images/mouse_sleep.png")
img_mouse_strong_eye = pygame.image.load("./images/mouse_strong_eye.png")
img_mouse_strong = pygame.image.load("./images/mouse_strong.png")
img_mouse = pygame.image.load("./images/mouse.png")
img_dungeon_cheese = pygame.image.load("./images/dungeon2.png")
img_dungeon_wall = pygame.image.load("./images/dungeon1.png")
img_dungeon_chest = pygame.image.load("./images/chest.png")
img_boss_buttle = pygame.image.load("./images/boss_battle.png")
img_finish = pygame.image.load("./images/finish.png")
img_dungeon = pygame.image.load("./images/dungeon.png")
img_attack = pygame.image.load("./images/effect_a.png")
img_magic = pygame.image.load("./images/effect_b.png")
img_heal = pygame.image.load("./images/heal.png")
img_start_txt = pygame.image.load("./images/start.png")
img_finish_txt = pygame.image.load("./images/finish_txt.png")
img_gameover_txt = pygame.image.load("./images/gameover.png")
img_space_txt = pygame.image.load("./images/space.png")
img_no_mouse = pygame.image.load("./images/no_mouse.jpg")
img_dark = pygame.image.load("./images/dark.png")
img_bad_txt = pygame.image.load("./images/bad.png")
img_damage_txt = pygame.image.load("./images/damage.png")
img_good_txt = pygame.image.load("./images/good.png")
img_kougeki_txt = pygame.image.load("./images/kougeki.png")
img_mahou_txt = pygame.image.load("./images/mahou.png")
img_kahuku_txt = pygame.image.load("./images/kaihuku.png")
img_bougyo_txt = pygame.image.load("./images/bougyo.png")
img_mouse_kougeki_txt = pygame.image.load("./images/mouse_kougeki.png")

clock_time = 30

#タイピングゲームに必要な変数、配列
index = 0
question =[
    "company",
    "office",
    "meeting",
    "department",
    "worker",
    "several",
    "job",
    "money",
    "problem",
    "sale",
    "store",
    "customer",
    "product",
    "vacation",
    "increase",
    "machine",
    "same",
    "found",
    "offer",
    "believe",
    "order",
    "receive",
    "let",
    "due",
    "report",
    "price",
    "university",
    "however",
    "survey",
    "kind",
    "major",
    "manager",
    "purpose",
    "change",
    "bank",
    "quality",
    "although",
    "someone",
    "passenger",
    "allow",
    "appear",
    "annual",
    "refund",
    "receipt",
    "concern",
    "way",
    "prepare",
    "early",
    "renovation",
    "special",
    "participant",
    "fine",
    "medical",
    "return",
    "catering",
    "ensure",
    "estimate",
    "potential",
    "remind",
    "intend",
    "delighted",
    "cinplimentary",
    "mayor",
    "venue",
    "fabric",
    "patient",
    "attach",
    "conversation",
    "anyway",
    "paperwork",
    "greet",
    "realize",
    "status",
    "procedure",
    "cause",
    "save",
    "negotiate",
    "lobby",
    "exchange",
    "distance",
    "admission",
    "inquire"
]
len_question = len(question)
nokori = []
len_nokori = 0
wordok = True
word = ""
now_ascii = 0
now = 0
ac_count = 0
neko = img_neko_magao
type_down = False
lenzoku = True
back_ascii = 0
word_size_width = 0
word_size_height = 0
count_txt = None
count = 41
lenzoku_ac = 0

#ダンジョンに必要な変数、配列
dungeon_H = 30
dungeon_W = 30
M = 24 #1マスの大きさ
R = M/2

cost = [[0 for _ in range(dungeon_W)]for _ in range(dungeon_H)]
dungeon = [[0 for _ in range(dungeon_W+5)]for _ in range(dungeon_H+5)]
for i in range(-2,3,1):
    dungeon[1][dungeon_W//3+i] = 1
    dungeon[4][dungeon_W//3+i] = 1
    dungeon[dungeon_H-2][dungeon_W//2+i] = 1
    dungeon[dungeon_H-5][dungeon_W//2+i] = 1
    for j in range(2,4):
        if i == -2 or i == 2:
            dungeon[j][dungeon_W//3+i] = 1
        else:
            dungeon[j][dungeon_W//3+i] = 2
    for j in range(dungeon_H-4,dungeon_H-2,1):
        if i == -2 or i == 2:
            dungeon[j][dungeon_W//2+i] = 1
        else:
            dungeon[j][dungeon_W//2+i] = 2

DUNGEON = copy.deepcopy(dungeon)

p_pos_x = dungeon_W//2 
p_pos_y = dungeon_H-3
boss_pos_x = dungeon_W//3
boss_pos_y = 2
pos_x = 0
pos_y = 0
select = 0
cleck = True
gameover = False

p_status = {"HP":100,"MP":0,"ATK":50,"DEF":50,"DEX":70,"LUK":30}
boss_status = {"HP":400,"ATK":200,"DEF":100}
HP = p_status["HP"]
DEF = p_status["DEF"]
ATK = p_status["ATK"]

WEPPON = {"Buki":{"Good":70,"Bad":-20},"Bougu":{"Good":70,"Bad":-20}}
BUKI_OK = ""
BOUGU_OK = ""
buki = ""
weppon = ""

damage = 0
damage_txt = ""

cost_M = [0,2,1,5]
a = 0

score = 0
tmr = 0

#マス配置関数
def put(bg,img,x,y,size = M,place_x = 0,place_y = 0):
    return bg.blit(pygame.transform.scale(img,(size,size)),[place_x+size*x,place_y+size*y])

#数値配置関数
def int_put(bg,word_txt,x,y,font):
    txt = font.render(str(word_txt),True,BLACK)
    return bg.blit(txt,[x,y])

#本編
def turn(bg,clock):
    global index,wordok,word,now_ascii,now,len_word,d,ac_count,start_time,\
        time,select,pos_x,pos_y,p_pos_x,p_pos_y,neko,type_down,difficult,nokori,\
        len_nokori,lenzoku,clock_time,back_ascii,word_size_width,word_size_height,\
        count,count_txt,a,cleck,gameover,p_status,question,dungeon,boss_pos_x,boss_pos_y,\
        cost,DUNGEON,tmr,boss_status,defence,lenzoku_ac,weppon,BUKI_OK,\
        BOUGU_OK,buki,ATK,DEF,damage,damage_txt,HP

    key = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mbtn1, mbtn2, mbtn3 = pygame.mouse.get_pressed()
    font = pygame.font.SysFont(None,80)
    font_0 = pygame.font.SysFont(None,45)
    font_1 = pygame.font.SysFont(None,150)
    font_2 = pygame.font.SysFont(None,65)
    font_3 = pygame.font.SysFont(None,300)
    font_4 = pygame.font.SysFont(None,100)

    #タイトル
    if index == 0:
        bg.blit(img_title,[0,0])
        if mouse_x >= 865 and mouse_x <= 1150 and mouse_y >= 320 and mouse_y <= 440:
            bg.blit(img_nikukyu,[700,320])
            difficult = 1
            if mbtn1 == 1:
                index = 0.5
                tmr = 0
        elif mouse_x >= 865 and mouse_x <= 1260 and mouse_y >= 460 and mouse_y <= 555:
            bg.blit(img_nikukyu,[700,460])
            difficult = 2
            if mbtn1 == 1:
                index = 0.5
                tmr = 0
        elif mouse_x >= 865 and mouse_x <= 1150 and mouse_y >= 600 and mouse_y <= 640:
            bg.blit(img_nikukyu,[700,600])
            difficult = 3
            if mbtn1 == 1:
                index = 0.5
                tmr = 0
        
    if index == 0.5:
        if tmr < 30 and tmr % 2 == 0:
            put(bg,img_dark,0,0,1280)
        elif 30 <= tmr:
            index = 1

    if index == 1:
        bg.blit(img_typing,[0,0])
        bg.blit(neko,[0,360]) 
        w = font_4.render("30",True,BLACK)
        bg.blit(w,[20,20])
        ac_count_txt = font_4.render("Pt:"+str(ac_count),True,BLACK)
        bg.blit(ac_count_txt,[1050,20])

        bg.blit(img_start_txt,[250,250])

        if key[pygame.K_SPACE] == 1:
            start_time = pygame.time.get_ticks()
            index = 2 

    #タイピングゲームフェーズ
    if index == 2:
        bg.blit(img_typing,[0,0])
        bg.blit(neko,[0,360])

        time = pygame.time.get_ticks() - start_time
        time //= 1000
        time = 30 - time
        time_txt = font_4.render(str(time),True,BLACK)
        bg.blit(time_txt,[20,20])

        count += 1
        if count <= 40:
            bg.blit(count_txt,[1150,80])

        if len_nokori == 0:
            nokori = copy.deepcopy(question)

        len_nokori = len(nokori)

        if wordok:
            d = random.randint(0,len_nokori-1)
            
            word = nokori.pop(d)
            len_word = len(word)
            now = 0

            wordok = False

        txt = font_1.render(word,True,BLACK)
        txt_end = font_1.render(word[0:now],True,GRAY)
        word_size_width,word_size_height = pygame.font.Font.size(font,word)
        bg.blit(txt,[640-word_size_width,250])
        bg.blit(txt_end,[640-word_size_width,250])
        ac_count_txt = font_4.render("Pt:"+str(ac_count),True,BLACK)
        bg.blit(ac_count_txt,[1050,20])
            
        if now != len_word:
            now_word = word[now]
            now_ascii = ord(now_word)

            if key[back_ascii] == 0:
                lenzoku = True

            if key[now_ascii] == 1 and lenzoku:
                type_down = False
                lenzoku = False
                neko = img_neko_egao
                now += 1
                lenzoku_ac += 1
                ac_count += (lenzoku_ac//5)%6
                ac_count += 1
                back_ascii = now_ascii
                count_txt = font.render("+"+str(1+((lenzoku_ac//5)%6)) ,True,RED)
                count = 0
            elif 1 in key and type_down:
                type_down = False
                neko = img_neko_zannen
                lenzoku_ac = 0
                ac_count -= 1
                if ac_count > 0:
                    count_txt = font.render("-1",True,BLUE)
                    count = 0
                if ac_count < 0:
                    ac_count = 0
            elif 1 not in key:
                type_down = True
        
        else:
            lenzoku = False
            wordok = True

        if time == 0:
            index = 3
            
        
    #タイピングゲーム終了
    if index == 3:
        bg.blit(img_typing,[0,0])
        bg.blit(neko,[0,360])
        time_txt = font.render("0",True,BLACK)
        bg.blit(time_txt,[20,20])
        ac_count_txt = font.render("Pt:"+str(ac_count),True,BLACK)
        bg.blit(ac_count_txt,[1100,20])
        
        bg.blit(img_finish_txt,[430,250])
        bg.blit(img_space_txt,[290,350])

        if key[pygame.K_SPACE] == 1:
            index = 3.5
            tmr = 0

    if index == 3.5:
        if tmr < 30 and tmr % 2 == 0:
            put(bg,img_dark,0,0,1280)
        elif 30 <= tmr:
            index = 4
    
    #ダンジョン作成
    if index == 4:
        bg.blit(img_dungeon_create,[0,0])

        for y in range(dungeon_H):
            for x in range(dungeon_W):
                if dungeon[y][x] == 1:
                    if dungeon[y+1][x] == 1:
                        put(bg,img_dungeon_wall,x,y)
                    else:
                        put(bg,img_dungeon_cheese,x,y)
                    
                if dungeon[y][x] == 2:
                    put(bg,img_dungeon_floor,x,y)

                if dungeon[y][x] == 3:
                    put(bg,img_dungeon_chest,x,y)
                    
        put(bg,img_mouse_sleep,boss_pos_x,boss_pos_y)
        put(bg,img_neko_magao,p_pos_x,p_pos_y)
        pygame.draw.rect(bg,PINK,[pos_x*M, pos_y*M, M, M],3)
    
        ac_count_txt = font.render(str(ac_count),True,BLACK)
        bg.blit(ac_count_txt,[750,720-115])

        int_put(bg,p_status["HP"],1025,310,font)
        int_put(bg,p_status["MP"],1025,370,font)
        int_put(bg,p_status["ATK"],1025,435,font)
        int_put(bg,p_status["DEF"],1025,500,font)
        int_put(bg,p_status["DEX"],1025,565,font)
        int_put(bg,p_status["LUK"],1025,635,font)

        if mouse_x < 24*30:
            pos_x = mouse_x//M
            pos_y = mouse_y//M

        if mbtn1 == 1:
            if 720 < mouse_x and mouse_x < 1000 and 0 < mouse_y and mouse_y < 140:
                select = 2
            if 1000 < mouse_x and mouse_x < 1280 and 0 < mouse_y and mouse_y < 140:
                select = 1
            if 720 < mouse_x and mouse_x < 1000 and 140 < mouse_y and mouse_y < 240:
                select = 3
            if 1000 < mouse_x and mouse_x < 1280 and 140 < mouse_y and mouse_y < 240:
                select = -1

            if 1155 < mouse_x and mouse_x < 1265 and cleck:
                if mouse_x < 1202:
                    if ac_count > 0:
                        a = 1
                    else:
                        a = 0
                elif 1217 < mouse_x:
                    a = -1
                if 316 < mouse_y and mouse_y < 362:
                    if a == 1:
                        p_status["HP"] += a
                        ac_count -= a
                    elif a == -1:
                        if p_status["HP"] > 0:
                            p_status["HP"] += a
                            ac_count -= a
                if 384 < mouse_y and mouse_y < 430:
                    if a == 1:
                        p_status["MP"] += a
                        ac_count -= a
                    elif a == -1:
                        if p_status["MP"] > 0:
                            p_status["MP"] += a
                            ac_count -= a
                if 450 < mouse_y and mouse_y < 496:
                    if a == 1:
                        p_status["ATK"] += a
                        ac_count -= a
                    elif a == -1:
                        if p_status["ATK"] > 0:
                            p_status["ATK"] += a
                            ac_count -= a
                if 514 < mouse_y and mouse_y < 560:
                    if a == 1:
                        p_status["DEF"] += a
                        ac_count -= a
                    elif a == -1:
                        if p_status["DEF"] > 0:
                            p_status["DEF"] += a
                            ac_count -= a
                if 580 < mouse_y and mouse_y < 625:
                    if a == 1:
                        if p_status["DEX"] < 100:
                            p_status["DEX"] += a
                            ac_count -= a
                    elif a == -1:
                        if p_status["DEX"] > 0:
                            p_status["DEX"] += a
                            ac_count -= a
                if 644 < mouse_y and mouse_y < 690:
                    if a == 1:
                        if p_status["LUK"] < 100:
                            p_status["LUK"] += a
                            ac_count -= a
                    elif a == -1:
                        if p_status["LUK"] > 0:
                            p_status["LUK"] += a
                            ac_count -= a
                cleck = False
        else:
            cleck = True
        
        if select == 2:
            pygame.draw.rect(bg,PINK,[720, 0, 280, 140],3)
        if select == 1:
            pygame.draw.rect(bg,PINK,[1000, 0, 280, 140],3)
        if select == 3:
            pygame.draw.rect(bg,PINK,[720, 140, 280, 140],3)
        if select == -1:
            pygame.draw.rect(bg,PINK,[1000, 140, 280, 140],3)

        if mbtn1 == 1 and mouse_x < 24*30:
            if select == -1:
                dungeon[pos_y][pos_x] = DUNGEON[pos_y][pos_x]
                ac_count += cost[pos_y][pos_x]
                cost[pos_y][pos_x] = 0

            elif dungeon[pos_y][pos_x] != select and ac_count >= cost_M[select]:
                if select != 3 or dungeon[pos_y][pos_x] == 2:
                    if select == 3:
                        dungeon[pos_y][pos_x] = select
                        cost[pos_y][pos_x] += cost_M[select]
                        ac_count -= cost_M[select]
                    else:
                        dungeon[pos_y][pos_x] = select
                        ac_count += cost[pos_y][pos_x]
                        cost[pos_y][pos_x] = cost_M[select]
                        ac_count -= cost_M[select]
        
        if key[pygame.K_RETURN] == 1:
            ATK = p_status["ATK"]
            DEF = p_status["DEF"]
            clock_time = 10
            index = 4.5
            tmr = 0
            p_status["HP"] = HP
    
    if index == 4.5:
        if tmr < 30 and tmr % 2 == 0:
            put(bg,img_dark,0,0,1280)
        elif 30 <= tmr:
            index = 5
    
    #ダンジョン探索
    if index == 5:
        bg.blit(img_dungeon,[0,0])
        if weppon == "Buki":
            p_status["ATK"] = ATK
            p_status["ATK"] += WEPPON["Buki"][buki]
            BUKI_OK = buki
        elif weppon == "Bougu":
            p_status["DEF"] = DEF
            p_status["DEF"] += WEPPON["Bougu"][buki]
            BOUGU_OK = buki
        if BUKI_OK == "Good":
            bg.blit(img_good_txt,[925,720-150])
        elif BUKI_OK == "Bad":
            bg.blit(img_bad_txt,[925,720-150])
        if BOUGU_OK == "Good":
            bg.blit(img_good_txt,[925,720-63])
        elif BOUGU_OK == "Bad":
            bg.blit(img_bad_txt,[925,720-63])        

        for y in range(dungeon_H):
            for x in range(dungeon_W):
                if dungeon[y][x] == 1:
                    if dungeon[y+1][x] == 1:
                        put(bg,img_dungeon_wall,x,y,13,890,0)
                    else:
                        put(bg,img_dungeon_cheese,x,y,13,890,0)
                    
                if dungeon[y][x] == 2:
                    put(bg,img_dungeon_floor,x,y,13,890,0)

                if dungeon[y][x] == 3:
                    put(bg,img_dungeon_chest,x,y,13,890,0)

        put(bg,img_mouse_sleep,boss_pos_x,boss_pos_y,13,890,0)
        put(bg,img_neko_magao,p_pos_x,p_pos_y,13,890,0)

        int_put(bg,p_status["HP"],1170,400,font_2)
        int_put(bg,p_status["MP"],1170,450,font_2)
        int_put(bg,p_status["ATK"],1170,500,font_2)
        int_put(bg,p_status["DEF"],1170,550,font_2)
        int_put(bg,p_status["DEX"],1170,598,font_2)
        int_put(bg,p_status["LUK"],1170,655,font_2)
            
        for y in range(-5,6):
            for x in range(-5,6):
                if dungeon[p_pos_y+y][p_pos_x+x] == 1:
                    if dungeon[p_pos_y+y+1][p_pos_x+x] == 1:
                        put(bg,img_dungeon_wall,x+4,y+4,80)
                    else:
                        put(bg,img_dungeon_cheese,x+4,y+4,80)

                if dungeon[p_pos_y+y][p_pos_x+x] == 2:
                    put(bg,img_dungeon_floor,x+4,y+4,80)

                if dungeon[p_pos_y+y][p_pos_x+x] == 3:
                    put(bg,img_dungeon_chest,x+4,y+4,80)
                if p_pos_y+y == boss_pos_y and p_pos_x+x == boss_pos_x:
                    put(bg,img_mouse_sleep,x+4,y+4,80)
        
        put(bg,img_neko_magao,0,0,80,80*4,80*4)    

        if key[pygame.K_UP] == 1 or key[pygame.K_w]:
            if dungeon[p_pos_y-1][p_pos_x] != 1: 
                p_pos_y -= 1
        if key[pygame.K_DOWN] == 1 or key[pygame.K_s]:
            if dungeon[p_pos_y+1][p_pos_x] != 1:
                p_pos_y += 1
        if key[pygame.K_LEFT] == 1 or key[pygame.K_a]:
            if dungeon[p_pos_y][p_pos_x-1] != 1:
                p_pos_x -= 1
        if key[pygame.K_RIGHT] == 1 or key[pygame.K_d]:
            if dungeon[p_pos_y][p_pos_x+1] != 1:
                p_pos_x += 1         
        if p_pos_x == boss_pos_x and p_pos_y == boss_pos_y:
            index = 5.5
            tmr = 0
            ATK = p_status["HP"]
            DEF = p_status["DEF"]
        if dungeon[p_pos_y][p_pos_x] == 3:
            dungeon[p_pos_y][p_pos_x] = 2
            d = random.randint(0,100)
            D = random.randint(0,100)
            if d <= p_status["LUK"]:
                buki = "Good"
            else:
                buki = "Bad"
            if D <= 50:
                weppon = "Buki"
            else:
                weppon = "Bougu"           

        if dungeon[p_pos_y][p_pos_x] == 0:
            p_pos_x = dungeon_W//2 
            p_pos_y = dungeon_H-3
            p_status["HP"] -= 10

        if p_status["HP"] <= 0:
            index = 13
            gameover = True
            tmr = 0   

    if index == 5.5:
        if tmr < 30 and tmr % 2 == 0:
            put(bg,img_dark,0,0,1280)
        elif 30 <= tmr:
            index = 6
    
    #ボス戦
    #プレイヤーのターン
    if index == 6:
        bg.blit(img_boss_buttle,[0,0])
        int_put(bg,p_status["HP"],1280-955,510,font)
        int_put(bg,p_status["MP"],1280-955,610,font)
        
        if p_status["HP"] <= 0:
            p_status["HP"] = 0
            index = 13
            gameover = True
            tmr = 0
    
        if boss_status["HP"] <= 0:
            index = 12
            tmr = 0

        defence = False

        if 1280-355 < mouse_x and mouse_x < 1280-130 and 363 < mouse_y and mouse_y < 433:
            put(bg,img_nikukyu,0,0,80,830,363)
            if mbtn1 == 1:
                tmr = 0
                index = 7

        if 1280-355 < mouse_x and mouse_x < 1280-185 and 450 < mouse_y and mouse_y < 516:
            put(bg,img_nikukyu,0,0,80,830,450)
            if mbtn1 == 1 and p_status["MP"] >= 10:
                tmr = 0
                index = 8

        if 1280-355 < mouse_x and mouse_x < 1280-130 and 525 < mouse_y and mouse_y < 590:
            put(bg,img_nikukyu,0,0,80,830,525)
            if mbtn1 == 1 and p_status["MP"] >= 5:
                tmr = 0
                index = 9

        if 1280-355 < mouse_x and mouse_x < 1280-130 and 603 < mouse_y and mouse_y < 670:
            put(bg,img_nikukyu,0,0,80,830,603)
            if mbtn1 == 1:
                tmr = 0
                index = 10

    #プレイヤーの攻撃
    if index == 7:
        bg.blit(img_boss_buttle,[0,0])
        int_put(bg,p_status["HP"],1280-955,510,font)
        int_put(bg,p_status["MP"],1280-955,610,font)
        if 0 <= tmr <= 5:
            bg.blit(img_kougeki_txt,[50,50])
        if 5 < tmr < 10:
            bg.blit(img_attack,[1000-(tmr-3)*120,-300+(tmr-3)*120])
        if tmr == 10:
            d = random.randint(0,100)
            damage = p_status["ATK"]-boss_status["DEF"]
            if damage < 0 or d > p_status["DEX"]:
                damage = 0
            damage_txt = font.render(str(damage),True,RED)
            boss_status["HP"] -= damage
                
        if 10 < tmr < 15:
            bg.blit(damage_txt,[50,150])
            bg.blit(img_damage_txt,[130,150])
            if tmr%2 == 0:
                bg.blit(img_no_mouse,[0,0])
        if 15 <= tmr < 20:
            bg.blit(damage_txt,[50,150])
            bg.blit(img_damage_txt,[150,150])
        if tmr == 20:
            if boss_status["HP"] <= 0:
                index = 12
                tmr = 0
            else:
                tmr = 0
                index = 11

    #プレイヤーのまほう
    if index == 8:
        bg.blit(img_boss_buttle,[0,0])
        int_put(bg,p_status["HP"],1280-955,510,font)
        int_put(bg,p_status["MP"],1280-955,610,font)
        if 0 <= tmr <= 5:
            bg.blit(img_mahou_txt,[50,50])
        if 5 < tmr < 10:
            put(bg,img_magic,0,0,tmr*30,600-tmr*15,250-tmr*15)
        if tmr == 10:
            d = random.randint(0,100)
            damage = p_status["ATK"]*1.3-boss_status["DEF"]
            if damage < 0 or d > p_status["DEX"]:
                damage = 0
            damage_txt = font.render(str(damage),True,RED)
            p_status["MP"] -= 10
            boss_status["HP"] -= damage
        
        if 10 < tmr < 15:
            bg.blit(damage_txt,[50,100])
            bg.blit(img_damage_txt,[130,150])
            if tmr%2 == 0:
                bg.blit(img_no_mouse,[0,0])
        if 15 <= tmr < 20:
            bg.blit(damage_txt,[50,150])
            bg.blit(img_damage_txt,[130,150])
        if tmr == 20:
            if boss_status["HP"] <= 0:
                index = 12
                tmr = 0
            tmr = 0
            index = 11

    #プレイヤーの回復
    if index == 9:
        if tmr < 5 or 13 < tmr:
            bg.blit(img_boss_buttle,[0,0])
            int_put(bg,p_status["HP"],1280-955,510,font)
            int_put(bg,p_status["MP"],1280-955,610,font)
        if 0 <= tmr <= 5:
            bg.blit(img_kahuku_txt,[50,50])
        if 5 < tmr < 13:
            put(bg,img_heal,0,0,1280)
        if tmr == 13:
            p_status["HP"] = HP
            p_status["MP"] -= 5
        if tmr == 15:
            tmr = 0
            index = 11
    
    #プレイヤーの防御
    if index == 10:
        bg.blit(img_boss_buttle,[0,0])
        int_put(bg,p_status["HP"],1280-955,510,font)
        int_put(bg,p_status["MP"],1280-955,610,font)
        if 0 <= tmr <= 5:
            bg.blit(img_bougyo_txt,[50,50])
        if tmr == 10:
            p_status["DEF"] *= 1.5
            defence = True
            tmr = 0
            index = 11

    #敵の攻撃
    if index == 11:
        bg.blit(img_boss_buttle,[0,0])
        int_put(bg,p_status["HP"],1280-955,510,font)
        int_put(bg,p_status["MP"],1280-955,610,font)
        if 0 <= tmr <= 5:
            bg.blit(img_mouse_kougeki_txt,[50,50])
        if 5 < tmr < 10:
            bg.blit(img_boss_buttle,[tmr%2*10,tmr%2*10])
            int_put(bg,p_status["HP"],1280-955+tmr%2*10,510+tmr%2*10,font)
            int_put(bg,p_status["MP"],1280-955+tmr%2*10,610+tmr%2*10,font)
        if tmr == 10:
            damage = boss_status["ATK"]-p_status["DEF"]
            if damage < 0:
                damage = 0
            damage_txt = font.render(str(damage),True,RED)
            p_status["HP"] -= damage
            if p_status["HP"] < 0:
                p_status["HP"] = 0
        
        if 10 < tmr < 20:
            bg.blit(damage_txt,[50,150])
            bg.blit(img_damage_txt,[150,150])

        if tmr == 20:
            if defence:
                p_status["DEF"] = DEF
            index = 6
            tmr = 0

    #結果
    if index == 12:
        bg.blit(img_finish,[0,0])
        score = ac_count * 1000
        if gameover:
            score = 0
        txt = font_3.render(str(score),True,BLACK)
        word_size_width,word_size_height = pygame.font.Font.size(font,str(score))
        bg.blit(txt,[830-word_size_width,300])
        tmr = 1
        index = 14

    if index == 13:
        if tmr < 30 and tmr % 2 == 0:
            bg.blit(img_gameover_txt,[280,300])
        elif 30 <= tmr:
            index = 12

    if index == 14:
        if tmr <= ac_count and gameover == False:
            d_x = random.randint(20,1280-770)
            d_y = random.randint(150,474)
            bg.blit(img_nekokan,[d_x,d_y])
        if 1280-517 < mouse_x and mouse_x < 1280-155 and 551 < mouse_y and mouse_y < 630 and mbtn1 == 1:
            clock_time = 30
            index = 0
            nokori = []
            len_nokori = 0
            wordok = True
            word = ""
            now_ascii = 0
            now = 0
            ac_count = 0
            neko = img_neko_magao
            type_down = False
            lenzoku = True
            back_ascii = 0
            word_size_width = 0
            word_size_height = 0
            count_txt = None
            count = 41

            cost = [[0 for _ in range(dungeon_W)]for _ in range(dungeon_H)]
            dungeon = [[0 for _ in range(dungeon_W+5)]for _ in range(dungeon_H+5)]
            for i in range(-2,3,1):
                dungeon[1][dungeon_W//3+i] = 1
                dungeon[4][dungeon_W//3+i] = 1
                dungeon[dungeon_H-2][dungeon_W//2+i] = 1
                dungeon[dungeon_H-5][dungeon_W//2+i] = 1
                for j in range(2,4):
                    if i == -2 or i == 2:
                        dungeon[j][dungeon_W//3+i] = 1
                    else:
                        dungeon[j][dungeon_W//3+i] = 2
                for j in range(dungeon_H-4,dungeon_H-2,1):
                    if i == -2 or i == 2:
                        dungeon[j][dungeon_W//2+i] = 1
                    else:
                        dungeon[j][dungeon_W//2+i] = 2

            DUNGEON = copy.deepcopy(dungeon)

            p_pos_x = dungeon_W//2 
            p_pos_y = dungeon_H-3
            boss_pos_x = dungeon_W//3
            boss_pos_y = 2
            pos_x = 0
            pos_y = 0
            select = 0
            cleck = True
            gameover = False

            p_status = {"HP":100,"MP":0,"ATK":50,"DEF":50,"DEX":70,"LUK":40}
            boss_status = {"HP":400,"ATK":100,"DEF":60,"DEX":85}
            a = 0

            score = 0
            BUKI_OK = ""
            BOUGU_OK = ""
            buki = ""
            weppon = ""
            HP = p_status["HP"]
            DEF = p_status["DEF"]
            ATK = p_status["ATK"]

    if key[pygame.K_ESCAPE] == 1:
            clock_time = 30
            index = 0
            nokori = []
            len_nokori = 0
            wordok = True
            word = ""
            now_ascii = 0
            now = 0
            ac_count = 0
            neko = img_neko_magao
            type_down = False
            lenzoku = True
            back_ascii = 0
            word_size_width = 0
            word_size_height = 0
            count_txt = None
            count = 41

            cost = [[0 for _ in range(dungeon_W)]for _ in range(dungeon_H)]
            dungeon = [[0 for _ in range(dungeon_W+5)]for _ in range(dungeon_H+5)]
            for i in range(-2,3,1):
                dungeon[1][dungeon_W//3+i] = 1
                dungeon[4][dungeon_W//3+i] = 1
                dungeon[dungeon_H-2][dungeon_W//2+i] = 1
                dungeon[dungeon_H-5][dungeon_W//2+i] = 1
                for j in range(2,4):
                    if i == -2 or i == 2:
                        dungeon[j][dungeon_W//3+i] = 1
                    else:
                        dungeon[j][dungeon_W//3+i] = 2
                for j in range(dungeon_H-4,dungeon_H-2,1):
                    if i == -2 or i == 2:
                        dungeon[j][dungeon_W//2+i] = 1
                    else:
                        dungeon[j][dungeon_W//2+i] = 2

            DUNGEON = copy.deepcopy(dungeon)

            p_pos_x = dungeon_W//2 
            p_pos_y = dungeon_H-3
            boss_pos_x = dungeon_W//3
            boss_pos_y = 2
            pos_x = 0
            pos_y = 0
            select = 0
            cleck = True
            gameover = False

            p_status = {"HP":100,"MP":0,"ATK":50,"DEF":50,"DEX":70,"LUK":40}
            boss_status = {"HP":400,"ATK":100,"DEF":60,"DEX":85}
            a = 0

            score = 0
            BUKI_OK = ""
            BOUGU_OK = ""
            buki = ""
            weppon = ""
            HP = p_status["HP"]
            DEF = p_status["DEF"]
            ATK = p_status["ATK"]

    tmr += 1
    pygame.display.update()
    clock.tick(clock_time)




def main():
    pygame.init()
    pygame.display.set_caption("にゃんとなくあの味を求めて")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        turn(screen,clock)

if __name__ == "__main__":
    main()
