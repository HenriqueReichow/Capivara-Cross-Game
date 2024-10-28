import pyxel as px
import random
import webbrowser

telainicio = 0
telaplay = 1
telaperder = 2
telaganhar = 3
telapause = 4

class carros:
    def __init__(self, posx, posy, direcão, velocidade):
        self.posx = posx
        self.posy = posy
        self.direcão = direcão
        self.velocidade = velocidade
        self.tipo = random.choice([2,3,4,5])

    def mover(self):
        if self.direcão == 1:
            self.posx += self.velocidade 
            if self.posx > px.width:
                self.posx = 0 
        if self.direcão == 0:
            self.posx -= self.velocidade
            if self.posx < 0:
                self.posx = 1280

    def draw(self):
        #2 = carro vermelho / 3 = carro branco / 4 = camionete / 5 = jeep militar
        if self.tipo == 2:
            if self.direcão == 0:
                px.blt(self.posx,self.posy,0,65,79,65,33,0)
            else:
                px.blt(self.posx,self.posy,0,65,46,65,33,0)
        elif self.tipo == 3:
            if self.direcão == 0:
                px.blt(self.posx,self.posy,0,0,79,65,33,0)
            else:
                px.blt(self.posx,self.posy,0,0,46,65,33,0)
        elif self.tipo == 4:
            if self.direcão == 0:
                px.blt(self.posx,self.posy,0,130,79,77,33,0)
            else:
                px.blt(self.posx,self.posy,0,130,46,77,33,0)
        elif self.tipo == 5:
            if self.direcão == 0:
                px.blt(self.posx,self.posy,0,0,145,75,33,0)
            else:
                px.blt(self.posx,self.posy,0,0,112,75,33,0)

class capivara:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.estado = 0
        self.j = 0

    def andar(self):
        if px.btnp(px.KEY_UP) == True:   
            self.y -= 38
            self.estado = 0
        if px.btnp(px.KEY_DOWN) == True:   
            self.y += 38
            self.estado = 0 
        if px.btnp(px.KEY_RIGHT) == True:   
            self.x += 38
            self.estado = 2
        if px.btnp(px.KEY_LEFT) == True:
            self.x -= 38
            self.estado = 1 
        if self.y < 114:
            self.j += 1
            self.y = 574
            self.x = 640
        if self.y >= 600:
            self.y -= 38
            self.estado = 0

    def desenho(self): 
        if self.estado == 0:  
            px.blt(self.x,self.y,0,28,0,17,23,0)
        if self.estado == 1: 
            px.blt(self.x,self.y,0,0,23,28,23,0)
        if self.estado == 2:
            px.blt(self.x,self.y,0,0,0,28,23,0)
        if self.j == 1 or self.j == 2 or self.j == 3:
            px.blt(640,76,0,28,0,17,23,0)
        if self.j == 2 or self.j == 3:
            px.blt(680,76,0,28,0,17,23,0)
        if self.j == 3:
            px.blt(600,76,0,28,0,17,23,0)

class ambiente:
    def __init__(self, y):
        self.y = y
        self.x = 0
    def criar(self):
        for i in range(12): 
            self.y += 38
    def draw(self):
        a = 570
        for i in range(11):
            a -= 38
            px.rect(0,a,1280,3,10)
        self.x = 0
        while self.x < px.width:
            px.blt(self.x,574,0,129,0,15,38,0)
            px.blt(self.x,76,0,129,0,15,38,0)
            px.blt(self.x,308,0,129,0,15,38,0)
            self.x += 15 
        px.blt(0,0,0,0,179,256,119,0);px.blt(256,0,0,0,179,256,119,0);px.blt(512,0,0,0,179,256,119,0);px.blt(768,0,0,0,179,256,119,0);px.blt(1024,0,0,0,179,256,119,0)
        px.rect(0,601,1280,37,13)
        px.rect(0,602,1280,3,1)
        px.rect(0,602,3,38,1)
        px.rect(1277,602,3,38,1)
        px.rect(0,637,1280,3,1)
        px.text(614,615,'- CAPIVARA CROSS -',5)
        
