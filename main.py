# Ranad Jamal Oweis 169893
# Shatha Bassam Arar 171454

# import libraries
import pygame
import random
import os
from pathlib import Path
from pygame import mixer

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
SCORE_FILE = BASE_DIR / "score.txt"

# initialize Pygame
mixer.init()
pygame.init()

# game window dimensions (constants)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("titan jump")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# load music and sounds
pygame.mixer.music.load(str(ASSETS_DIR / 'season 4 opening.mp3'))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0)
jump_sound = pygame.mixer.Sound(str(ASSETS_DIR / 'swordjump.wav'))
jump_sound.set_volume(0.1)
sword_sound = pygame.mixer.Sound(str(ASSETS_DIR / 'sword.mp3'))
sword_sound.set_volume(0.1)
death_sound = pygame.mixer.Sound(str(ASSETS_DIR / 'Levi_tell_Erwin_to_leave_his_dream_and_die.mp3'))
death_sound.set_volume(0.6)

# game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0
# for Enemy
ENEMY_SPAWN_RATE = 10  # Higher value means less frequent spawning
MIN_ENEMY_SPACING = 200  # Minimum vertical spacing between enemies
last_enemy_y = -MIN_ENEMY_SPACING  # Initial value to ensure the first enemy can spawn
# for score
if os.path.exists(SCORE_FILE):
	with open(SCORE_FILE, 'r') as file:
		high_score = int(file.read())
else:
	high_score = 0

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PANEL = (58, 75, 59)
LINT = (186, 204, 129)

# define fonts
font_small = pygame.font.SysFont('Lucida sans', 20)
font_big = pygame.font.SysFont('Lucida sans', 24)

# load images
bg_image = pygame.image.load(str(ASSETS_DIR / 'wallbg.png')).convert_alpha()
levi_image = pygame.image.load(str(ASSETS_DIR / 'levi2.png')).convert_alpha()
platform_image = pygame.image.load(str(ASSETS_DIR / 'stone.png')).convert_alpha()
game_over_image = pygame.image.load(str(ASSETS_DIR / 'gameover_img.jpg')).convert_alpha()

# enemies
enemy_image = pygame.image.load(str(ASSETS_DIR / 'titan.png')).convert_alpha()

# function for outputting text onto the screen
def draw_text(text, font, text_color, x, y):
	img = font.render(text, True, text_color)
	screen.blit(img, (x, y))

# function for drawing info panel (to display current score)
def draw_panel():
	pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
	pygame.draw.line(screen, PANEL, (0, 30), (SCREEN_WIDTH, 30), 2)
	draw_text('SCORE: ' + str(score), font_small, LINT, 5, 0)

# function for drawing the background
def draw_bg(bg_scroll):
	screen.blit(bg_image, (0, 0))
	#screen.blit(bg_image, (0, -600 + bg_scroll))

# player class
class Player():
	def __init__(self, x, y):
		self.image = pygame.transform.scale(levi_image,(100,100))
		self.width = 60
		self.height = 87
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (x, y)
		self.vel_y = 0
		self.flip = False

	def move(self):
		# reset variables
		scroll = 0
		dx = 0
		dy = 0

		# process key-presses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			dx = -8
			self.flip = False
		if key[pygame.K_RIGHT]:
			dx = 8
			self.flip = True

		# gravity
		self.vel_y += GRAVITY
		dy += self.vel_y

		# ensure player doesn't go off the edge of the screen
		if self.rect.left + dx < 0:
			dx = - self.rect.left
		if self.rect.right + dx > SCREEN_WIDTH:
			dx = SCREEN_WIDTH - self.rect.right

		# check collision with platforms
		for platform in platform_group:
			# collision in the y direction
			if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				# check if above the platform
				if self.rect.bottom < platform.rect.centery:
					if self.vel_y > 0:
						self.rect.bottom = platform.rect.top
						dy = 0
						self.vel_y = -20
						jump_sound.play()
						sword_sound.play()

		# check if the player has bounced to the top of the screen
		if self.rect.top <= SCROLL_THRESH:
			# if player is jumping
			if self.vel_y < 0:
				scroll = -dy

		# update rectangle position
		self.rect.x += dx
		self.rect.y += dy + scroll

		return scroll

	def draw(self):
		screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x-25, self.rect.y-9))
		#pygame.draw.rect(screen, WHITE, self.rect, 2)


