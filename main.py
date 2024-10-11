import pygame
import time
import random
pygame.font.init()

width,height=900 , 650
win=pygame.display.set_mode((width, height))
pygame.display.set_caption("space")


BG=pygame.transform.scale(pygame.image.load("data/blackcolored.jpg"),(width,height))


#variables:
player_width=20
player_height=10
player_vel=6
star_width=2
star_height=2
star_vel=7
font=pygame.font.SysFont("comicsans",40)



#draw function:
def draw(player,elasped_time,stars):
    win.blit(BG,(0,0))
    
    time_text=font.render(f"time: {round(elasped_time)}s",1,"white")
    win.blit(time_text,(10,10))
    
    pygame.draw.rect(win,"red",player)
    for star in stars:
        pygame.draw.rect(win,"yellow",star)
    
    pygame.display.update()
    
    
   

    
#The main function:


def main():
    
    run=True 
    player=pygame.Rect(width/2,height-player_height,
                       player_width,player_height)
    clock=pygame.time.Clock()
    
    start_time=time.time()
    elapsed_time=0
    
    
    star_add_increment=2000
    star_count=0
    stars=[]
    hit=False
    
    while run:
        star_count+=clock.tick(60)
        elapsed_time=time.time()-start_time
        
        if star_count>star_add_increment:
            for _ in range(30):
                star_x=random.randint(0,width-star_width)
                star=pygame.Rect(star_x,-star_height,star_width,star_height)
                stars.append(star)
            star_add_increment=max(100,star_add_increment-100)
            star_count=0
                
                
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            
            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-player_vel>=0:
            player.x-=player_vel
        elif keys[pygame.K_RIGHT] and player.x+player_vel+player_width<=width:
            player.x+=player_vel
        #    elif keys[pygame.K_UP] and player.y>=0:
        #        player.y-=player_vel
        #    elif keys[pygame.K_DOWN] and player.y+player_vel+player_height<=height:
        #        player.y+=player_vel#
        
        for star in stars[:]:
            star.y+=star_vel
            if star.y>height:
                stars.remove(star)
            elif star.y+star.height>=player.y and star.colliderect(player):
                stars.remove(star)
                hit=True
                break
        if hit:
            pygame.de
            break
        
        draw(player,elapsed_time,stars)
    pygame.quit
    
if __name__=="__main__":
    main()