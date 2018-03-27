import pygame
#import time#怕程序卡

def main():
	#1.创建一个窗口
	screen = pygame.display.set_mode((480,852),0,32)

	#2.创建一个背景图片
	background = pygame.image.load("./feiji/background.png")

	#创建一个飞机图片
	hero = pygame.image.load("./feiji/hero1.png")

	x = 210
	y = 700

	while True:
		screen.blit(background,(0,0))

		screen.blit(hero,(x,y))

		pygame.display.update()

		x+=1
		y-=1
		#time.sleep(0.01)#怕程序卡


if __name__ == "__main__":
	main()
