import pygame
import math

#using the distance method
def distFromPoints(point1, point2):
    distance = math.sqrt( ((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2) )
    
    return distance

def main():
    """ Set up the game and run the main game loop """
    pygame.init()

    # Created surface of (width, height), and its window.
    surfaceWidth = 1280 
    surfaceHeight = 720
    mainSurface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
    gameState = "start"
    
    #Font data
    font = pygame.font.SysFont("Arial", 40)
    font2 = pygame.font.SysFont("Algerian", 75)

    #Circle data
    circleColor = "red"
    circlePos = [50,50]
    circle2Pos = [1085,600]
    circleSize = 20
    circleRadius = circleSize/2
    circle2Size = 30
    circle2Radius = circle2Size/2
    circleSpeed = 1

    #Controlling movement of the circle
    moveCircleRight = False 
    moveCircleUp = False
    moveCircleDown = False
    moveCircleLeft = False

    #Defining various rectangles
    rect0D = [475,500,280,100]
    
    rectlvl1D = [450,300,280,100]
    rectlvl2D = [450,500,280,100]
    
    rect1D = [250,-1,20,500]
    rect2D = [250,600,20,121]
    rect3D = [400,100,20,650]
    rect4D = [550,-1,20,350]
    rect5D = [550,450,20,321]
    rect6D = [700,-1,150,20]
    rect7D = [850,-1,20,150]
    rect8D = [700,149,170,20]
    rect9D = [700,298,170,20]
    rect10D = [700,298,20,150]
    rect11D = [550,447,170,20]
    rect12D = [700,596,170,20]
    rect13D = [850,447,20,150]
    rect14D = [1150,298,170,20]
    rect15Da = [850,447,300,20]
    rect15Db = [850,447,175,20]
    rect16D = [1000,100,20,250]
    rect17D = [1150,150,20,465]
    
    rectFD = [1180,620,100,100]
    
    rectNextD = [490,540,225,65]
    rectRetryD = [525,500,210,50]
    

    """Note:
        Gamestates included: 'start', 'game_levels', 'game_level1', 'game_level2', 'win1', 'win', 'lose'"""


    #The actual loop
    while True:
        ev = pygame.event.poll()   
        if ev.type == pygame.QUIT:  
            break
        
        #Start screen with 2 buttons
        if gameState == "start":
            mainSurface.fill("gray")
            pygame.draw.rect(mainSurface, "firebrick", rect0D)
            text1 = "MAZE.INC"
            text2 = "START"
            renderedText1 = font2.render(text1, 1, pygame.Color("maroon"))
            renderedText2 = font.render(text2, 1, pygame.Color("navy"))
            mainSurface.blit(renderedText1, (500,150))
            mainSurface.blit(renderedText2, (550,525))
            
            if ev.type == pygame.MOUSEBUTTONUP:
                if rect0D[0] < pygame.mouse.get_pos()[0] < (rect0D[0] + rect0D[2])\
                   and rect0D[1] < pygame.mouse.get_pos()[1] < (rect0D[1] + rect0D[3]):
                    gameState = "game_levels"

        #Game levels screen taking you to either level 1 or 2
        elif gameState == "game_levels":
            mainSurface.fill("cyan")
            pygame.draw.rect(mainSurface, "maroon", rectlvl1D)
            pygame.draw.rect(mainSurface, "maroon", rectlvl2D)
            textlvl1 = "LEVEL 1"
            textlvl2 = "LEVEL 2"
            renderedtextlvl1 = font.render(textlvl1, 1, pygame.Color("black"))
            renderedtextlvl2 = font.render(textlvl2, 1, pygame.Color("black"))
            mainSurface.blit(renderedtextlvl1, (510,325))
            mainSurface.blit(renderedtextlvl2, (510,525))
            
            if ev.type == pygame.MOUSEBUTTONUP:
                if rectlvl1D[0] < pygame.mouse.get_pos()[0] < (rectlvl1D[0] + rectlvl1D[2])\
                   and rectlvl1D[1] < pygame.mouse.get_pos()[1] < (rectlvl1D[1] + rectlvl1D[3]):
                    gameState = "game_level1"
                
                if rectlvl2D[0] < pygame.mouse.get_pos()[0] < (rectlvl2D[0] + rectlvl2D[2])\
                   and rectlvl2D[1] < pygame.mouse.get_pos()[1] < (rectlvl2D[1] + rectlvl2D[3]):
                    gameState = "game_level2"

        #After winning level 1, this WIN screen allows you to move to the next level        
        elif gameState == "win1":
            mainSurface.fill("darkgreen")
            textWin = "YOU WIN"
            textNext = "Next Level"
            renderedtextWin = font2.render(textWin, 1, pygame.Color("lightpink"))
            renderedtextNext = font.render(textNext, 1, pygame.Color("black"))
            pygame.draw.rect(mainSurface, "gray", rectNextD)
            mainSurface.blit(renderedtextWin, (490, 310))
            mainSurface.blit(renderedtextNext, (510, 550))
            if ev.type == pygame.MOUSEBUTTONUP:
                if rectNextD[0] < pygame.mouse.get_pos()[0] < (rectNextD[0] + rectNextD[2])\
                   and rectNextD[1] < pygame.mouse.get_pos()[1] < (rectNextD[1] + rectNextD[3]):
                    circlePos = [50,50]
                    moveCircleRight = False 
                    moveCircleUp = False
                    moveCircleDown = False
                    moveCircleLeft = False
                    gameState = "game_level2"

        #This is basically a WIN screen without any buttons
        elif gameState == "win":
            mainSurface.fill("darkgreen")
            textWin = "YOU WIN"
            renderedtextWin = font2.render(textWin, 1, pygame.Color("lightpink"))
            mainSurface.blit(renderedtextWin, (490, 310))

        #A LOSE screen designed to have a retry button
        elif gameState == "lose":
            mainSurface.fill("black")
            textLose = "YOU LOSE"
            textRetry = "Retry"
            renderedtextLose = font2.render(textLose, 1, pygame.Color("red"))
            renderedtextRetry = font.render(textRetry, 1, pygame.Color("black"))
            pygame.draw.rect(mainSurface, "gray", rectRetryD)
            mainSurface.blit(renderedtextLose, (500, 250))
            mainSurface.blit(renderedtextRetry, (585,500))
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if rectRetryD[0] < pygame.mouse.get_pos()[0] < (rectRetryD[0] + rectRetryD[2])\
                   and rectRetryD[1] < pygame.mouse.get_pos()[1] < (rectRetryD[1] + rectRetryD[3]):
                    circlePos = [50,50]
                    moveCircleRight = False
                    moveCircleUp = False
                    moveCircleDown = False
                    moveCircleLeft = False
                    gameState = "game_level2"
        
        #Level 1
        elif gameState == "game_level1":
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    moveCircleRight = True
                elif ev.key == pygame.K_UP:
                    moveCircleUp = True
                elif ev.key == pygame.K_LEFT:
                    moveCircleLeft = True
                elif ev.key == pygame.K_DOWN:
                    moveCircleDown = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_RIGHT:
                    moveCircleRight = False
                elif ev.key == pygame.K_UP:
                    moveCircleUp = False
                elif ev.key == pygame.K_LEFT:
                    moveCircleLeft = False
                elif ev.key == pygame.K_DOWN:
                    moveCircleDown = False
            
            #Changing colors of the ball based on the key pressed
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_b:
                    circleColor = "black"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_y:
                    circleColor = "yellow"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_o:
                    circleColor = "orange"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_g:
                    circleColor = "green"

            #Moving the circle
            if moveCircleRight:
                circlePos[0] += 0.6
            elif moveCircleUp:
                circlePos[1] -= 0.6
            elif moveCircleDown:
                circlePos[1] += 0.6
            elif moveCircleLeft:
                circlePos[0] -= 0.6
            
            if circlePos[0] > surfaceWidth:
                circlePos[0] = surfaceWidth
            elif circlePos[0] < 0:
                circlePos[0] = 0
            elif circlePos[1] < 0:
                circlePos[1] = 0
            elif circlePos[1] > surfaceHeight:
                circlePos[1] = surfaceHeight
        
        #rect1(top)
            if rect1D[0] < (circlePos[0] + circleRadius) < (rect1D[0] + rect1D[2])\
               and rect1D[1] < circlePos[1] < (rect1D[1] + rect1D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0] - circleRadius
        
            if rect1D[0] < (circlePos[0] - circleRadius) < (rect1D[0] + rect1D[2])\
               and rect1D[1] < circlePos[1] < (rect1D[1] + rect1D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2] + circleRadius
            
            if rect1D[0] < circlePos[0] < (rect1D[0] + rect1D[2])\
               and rect1D[1] < (circlePos[1] - circleRadius) < (rect1D[1] + rect1D[3]) and moveCircleUp:
                circlePos[1] = rect1D[1] + rect1D[3] + circleRadius
        
        #rect2(bottom)
            if rect1D[0] < (circlePos[0] + circleRadius) < (rect1D[0] + rect2D[2])\
               and rect2D[1] < circlePos[1] < (rect2D[1] + rect2D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0] - circleRadius
            
            if rect1D[0] < (circlePos[0] - circleRadius) < (rect1D[0] + rect2D[2])\
               and rect2D[1] < circlePos[1] < (rect2D[1] + rect2D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2] + circleRadius
            
            if rect1D[0] < circlePos[0] < (rect1D[0] + rect2D[2])\
               and rect2D[1] < (circlePos[1] + circleRadius) < (rect2D[1] + rect2D[3]) and moveCircleDown:
                circlePos[1] = rect2D[1] - circleRadius
        
        #rect3(bottom)
            if rect3D[0] < (circlePos[0] + circleRadius) < (rect3D[0] + rect3D[2])\
               and rect3D[1] < circlePos[1] < (rect3D[1] + rect3D[3]) and moveCircleRight:
                circlePos[0] = rect3D[0] - circleRadius
            
            if rect3D[0] < (circlePos[0] - circleRadius) < (rect3D[0] + rect3D[2])\
               and rect3D[1] < circlePos[1] < (rect3D[1] + rect3D[3]) and moveCircleLeft:
                circlePos[0] = rect3D[0] + rect1D[2] + circleRadius
        
            if rect3D[0] < circlePos[0] < (rect3D[0] + rect3D[2])\
               and rect3D[1] < (circlePos[1] + circleRadius) < (rect3D[1] + rect3D[3]) and moveCircleDown:
                circlePos[1] = rect3D[1] - circleRadius
            
        #rect4(top)    
            if rect4D[0] < (circlePos[0] + circleRadius) < (rect4D[0] + rect4D[2])\
               and rect4D[1] < circlePos[1] < (rect4D[1] + rect4D[3]) and moveCircleRight:
                circlePos[0] = rect4D[0] - circleRadius
            
            if rect4D[0] < (circlePos[0] - circleRadius) < (rect4D[0] + rect4D[2])\
               and rect4D[1] < circlePos[1] < (rect4D[1] + rect4D[3]) and moveCircleLeft:
                circlePos[0] = rect4D[0] + rect4D[2] + circleRadius

            if rect4D[0] < circlePos[0] < (rect4D[0] + rect4D[2])\
               and rect4D[1] < (circlePos[1] - circleRadius) < (rect4D[1] + rect4D[3]) and moveCircleUp:
                circlePos[1] = rect4D[1] + rect4D[3] + circleRadius
        
        #rect5(bottom)
            if rect5D[0] < (circlePos[0] + circleRadius) < (rect5D[0] + rect5D[2])\
               and rect5D[1] < circlePos[1] < (rect5D[1] + rect5D[3]) and moveCircleRight:
                circlePos[0] = rect5D[0] - circleRadius
        
            if rect5D[0] < (circlePos[0] - circleRadius) < (rect5D[0] + rect5D[2])\
               and rect5D[1] < circlePos[1] < (rect5D[1] + rect5D[3]) and moveCircleLeft:
                circlePos[0] = rect5D[0] + rect5D[2] + circleRadius
            
            if rect5D[0] < circlePos[0] < (rect5D[0] + rect5D[2])\
               and rect5D[1] < (circlePos[1] + circleRadius) < (rect5D[1] + rect5D[3]) and moveCircleDown:
                circlePos[1] = rect5D[1] - circleRadius
                
        #rect6(top)
            if rect6D[0] < (circlePos[0] + circleRadius) < (rect6D[0] + rect6D[2])\
               and rect6D[1] < circlePos[1] < (rect6D[1] + rect6D[3]) and moveCircleRight:
                circlePos[0] = rect6D[0] - circleRadius
                
            if rect6D[0] < (circlePos[0] - circleRadius) < (rect6D[0] + rect6D[2])\
               and rect6D[1] < circlePos[1] < (rect6D[1] + rect6D[3]) and moveCircleLeft:
                circlePos[0] = rect6D[0] + rect6D[2] + circleRadius
                
            if rect6D[0] < circlePos[0] < (rect6D[0] + rect6D[2])\
               and rect6D[1] < (circlePos[1] - circleRadius) < (rect6D[1] + rect6D[3]) and moveCircleUp:
                circlePos[1] = rect6D[1] + rect6D[3] + circleRadius
        #rect7(top)
            if rect7D[0] < (circlePos[0] + circleRadius) < (rect7D[0] + rect7D[2])\
               and rect7D[1] < circlePos[1] < (rect7D[1] + rect7D[3]) and moveCircleRight:
                circlePos[0] = rect7D[0] - circleRadius
                
            if rect7D[0] < (circlePos[0] - circleRadius) < (rect7D[0] + rect7D[2])\
               and rect7D[1] < circlePos[1] < (rect7D[1] + rect7D[3]) and moveCircleLeft:
                circlePos[0] = rect7D[0] + rect7D[2] + circleRadius
                
            if rect7D[0] < circlePos[0] < (rect7D[0] + rect7D[2])\
               and rect7D[1] < (circlePos[1] - circleRadius) < (rect7D[1] + rect7D[3]) and moveCircleUp:
                circlePos[1] = rect7D[1] + rect7D[3] + circleRadius
        
        #rect8(top)
            if rect8D[0] < (circlePos[0] + circleRadius) < (rect8D[0] + rect8D[2])\
               and rect8D[1] < circlePos[1] < (rect8D[1] + rect8D[3]) and moveCircleRight:
                circlePos[0] = rect8D[0] - circleRadius
                
            if rect8D[0] < (circlePos[0] - circleRadius) < (rect8D[0] + rect8D[2])\
               and rect8D[1] < circlePos[1] < (rect8D[1] + rect8D[3]) and moveCircleLeft:
                circlePos[0] = rect8D[0] + rect8D[2] + circleRadius
                
            if rect8D[0] < circlePos[0] < (rect8D[0] + rect8D[2])\
               and rect8D[1] < (circlePos[1] - circleRadius) < (rect8D[1] + rect8D[3]) and moveCircleUp:
                circlePos[1] = rect8D[1] + rect8D[3] + circleRadius
                
            if rect8D[0] < circlePos[0] < (rect8D[0] + rect8D[2])\
               and rect8D[1] < (circlePos[1] + circleRadius) < (rect8D[1] + rect8D[3]) and moveCircleDown:
                circlePos[1] = rect8D[1] - circleRadius
                
        #rect9(middle)
            if rect9D[0] < (circlePos[0] + circleRadius) < (rect9D[0] + rect9D[2])\
               and rect9D[1] < circlePos[1] < (rect9D[1] + rect9D[3]) and moveCircleRight:
                circlePos[0] = rect9D[0] - circleRadius
            
            if rect9D[0] < (circlePos[0] - circleRadius) < (rect9D[0] + rect9D[2])\
               and rect9D[1] < circlePos[1] < (rect9D[1] + rect9D[3]) and moveCircleLeft:
                circlePos[0] = rect9D[0] + rect9D[2] + circleRadius
                
            if rect9D[0] < circlePos[0] < (rect9D[0] + rect9D[2])\
               and rect9D[1] < (circlePos[1] - circleRadius) < (rect9D[1] + rect9D[3]) and moveCircleUp:
                circlePos[1] = rect9D[1] + rect9D[3] + circleRadius
                
            if rect9D[0] < circlePos[0] < (rect9D[0] + rect9D[2])\
               and rect9D[1] < (circlePos[1] + circleRadius) < (rect9D[1] + rect9D[3]) and moveCircleDown:
                circlePos[1] = rect9D[1] - circleRadius
                
        #rect10(middle)
            if rect10D[0] < (circlePos[0] + circleRadius) < (rect10D[0] + rect10D[2])\
               and rect10D[1] < circlePos[1] < (rect10D[1] + rect10D[3]) and moveCircleRight:
                circlePos[0] = rect10D[0] - circleRadius
            
            if rect10D[0] < (circlePos[0] - circleRadius) < (rect10D[0] + rect10D[2])\
               and rect10D[1] < circlePos[1] < (rect10D[1] + rect10D[3]) and moveCircleLeft:
                circlePos[0] = rect10D[0] + rect10D[2] + circleRadius
                
            if rect10D[0] < circlePos[0] < (rect10D[0] + rect10D[2])\
               and rect10D[1] < (circlePos[1] - circleRadius) < (rect10D[1] + rect10D[3]) and moveCircleUp:
                circlePos[1] = rect10D[1] + rect10D[3] + circleRadius
                
            if rect10D[0] < circlePos[0] < (rect10D[0] + rect10D[2])\
               and rect10D[1] < (circlePos[1] + circleRadius) < (rect10D[1] + rect10D[3]) and moveCircleDown:
                circlePos[1] = rect10D[1] - circleRadius
                
        #rect11
            if rect11D[0] < (circlePos[0] + circleRadius) < (rect11D[0] + rect11D[2])\
               and rect11D[1] < circlePos[1] < (rect11D[1] + rect11D[3]) and moveCircleRight:
                circlePos[0] = rect11D[0] - circleRadius
            
            if rect11D[0] < (circlePos[0] - circleRadius) < (rect11D[0] + rect11D[2])\
               and rect11D[1] < circlePos[1] < (rect11D[1] + rect11D[3]) and moveCircleLeft:
                circlePos[0] = rect11D[0] + rect11D[2] + circleRadius
                
            if rect11D[0] < circlePos[0] < (rect11D[0] + rect11D[2])\
               and rect11D[1] < (circlePos[1] - circleRadius) < (rect11D[1] + rect11D[3]) and moveCircleUp:
                circlePos[1] = rect11D[1] + rect11D[3] + circleRadius
                
            if rect11D[0] < circlePos[0] < (rect11D[0] + rect11D[2])\
               and rect11D[1] < (circlePos[1] + circleRadius) < (rect11D[1] + rect11D[3]) and moveCircleDown:
                circlePos[1] = rect11D[1] - circleRadius
        
        #rect12
            if rect12D[0] < (circlePos[0] + circleRadius) < (rect12D[0] + rect12D[2])\
               and rect12D[1] < circlePos[1] < (rect12D[1] + rect12D[3]) and moveCircleRight:
                circlePos[0] = rect12D[0] - circleRadius
            
            if rect12D[0] < (circlePos[0] - circleRadius) < (rect12D[0] + rect12D[2])\
               and rect12D[1] < circlePos[1] < (rect12D[1] + rect12D[3]) and moveCircleLeft:
                circlePos[0] = rect12D[0] + rect12D[2] + circleRadius
                
            if rect12D[0] < circlePos[0] < (rect12D[0] + rect12D[2])\
               and rect12D[1] < (circlePos[1] - circleRadius) < (rect12D[1] + rect12D[3]) and moveCircleUp:
                circlePos[1] = rect12D[1] + rect12D[3] + circleRadius
                
            if rect12D[0] < circlePos[0] < (rect12D[0] + rect12D[2])\
               and rect12D[1] < (circlePos[1] + circleRadius) < (rect12D[1] + rect12D[3]) and moveCircleDown:
                circlePos[1] = rect12D[1] - circleRadius
                
        #rect13
            if rect13D[0] < (circlePos[0] + circleRadius) < (rect13D[0] + rect13D[2])\
               and rect13D[1] < circlePos[1] < (rect13D[1] + rect13D[3]) and moveCircleRight:
                circlePos[0] = rect13D[0] - circleRadius
            
            if rect13D[0] < (circlePos[0] - circleRadius) < (rect13D[0] + rect13D[2])\
               and rect13D[1] < circlePos[1] < (rect13D[1] + rect13D[3]) and moveCircleLeft:
                circlePos[0] = rect13D[0] + rect13D[2] + circleRadius
                
            if rect13D[0] < circlePos[0] < (rect13D[0] + rect13D[2])\
               and rect13D[1] < (circlePos[1] - circleRadius) < (rect13D[1] + rect13D[3]) and moveCircleUp:
                circlePos[1] = rect13D[1] + rect13D[3] + circleRadius
                
            if rect13D[0] < circlePos[0] < (rect13D[0] + rect13D[2])\
               and rect13D[1] < (circlePos[1] + circleRadius) < (rect13D[1] + rect13D[3]) and moveCircleDown:
                circlePos[1] = rect13D[1] - circleRadius
        
        #rect14
            if rect14D[0] < (circlePos[0] + circleRadius) < (rect14D[0] + rect14D[2])\
               and rect14D[1] < circlePos[1] < (rect14D[1] + rect14D[3]) and moveCircleRight:
                circlePos[0] = rect14D[0] - circleRadius
            
            if rect14D[0] < (circlePos[0] - circleRadius) < (rect14D[0] + rect14D[2])\
               and rect14D[1] < circlePos[1] < (rect14D[1] + rect14D[3]) and moveCircleLeft:
                circlePos[0] = rect14D[0] + rect14D[2] + circleRadius
                
            if rect14D[0] < circlePos[0] < (rect14D[0] + rect14D[2])\
               and rect14D[1] < (circlePos[1] - circleRadius) < (rect14D[1] + rect14D[3]) and moveCircleUp:
                circlePos[1] = rect14D[1] + rect14D[3] + circleRadius
                
            if rect14D[0] < circlePos[0] < (rect14D[0] + rect14D[2])\
               and rect14D[1] < (circlePos[1] + circleRadius) < (rect14D[1] + rect14D[3]) and moveCircleDown:
                circlePos[1] = rect14D[1] - circleRadius
        
        #rect15
            if rect15Da[0] < (circlePos[0] + circleRadius) < (rect15Da[0] + rect15Da[2])\
               and rect15Da[1] < circlePos[1] < (rect15Da[1] + rect15Da[3]) and moveCircleRight:
                circlePos[0] = rect15Da[0] - circleRadius
            
            if rect15Da[0] < (circlePos[0] - circleRadius) < (rect15Da[0] + rect15Da[2])\
               and rect15Da[1] < circlePos[1] < (rect15Da[1] + rect15Da[3]) and moveCircleLeft:
                circlePos[0] = rect15Da[0] + rect15Da[2] + circleRadius
                
            if rect15Da[0] < circlePos[0] < (rect15Da[0] + rect15Da[2])\
               and rect15Da[1] < (circlePos[1] - circleRadius) < (rect15Da[1] + rect15Da[3]) and moveCircleUp:
                circlePos[1] = rect15Da[1] + rect15Da[3] + circleRadius
                
            if rect15Da[0] < circlePos[0] < (rect15Da[0] + rect15Da[2])\
               and rect15Da[1] < (circlePos[1] + circleRadius) < (rect15Da[1] + rect15Da[3]) and moveCircleDown:
                circlePos[1] = rect15Da[1] - circleRadius
        
        #rect16
            if rect16D[0] < (circlePos[0] + circleRadius) < (rect16D[0] + rect16D[2])\
               and rect16D[1] < circlePos[1] < (rect16D[1] + rect16D[3]) and moveCircleRight:
                circlePos[0] = rect16D[0] - circleRadius
            
            if rect16D[0] < (circlePos[0] - circleRadius) < (rect16D[0] + rect16D[2])\
               and rect16D[1] < circlePos[1] < (rect16D[1] + rect16D[3]) and moveCircleLeft:
                circlePos[0] = rect16D[0] + rect16D[2] + circleRadius
                
            if rect16D[0] < circlePos[0] < (rect16D[0] + rect16D[2])\
               and rect16D[1] < (circlePos[1] - circleRadius) < (rect16D[1] + rect16D[3]) and moveCircleUp:
                circlePos[1] = rect16D[1] + rect16D[3] + circleRadius
                
            if rect16D[0] < circlePos[0] < (rect16D[0] + rect16D[2])\
               and rect16D[1] < (circlePos[1] + circleRadius) < (rect16D[1] + rect16D[3]) and moveCircleDown:
                circlePos[1] = rect16D[1] - circleRadius    
        
        #rect17
            if rect17D[0] < (circlePos[0] + circleRadius) < (rect17D[0] + rect17D[2])\
               and rect17D[1] < circlePos[1] < (rect17D[1] + rect17D[3]) and moveCircleRight:
                circlePos[0] = rect17D[0] - circleRadius
            
            if rect17D[0] < (circlePos[0] - circleRadius) < (rect17D[0] + rect17D[2])\
               and rect17D[1] < circlePos[1] < (rect17D[1] + rect17D[3]) and moveCircleLeft:
                circlePos[0] = rect17D[0] + rect17D[2] + circleRadius
                
            if rect17D[0] < circlePos[0] < (rect17D[0] + rect17D[2])\
               and rect17D[1] < (circlePos[1] - circleRadius) < (rect17D[1] + rect17D[3]) and moveCircleUp:
                circlePos[1] = rect17D[1] + rect17D[3] + circleRadius
                
            if rect17D[0] < circlePos[0] < (rect17D[0] + rect17D[2])\
               and rect17D[1] < (circlePos[1] + circleRadius) < (rect17D[1] + rect17D[3]) and moveCircleDown:
                circlePos[1] = rect17D[1] - circleRadius
                
        #rectF
            if rectFD[0] < circlePos[0] < (rectFD[0] + rectFD[2])\
               and rectFD[1] < circlePos[1] < (rectFD[1] + rectFD[3]):
                gameState = "win1"
                   

         #Background color and the shapes drawn
            mainSurface.fill("dodgerblue")
            pygame.draw.circle(mainSurface, circleColor, circlePos, 20)
            pygame.draw.rect(mainSurface, "darkmagenta", rect1D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect2D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect3D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect4D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect5D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect6D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect7D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect8D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect9D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect10D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect11D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect12D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect13D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect14D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect15Da)
            pygame.draw.rect(mainSurface, "darkmagenta", rect16D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect17D)
            pygame.draw.rect(mainSurface, "firebrick", rectFD)


        #Level 2
        elif gameState == "game_level2":
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    moveCircleRight = True
                elif ev.key == pygame.K_UP:
                    moveCircleUp = True
                elif ev.key == pygame.K_LEFT:
                    moveCircleLeft = True
                elif ev.key == pygame.K_DOWN:
                    moveCircleDown = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_RIGHT:
                    moveCircleRight = False
                elif ev.key == pygame.K_UP:
                    moveCircleUp = False
                elif ev.key == pygame.K_LEFT:
                    moveCircleLeft = False
                elif ev.key == pygame.K_DOWN:
                    moveCircleDown = False
            

            #Changing colors of the ball based on the key pressed
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_b:
                    circleColor = "black"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_y:
                    circleColor = "yellow"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_o:
                    circleColor = "orange"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_g:
                    circleColor = "green"

            #Moving the circle
            if moveCircleRight:
                circlePos[0] += 0.6
            elif moveCircleUp:
                circlePos[1] -= 0.6
            elif moveCircleDown:
                circlePos[1] += 0.6
            elif moveCircleLeft:
                circlePos[0] -= 0.6
            
            if circlePos[0] > surfaceWidth:
                circlePos[0] = surfaceWidth
            elif circlePos[0] < 0:
                circlePos[0] = 0
            elif circlePos[1] < 0:
                circlePos[1] = 0
            elif circlePos[1] > surfaceHeight:
                circlePos[1] = surfaceHeight
        
        #rect1(top)
            if rect1D[0] < (circlePos[0] + circleRadius) < (rect1D[0] + rect1D[2])\
               and rect1D[1] < circlePos[1] < (rect1D[1] + rect1D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0] - circleRadius
        
            if rect1D[0] < (circlePos[0] - circleRadius) < (rect1D[0] + rect1D[2])\
               and rect1D[1] < circlePos[1] < (rect1D[1] + rect1D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2] + circleRadius
            
            if rect1D[0] < circlePos[0] < (rect1D[0] + rect1D[2])\
               and rect1D[1] < (circlePos[1] - circleRadius) < (rect1D[1] + rect1D[3]) and moveCircleUp:
                circlePos[1] = rect1D[1] + rect1D[3] + circleRadius
        
        #rect2(bottom)
            if rect1D[0] < (circlePos[0] + circleRadius) < (rect1D[0] + rect2D[2])\
               and rect2D[1] < circlePos[1] < (rect2D[1] + rect2D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0] - circleRadius
            
            if rect1D[0] < (circlePos[0] - circleRadius) < (rect1D[0] + rect2D[2])\
               and rect2D[1] < circlePos[1] < (rect2D[1] + rect2D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2] + circleRadius
            
            if rect1D[0] < circlePos[0] < (rect1D[0] + rect2D[2])\
               and rect2D[1] < (circlePos[1] + circleRadius) < (rect2D[1] + rect2D[3]) and moveCircleDown:
                circlePos[1] = rect2D[1] - circleRadius
        
        #rect3(bottom)
            if rect3D[0] < (circlePos[0] + circleRadius) < (rect3D[0] + rect3D[2])\
               and rect3D[1] < circlePos[1] < (rect3D[1] + rect3D[3]) and moveCircleRight:
                circlePos[0] = rect3D[0] - circleRadius
            
            if rect3D[0] < (circlePos[0] - circleRadius) < (rect3D[0] + rect3D[2])\
               and rect3D[1] < circlePos[1] < (rect3D[1] + rect3D[3]) and moveCircleLeft:
                circlePos[0] = rect3D[0] + rect1D[2] + circleRadius
        
            if rect3D[0] < circlePos[0] < (rect3D[0] + rect3D[2])\
               and rect3D[1] < (circlePos[1] + circleRadius) < (rect3D[1] + rect3D[3]) and moveCircleDown:
                circlePos[1] = rect3D[1] - circleRadius
            
        #rect4(top)    
            if rect4D[0] < (circlePos[0] + circleRadius) < (rect4D[0] + rect4D[2])\
               and rect4D[1] < circlePos[1] < (rect4D[1] + rect4D[3]) and moveCircleRight:
                circlePos[0] = rect4D[0] - circleRadius
            
            if rect4D[0] < (circlePos[0] - circleRadius) < (rect4D[0] + rect4D[2])\
               and rect4D[1] < circlePos[1] < (rect4D[1] + rect4D[3]) and moveCircleLeft:
                circlePos[0] = rect4D[0] + rect4D[2] + circleRadius

            if rect4D[0] < circlePos[0] < (rect4D[0] + rect4D[2])\
               and rect4D[1] < (circlePos[1] - circleRadius) < (rect4D[1] + rect4D[3]) and moveCircleUp:
                circlePos[1] = rect4D[1] + rect4D[3] + circleRadius
        
        #rect5(bottom)
            if rect5D[0] < (circlePos[0] + circleRadius) < (rect5D[0] + rect5D[2])\
               and rect5D[1] < circlePos[1] < (rect5D[1] + rect5D[3]) and moveCircleRight:
                circlePos[0] = rect5D[0] - circleRadius
        
            if rect5D[0] < (circlePos[0] - circleRadius) < (rect5D[0] + rect5D[2])\
               and rect5D[1] < circlePos[1] < (rect5D[1] + rect5D[3]) and moveCircleLeft:
                circlePos[0] = rect5D[0] + rect5D[2] + circleRadius
            
            if rect5D[0] < circlePos[0] < (rect5D[0] + rect5D[2])\
               and rect5D[1] < (circlePos[1] + circleRadius) < (rect5D[1] + rect5D[3]) and moveCircleDown:
                circlePos[1] = rect5D[1] - circleRadius
                
        #rect6(top)
            if rect6D[0] < (circlePos[0] + circleRadius) < (rect6D[0] + rect6D[2])\
               and rect6D[1] < circlePos[1] < (rect6D[1] + rect6D[3]) and moveCircleRight:
                circlePos[0] = rect6D[0] - circleRadius
                
            if rect6D[0] < (circlePos[0] - circleRadius) < (rect6D[0] + rect6D[2])\
               and rect6D[1] < circlePos[1] < (rect6D[1] + rect6D[3]) and moveCircleLeft:
                circlePos[0] = rect6D[0] + rect6D[2] + circleRadius
                
            if rect6D[0] < circlePos[0] < (rect6D[0] + rect6D[2])\
               and rect6D[1] < (circlePos[1] - circleRadius) < (rect6D[1] + rect6D[3]) and moveCircleUp:
                circlePos[1] = rect6D[1] + rect6D[3] + circleRadius
        #rect7(top)
            if rect7D[0] < (circlePos[0] + circleRadius) < (rect7D[0] + rect7D[2])\
               and rect7D[1] < circlePos[1] < (rect7D[1] + rect7D[3]) and moveCircleRight:
                circlePos[0] = rect7D[0] - circleRadius
                
            if rect7D[0] < (circlePos[0] - circleRadius) < (rect7D[0] + rect7D[2])\
               and rect7D[1] < circlePos[1] < (rect7D[1] + rect7D[3]) and moveCircleLeft:
                circlePos[0] = rect7D[0] + rect7D[2] + circleRadius
                
            if rect7D[0] < circlePos[0] < (rect7D[0] + rect7D[2])\
               and rect7D[1] < (circlePos[1] - circleRadius) < (rect7D[1] + rect7D[3]) and moveCircleUp:
                circlePos[1] = rect7D[1] + rect7D[3] + circleRadius
        
        #rect8(top)
            if rect8D[0] < (circlePos[0] + circleRadius) < (rect8D[0] + rect8D[2])\
               and rect8D[1] < circlePos[1] < (rect8D[1] + rect8D[3]) and moveCircleRight:
                circlePos[0] = rect8D[0] - circleRadius
                
            if rect8D[0] < (circlePos[0] - circleRadius) < (rect8D[0] + rect8D[2])\
               and rect8D[1] < circlePos[1] < (rect8D[1] + rect8D[3]) and moveCircleLeft:
                circlePos[0] = rect8D[0] + rect8D[2] + circleRadius
                
            if rect8D[0] < circlePos[0] < (rect8D[0] + rect8D[2])\
               and rect8D[1] < (circlePos[1] - circleRadius) < (rect8D[1] + rect8D[3]) and moveCircleUp:
                circlePos[1] = rect8D[1] + rect8D[3] + circleRadius
                
            if rect8D[0] < circlePos[0] < (rect8D[0] + rect8D[2])\
               and rect8D[1] < (circlePos[1] + circleRadius) < (rect8D[1] + rect8D[3]) and moveCircleDown:
                circlePos[1] = rect8D[1] - circleRadius
                
        #rect9(middle)
            if rect9D[0] < (circlePos[0] + circleRadius) < (rect9D[0] + rect9D[2])\
               and rect9D[1] < circlePos[1] < (rect9D[1] + rect9D[3]) and moveCircleRight:
                circlePos[0] = rect9D[0] - circleRadius
            
            if rect9D[0] < (circlePos[0] - circleRadius) < (rect9D[0] + rect9D[2])\
               and rect9D[1] < circlePos[1] < (rect9D[1] + rect9D[3]) and moveCircleLeft:
                circlePos[0] = rect9D[0] + rect9D[2] + circleRadius
                
            if rect9D[0] < circlePos[0] < (rect9D[0] + rect9D[2])\
               and rect9D[1] < (circlePos[1] - circleRadius) < (rect9D[1] + rect9D[3]) and moveCircleUp:
                circlePos[1] = rect9D[1] + rect9D[3] + circleRadius
                
            if rect9D[0] < circlePos[0] < (rect9D[0] + rect9D[2])\
               and rect9D[1] < (circlePos[1] + circleRadius) < (rect9D[1] + rect9D[3]) and moveCircleDown:
                circlePos[1] = rect9D[1] - circleRadius
                
        #rect10(middle)
            if rect10D[0] < (circlePos[0] + circleRadius) < (rect10D[0] + rect10D[2])\
               and rect10D[1] < circlePos[1] < (rect10D[1] + rect10D[3]) and moveCircleRight:
                circlePos[0] = rect10D[0] - circleRadius
            
            if rect10D[0] < (circlePos[0] - circleRadius) < (rect10D[0] + rect10D[2])\
               and rect10D[1] < circlePos[1] < (rect10D[1] + rect10D[3]) and moveCircleLeft:
                circlePos[0] = rect10D[0] + rect10D[2] + circleRadius
                
            if rect10D[0] < circlePos[0] < (rect10D[0] + rect10D[2])\
               and rect10D[1] < (circlePos[1] - circleRadius) < (rect10D[1] + rect10D[3]) and moveCircleUp:
                circlePos[1] = rect10D[1] + rect10D[3] + circleRadius
                
            if rect10D[0] < circlePos[0] < (rect10D[0] + rect10D[2])\
               and rect10D[1] < (circlePos[1] + circleRadius) < (rect10D[1] + rect10D[3]) and moveCircleDown:
                circlePos[1] = rect10D[1] - circleRadius
                
        #rect11
            if rect11D[0] < (circlePos[0] + circleRadius) < (rect11D[0] + rect11D[2])\
               and rect11D[1] < circlePos[1] < (rect11D[1] + rect11D[3]) and moveCircleRight:
                circlePos[0] = rect11D[0] - circleRadius
            
            if rect11D[0] < (circlePos[0] - circleRadius) < (rect11D[0] + rect11D[2])\
               and rect11D[1] < circlePos[1] < (rect11D[1] + rect11D[3]) and moveCircleLeft:
                circlePos[0] = rect11D[0] + rect11D[2] + circleRadius
                
            if rect11D[0] < circlePos[0] < (rect11D[0] + rect11D[2])\
               and rect11D[1] < (circlePos[1] - circleRadius) < (rect11D[1] + rect11D[3]) and moveCircleUp:
                circlePos[1] = rect11D[1] + rect11D[3] + circleRadius
                
            if rect11D[0] < circlePos[0] < (rect11D[0] + rect11D[2])\
               and rect11D[1] < (circlePos[1] + circleRadius) < (rect11D[1] + rect11D[3]) and moveCircleDown:
                circlePos[1] = rect11D[1] - circleRadius
        
        #rect12
            if rect12D[0] < (circlePos[0] + circleRadius) < (rect12D[0] + rect12D[2])\
               and rect12D[1] < circlePos[1] < (rect12D[1] + rect12D[3]) and moveCircleRight:
                circlePos[0] = rect12D[0] - circleRadius
            
            if rect12D[0] < (circlePos[0] - circleRadius) < (rect12D[0] + rect12D[2])\
               and rect12D[1] < circlePos[1] < (rect12D[1] + rect12D[3]) and moveCircleLeft:
                circlePos[0] = rect12D[0] + rect12D[2] + circleRadius
                
            if rect12D[0] < circlePos[0] < (rect12D[0] + rect12D[2])\
               and rect12D[1] < (circlePos[1] - circleRadius) < (rect12D[1] + rect12D[3]) and moveCircleUp:
                circlePos[1] = rect12D[1] + rect12D[3] + circleRadius
                
            if rect12D[0] < circlePos[0] < (rect12D[0] + rect12D[2])\
               and rect12D[1] < (circlePos[1] + circleRadius) < (rect12D[1] + rect12D[3]) and moveCircleDown:
                circlePos[1] = rect12D[1] - circleRadius
                
        #rect13
            if rect13D[0] < (circlePos[0] + circleRadius) < (rect13D[0] + rect13D[2])\
               and rect13D[1] < circlePos[1] < (rect13D[1] + rect13D[3]) and moveCircleRight:
                circlePos[0] = rect13D[0] - circleRadius
            
            if rect13D[0] < (circlePos[0] - circleRadius) < (rect13D[0] + rect13D[2])\
               and rect13D[1] < circlePos[1] < (rect13D[1] + rect13D[3]) and moveCircleLeft:
                circlePos[0] = rect13D[0] + rect13D[2] + circleRadius
                
            if rect13D[0] < circlePos[0] < (rect13D[0] + rect13D[2])\
               and rect13D[1] < (circlePos[1] - circleRadius) < (rect13D[1] + rect13D[3]) and moveCircleUp:
                circlePos[1] = rect13D[1] + rect13D[3] + circleRadius
                
            if rect13D[0] < circlePos[0] < (rect13D[0] + rect13D[2])\
               and rect13D[1] < (circlePos[1] + circleRadius) < (rect13D[1] + rect13D[3]) and moveCircleDown:
                circlePos[1] = rect13D[1] - circleRadius
        
        #rect14
            if rect14D[0] < (circlePos[0] + circleRadius) < (rect14D[0] + rect14D[2])\
               and rect14D[1] < circlePos[1] < (rect14D[1] + rect14D[3]) and moveCircleRight:
                circlePos[0] = rect14D[0] - circleRadius
            
            if rect14D[0] < (circlePos[0] - circleRadius) < (rect14D[0] + rect14D[2])\
               and rect14D[1] < circlePos[1] < (rect14D[1] + rect14D[3]) and moveCircleLeft:
                circlePos[0] = rect14D[0] + rect14D[2] + circleRadius
                
            if rect14D[0] < circlePos[0] < (rect14D[0] + rect14D[2])\
               and rect14D[1] < (circlePos[1] - circleRadius) < (rect14D[1] + rect14D[3]) and moveCircleUp:
                circlePos[1] = rect14D[1] + rect14D[3] + circleRadius
                
            if rect14D[0] < circlePos[0] < (rect14D[0] + rect14D[2])\
               and rect14D[1] < (circlePos[1] + circleRadius) < (rect14D[1] + rect14D[3]) and moveCircleDown:
                circlePos[1] = rect14D[1] - circleRadius
        
        #rect15
            if rect15Db[0] < (circlePos[0] + circleRadius) < (rect15Db[0] + rect15Db[2])\
               and rect15Db[1] < circlePos[1] < (rect15Db[1] + rect15Db[3]) and moveCircleRight:
                circlePos[0] = rect15Db[0] - circleRadius
            
            if rect15Db[0] < (circlePos[0] - circleRadius) < (rect15Db[0] + rect15Db[2])\
               and rect15Db[1] < circlePos[1] < (rect15Db[1] + rect15Db[3]) and moveCircleLeft:
                circlePos[0] = rect15Db[0] + rect15Db[2] + circleRadius
                
            if rect15Db[0] < circlePos[0] < (rect15Db[0] + rect15Db[2])\
               and rect15Db[1] < (circlePos[1] - circleRadius) < (rect15Db[1] + rect15Db[3]) and moveCircleUp:
                circlePos[1] = rect15Db[1] + rect15Db[3] + circleRadius
                
            if rect15Db[0] < circlePos[0] < (rect15Db[0] + rect15Db[2])\
               and rect15Db[1] < (circlePos[1] + circleRadius) < (rect15Db[1] + rect15Db[3]) and moveCircleDown:
                circlePos[1] = rect15Db[1] - circleRadius
        
        #rect16
            if rect16D[0] < (circlePos[0] + circleRadius) < (rect16D[0] + rect16D[2])\
               and rect16D[1] < circlePos[1] < (rect16D[1] + rect16D[3]) and moveCircleRight:
                circlePos[0] = rect16D[0] - circleRadius
            
            if rect16D[0] < (circlePos[0] - circleRadius) < (rect16D[0] + rect16D[2])\
               and rect16D[1] < circlePos[1] < (rect16D[1] + rect16D[3]) and moveCircleLeft:
                circlePos[0] = rect16D[0] + rect16D[2] + circleRadius
                
            if rect16D[0] < circlePos[0] < (rect16D[0] + rect16D[2])\
               and rect16D[1] < (circlePos[1] - circleRadius) < (rect16D[1] + rect16D[3]) and moveCircleUp:
                circlePos[1] = rect16D[1] + rect16D[3] + circleRadius
                
            if rect16D[0] < circlePos[0] < (rect16D[0] + rect16D[2])\
               and rect16D[1] < (circlePos[1] + circleRadius) < (rect16D[1] + rect16D[3]) and moveCircleDown:
                circlePos[1] = rect16D[1] - circleRadius    
        
        #rect17
            if rect17D[0] < (circlePos[0] + circleRadius) < (rect17D[0] + rect17D[2])\
               and rect17D[1] < circlePos[1] < (rect17D[1] + rect17D[3]) and moveCircleRight:
                circlePos[0] = rect17D[0] - circleRadius
            
            if rect17D[0] < (circlePos[0] - circleRadius) < (rect17D[0] + rect17D[2])\
               and rect17D[1] < circlePos[1] < (rect17D[1] + rect17D[3]) and moveCircleLeft:
                circlePos[0] = rect17D[0] + rect17D[2] + circleRadius
                
            if rect17D[0] < circlePos[0] < (rect17D[0] + rect17D[2])\
               and rect17D[1] < (circlePos[1] - circleRadius) < (rect17D[1] + rect17D[3]) and moveCircleUp:
                circlePos[1] = rect17D[1] + rect17D[3] + circleRadius
                
            if rect17D[0] < circlePos[0] < (rect17D[0] + rect17D[2])\
               and rect17D[1] < (circlePos[1] + circleRadius) < (rect17D[1] + rect17D[3]) and moveCircleDown:
                circlePos[1] = rect17D[1] - circleRadius

        #rectF
            if rectFD[0] < circlePos[0] < (rectFD[0] + rectFD[2])\
               and rectFD[1] < circlePos[1] < (rectFD[1] + rectFD[3]):
                gameState = "win"
                
        #circle2 (colliding with this circle makes you lose)
            circle2Pos[1] += circleSpeed
            if (circle2Pos[1] + circle2Radius) > surfaceHeight or (circle2Pos[1] - circle2Radius) < 0:
                circleSpeed = -circleSpeed
                
            if distFromPoints(circlePos, circle2Pos) < (circleSize + circle2Size):
                gameState = "lose"

            #Background color and the various shapes drawn
            mainSurface.fill("navy")
  
            pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize)
            pygame.draw.circle(mainSurface, "gray", circle2Pos, circle2Size)
            pygame.draw.rect(mainSurface, "lightpink", rect1D)
            pygame.draw.rect(mainSurface, "lightpink", rect2D)
            pygame.draw.rect(mainSurface, "lightpink", rect3D)
            pygame.draw.rect(mainSurface, "lightpink", rect4D)
            pygame.draw.rect(mainSurface, "lightpink", rect5D)
            pygame.draw.rect(mainSurface, "lightpink", rect6D)
            pygame.draw.rect(mainSurface, "lightpink", rect7D)
            pygame.draw.rect(mainSurface, "lightpink", rect8D)
            pygame.draw.rect(mainSurface, "lightpink", rect9D)
            pygame.draw.rect(mainSurface, "lightpink", rect10D)
            pygame.draw.rect(mainSurface, "lightpink", rect11D)
            pygame.draw.rect(mainSurface, "lightpink", rect12D)
            pygame.draw.rect(mainSurface, "lightpink", rect13D)
            pygame.draw.rect(mainSurface, "lightpink", rect14D)
            pygame.draw.rect(mainSurface, "lightpink", rect15Db)
            pygame.draw.rect(mainSurface, "lightpink", rect16D)
            pygame.draw.rect(mainSurface, "lightpink", rect17D)
            pygame.draw.rect(mainSurface, "gray", rectFD)


        pygame.display.flip()   #Displaying the screen

    pygame.quit()     #Closing the screen

main()