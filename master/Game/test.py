from tower import Tower
from circle import Circle
from square import Square
from ice_tower import Ice_Tower
from enemy import Enemy
from red_giant import Red_Orc
from yellow_dwarf import Yellow_Dwarf
from orange_giant import Orange_Giant
from pink_bandit import Pink_Bandit
from level_one import Level_One
import time


class Tester:
    """
    Tester class that runs in setup()
    Tests the functions within each class
    """
    circle = Circle(100, 100)
    square = Square(100, 100)
    ice_tower = Ice_Tower(100, 100)
    yellow_dwarf = Yellow_Dwarf(100, 100)
    red_orc = Red_Orc(100, 100)
    orange_giant = Orange_Giant(100, 100)
    pink_bandit = Pink_Bandit(100, 100)
    level_one = Level_One()
    enemies = []

    def test_tower(self):
        """
        Function which tests the functions of the Tower classes
        """
        # Tests initialization of tower
        assert self.circle.tier == 1, "Should start at tier 1"
        assert self.circle.xLoc == 100, "x value should equal to passed parameters"
        assert self.circle.damage == 35, "Damage should start at 35"
        assert self.circle.type == "circle", "Tower type should be circle"
        assert self.square.tier == 1, "Should start at tier 1"
        assert self.square.yLoc == 100, "y value should be equal to passed in parameters"
        assert self.square.projectileY == 100, "Projectile should start at the tower location"
        assert self.square.upgrade_cost == 160, "Upgrade should cost 160 for tier 2"
        assert self.square.type == "square", "Tower type should be square"
        assert self.ice_tower.type == "ice tower", "Tower type should be ice tower"
        assert self.ice_tower.upgrade_cost == 120, "Upgrade cost starts at 120 for tier 2"

        # Tests tower upgrade()
        self.circle.upgrade()
        assert self.circle.tier == 2, "Circle: should increase tower tier by one"
        assert self.circle.projectile_speed == 1.5, "Circle: should increase projectile speed by 0.1"
        assert self.circle.tower_range == 100, "Circle: should increase range by 15"
        assert self.circle.upgrade_cost == 160, "Circle: upgrade should cost 160 for tier 3"
        self.square.upgrade()
        self.square.upgrade()
        assert self.square.tier == 3, "Should have reached tier three"
        assert self.square.tower_range == 110, "Range should have increased by 30"
        assert self.square.damage == 285, "Damage should be set to 285"
        assert self.square.projectile_speed == 1, "Should not change projectile speed"
        self.ice_tower.upgrade()
        assert self.ice_tower.upgrade_cost == 200, "Should cost 200 for tier three"
        assert self.ice_tower.tower_range == 95, "Should have a range of 90 at tier two"
        assert self.ice_tower.slowing_time == 1.5, "Should have a slowing effect for 1.5 seconds"
        assert self.ice_tower.projectile_speed == 1.15, "Should have increased projectile speed by 0.05"

        # Test tower find_enemy()
        self.enemies.append(Yellow_Dwarf(100, 0))
        self.enemies.append(Red_Orc(100, 205))
        self.circle.find_enemy(self.enemies)
        assert self.circle.targeted_enemy.type == "yellow dwarf", "Circle should have found yellow dwarf"
        self.ice_tower.find_enemy(self.enemies)
        assert self.ice_tower.targeted_enemy is None, "Ice tower should have nothing in range"
        self.enemies.pop(0)
        self.circle.find_enemy(self.enemies)
        assert self.circle.targeted_enemy is None, "Circle should now have nothing in range"
        self.square.find_enemy(self.enemies)
        assert self.square.targeted_enemy.type == "red orc", "Square should have found red giant"
        self.square.trgtd_enemy = None
        self.enemies.pop(0)
        self.square.find_enemy(self.enemies)
        assert self.square.targeted_enemy is None, "Should find nothing in an empty list"

        # Test tower target_enemy()
        self.enemies.append(Yellow_Dwarf(100, 110))
        self.circle.find_enemy(self.enemies)
        self.circle.target_enemy()
        assert self.circle.targeted_enemy is None, "Should have reset the targeted_enemy"
        self.enemies[0] = Yellow_Dwarf(115, 110)
        self.circle.find_enemy(self.enemies)
        self.circle.target_enemy()
        assert self.circle.targetX == 115, "Target x should not change"
        assert self.circle.targetY == 117.5, "Target y should increase"
        self.ice_tower.xLoc = 800
        self.ice_tower.yLoc = 800
        self.enemies[0] = Yellow_Dwarf(750, 777)
        self.ice_tower.find_enemy(self.enemies)
        self.ice_tower.target_enemy()
        assert self.ice_tower.targetX == 766, "Target x should increase"
        assert self.ice_tower.targetY == 777, "Target y should not change"
        self.ice_tower.targeted_enemy.speed = self.ice_tower.targeted_enemy.slowed_speed
        self.ice_tower.target_enemy()
        assert self.ice_tower.targetX == 761.2, "Target x should increase"
        assert self.ice_tower.targetY == 777, "Target y should not change"
        self.enemies.pop(0)

        # Test tower detect_enemy()
        self.enemies.append(Yellow_Dwarf(150, 50))
        self.circle.find_enemy(self.enemies)
        self.circle.target_enemy()
        while self.circle.targeted_enemy is not None:
            self.enemies[0].update()
            self.circle.shoot_projectile()
            self.circle.detect_enemy_hit()
        assert self.enemies[0].health == 55, "Health should lower by 55"
        assert self.circle.enemy_targeted is False, "Targeting should reset"
        self.circle = Circle(512, 220)
        self.circle.upgrade()
        self.circle.upgrade()
        self.enemies[0] = Red_Orc(560, 318)
        self.circle.find_enemy(self.enemies)
        self.circle.target_enemy()
        while self.circle.targeted_enemy is not None:
            self.enemies[0].update()
            self.circle.shoot_projectile()
            self.circle.detect_enemy_hit()
        assert self.enemies[0].health == 380, "Targeting should have reset, projectile should not have hit"
        assert self.circle.enemy_targeted is False, "Targeting should have reset"

    def test_enemy(self):
        """
        Function which tests the functions of the Enemy classes
        """
        # Test initializing enemy
        assert self.yellow_dwarf.xLoc == 100, "Should equal value passed in"
        assert self.red_orc.yLoc == 100, "Should equal value passed in"
        assert self.yellow_dwarf.type == "yellow dwarf", "Type should be yellow dwarf"
        assert self.red_orc.type == "red orc", "Type should be red giant"
        assert self.yellow_dwarf.speed == 0.8, "Speed should start as original speed"
        assert self.red_orc.slowed_speed == 0.56, "Slowed speed should be 70% of original speed"
        assert self.orange_giant.type == "orange giant", "Type should be orange giant"
        assert self.pink_bandit.type == "pink bandit", "Type should be pink bandit"
        assert self.orange_giant.speed == 0.6, "Speed should be original speed"
        assert self.pink_bandit.slowed_speed == 1.1*0.7, "Slowed speed should be 70% original speed"

        # Test enemy.update()
        self.yellow_dwarf.is_slowed = True
        self.yellow_dwarf.time_slowed = time.time() + 1
        self.yellow_dwarf.update()
        assert self.yellow_dwarf.is_slowed is True, "Should be slowed"
        assert self.yellow_dwarf.speed == 0.56, "Speed should equal slowed speed"
        self.yellow_dwarf.time_slowed = time.time()
        self.yellow_dwarf.update()
        assert self.yellow_dwarf.is_slowed is False, "Slow should have ended"
        self.red_orc = Red_Orc(560, 320)
        self.red_orc.update()
        assert self.red_orc.xLoc == 560.8, "Location should have increased by speed"
        assert self.red_orc.yLoc == 320, "y coordinate should not have changed"
        self.red_orc = Red_Orc(800, 400)
        self.red_orc.update()
        assert self.red_orc.yLoc == 400.8, "y coordinate should have increased"
        assert self.red_orc.is_invisible is True, "Should be invisible"
        self.red_orc = Red_Orc(800, 480)
        self.red_orc.update()
        assert self.red_orc.xLoc == 800.8, "x coordinate should have increased"
        assert self.red_orc.yLoc == 480, "y coordinate should not have changed"
        assert self.red_orc.is_invisible is False, "Should not be invisible"
        self.red_orc.xLoc = 1281
        self.red_orc.update()
        assert self.red_orc.course_passed is True, "Should have passed course"

        # Test enemy.is_living()
        self.yellow_dwarf.health = 0
        assert self.yellow_dwarf.is_living() is False, "YD should be dead with 0 health"
        self.red_orc.health = 0
        assert self.red_orc.is_living() is False, "RO should be dead with 0 health"
        self.yellow_dwarf.health = 100
        assert self.yellow_dwarf.is_living() is True, "YD should be alive with positive health"
        self.red_orc.health = -120349512432
        assert self.red_orc.is_living() is False, "RO should be dead with any health below 0"

    def test_level_one(self):
        """
        Function which tests the functions from the Level_One class
        Note: Limited functions appear here as they rely on mouseX and mouseY
        to do anything
        """
        assert self.level_one.tier_two_locked is True, "Tier two should be locked at wave 0"
        assert self.level_one.tier_three_locked is True, "Tier three should be locked at wave 0"
        self.level_one.wave = 3
        self.level_one.is_upgrade_locked()
        assert self.level_one.tier_two_locked is False, "Tier two unlocked by wave 3"
        assert self.level_one.tier_three_locked is True, "Tier three should still be locked"
        self.level_one.wave = 5
        self.level_one.is_upgrade_locked()
        assert self.level_one.tier_two_locked is False, "Tier two unlocked by wave 5"
        assert self.level_one.tier_three_locked is False, "Tier three unlocked by wave 5"

        self.level_one.lives = 20
        assert self.level_one.is_game_over() is False, "Game should not be over with full lives"
        self.level_one.lives = 0
        assert self.level_one.is_game_over() is True, "Game should be over with 0 lives"
        self.level_one.lives = 20
        self.level_one.wave = 7
        assert self.level_one.is_level_passed() is True, "Game should be won"
        self.level_one.wave = 6
        assert self.level_one.is_level_passed() is False, "Game should not be over yet"
