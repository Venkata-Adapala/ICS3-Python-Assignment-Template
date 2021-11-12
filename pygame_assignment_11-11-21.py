import pygame
import math

def distFromPoints(point1, point2):
    distance = math.sqrt( ((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2) )
    return distance

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceWidth = 1280   # Desired physical surface size, in pixels.
    surfaceHeight = 720

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
    gameState = "start"

    # Set up some data to describe a small circle and its color
    font = pygame.font.SysFont("Arial", 40)
    font2 = pygame.font.SysFont("Algerian", 75)
    
    circleColor = "red"        # A color is a mix of (Red, Green, Blue)
    circlePos = [50,50]
    circle2Pos = [800,600]
    circleSize = 20
    circle2Size = 30
    circleSpeed = 0.75
    moveCircleRight = False #Control whether the circle should move or not
    moveCircleUp = False
    moveCircleDown = False
    moveCircleLeft = False
    
    rect0D = [450,500,280,100]
    rectlvl1D = [450,300,280,100]
    rectlvl2D = [450,500,280,100]
    rect1D = [250,-1,20,500]
    rect2D = [250,600,20,121]
    rect3D = [400,100,20,650]
    rect4D = [550,-1,20,350]
    rect5D = [550,450,20,321]
    rectFD = [1180,620,100,100]
    rectNextD = [490,540,225,65]

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
        if gameState == "start":
            mainSurface.fill("gray")
            pygame.draw.rect(mainSurface, "firebrick", rect0D)
            text1 = "MAZE.INC"
            text2 = "START"
            renderedText1 = font2.render(text1, 1, pygame.Color("maroon"))
            renderedText2 = font.render(text2, 1, pygame.Color("navy"))
            mainSurface.blit(renderedText1, (455,150))
            mainSurface.blit(renderedText2, (530,525))
            
            if ev.type == pygame.MOUSEBUTTONUP:
                if rect0D[0] <= pygame.mouse.get_pos()[0] <= (rect0D[0] + rect0D[2])\
                   and rect0D[1] <= pygame.mouse.get_pos()[1] <= (rect0D[1] + rect0D[3]):
                    gameState = "game_levels"
        
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
                if rectlvl1D[0] <= pygame.mouse.get_pos()[0] <= (rectlvl1D[0] + rectlvl1D[2])\
                   and rectlvl1D[1] <= pygame.mouse.get_pos()[1] <= (rectlvl1D[1] + rectlvl1D[3]):
                    gameState = "game_level1"
                
                if rectlvl2D[0] <= pygame.mouse.get_pos()[0] <= (rectlvl2D[0] + rectlvl2D[2])\
                   and rectlvl2D[1] <= pygame.mouse.get_pos()[1] <= (rectlvl2D[1] + rectlvl2D[3]):
                    gameState = "game_level2"
                
        elif gameState == "win":
            mainSurface.fill("darkgreen")
            textWin = "YOU WIN"
            renderedtextWin = font2.render(textWin, 1, pygame.Color("pink"))
            mainSurface.blit(renderedtextWin, (490, 310))
        
        elif gameState == "lose":
            mainSurface.fill("black")
            textLose = "YOU LOSE"
            renderedtextLose = font2.render(textLose, 1, pygame.Color("red"))
            mainSurface.blit(renderedtextLose, (500, 310))
        
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
            
        # Update your game objects and data structures here...
            if moveCircleRight:
                circlePos[0] += 0.6
            elif moveCircleUp:
                circlePos[1] -= 0.6
            elif moveCircleDown:
                circlePos[1] += 0.6
            elif moveCircleLeft:
                circlePos[0] -= 0.6
            
            if circlePos[0] >= surfaceWidth:
                circlePos[0] = surfaceWidth
            elif circlePos[0] <= 0:
                circlePos[0] = 0
            elif circlePos[1] <= 0:
                circlePos[1] = 0
            elif circlePos[1] >= surfaceHeight:
                circlePos[1] = surfaceHeight
        
        #rect1(top)
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect1D[2])\
               and rect1D[1] <= circlePos[1] <= (rect1D[1] + rect1D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0]
        
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect1D[2])\
               and rect1D[1] <= circlePos[1] <= (rect1D[1] + rect1D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2]
            
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect1D[2])\
               and rect1D[1] <= circlePos[1] <= (rect1D[1] + rect1D[3]) and moveCircleUp:
                circlePos[1] = rect1D[1] + rect1D[3]
        
        #rect2(bottom)
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect2D[2])\
               and rect2D[1] <= circlePos[1] <= (rect2D[1] + rect2D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0]
            
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect2D[2])\
               and rect2D[1] <= circlePos[1] <= (rect2D[1] + rect2D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2]
            
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect2D[2])\
               and rect2D[1] <= circlePos[1] <= (rect2D[1] + rect2D[3]) and moveCircleDown:
                circlePos[1] = rect2D[1]
        
        #rect3(bottom)
            if rect3D[0] <= circlePos[0] <= (rect3D[0] + rect3D[2])\
               and rect3D[1] <= circlePos[1] <= (rect3D[1] + rect3D[3]) and moveCircleRight:
                circlePos[0] = rect3D[0]
            
            if rect3D[0] <= circlePos[0] <= (rect3D[0] + rect3D[2])\
               and rect3D[1] <= circlePos[1] <= (rect3D[1] + rect3D[3]) and moveCircleLeft:
                circlePos[0] = rect3D[0] + rect1D[2]
        
            if rect3D[0] <= circlePos[0] <= (rect3D[0] + rect3D[2])\
               and rect3D[1] <= circlePos[1] <= (rect3D[1] + rect3D[3]) and moveCircleDown:
                circlePos[1] = rect3D[1]
            
        #rect4(top)    
            if rect4D[0] <= circlePos[0] <= (rect4D[0] + rect4D[2])\
               and rect4D[1] <= circlePos[1] <= (rect4D[1] + rect4D[3]) and moveCircleRight:
                circlePos[0] = rect4D[0]
            
            if rect4D[0] <= circlePos[0] <= (rect4D[0] + rect4D[2])\
               and rect4D[1] <= circlePos[1] <= (rect4D[1] + rect4D[3]) and moveCircleLeft:
                circlePos[0] = rect4D[0] + rect4D[2]

            if rect4D[0] <= circlePos[0] <= (rect4D[0] + rect4D[2])\
               and rect4D[1] <= circlePos[1] <= (rect4D[1] + rect4D[3]) and moveCircleUp:
                circlePos[1] = rect4D[1] + rect4D[3]
        
        #rect5(bottom)
            if rect5D[0] <= circlePos[0] <= (rect5D[0] + rect5D[2])\
               and rect5D[1] <= circlePos[1] <= (rect5D[1] + rect5D[3]) and moveCircleRight:
                circlePos[0] = rect5D[0]
        
            if rect5D[0] <= circlePos[0] <= (rect5D[0] + rect5D[2])\
               and rect5D[1] <= circlePos[1] <= (rect5D[1] + rect5D[3]) and moveCircleLeft:
                circlePos[0] = rect5D[0] + rect5D[2]
            
            if rect5D[0] <= circlePos[0] <= (rect5D[0] + rect5D[2])\
               and rect5D[1] <= circlePos[1] <= (rect5D[1] + rect5D[3]) and moveCircleDown:
                circlePos[1] = rect5D[1]

        #rectF
            if rectFD[0] <= circlePos[0] <= (rectFD[0] + rectFD[2])\
               and rectFD[1] <= circlePos[1] <= (rectFD[1] + rectFD[3]):
                gameState = "win"
                   
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
            mainSurface.fill("dodgerblue")
               
        # Draw something  on the surface
            pygame.draw.circle(mainSurface, circleColor, circlePos, 20)
            pygame.draw.rect(mainSurface, "darkmagenta", rect1D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect2D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect3D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect4D)
            pygame.draw.rect(mainSurface, "darkmagenta", rect5D)
            pygame.draw.rect(mainSurface, "firebrick", rectFD)

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
            

        # Update your game objects and data structures here...
            if moveCircleRight:
                circlePos[0] += 0.6
            elif moveCircleUp:
                circlePos[1] -= 0.6
            elif moveCircleDown:
                circlePos[1] += 0.6
            elif moveCircleLeft:
                circlePos[0] -= 0.6
            
            if circlePos[0] >= surfaceWidth:
                circlePos[0] = surfaceWidth
            elif circlePos[0] <= 0:
                circlePos[0] = 0
            elif circlePos[1] <= 0:
                circlePos[1] = 0
            elif circlePos[1] >= surfaceHeight:
                circlePos[1] = surfaceHeight
        
        #rect1(top)
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect1D[2])\
               and rect1D[1] <= circlePos[1] <= (rect1D[1] + rect1D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0]
        
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect1D[2])\
               and rect1D[1] <= circlePos[1] <= (rect1D[1] + rect1D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2]
            
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect1D[2])\
               and rect1D[1] <= circlePos[1] <= (rect1D[1] + rect1D[3]) and moveCircleUp:
                circlePos[1] = rect1D[1] + rect1D[3]
        
        #rect2(bottom)
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect2D[2])\
               and rect2D[1] <= circlePos[1] <= (rect2D[1] + rect2D[3]) and moveCircleRight:
                circlePos[0] = rect1D[0]
            
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect2D[2])\
               and rect2D[1] <= circlePos[1] <= (rect2D[1] + rect2D[3]) and moveCircleLeft:
                circlePos[0] = rect1D[0] + rect1D[2]
            
            if rect1D[0] <= circlePos[0] <= (rect1D[0] + rect2D[2])\
               and rect2D[1] <= circlePos[1] <= (rect2D[1] + rect2D[3]) and moveCircleDown:
                circlePos[1] = rect2D[1]
        
        #rect3(bottom)
            if rect3D[0] <= circlePos[0] <= (rect3D[0] + rect3D[2])\
               and rect3D[1] <= circlePos[1] <= (rect3D[1] + rect3D[3]) and moveCircleRight:
                circlePos[0] = rect3D[0]
            
            if rect3D[0] <= circlePos[0] <= (rect3D[0] + rect3D[2])\
               and rect3D[1] <= circlePos[1] <= (rect3D[1] + rect3D[3]) and moveCircleLeft:
                circlePos[0] = rect3D[0] + rect1D[2]
        
            if rect3D[0] <= circlePos[0] <= (rect3D[0] + rect3D[2])\
               and rect3D[1] <= circlePos[1] <= (rect3D[1] + rect3D[3]) and moveCircleDown:
                circlePos[1] = rect3D[1]
            
        #rect4(top)    
            if rect4D[0] <= circlePos[0] <= (rect4D[0] + rect4D[2])\
               and rect4D[1] <= circlePos[1] <= (rect4D[1] + rect4D[3]) and moveCircleRight:
                circlePos[0] = rect4D[0]
            
            if rect4D[0] <= circlePos[0] <= (rect4D[0] + rect4D[2])\
               and rect4D[1] <= circlePos[1] <= (rect4D[1] + rect4D[3]) and moveCircleLeft:
                circlePos[0] = rect4D[0] + rect4D[2]

            elif rect4D[0] <= circlePos[0] <= (rect4D[0] + rect4D[2])\
               and rect4D[1] <= circlePos[1] <= (rect4D[1] + rect4D[3]) and moveCircleUp:
                circlePos[1] = rect4D[1] + rect4D[3]
        
        #rect5(bottom)
            if rect5D[0] <= circlePos[0] <= (rect5D[0] + rect5D[2])\
               and rect5D[1] <= circlePos[1] <= (rect5D[1] + rect5D[3]) and moveCircleRight:
                circlePos[0] = rect5D[0]
        
            if rect5D[0] <= circlePos[0] <= (rect5D[0] + rect5D[2])\
               and rect5D[1] <= circlePos[1] <= (rect5D[1] + rect5D[3]) and moveCircleLeft:
                circlePos[0] = rect5D[0] + rect5D[2]
            
            if rect5D[0] <= circlePos[0] <= (rect5D[0] + rect5D[2])\
               and rect5D[1] <= circlePos[1] <= (rect5D[1] + rect5D[3]) and moveCircleDown:
                circlePos[1] = rect5D[1]

        #rectF
            if rectFD[0] <= circlePos[0] <= (rectFD[0] + rectFD[2])\
               and rectFD[1] <= circlePos[1] <= (rectFD[1] + rectFD[3]):
                gameState = "win"
                
        #circle2
            circle2Pos[1] += circleSpeed
            if circle2Pos[1] >= surfaceHeight or circle2Pos[1] <= 0:
                circleSpeed = -circleSpeed
                
            if distFromPoints(circlePos, circle2Pos) <= (circleSize + circle2Size):
                gameState = "lose"
                   
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
            mainSurface.fill("navy")
  
         # Draw something  on the surface
            pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize)
            pygame.draw.circle(mainSurface, "gray", circle2Pos, circle2Size)
            pygame.draw.rect(mainSurface, "lightpink", rect1D)
            pygame.draw.rect(mainSurface, "lightpink", rect2D)
            pygame.draw.rect(mainSurface, "lightpink", rect3D)
            pygame.draw.rect(mainSurface, "lightpink", rect4D)
            pygame.draw.rect(mainSurface, "lightpink", rect5D)
            pygame.draw.rect(mainSurface, "gray", rectFD)
            
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
