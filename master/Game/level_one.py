from enemy import Enemy
from yellow_dwarf import Yellow_Dwarf
from red_giant import Red_Orc
from orange_giant import Orange_Giant
from pink_bandit import Pink_Bandit
from tower import Tower
from circle import Circle
from square import Square
from ice_tower import Ice_Tower
import random


class Level_One:
    gold = 340
    lives = 20
    enemies = []
    towers = []

    land_plots = []
    land_plots.append([620, 170])
    land_plots.append([502, 220])
    land_plots.append([920, 430])
    land_plots.append([1050, 530])
    land_plots.append([1180, 427])
    land_plots.append([743, 263])
    land_plots.append([501, 100])
    land_plots.append([650, 260])
    land_plots.append([610, 384])
    build_tower = False
    tower_options = []
    tower_options.append([150, 640])
    tower_options.append([250, 640])
    build_loc = []

    wave = 0
    tutorial_page = 1
    done_spawning = False
    playing_level = False
    tier_two_locked = True
    tier_three_locked = True
    correct_mouse = False
    restart = False
    quit = False
    completed = False
    degree = 0

    def spawn_enemies(self):
        """
        Draws all enemies, and spawns new enemies as the wave increases
        """
        # Adding enemies to the wave
        if not self.done_spawning:
            if self.wave == 1:
                for i in range(3):
                    self.enemies.append(Yellow_Dwarf(randomX, -10-(i*15)))
                for i in range(4):
                    self.enemies.append(Yellow_Dwarf(randomX, -140-(i*15)))
                self.done_spawning = True
            if self.wave == 2:
                self.enemies.append(Yellow_Dwarf(563, -10))
                self.enemies.append(Yellow_Dwarf(558, -20))
                self.enemies.append(Red_Orc(560, -45))
                self.enemies.append(Red_Orc(561, -65))
                for i in range(4):
                    self.enemies.append(Yellow_Dwarf(randomX, -160-(i*15)))
                self.done_spawning = True
            if self.wave == 3:
                self.enemies.append(Orange_Giant(560, -10))
                for i in range(3):
                    self.enemies.append(Yellow_Dwarf(randomX, -200-(i*15)))
                for i in range(2):
                    self.enemies.append(Red_Orc(randomX, -260-(i*15)))
                self.done_spawning = True
            if self.wave == 4:
                for i in range(3):
                    enemy_x = random.randint(557, 563)
                    self.enemies.append(Red_Orc(randomX, -10-(i*17)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(randomX, -60-(i*15)))
                for i in range(3):
                    enemy_x = random.randint(557, 563)
                    self.enemies.append(Red_Orc(randomX, -230-(i*21)))
                self.done_spawning = True
            if self.wave == 5:
                for i in range(3):
                    self.enemies.append(Red_Orc(randomX, -10-(i*17)))
                for i in range(2):
                    self.enemies.append(Pink_Bandit(randomX, -10-(i*20)))
                for i in range(5):
                    self.enemies.append(Red_Orc(randomX, -200-(i*20)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(randomX, -330-(i*15)))
                self.done_spawning = True
            if self.wave == 6:
                for i in range(2):
                    self.enemies.append(Red_Orc(randomX, -10-(i*30)))
                for i in range(3):
                    self.enemies.append(Pink_Bandit(randomX, -100-(i*20)))
                for i in range(2):
                    self.enemies.append(Orange_Giant(randomX, -160-(i*30)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(randomX, -300-(i*15)))
                for i in range(2):
                    self.enemies.append(Red_Orc(randomX, -420-(i*30)))
                self.done_spawning = True
            if self.wave == 7:
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(randomX, -10-(i*15)))
                for i in range(2):
                    self.enemies.append(Pink_Bandit(randomX, -100-(i*20)))
                for i in range(2):
                    self.enemies.append(Orange_Giant(randomX, -180-(i*30)))
                for i in range(3):
                    self.enemies.append(Red_Orc(randomX, -250-(i*20)))
                for i in range(3):
                    self.enemies.append(Orange_Giant(randomX, -340-(i*30)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(randomX, -480-(i*15)))
                for i in range(3):
                    self.enemies.append(Red_Orc(randomX, -600-(i*20)))
                for i in range(2):
                    self.enemies.append(Pink_Bandit(randomX, -700-(i*15)))
                self.done_spawning = True

        # Drawing enemies
        for enemy in self.enemies:
            enemy.draw_enemy()
            enemy.update()
            if not enemy.is_living():
                self.gold += enemy.gold_worth
                self.enemies.remove(enemy)
            if enemy.course_passed:
                self.lives -= enemy.weight
                self.enemies.remove(enemy)

    def draw_level(self):
        """
        Draws the path followed by the enemies, plots where towers can be
        built, and other information
        """
        # Path
        fill(91, 160, 91)
        rect(545, -5, 30, 335)
        rect(545, 305, 250, 30)
        rect(800, 465, 485, 30)
        # Land plots
        fill("#f3f972")
        for plot in self.land_plots:
            ellipse(plot[0], plot[1], 30, 30)
        # Gold bar
        fill(255, 255, 0)
        text("Gold: " + str(self.gold), 100, 75)
        # Number of lives left
        fill(255, 10, 10)
        text("Lives: "+str(self.lives), 100, 55)
        # Spawn next wave
        fill(100, 100, 100)
        rect(100, 100, 50, 50)
        if len(self.enemies) == 0:
            fill(255)
            text("Click to spawn next wave", 100, 165)
        text("Wave: " + str(self.wave) + " / 7", 100, 180)

    def build_towers(self):
        """
        Draws all towers, searches for nearby enemies, targets enemies,
        and attacks targets
        """
        for tower in self.towers:
            tower.draw_tower()
            if tower.is_selected:
                tower.show_range()
                fill(240, 240, 0)
                if tower.tier < 3:
                    rect(tower.xLoc-10, tower.yLoc-50, 20, 20)
                    if tower.tier == 1 and self.tier_two_locked:
                        text("Upgrade locked", tower.xLoc-45, tower.yLoc+40)
                    elif tower.tier == 2 and self.tier_three_locked:
                        text("Upgrade locked", tower.xLoc-45, tower.yLoc+40)
                    else:
                        msg_loc = [tower.xLoc-60, tower.yLoc+40]
                        cost = tower.upgrade_cost
                        text(f"Upgrade cost: {cost}", msg_loc[0], msg_loc[1])
                else:
                    text("Tower at max level!", tower.xLoc-50, tower.yLoc+40)
            has_trgt_enmy = tower.targeted_enemy is not None
            enemy_targetable = not tower.targeted_enemy.is_invisible
            if has_trgtd_enmy is not None and not tower.enemy_targeted:
                tower.target_enemy()
            elif tower.enemy_targeted and has_trgtd_enmy and enemy_targetable:
                tower.shoot_projectile()
                tower.detect_enemy_hit()
            else:
                tower.find_enemy(self.enemies)

        if self.build_tower:
            fill(1, 139, 4)
            ellipse(150, 640, 30, 30)
            fill(204, 12, 2)
            rect(235, 625, 30, 30)
            fill(107, 166, 229)
            ellipse(350, 640, 30, 30)
            fill(240, 240, 10)
            text("Cost: 70", 125, 670)
            text("Cost: 90", 225, 670)
            text("Cost: 80", 325, 670)

    def build_new_tower(self):
        """
        Builds a new tower in the selected land plot
        """
        # Builds Circle
        mouseX_crct = mouseX in range(135, 165)
        mouse_correct = mouseX_crct and mouseY in range(625, 655)
        if self.gold >= 70 and self.build_tower and mouse_cprrect:
            self.towers.append(Circle(self.build_loc[0], self.build_loc[1]))
            self.gold -= 70
            self.build_tower = False
            for plot in self.land_plots:
                correct_x = plot[0] == self.build_loc[0]
                correct_y = plot[1] == self.build_loc[1]
                if correct_x and correct_y:
                    self.land_plots.remove(plot)
            self.build_loc.pop(0)
            self.build_loc.pop(0)

        # Builds Square
        mouseX_crct = mouseX in range(235, 265)
        mouse_correct = mouseX_crct and mouseY in range(625, 655)
        if self.gold >= 90 and self.build_tower and mouse_correct:
            self.towers.append(Square(self.build_loc[0], self.build_loc[1]))
            self.gold -= 90
            self.build_tower = False
            for plot in self.land_plots:
                correct_x = plot[0] == self.build_loc[0]
                correct_y = plot[1] == self.build_loc[1]
                if correct_x and correct_y:
                    self.land_plots.remove(plot)
            self.build_loc.pop(0)
            self.build_loc.pop(0)

        # Builds Ice Tower
        mouseX_crct = mouseX in range(335, 365)
        mouse_correct = mouseX_crct and mouseY in range(625, 655)
        if self.gold >= 80 and self.build_tower and mouse_correct:
            self.towers.append(Ice_Tower(self.build_loc[0], self.build_loc[1]))
            self.gold -= 80
            self.build_tower = False
            for plot in self.land_plots:
                correct_x = plot[0] == self.build_loc[0]
                correct_y = plot[1] == self.build_loc[1
                if correct_x and correct_y:
                    self.land_plots.remove(plot)
            self.build_loc.pop(0)
            self.build_loc.pop(0)

    def upgrade_towers(self):
        """
        Checks whether or not upgrades are locked, and allows
        the player to upgrade a tower if the tower is selected
        and if they have enough gold
        """
        self.is_upgrade_locked()
        for tower in self.towers:
            selected = tower.is_selected
            enough_gold = self.gold >= tower.upgrade_cost
            mouseX_correct = mouseX in range(tower.xLoc-10, tower.xLoc+10)
            mouseY_correct = mouseY in range(tower.yLoc-50, tower.yLoc-30)
            if enough_gold and selected and mouseX_correct and mouseY_correct and tower.tier < 3:
                if tower.tier == 1 and not self.tier_two_locked:
                    self.gold -= tower.upgrade_cost
                    tower.upgrade()
                    tower.is_selected = False
                elif tower.tier == 2 and not self.tier_three_locked:
                    self.gold -= tower.upgrade_cost
                    tower.upgrade()
                    tower.is_selected = False

    def is_upgrade_locked(self):
        """
        Checks how many of the upgrades are locked
        """
        if self.wave > 1:
            self.tier_two_locked = False
        if self.wave > 4:
            self.tier_three_locked = False

    def tower_is_selected(self):
        """
        Checks whether or not the player clicked on a tower, and
        if they have, the tower becomes selected
        """
        for tower in self.towers:
            if mouseX in range(tower.xLoc-25, tower.xLoc+25) and mouseY in range(tower.yLoc-25, tower.yLoc+25):
                if tower.is_selected:
                    tower.is_selected = False
                else:
                    tower.is_selected = True

    def select_land_plot(self):
        """
        Detects whether or not the player has selected a land plot
        If a land plot has been selected, options to build a tower
        appear.
        """
        for plot in self.land_plots:
            if mouseX in range(plot[0]-20, plot[0]+20) and mouseY in range(plot[1]-20, plot[1]+20):
                if self.build_tower:
                    self.build_tower = False
                    self.build_loc.pop(0)
                    self.build_loc.pop(0)
                else:
                    self.build_tower = True
                    self.build_loc.append(plot[0])
                    self.build_loc.append(plot[1])

    def increment_wave(self):
        """
        Increments the wave if the wave has been completed and the user
        has clicked in the box to call a wave
        """
        if mouseX in range(100, 150) and mouseY in range(100, 150) and len(self.enemies) == 0 and self.wave < 7:
            self.wave += 1
            self.done_spawning = False

    def increment_tutorial_page(self):
        """
        Increments the page of the tutorial if the user clicks
        on the next button at the bottom corner of the tutorial image
        """
        if mouseX in range(900, 960) and mouseY in range(540, 580):
            self.tutorial_page += 1

    def is_game_over(self):
        """
        Returns whether or not the player has lost the game
        """
        if self.lives <= 0:
            return True
        return False

    def is_level_passed(self):
        """
        Returns whether or not the player has successfully cleared
        the level
        """
        if self.wave == 7 and len(self.enemies) == 0 and self.lives > 0:
            return True
        return False

    def choose_option(self):
        """
        Allows the user to quit the level if the level is over
        """
        if mouseX in range(480, 800) and mouseY in range(380, 450):
            self.quit = True


    def randomX(self):
        return random.randint(557, 563)
