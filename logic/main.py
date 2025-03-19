import pygame
import sys
from map_class import maps, map_movement
from movement import collision
from encounter_logic import is_encounter, choose_pokemon
import pokemon_data as pokeData

STEP = 50
TESTSTEP = 500

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.Menu = self.Menu()
        self.menu_visible = False
        self.clock = pygame.time.Clock()
        self.encounter_screen_visible = False


        # Set up the window
        self.window_size = (600, 600)
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Pokemon Yellow")

        # Set up the player
        self.player_x, self.player_y = 40, 40
        player_image = pygame.image.load("G:/My Drive/python/Pokemon Yellow/logic/PlayerDown.PNG")
        player_width, player_height = self.player_x, self.player_y
        self.player_image = pygame.transform.scale(player_image, (player_width, player_height))
        self.player_rect = self.player_image.get_rect()
        self.player_pos = [300, 300]
        # Map position
        self.x, self.y = 25, 25

    class Encounter():
        def __init__(self):
            super().__init__()
            self.level, self.species = choose_pokemon('Route 1')
            self.wild_pokemon = pokeData.Wild_pokemon(level=self.level, species=self.species.lower())
            self.opponent_pokemon = pygame.image.load(self.wild_pokemon.front_pic)
            self.opponent_pokemon = pygame.transform.scale(self.opponent_pokemon, (300, 300))
            self.opponent_pokemon_rect = self.opponent_pokemon.get_rect()
            self.opponent_pokemon_rect.topright = (100, 0)
            self.owned_pokemon = pygame.image.load(self.wild_pokemon.back_pic)
            self.owned_pokemon = pygame.transform.scale(self.owned_pokemon, (200, 200))
            self.owned_pokemon_rect = self.owned_pokemon.get_rect()
            self.owned_pokemon_rect.bottomleft = (500, 600)
            print(vars(self.wild_pokemon))
        
        def display_encounter(self):
            if self.opponent_pokemon_rect.right >= 600:
                game.window.fill((0, 0, 0))
                game.window.blit(self.opponent_pokemon, self.opponent_pokemon_rect)
                game.window.blit(self.owned_pokemon, self.owned_pokemon_rect)
            else:
                while self.opponent_pokemon_rect.right < 600:
                    # Move the opponent Pokemon
                    self.opponent_pokemon_rect.right += 1
                    # Move the owned Pokemon
                    self.owned_pokemon_rect.left -= 1
                    game.window.fill((0, 0, 0))
                    game.window.blit(self.opponent_pokemon, self.opponent_pokemon_rect)
                    game.window.blit(self.owned_pokemon, self.owned_pokemon_rect)
                    pygame.display.flip()

    def hide_menu(self):
        self.menu_visible = False
        self.Menu.menu.fill((255, 255, 255))

    def show_menu(self):
        self.menu_visible = True
        self.Menu.selected_option = 0

    def show_encounter(self):
        self.encounter_screen_visible = True
        self.pokemon_encounter = self.Encounter()
        self.pokemon_encounter.wild_pokemon.load_starting_data()
        self.pokemon_encounter.wild_pokemon.starting_exp()

    def hide_encounter(self):
        self.encounter_screen_visible = False

    def select_menu_option(self):
        selected_option = self.Menu.menu_options[self.Menu.selected_option]
        if selected_option == 'Exit':
            pygame.quit()
            sys.exit()
        elif selected_option == 'Pokedex':
            self.Menu.Pokedex.show_pokedex()
        elif selected_option == 'Items':
            self.Menu.Item_bag_menu.show_item_bag()
        else:
            print(selected_option)

    class Menu():
        # Main menu in game
        def __init__(self):
            super().__init__()
            self.menu_options = ['Pokedex', 'Pokemon', 'Items','Player', 'Save', 'Option','Exit']
            self.selected_option = 0
            self.menu_width = 200
            self.menu_height = 600
            self.menu = pygame.Surface((self.menu_width, self.menu_height))
            self.menu.fill((255, 255, 255))
            self.font = pygame.font.Font(None, 50)
            self.text_color = (0, 0, 0)
            self.selected_color = (0, 0, 0)
            self.unselected_color = (0, 0, 0)
            self.Pokedex = self.Pokedex()
            self.Item_bag_menu = self.Item_bag_menu()
            # self.current_area = self.current_area()

        def move_menu_selection(self, direction):
            self.menu.fill((255, 255, 255))  # Clear the menu surface
            self.selected_option = (self.selected_option + direction) % len(self.menu_options)

        def display_menu(self):
            # Draw border around the menu
            pygame.draw.rect(self.menu, (0, 0, 0), pygame.Rect(0, 0, self.menu_width, self.menu_height), 1)

            for i, option in enumerate(self.menu_options):
                text = self.font.render(option, True, self.text_color)
                if i == self.selected_option:
                    text = self.font.render(option, True, self.selected_color)
                else:
                    text = self.font.render(option, True, self.unselected_color)
                text_rect = text.get_rect()
                text_rect.topleft = (40, 60 * i + 10)
                self.menu.blit(text, text_rect)

            # Draw arrow pointing at selected option
            arrow_surface = self.font.render('>', True, self.selected_color)
            arrow_rect = arrow_surface.get_rect()
            arrow_rect.topleft = (self.menu_width // 10, 7.5 + self.selected_option * 60)
            self.menu.blit(arrow_surface, arrow_rect)
            game.window.blit(self.menu, (0, 0))
        
        class Owned_pokemon_menu():
            def __init__(self):
                super().__init__()
                

        class Item_bag_menu():
            def __init__(self):
                super().__init__()
                self.item_bag_visible = False
                self.background = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_menu_background.png')
                self.background = pygame.transform.scale(self.background, (600, 450))
                self.background_rect = self.background.get_rect()
                self.background_rect.topleft = (0,0)
                self.poke_ball_pouch_bag = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_poke_balls_pouch.png')
                self.poke_ball_pouch_bag = pygame.transform.scale(self.poke_ball_pouch_bag, (160,151))
                self.poke_ball_pouch_bag_rect = self.poke_ball_pouch_bag.get_rect()
                self.poke_ball_pouch_bag_rect.topleft = (17, 124)
                self.key_items_pouch_bag = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_key_items_pouch_sprite.png')
                self.key_items_pouch_bag = pygame.transform.scale(self.key_items_pouch_bag, (170,145))
                self.key_items_pouch_bag_rect = self.key_items_pouch_bag.get_rect()
                self.key_items_pouch_bag_rect.topleft = (15, 128)
                self.items_pouch_bag = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_items_pouch.png')
                self.items_pouch_bag = pygame.transform.scale(self.items_pouch_bag, (150,150))
                self.items_pouch_rect = self.items_pouch_bag.get_rect()
                self.items_pouch_rect.topleft = (25, 125)
                self.items_tag = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_tag_itmes.png')
                self.items_tag = pygame.transform.scale(self.items_tag, (210, 90))
                self.items_tag_rect = self.items_tag.get_rect()
                self.items_tag_rect.topleft = (0, -2)
                self.key_items_tag = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_tag_key_items.png')
                self.key_items_tag = pygame.transform.scale(self.key_items_tag, (213, 92))
                self.key_items_tag_rect = self.key_items_tag.get_rect()
                self.key_items_tag_rect.topleft = (0, -3)
                self.poke_balls_pouch_tag = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_tag_poke_balls.png')
                self.poke_balls_pouch_tag = pygame.transform.scale(self.poke_balls_pouch_tag, (218, 94))
                self.poke_balls_tag_rect = self.poke_balls_pouch_tag.get_rect()
                self.poke_balls_tag_rect.topleft = (-2, -2)
                self.switch_pouch_arrow_right = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_pouch_select_right_arrow.png')
                self.switch_pouch_arrow_right = pygame.transform.scale(self.switch_pouch_arrow_right, (50, 50))
                self.switch_pouch_arrow_right = self.switch_pouch_arrow_right.get_rect()
                self.switch_pouch_arrow_left = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_pouch_select_left_arrow.png')
                self.switch_pouch_arrow_left = pygame.transform.scale(self.switch_pouch_arrow_left, (50, 50))
                self.switch_pouch_arrow_left = self.switch_pouch_arrow_left.get_rect()
                self.scroll_down_items_in_pouch_arrow = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/menu/bag_items_list_down_arrow.png')
                self.scroll_down_items_in_pouch_arrow = pygame.transform.scale(self.scroll_down_items_in_pouch_arrow, (50, 50))
                self.scroll_down_items_in_pouch_arrow = self.scroll_down_items_in_pouch_arrow.get_rect()
                self.pouches_in_bag = ['Items','Key Items', 'Poke Balls']
                self.current_pouch_in_bag = self.pouches_in_bag[0]
                self.items_in_key_items_pouch = ['Key Test 1', 'Key Test 2', 'Key Test 3', 'Key Test 4', 'Key Test 5', 'Key Test 1', 'Key Test 2', 'Key Test 3', 'Key Test 4', 'Key Test 5']
                self.items_in_poke_balls_pouch = ['Balls Test 1', 'Balls Test 2', 'Balls Test 3', 'Balls Test 4', 'Balls Test 5','Key Test 1', 'Key Test 2', 'Key Test 3', 'Key Test 4', 'Key Test 5']
                self.items_in_items_pouch = ['Items Test 1', 'Items Test 2', 'Items Test 3', 'Items Test 4', 'Items Test 5','Key Test 1', 'Key Test 2', 'Key Test 3', 'Key Test 4', 'Key Test 5']
                self.items_in_all_pouches = {
                    'Items': self.items_in_items_pouch,
                    'Key Items': self.items_in_key_items_pouch,
                    'Poke Balls': self.items_in_poke_balls_pouch
                }
                self.font = pygame.font.SysFont(None, 40)

                self.total_items = len(self.items_in_all_pouches[self.current_pouch_in_bag])
                self.visible_items = min(5, self.total_items)
                self.start_index = 0
                self.selected_index = 0
                self.selected_item_index = 0
            
            def scroll_up(self):
                    if self.selected_item_index != 0:
                        self.selected_item_index -= 1
                    self.selected_index -= 1

                    if self.selected_index < 0:
                        self.start_index -= 1
                        self.selected_index = 0

                        if self.start_index < 0:
                            self.start_index = 0
            
            def scroll_down(self):
                if self.selected_item_index != len(self.items_in_all_pouches[self.current_pouch_in_bag]) - 1:
                    self.selected_item_index += 1
                self.selected_index += 1

                if self.selected_index >= self.visible_items:
                    self.start_index += 1
                    self.selected_index = self.visible_items - 1

                    if self.start_index + self.visible_items > self.total_items:
                        self.start_index = self.total_items - self.visible_items


            def show_item_bag(self):
                game.menu_visible = False
                self.item_bag_visible = True
            
            def hide_item_bag(self):
                self.item_bag_visible = False
                game.menu_visible = True
            
            def display_item_bag(self):
                self.bag_displays = {
                    'Items': {
                        'tag': self.items_tag,
                        'tag rect': self.items_tag_rect,
                        'bag': self.items_pouch_bag,
                        'bag rect': self.items_pouch_rect
                    },
                    'Key Items': {
                        'tag': self.key_items_tag,
                        'tag rect': self.key_items_tag_rect,
                        'bag': self.key_items_pouch_bag,
                        'bag rect': self.key_items_pouch_bag_rect
                    },
                    'Poke Balls': {
                        'tag': self.poke_balls_pouch_tag,
                        'tag rect': self.poke_balls_tag_rect,
                        'bag': self.poke_ball_pouch_bag,
                        'bag rect': self.poke_ball_pouch_bag_rect
                    }
                }
                game.window.fill((0, 0, 0))
                game.window.blit(self.background, self.background_rect)
                for i, item in enumerate(self.items_in_all_pouches[self.current_pouch_in_bag][self.start_index:self.start_index + self.visible_items]):
                    text = self.font.render(item, True, (0, 0, 0))
                    y = 40 + i * 45
                    game.window.blit(text, (250, y))

                    if i == self.selected_index:
                        arrow_text = self.font.render(">", True, (255, 0, 0))
                        game.window.blit(arrow_text, (230, y - 3))
                self.selected_item = self.items_in_all_pouches[self.current_pouch_in_bag][self.selected_item_index]
                game.window.blit(self.bag_displays[self.current_pouch_in_bag]['tag'], self.bag_displays[self.current_pouch_in_bag]['tag rect'])
                game.window.blit(self.bag_displays[self.current_pouch_in_bag]['bag'], self.bag_displays[self.current_pouch_in_bag]['bag rect'])

            
            def new_pouch(self, dir):
                self.selected_item_index = 0
                self.start_index = 0
                self.selected_index = 0
                index = self.pouches_in_bag.index(self.current_pouch_in_bag)
                pouch_count = len(self.pouches_in_bag)
                if dir == 'right':
                    self.current_pouch_in_bag = self.pouches_in_bag[(index + 1) % pouch_count]
                elif dir == 'left':
                    self.current_pouch_in_bag = self.pouches_in_bag[(index - 1) % pouch_count]



        # Set up PokeDex
        class Pokedex():
            def __init__(self):
                super().__init__()
                self.pokemon_number_in_dict = 1
                self.pokedex_visible = False
                self.pokedex_background = pygame.image.load('G:/My Drive/python/Pokemon Yellow/Sprites/pokedex_background.png')
                self.pokedex_background = pygame.transform.scale(self.pokedex_background, (600, 600))
                self.pokedex_background_rect = self.pokedex_background.get_rect(topleft=(0,0))
                self.update_values()

            # Update the pokedex page when init and scrolling
            def update_values(self):
                self.pokemon_no = str(self.pokemon_number_in_dict)
                self.pokedex_name = pokeData.pokedex_values[self.pokemon_no]['name']
                self.pokedex_ht = '??'
                self.pokedex_wt ='??'
                self.pokedex_descr = pokeData.pokedex_values[self.pokemon_no]['description'].split(' ')
                self.pokedex_font = pygame.font.Font(None, 30)
                self.pokedex_font_color = (36, 36, 36)
                if self.pokemon_number_in_dict < 10:
                    self.pokedex_no = self.pokedex_font.render(f'No 00{self.pokemon_number_in_dict}', True, self.pokedex_font_color)
                elif self.pokemon_number_in_dict < 100:
                    self.pokedex_no = self.pokedex_font.render(f'No 0{self.pokemon_number_in_dict}', True, self.pokedex_font_color)
                else:
                    self.pokedex_no = self.pokedex_font.render(f'No {self.pokemon_number_in_dict}', True, self.pokedex_font_color)            
                self.pokedex_no_rect = self.pokedex_no.get_rect()
                self.pokedex_no_rect.topright = (580, 20)
                # self.pokedex_descr = pokeData.pokedex[kanto_pokedex[self.pokemon_number_in_dict]].split(' ')
                self.pokedex_info_cut1 = len(self.pokedex_descr) // 3
                self.pokedex_info_cut2 = 2 * len(self.pokedex_descr) // 3
                self.pokedex_desc_img1 = self.pokedex_font.render(' '.join(self.pokedex_descr[:self.pokedex_info_cut1]), True, self.pokedex_font_color)
                self.pokedex_desc_img_rect1 = self.pokedex_desc_img1.get_rect()
                self.pokedex_desc_img_rect1.topleft = (50, 340)
                self.pokedex_desc_img2 = self.pokedex_font.render(' '.join(self.pokedex_descr[self.pokedex_info_cut1:self.pokedex_info_cut2]), True, self.pokedex_font_color)
                self.pokedex_desc_img_rect2 = self.pokedex_desc_img2.get_rect()
                self.pokedex_desc_img_rect2.topleft = (50, 390)
                self.pokedex_desc_img3 = self.pokedex_font.render(' '.join(self.pokedex_descr[self.pokedex_info_cut2:]), True, self.pokedex_font_color)
                self.pokedex_desc_img_rect3 = self.pokedex_desc_img3.get_rect()
                self.pokedex_desc_img_rect3.topleft = (50, 440)
                self.pokedex_img_path = f"Sprites/front/{pokeData.pokedex_values[self.pokemon_no]['name']}.png"
                self.pokedex_pokemon_img = pygame.image.load(self.pokedex_img_path)
                self.pokedex_pokemon_img = pygame.transform.scale(self.pokedex_pokemon_img, (200, 200))
                self.pokedex_pokemon_img_rect = self.pokedex_pokemon_img.get_rect()
                self.pokedex_pokemon_img_rect.topright = (540, 80)
            
            #Show pokedex to screen
            def display_pokedex(self):
                game.window.fill((0, 0, 0))
                game.window.blit(self.pokedex_background, self.pokedex_background_rect)
                game.window.blit(self.pokedex_no, self.pokedex_no_rect)
                game.window.blit(self.pokedex_desc_img1, self.pokedex_desc_img_rect1)
                game.window.blit(self.pokedex_desc_img2, self.pokedex_desc_img_rect2)
                game.window.blit(self.pokedex_desc_img3, self.pokedex_desc_img_rect3)
                game.window.blit(self.pokedex_pokemon_img, self.pokedex_pokemon_img_rect)

            # Pokemon number + 1 to pokedex screen
            def scroll_up(self):
                if self.pokemon_number_in_dict == 151:
                    self.pokemon_number_in_dict = 1
                else:
                    self.pokemon_number_in_dict += 1
                self.update_values()
            
            # Pokemon number - 1 to pokedex screen
            def scroll_down(self):
                if self.pokemon_number_in_dict == 1:
                    self.pokemon_number_in_dict = 151
                else:
                    self.pokemon_number_in_dict -= 1
                self.update_values()

            def show_pokedex(self):
                game.menu_visible = False
                self.pokedex_visible = True
            
            def hide_pokedex(self):
                self.pokedex_visible = False
    
    # Get area player is in
    def current_area(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Key pressed to movement in map movement
            key_movements = {
                pygame.K_LEFT: ('x', STEP, 'Left'),
                pygame.K_RIGHT: ('x', -1 * STEP, 'Right'),
                pygame.K_UP: ('y', STEP, 'Up'),
                pygame.K_DOWN: ('y', -1 * STEP, 'Down'),
                pygame.K_a: ('x', TESTSTEP, 'A'),
                pygame.K_d: ('x', -1 * TESTSTEP, 'D'),
                pygame.K_w: ('y', TESTSTEP, 'W'),
                pygame.K_s: ('y', -1 * TESTSTEP, 'S')
            }

            # Key pressed listeners
            if event.type == pygame.KEYDOWN:
                if not self.menu_visible and not self.encounter_screen_visible and not self.Menu.Pokedex.pokedex_visible and not self.Menu.Item_bag_menu.item_bag_visible:
                    is_surfing = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in key_movements:
                            axis, step, direction = key_movements[event.key]
                            if collision(self.x, self.y, direction):
                                if axis == 'x':
                                    self.x += step
                                elif axis == 'y':
                                    self.y += step
                                if is_encounter(self.x, self.y):
                                    self.show_encounter()
                                map_movement(axis, step, maps)
                        # elif event.key == pygame.K_SPACE:
                            # with open('collisions.py', 'a') as file:
                            #     file.write(f'{self.x, self.y}\n')
                            # with open('ledgeup.py', 'a') as file:
                            #     file.write(f'{self.x, self.y}\n')
                            # with open('logic/encounter_areas.py', 'a') as file:
                            #     file.write(f'{self.x, self.y}\n'
                        elif event.key == pygame.K_q:
                            if not self.encounter_screen_visible:
                                self.show_menu()

                elif self.menu_visible:
                    # Navigate menu options
                    if event.key == pygame.K_q:
                        self.hide_menu()
                    elif event.key == pygame.K_UP:
                        self.Menu.move_menu_selection(-1)
                    elif event.key == pygame.K_DOWN:
                        self.Menu.move_menu_selection(1)
                    elif event.key == pygame.K_RETURN:
                        self.select_menu_option()
                
                elif self.Menu.Pokedex.pokedex_visible:
                    self.hide_menu()
                    if event.key == pygame.K_o:
                        self.Menu.Pokedex.pokedex_visible = False
                        self.show_menu()
                    elif event.key == pygame.K_LEFT:
                        self.Menu.Pokedex.scroll_down()
                    elif event.key == pygame.K_RIGHT:
                        self.Menu.Pokedex.scroll_up()

                elif self.Menu.Item_bag_menu.item_bag_visible:
                    if event.key == pygame.K_o:
                        self.Menu.Item_bag_menu.hide_item_bag()
                    elif event.key == pygame.K_LEFT:
                        self.Menu.Item_bag_menu.new_pouch('left')
                    elif event.key == pygame.K_RIGHT:
                        self.Menu.Item_bag_menu.new_pouch('right')
                    elif event.key == pygame.K_UP:
                        self.Menu.Item_bag_menu.scroll_up()
                    elif event.key == pygame.K_DOWN:
                        self.Menu.Item_bag_menu.scroll_down()
                    elif event.key == pygame.K_RETURN:
                        print(self.Menu.Item_bag_menu.selected_item)
                elif event.key == pygame.K_o:
                    self.encounter_screen_visible = False

                


    def draw(self):
        self.window.fill((0, 0, 0))  # Clear the window

        # Draw the maps
        for map in maps:
            x = maps[map]['x']
            y = maps[map]['y']
            image = maps[map]['image']
            self.window.blit(image, (x, y))

        # Draw the player
        self.player_rect.center = self.player_pos
        self.window.blit(self.player_image, self.player_rect)

        # Draw the Pokedex
        if self.Menu.Pokedex.pokedex_visible:
            self.Menu.Pokedex.display_pokedex()

        # Draw the encounter
        if self.encounter_screen_visible:
            self.pokemon_encounter.display_encounter()
    
        # Draw the menu
        elif self.menu_visible:
            self.Menu.display_menu()
        
        elif self.Menu.Item_bag_menu.item_bag_visible:
            self.Menu.Item_bag_menu.display_item_bag()

        # Update the display
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)

    def run(self):
        while True:
            self.handle_events()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
