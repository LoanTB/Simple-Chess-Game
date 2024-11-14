import pygame,random,os

pygame.init()
timer = pygame.time.Clock()

resolution = (700,700)
screen = pygame.display.set_mode(resolution)

imgRepo = []
for (repertoire, sousRepertoires, fichiers) in os.walk("images"):
    imgRepo.extend(fichiers)

img = {}
for i in imgRepo:
    img[i[0:-4]] = [None,None]
    img[i[0:-4]][0] = pygame.image.load("images/"+i)
    img[i[0:-4]][1] = img[i[0:-4]][0].get_rect()
    img[i[0:-4]][0] = pygame.transform.scale(img[i[0:-4]][0],(int(img[i[0:-4]][1][2]*(resolution[0]/9)/img[i[0:-4]][1][3]),int(img[i[0:-4]][1][3]*(resolution[0]/9)/img[i[0:-4]][1][3])))
    img[i[0:-4]][1] = img[i[0:-4]][0].get_rect()

map = []
for x in range(8):
    map.append([])
    for y in range(8):
        if y == 1:
            map[x].append([-1,1])
        elif y == 6:
            map[x].append([1,1])
        elif y == 0 and (x == 0 or x == 7):
            map[x].append([-1,5])
        elif y == 7 and (x == 0 or x == 7):
            map[x].append([1,5])
        elif y == 0 and (x == 1 or x == 6):
            map[x].append([-1,3])
        elif y == 7 and (x == 1 or x == 6):
            map[x].append([1,3])
        elif y == 0 and (x == 2 or x == 5):
            map[x].append([-1,4])
        elif y == 7 and (x == 2 or x == 5):
            map[x].append([1,4])
        elif y == 0 and x == 3:
            map[x].append([-1,9])
        elif y == 7 and x == 3:
            map[x].append([1,9])
        elif y == 0 and x == 4:
            map[x].append([-1,10])
        elif y == 7 and x == 4:
            map[x].append([1,10])
        else:
            map[x].append([0,0])

# Return 0 si y'a rien, return 1 si c'est dehors
# Return 3 si c'est un but contre son camp,
# Return 2 si c'est l'heure de manger
def busy(x,y,t):
    global map
    if x > 7 or x < 0 or y > 7 or y < 0:
        return 1
    if map[x][y][0] == 0:
        return 0
    elif map[x][y][0] == t:
        return 3
    elif map[x][y][0] == t*-1:
        return 2
    else:
        print("Comprend pas là")

team = {"White":-1,"Black":1}
selected = [-1,-1]
clic = False
possible = []

