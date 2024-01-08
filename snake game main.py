import pygame
import time
import random

snake_speed = 20

# Window size
x = 600
y = 600

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()
pygame.display.set_caption('Hungry Snake')
game_window = pygame.display.set_mode((x, y))

fps = pygame.time.Clock()
snake_position = [100, 100]

# defining first 4 blocks of snake body
snake_body = [[0, 0],
			[10, 50],
			[20, 50],
			[30, 50]
			]
# food position
foodposition = [random.randrange(1, (x//10)) * 10,
				random.randrange(1, (y//10)) * 10]

foodspawn = True
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)

# game over function
def game_over():

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (x/2, y/2)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()


# Main Function
while True:
	
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	# If two keys pressed simultaneously, the snake shouldnot move into two
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == foodposition[0] and snake_position[1] == foodposition[1]:
		score += 10
		foodspawn = False
	else:
		snake_body.pop()
		
	if not foodspawn:
		foodposition = [random.randrange(1, (x//10)) * 10,
						random.randrange(1, (y//10)) * 10]
		
	foodspawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, white, pygame.Rect(
		foodposition[0], foodposition[1], 10, 10))

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > y-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score countinuously
	show_score(1, white, 'times new roman', 20)

	pygame.display.update()
	fps.tick(snake_speed)


#ENJOY THE GAME