# platform class
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, width, moving):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(platform_image,(width, 15))
		self.moving = moving
		self.move_counter = random.randint(0, 50)
		self.direction = random.choice([-1, 1])
		self.speed = random.randint(1, 2)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, scroll):
		# move platform side to side if it is a moving platform
		if self.moving == True :
			self.move_counter += 1
			self.rect.x += self.direction * self.speed

		# change platform direction if it has moved fully or hit a wall
		if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
			self.direction *= -1
			self.move_counter = 0

		# update platform's vertical position
		self.rect.y += scroll

		# check if platform has gone off the screen
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_image, (50, 79))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def update(self, scroll):
        self.rect.y += self.speed + scroll
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# player instance
levi = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# create sprite groups
platform_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
platform_group.add(platform)


# the game loop
run = True
while run:

	clock.tick(FPS)

	if not game_over:

		scroll = levi.move()

		# draw background
		bg_scroll += scroll
		if bg_scroll >= 600:
			bg_scroll = 0
		draw_bg(bg_scroll)

		# generate platforms
		if len(platform_group) < MAX_PLATFORMS:
			p_w = random.randint(60, 80)
			p_x = random.randint(0, SCREEN_WIDTH - p_w)
			p_y = platform.rect.y - random.randint(80, 120)
			p_type = random.randint(1, 2) # to randomise moving platforms
			if p_type == 1 and score > 500: # moving platforms after reaching score 500
				p_moving = True
			else:
				p_moving = False
			platform = Platform(p_x, p_y, p_w, p_moving)
			platform_group.add(platform)

		# generate enemies
		if score > 1000 and len(enemy_group) == 0:  # Only spawn if there are no enemies on the screen
			if random.randint(1, ENEMY_SPAWN_RATE) == 1:
				enemy_x = random.randint(0, SCREEN_WIDTH - 60)
				enemy_y = -60
				enemy = Enemy(enemy_x, enemy_y)
				enemy_group.add(enemy)
				last_enemy_y = enemy_y


		# update platforms and enemies
		platform_group.update(scroll)
		enemy_group.update(scroll)

		# update score
		if scroll > 0:
			score += scroll

		# draw line at previous high score
		pygame.draw.line(screen, LINT, (0, score - high_score + SCROLL_THRESH), (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3 )
		draw_text('HIGH SCORE', font_small, LINT, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

		# draw sprites
		platform_group.draw(screen)
		enemy_group.draw(screen)
		levi.draw()

		# draw panel
		draw_panel()

		# check for collision with enemies
		if pygame.sprite.spritecollide(levi, enemy_group, False):
			game_over = True
			pygame.mixer.music.pause() # pause the music
			death_sound.play()

		# check game over
		if levi.rect.top > SCREEN_HEIGHT:
			game_over = True
			pygame.mixer.music.pause()
			death_sound.play()


	else: # showing the 'game over' screen
		if fade_counter < SCREEN_WIDTH:
			fade_counter += 7
			for i in range(0, 6, 2):
				screen.blit(game_over_image, (0, i * 100), (0, i * 100, fade_counter, 100))
				screen.blit(game_over_image, (SCREEN_WIDTH - fade_counter, (i + 1) * 100),(SCREEN_WIDTH - fade_counter, (i + 1) * 100, SCREEN_WIDTH, 100))
		else:
			# update high score
			if score > high_score:
				high_score = score
				with open(SCORE_FILE, 'w') as file:
					file.write(str(high_score))
			# text for the 'game over' screen
			draw_text('GAME OVER!', font_big, WHITE, 120, 150)
			draw_text('SCORE: ' + str(score), font_small, WHITE, 136, 200)
			draw_text('High SCORE: ' + str(high_score), font_small, WHITE, 110, 250)
			draw_text('PRESS SPACE TO PLAY AGAIN', font_big, WHITE, 30, 300)

			# when space key is pressed to play again
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				pygame.mixer.music.unpause() # resume the music
				# reset game variables
				game_over = False
				score = 0
				scroll = 0
				fade_counter = 0
				# reposition levi(the player)
				levi.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
				# reset platforms and enemies
				platform_group.empty()
				enemy_group.empty()
				# create starting platform
				platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
				platform_group.add(platform)

	# event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# update high score
			if score > high_score:
				high_score = score
				with open(SCORE_FILE, 'w') as file:
					file.write(str(high_score))
			run = False

    # update display window
	pygame.display.update()


pygame.quit()


