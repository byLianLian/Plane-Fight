import pygame
#import time#怕程序卡

def main():
	#1.创建一个窗口
	screen = pygame.display.set_mode((480,852),0,32)
	#2.创建一个背景图片
	background = pygame.image.load("./feiji/background.png")
	while True:
		screen.blit(background,(0,0))
		pygame.display.update()
		#time.sleep(0.01)#怕程序卡

if __name__ == "__main__":
	main()