while True:
    timer.tick(20)
    screen.fill([0,0,0])
    flip = 1
    for x in range(8):
        for y in range(8):
            if flip == 1:
                pygame.draw.rect(screen, [50,50,50], [(x/8)*resolution[0],(y/8)*resolution[1],resolution[0]/8,resolution[1]/8])
            else:
                pygame.draw.rect(screen, [200,200,200], [(x/8)*resolution[0],(y/8)*resolution[1],resolution[0]/8,resolution[1]/8])
            if y < 7:
                flip *= -1
            piece = ""
            if map[x][y][1] == 1:
                piece = "Pion"
            elif map[x][y][1] == 3:
                piece = "Cavalier"
            elif map[x][y][1] == 4:
                piece = "Fou"
            elif map[x][y][1] == 5:
                piece = "Tour"
            elif map[x][y][1] == 9:
                piece = "Dame"
            elif map[x][y][1] == 10:
                piece = "Roi"
            if piece != "":
                if map[x][y][0] == -1:
                    screen.blit(img["Blanc-"+piece][0], [((x/8)*resolution[0])+(resolution[0]/8)/2-img["Blanc-"+piece][1][2]/2,((y/8)*resolution[1])+(resolution[1]/8)/2-img["Blanc-"+piece][1][3]/2])
                    if selected == [x,y] and possible == []:#Ou changement de tour
                        if piece == "Pion":
                            if y == 1:
                                if busy(x,y+2,map[x][y][0]) == 0:
                                    possible.append([x,y+2])
                            for i in [[x,y+1]]:
                                if busy(i[0],i[1],map[x][y][0]) == 0:
                                    possible.append(i)
                            for i in [[x+1,y+1],[x-1,y+1]]:
                                if busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Cavalier":
                            for i in [[x+1,y-2],[x+2,y-1],[x+2,y+1],[x+1,y+2],[x-1,y+2],[x-2,y+1],[x-2,y-1]]:
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Fou":
                            ListePos = []
                            for a in range(-1,2,2):
                                for b in range(-1,2,2):
                                    PosSearch = [x+a,y+b]
                                    while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                                        PosSearch[0] += a
                                        PosSearch[1] += b
                                    if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Tour":
                            ListePos = []
                            for a in range(-1,2,2):
                                PosSearch = [x+a,y]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[0] += a
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for b in range(-1,2,2):
                                PosSearch = [x,y+b]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[1] += b
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Dame":
                            ListePos = []
                            for a in range(-1,2,2):
                                for b in range(-1,2,2):
                                    PosSearch = [x+a,y+b]
                                    while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                                        PosSearch[0] += a
                                        PosSearch[1] += b
                                    if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                            for a in range(-1,2,2):
                                PosSearch = [x+a,y]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[0] += a
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for b in range(-1,2,2):
                                PosSearch = [x,y+b]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[1] += b
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Roi":
                            ListePos = []
                            for a in range(-1,2,2):
                                for b in range(-1,2,2):
                                    PosSearch = [x+a,y+b]
                                    if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0 or busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                            for a in range(-1,2,2):
                                PosSearch = [x+a,y]
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0 or busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for b in range(-1,2,2):
                                PosSearch = [x,y+b]
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0 or busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                else:
                    screen.blit(img["Noir-"+piece][0], [((x/8)*resolution[0])+(resolution[0]/8)/2-img["Noir-"+piece][1][2]/2,((y/8)*resolution[1])+(resolution[1]/8)/2-img["Noir-"+piece][1][3]/2])
                    if selected == [x,y] and possible == []:#Ou changement de tour
                        if piece == "Pion":
                            if y == 6:
                                if busy(x,y-2,map[x][y][0]) == 0:
                                    possible.append([x,y-2])
                            for i in [[x,y-1]]:
                                if busy(i[0],i[1],map[x][y][0]) == 0:
                                    possible.append(i)
                            for i in [[x+1,y-1],[x-1,y-1]]:
                                if busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Cavalier":
                            for i in [[x+1,y-2],[x+2,y-1],[x+2,y+1],[x+1,y+2],[x-1,y+2],[x-2,y+1],[x-2,y-1]]:
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Fou":
                            ListePos = []
                            for a in range(-1,2,2):
                                for b in range(-1,2,2):
                                    PosSearch = [x+a,y+b]
                                    while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                                        PosSearch[0] += a
                                        PosSearch[1] += b
                                    if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Tour":
                            ListePos = []
                            for a in range(-1,2,2):
                                PosSearch = [x+a,y]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[0] += a
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for b in range(-1,2,2):
                                PosSearch = [x,y+b]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[1] += b
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Dame":
                            ListePos = []
                            for a in range(-1,2,2):
                                for b in range(-1,2,2):
                                    PosSearch = [x+a,y+b]
                                    while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                                        PosSearch[0] += a
                                        PosSearch[1] += b
                                    if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                            for a in range(-1,2,2):
                                PosSearch = [x+a,y]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[0] += a
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for b in range(-1,2,2):
                                PosSearch = [x,y+b]
                                while busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                                    PosSearch[1] += b
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)
                        if piece == "Roi":
                            ListePos = []
                            for a in range(-1,2,2):
                                for b in range(-1,2,2):
                                    PosSearch = [x+a,y+b]
                                    if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0 or busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                        ListePos.append([PosSearch[0],PosSearch[1]])
                            for a in range(-1,2,2):
                                PosSearch = [x+a,y]
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0 or busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for b in range(-1,2,2):
                                PosSearch = [x,y+b]
                                if busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 0 or busy(PosSearch[0],PosSearch[1],map[x][y][0]) == 2:
                                    ListePos.append([PosSearch[0],PosSearch[1]])
                            for i in ListePos: #Checkup
                                if busy(i[0],i[1],map[x][y][0]) == 0 or busy(i[0],i[1],map[x][y][0]) == 2:
                                    possible.append(i)

    for i in possible:
        pygame.draw.circle(screen,[100,100,100],[(i[0]/8)*resolution[0]+(resolution[0]/8)/2,(i[1]/8)*resolution[1]+(resolution[1]/8)/2],(resolution[0]/8)/4)
        pygame.draw.circle(screen,[20,20,20],[(i[0]/8)*resolution[0]+(resolution[0]/8)/2,(i[1]/8)*resolution[1]+(resolution[1]/8)/2],(resolution[0]/8)/6)


    if clic:
        if selected == [-1,-1]:
            mouse = pygame.mouse.get_pos()
            selected = [int(mouse[0]/resolution[0]*8),int(mouse[1]/resolution[1]*8)]
        else:
            mouse = pygame.mouse.get_pos()
            if [int(mouse[0]/resolution[0]*8),int(mouse[1]/resolution[1]*8)] in possible:
                save = [map[selected[0]][selected[1]][0],map[selected[0]][selected[1]][1]]
                map[selected[0]][selected[1]] = [0,0]
                selected = [int(mouse[0]/resolution[0]*8),int(mouse[1]/resolution[1]*8)]
                map[selected[0]][selected[1]] = [save[0],save[1]]
                selected = [-1,-1]
                possible = []
            else:
                selected = [-1,-1]
                possible = []


    pygame.display.update()
    clic = False
    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clic = True
        """if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clic = False"""