class jogo:
    def __init__(self):
        px.init(1280,640)
        self.tela = 0 
        px.mouse(True)
        px.image(0).load(0,0,'data/ba.png')
        px.image(1).load(0,0,'data/cap.png')
        px.image(2).load(0,0,'data/lake.png')
        self.ambiente = ambiente(114)
        self.capivara = capivara(640,574)
        self.cars = [carros(400,118,0,24),carros(1040,118,0,24),#0,1(0)
                     carros(30,156,1,24),#2
                     carros(20,194,0,23),carros(660,194,0,23),#3,4(0)
                     carros(40,232,1,22),#5
                     carros(560,270,0,21),carros(1200,270,0,21),#6,7(0)
                     carros(1279,346,1,21),carros(639,346,1,21),#8,9
                     carros(567,384,0,21 ),#10(0)
                     carros(986,422,1,19),carros(350,422,1,19),#11,12
                     carros(123,460,0,16),#13(0)
                     carros(321,498,1,14),carros(800,498,1,14),#14,15
                     carros(90,536,0,13),carros(700,536,0,13)]#16,17(0)
        self.colisao = 0
        px.run(self.update, self.draw)

    def update(self):
        if self.tela == telainicio:
            self.telainicio()
            if px.btnp(px.KEY_SPACE) == 1:
                self.tela = 1
        if self.tela == 1:
            self.updatejogo()
        if self.tela == telaperder:
            self.telaperder()
            if px.btnp(px.KEY_SPACE) == True:
                self.tela = 1
        if self.tela == telaganhar:
            self.telaganhar()
            if px.btnp(px.KEY_SPACE) == True:
                self.tela = 1
        if self.tela == telapause:
            self.telapause()
            if px.btnp(px.KEY_SPACE) == True:
                self.tela = 1

    def updatejogo(self):
        for i in range(len(self.cars)):  
            self.cars[i].mover()
        self.ambiente.criar()
        self.capivara.andar()
        for i in range(len(self.cars)):
            if i == 0 or i==1 or i==3 or i==4 or i==6 or i==7 or i==10 or i==13 or i==16 or i==17:
                if (self.capivara.x + 28) >= self.cars[i].posx  and (self.cars[i].posy == self.capivara.y):
                    if self.cars[i].posx + 75 < self.capivara.x:
                        pass
                    else:  
                        self.capivara.x = 640
                        self.capivara.y = 574
                        self.colisao += 1
            elif i == 2 or i==5 or i==8 or i==9 or i==11 or i==12 or i==14 or i==15:           
                if self.capivara.x <= (self.cars[i].posx + 75) and (self.cars[i].posy == self.capivara.y):
                    if self.cars[i].posx > self.capivara.x + 28:
                        pass
                    else: 
                        self.capivara.x = 640
                        self.capivara.y = 574  
                        self.colisao += 1
        
    def telainicio(self):
        px.fullscreen(True)
        px.rect(0,0,1280,400,12)
        px.rect(0,400,1280,128,11)
        px.rect(0,478,1280,162,4)
        j = 0
        while j < px.width:
            px.blt(j,475,1,94,25,35,13,0)
            px.blt(j,400,1,93,0,36,24,0)
            j += 35
        px.blt(150,360,1,0,0,93,91,0);px.blt(800,370,1,0,174,49,50,0);px.blt(500,322,1,0,91,69,83,0)#arvore
        px.blt(80,340,1,0,91,69,83,0)#arvore
        px.blt(0,300,1,49,176,48,29,0)
        px.blt(200,45,1,49,176,48,29,0)
        px.blt(679,45,1,97,179,65,28,0)
        px.blt(800,157,1,97,179,65,28,0)
        px.blt(409,25,1,97,179,65,28,0)
        px.blt(1200,300,1,97,179,65,28,0)#media
        px.blt(1000,200,1,97,179,65,28,0)
        px.blt(0,19,1,97,179,65,28,0)
        px.blt(300,289,1,49,176,48,29,0)
        px.blt(90,89,1,49,176,48,29,0)
        px.blt(500,200,1,49,176,48,29,0)#pequena
        px.blt(700,278,1,49,176,48,29,0)
        px.blt(400,150,1,61,207,119,56,0)#grande
        px.blt(130,200,1,61,207,119,56,0)#grande
        px.blt(1200,50,1,61,207,119,56,0)#grande
        px.blt(900,10,1,61,207,119,56,0)#grande
        px.blt(1000,323,1,94,56,94,123,0)#arvore grande
        px.blt(250,410,1,94,37,56,19,0)
        px.blt(1200,450,1,94,37,56,19,0)
        px.blt(1100,410,1,94,37,56,19,0)
        px.blt(340,420,1,94,37,56,19,0)
        px.blt(815,430,1,94,37,56,19,0)
        px.blt(247,440,1,94,37,56,19,0)
        px.blt(900,400,1,94,37,56,19,0)
        px.blt(1250,400,1,94,37,56,19,0)
        px.blt(0,400,1,94,37,56,19,0)
        px.blt(120,455,1,94,37,56,19,0)
        px.blt(780,450,1,94,37,56,19,0)
        px.blt(80,430,1,94,37,56,19,0)
        px.blt(1000,450,1,94,37,56,19,0)
        px.blt(500,349,2,0,0,256,256,0)    
        px.text(15,600,'LUIS HENRIQUE K. REICHOW',px.frame_count % 16)
        px.text(15,620,'MATHEUS NUNES BUTTOW',px.frame_count % 16)
        #titulo
        px.blt(424,100,0,75,146,151,32,0)#Capiv
        px.blt(575,100,0,107,146,32,32,0)#A
        px.blt(607,100,0,139,114,32,32,0)#R
        px.blt(639,100,0,107,146,32,32,0)#A
        px.blt(686,100,0,75,146,32,32,0)#C
        px.blt(718,100,0,139,114,32,32,0)#R
        px.blt(750,100,0,171,114,32,32,0)#O
        px.blt(782,100,0,203,114,32,32,0)#S
        px.blt(814,100,0,203,114,32,32,0)#S
        px.blt(484,200,0,75,112,64,16,0)#pres
        px.blt(548,200,0,123,112,16,16,0)#s
        px.blt(574,200,0,123,112,16,16,0)#s
        px.blt(590,200,0,75,112,16,16,0)#p
        px.blt(606,200,0,91,128,16,16,0)#a
        px.blt(622,200,0,107,128,16,16,0)#c
        px.blt(638,200,0,107,112,16,16,0)#e
        px.blt(664,200,0,75,128,16,16,0)#t
        px.blt(680,200,0,123,128,16,16,0)#o
        px.blt(706,200,0,123,112,16,16,0)#s
        px.blt(722,200,0,75,128,16,16,0)#t
        px.blt(738,200,0,91,128,16,16,0)#a
        px.blt(754,200,0,91,112,16,16,0)#r
        px.blt(770,200,0,75,128,16,16,0)#t
        px.blt(513,250,0,75,112,64,16,0)#pres
        px.blt(577,250,0,123,112,16,16,0)#s
        px.blt(603,250,0,107,112,16,16,0)#e
        px.blt(619,250,0,123,112,16,16,0)#s
        px.blt(635,250,0,107,128,16,16,0)#c
        px.blt(661,250,0,75,128,16,16,0)#t
        px.blt(677,250,0,123,128,16,16,0)#o
        px.blt(703,250,0,107,112,16,16,0)#e
        px.blt(719,250,0,226,162,24,16,0)#xi
        px.blt(743,250,0,75,128,16,16,0)#t
        px.blt(1150,580,0,45,0,69,21,0)#credits
        if (px.mouse_x >= 1150 and px.mouse_x <= 1211) and (px.mouse_y <= 601 and px.mouse_y >= 580):
            if px.btnp(px.MOUSE_BUTTON_LEFT) == True:
                webbrowser.open('https://g1.globo.com/rs/rio-grande-do-sul/noticia/2016/09/em-5-anos-mais-de-17-mil-animais-morreram-atropelados-no-taim-no-rs.html')
    
    def draw(self):
        if self.tela == telainicio:
            self.telainicio()
        if self.tela == telaplay:
            self.drawjogo()
        if self.tela == telaperder:
            self.telaperder()
            if px.btnp(px.KEY_SPACE) == True:
                self.colisao = 0
                self.capivara.j = 0
                self.tela = 1
        if self.tela == telaganhar:
            self.telaganhar()
            if px.btnp(px.KEY_SPACE) == True:
                self.colisao = 0
                self.capivara.j = 0
                self.tela = 1
        if self.tela == telapause:
            self.telapause()
            if px.btnp(px.KEY_SPACE) == True:
                self.tela = 1
        if self.colisao >= 5:
            self.tela = 2
        if self.capivara.j == 3:
            self.tela = 3

    def telapause(self):
        px.rect(490,196,300,284,12)#fundo
        px.blt(510,225,1,61,207,119,56,0)#nuvens 
        px.blt(680,250,1,97,179,65,28,0)
        px.blt(650,210,1,49,176,48,29,0)
        h = 510#chão
        while h < 770:#chão
            px.blt(h,423,1,93,0,36,24,0)#chão
            px.blt(h,447,1,94,25,35,13,0)#chão
            h += 35
        px.blt(540,360,1,0,91,69,83,0)#arvore
        px.rect(540,170,200,52,13)#quadradopause
        px.rect(490,186,50,20,13)#bordas
        px.rect(740,186,50,20,13)
        px.rect(490,186,20,284,13)
        px.rect(770,186,20,284,13)
        px.rect(490,460,300,20,13)
        px.line(490,185,490,480,1)#laterais
        px.line(489,185,489,480,1)
        px.line(790,185,790,480,1)
        px.line(789,185,789,480,1)
        px.line(770,205,770,460,1)
        px.line(769,205,769,460,1)
        px.line(510,205,510,460,1)
        px.line(509,205,509,460,1)
        px.line(490,480,790,480,1)
        px.line(489,480,790,480,1)
        px.line(510,460,770,460,1)
        px.line(510,459,770,459,1)
        px.line(510,205,540,205,1);px.line(740,205,770,205,1)
        px.line(510,204,540,204,1);px.line(740,204,770,204,1)
        px.line(510,205,540,205,1);px.line(740,205,770,205,1)
        px.line(510,204,540,204,1);px.line(740,204,770,204,1)
        px.rectb(540,170,200,52,1)
        px.rectb(541,171,198,50,1)
        if (px.mouse_x <= 790 and px.mouse_x >= 490) and (px.mouse_y <= 480 and px.mouse_y >= 196):
            px.mouse(True)
        else:
            px.mouse(False)
        if (px.mouse_x <= 678 and px.mouse_x >= 609) and (px.mouse_y <= 295 and px.mouse_y >= 274):#continue
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                self.tela = 1
        if (px.mouse_x <= 678 and px.mouse_x >= 609) and (px.mouse_y <= 330 and px.mouse_y >= 309):#credits
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                webbrowser.open('https://g1.globo.com/rs/rio-grande-do-sul/noticia/2016/09/em-5-anos-mais-de-17-mil-animais-morreram-atropelados-no-taim-no-rs.html')
        if (px.mouse_x <= 662 and px.mouse_x >= 625) and (px.mouse_y <= 365 and px.mouse_y >= 344):#exit
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                px.quit()       
        px.blt(609,274,0,45,21,69,21,0)#continue
        px.blt(609,309,0,45,0,69,21,0)#credits
        px.blt(625,344,0,207,91,37,21,0)#exit
        #pause(letras):
        px.blt(544,180,0,139,146,32,32,0)#p
        px.blt(576,180,0,107,146,32,32,0)#a
        px.blt(608,180,0,176,0,32,32,0)#u
        px.blt(640,180,0,203,114,32,32,0)#s
        px.blt(672,180,0,144,0,32,32,0)#e
        px.blt(704,180,0,208,0,32,32,0)#d
    
    def telaperder(self):
        px.rect(0,0,1280,640,0)
        px.blt(504,200,0,207,59,32,32,0)#G
        px.blt(536,200,0,107,146,32,32,0)#A
        px.blt(568,200,1,129,0,32,32,0)#M
        px.blt(600,200,0,144,0,32,32,0)#E
        px.blt(647,200,0,171,114,32,32,0)#O
        px.blt(679,200,0,194,146,32,32,0)#V
        px.blt(711,200,0,144,0,32,32,0)#E
        px.blt(743,200,0,139,114,32,32,0)#R
        px.blt(484,313,0,75,112,64,16,0)#pres
        px.blt(548,313,0,123,112,16,16,0)#s
        px.blt(574,313,0,123,112,16,16,0)#s
        px.blt(590,313,0,75,112,16,16,0)#p
        px.blt(606,313,0,91,128,16,16,0)#a
        px.blt(622,313,0,107,128,16,16,0)#c
        px.blt(638,313,0,107,112,16,16,0)#e
        px.blt(664,313,0,75,128,16,16,0)#t
        px.blt(680,313,0,123,128,16,16,0)#o
        px.blt(706,313,0,123,112,16,16,0)#s
        px.blt(722,313,0,75,128,16,16,0)#t
        px.blt(738,313,0,91,128,16,16,0)#a
        px.blt(754,313,0,91,112,16,16,0)#r
        px.blt(770,313,0,75,128,16,16,0)#t
        px.rectb(0,0,1280,640,8)
        px.rectb(1,1,1278,638,8)
        px.blt(513,363,0,75,112,64,16,0)#pres
        px.blt(577,363,0,123,112,16,16,0)#s
        px.blt(603,363,0,107,112,16,16,0)#e
        px.blt(619,363,0,123,112,16,16,0)#s
        px.blt(635,363,0,107,128,16,16,0)#c
        px.blt(661,363,0,75,128,16,16,0)#t
        px.blt(677,363,0,123,128,16,16,0)#o
        px.blt(703,363,0,107,112,16,16,0)#e
        px.blt(719,363,0,226,162,24,16,0)#xi
        px.blt(743,363,0,75,128,16,16,0)#t
        px.blt(579,243,0,207,43,15,16,0)#y
        px.blt(595,243,0,123,128,16,16,0)#o
        px.blt(611,243,0,222,43,16,16,0)#u
        px.blt(637,243,0,238,43,16,16,0)#l
        px.blt(653,243,0,123,128,16,16,0)#o
        px.blt(669,243,0,123,112,16,16,0)#s
        px.blt(685,243,0,107,112,16,16,0)#e
        px.rectb(15,530,95,25,8)
        px.text(20,540,'LUIS HENRIQUE REICHOW',8)
        px.text(20,565,' MATHEUS NUNES BUTTOW',8)
        px.rectb(15,555,95,25,8)
        if (px.mouse_x <= 110 and px.mouse_x >= 15) and (px.mouse_y <= 555 and px.mouse_y >= 530):
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                webbrowser.open('https://www.instagram.com/reichow_henrique/')
        if (px.mouse_x <= 110 and px.mouse_x >= 15) and (px.mouse_y <= 580 and px.mouse_y >= 555):
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                webbrowser.open('https://www.instagram.com/matheusbuttow/')
        n = 5
        for i in range(50):
            px.text(n,620,'YOU LOSE!',8)
            px.text(n,15,'YOU LOSE!',8)
            n += 40
    
    def telaganhar(self):
        px.rect(0,0,1280,640,0)
        px.blt(484,233,0,75,112,64,16,0)#pres
        px.blt(548,233,0,123,112,16,16,0)#s
        px.blt(574,233,0,123,112,16,16,0)#s
        px.blt(590,233,0,75,112,16,16,0)#p
        px.blt(606,233,0,91,128,16,16,0)#a
        px.blt(622,233,0,107,128,16,16,0)#c
        px.blt(638,233,0,107,112,16,16,0)#e
        px.blt(664,233,0,75,128,16,16,0)#t
        px.blt(680,233,0,123,128,16,16,0)#o
        px.blt(706,233,0,123,112,16,16,0)#s
        px.blt(722,233,0,75,128,16,16,0)#t
        px.blt(738,233,0,91,128,16,16,0)#a
        px.blt(754,233,0,91,112,16,16,0)#r
        px.blt(770,233,0,75,128,16,16,0)#t
        px.rectb(0,0,1280,640,10)#contorno
        px.rectb(1,1,1278,638,10)#contorno
        px.blt(513,283,0,75,112,64,16,0)#pres
        px.blt(577,283,0,123,112,16,16,0)#s
        px.blt(603,283,0,107,112,16,16,0)#e
        px.blt(619,283,0,123,112,16,16,0)#s
        px.blt(635,283,0,107,128,16,16,0)#c
        px.blt(661,283,0,75,128,16,16,0)#t
        px.blt(677,283,0,123,128,16,16,0)#o
        px.blt(703,283,0,107,112,16,16,0)#e
        px.blt(719,283,0,226,162,24,16,0)#xi
        px.blt(743,283,0,75,128,16,16,0)#t
        px.blt(536,140,1,197,0,29,32,0)#Y
        px.blt(565,140,0,171,114,32,32,0)#O
        px.blt(597,140,0,176,0,32,32,0)#U
        px.blt(644,140,1,187,32,41,32,0)#W
        px.blt(685,140,0,171,146,23,32,0)#I
        px.blt(708,140,1,161,0,36,32,0)#N
        px.blt(606,400,1,189,65,67,61,0)#trofeu
        px.blt(621,368,1,189,150,38,27,0)#coroa
        px.text(530,430,'CLICK HERE >>>',10)
        px.text(692,430,'<<< CLICK HERE',10)
        px.rectb(15,530,95,25,10)
        px.text(20,540,'LUIS HENRIQUE REICHOW',10)
        px.text(20,565,' MATHEUS NUNES BUTTOW',10)
        px.rectb(15,555,95,25,10)
        if (px.mouse_x <= 110 and px.mouse_x >= 15) and (px.mouse_y <= 555 and px.mouse_y >= 530):
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                webbrowser.open('https://www.instagram.com/reichow_henrique/')
        if (px.mouse_x <= 110 and px.mouse_x >= 15) and (px.mouse_y <= 580 and px.mouse_y >= 555):
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                webbrowser.open('https://www.instagram.com/matheusbuttow/')
        #px.line()
        m = 5
        for i in range(50):
            px.text(m,620,'YOU WIN!',10)
            px.text(m,15,'YOU WIN!',10)
            m += 40
        for i in range(1):
            px.blt(random.uniform(0,1280),random.uniform(0,600),1,189,126,23,23,0)
            for i in range(5):
                px.blt(random.uniform(0,1280),random.uniform(0,600),1,213,126,5,5,0)
        if (px.mouse_x <= 673 and px.mouse_x >= 606) and (px.mouse_y <= 461 and px.mouse_y >= 400):
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                webbrowser.open('https://www.youtube.com/shorts/6seQQTJLDNo')
    
    def drawjogo(self):
        px.cls(0)
        for i in range(len(self.cars)):
            self.cars[i].draw()
        self.ambiente.draw()
        self.capivara.desenho()
        px.blt(1203,613,0,235,125,17,16,0)#capi
        px.blt(1166,613,0,235,125,17,16,0)#capi
        px.blt(1129,613,0,235,125,17,16,0)#capi
        if self.capivara.j == 1 or self.capivara.j == 2 or self.capivara.j == 3:
            px.blt(1129,613,0,28,23,17,16,0)#capiouro
        if self.capivara.j == 2 or self.capivara.j == 3:
            px.blt(1166,613,0,28,23,17,16,0)#capiouro
        if self.capivara.j == 3:
            px.blt(1203,613,0,28,23,17,16,0)#capiouro
        px.blt(60,613,0,114,0,14,14,0)#coração
        px.blt(94,613,0,114,0,14,14,0)#coração
        px.blt(128,613,0,114,0,14,14,0)#coração
        if self.colisao == 1 or self.colisao == 2 or self.colisao == 3:
            px.blt(60,613,0,114,14,14,14,0)#coraçãov
        if self.colisao == 2 or self.colisao == 3:
            px.blt(94,613,0,114,14,14,14,0)#coraçãov
        if self.colisao == 3 :
            px.blt(128,613,0,114,14,14,14,0)#coraçãov
        if self.colisao >= 3:
            self.tela = 2
        if self.capivara.j == 3:
            self.tela = 3
        px.blt(1075,611,0,234,141,21,21,0)#pause
        if (px.mouse_x <= 1093 and px.mouse_x >= 1075) and (px.mouse_y <= 632 and px.mouse_y >= 611):
            if px.btnp(px.MOUSE_BUTTON_LEFT):
                self.tela = 4

jogo()