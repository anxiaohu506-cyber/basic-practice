import pygame
import sys
import random
import math

# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("简化雷霆战机")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# 游戏时钟
clock = pygame.time.Clock()
FPS = 60

# 字体（尝试使用中文字体，若无则用默认字体）
try:
    font = pygame.font.SysFont('simsunnsimsun', 24)
    large_font = pygame.font.SysFont('simsunnsimsun', 48)
except:
    font = pygame.font.Font(None, 24)
    large_font = pygame.font.Font(None, 48)

class Player(pygame.sprite.Sprite):
    """玩家飞机类"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        # 画一个简单的三角形
        points = [(20, 0), (5, 30), (35, 30)]
        pygame.draw.polygon(self.image, GREEN, points)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 30
        self.speed_x = 0
        self.lives = 3
        self.invulnerable = False
        self.invulnerable_timer = 0

    def update(self):
        # 左右移动
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.speed_x = -5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.speed_x = 5
        self.rect.x += self.speed_x

        # 无敌状态计时
        if self.invulnerable:
            if pygame.time.get_ticks() - self.invulnerable_timer > 2000:  # 2秒无敌
                self.invulnerable = False

    def shoot(self):
        """发射子弹"""
        bullet = Bullet(self.rect.centerx, self.rect.top, -1)  # 向上
        return bullet

    def hit(self):
        """玩家被击中"""
        if not self.invulnerable:
            self.lives -= 1
            self.invulnerable = True
            self.invulnerable_timer = pygame.time.get_ticks()
            if self.lives <= 0:
                return True  # 游戏结束
        return False

class Bullet(pygame.sprite.Sprite):
    """子弹类，方向：-1向上（玩家），1向下（敌人）"""
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((3, 10))
        self.image.fill(YELLOW if direction == -1 else RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.direction = direction
        self.speed = 8

    def update(self):
        self.rect.y += self.speed * self.direction
        # 超出屏幕则移除
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    """敌人类（普通敌人，小Boss继承）"""
    # 类变量，用于添加子弹到全局组（由Game在初始化时设置）
    bullet_group = None
    all_sprites_group = None

    def __init__(self, x, y, hp, name, color, size=30):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size//2, size//2), size//2)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.hp = hp
        self.max_hp = hp
        self.name = name
        self.color = color
        self.size = size
        self.shoot_timer = pygame.time.get_ticks()
        self.shoot_delay = random.randint(1000, 3000)  # 随机射击延迟

    def update(self):
        # 敌人移动：缓慢向下
        self.rect.y += 1
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def shoot(self):
        """发射子弹，返回子弹对象（由外部调用后添加到组）"""
        bullet = Bullet(self.rect.centerx, self.rect.bottom, 1)
        return bullet

    def draw_hp_bar(self, surface):
        """绘制血量条"""
        bar_width = self.size
        bar_height = 5
        fill = (self.hp / self.max_hp) * bar_width
        outline_rect = pygame.Rect(self.rect.left, self.rect.top - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.left, self.rect.top - 10, fill, bar_height)
        pygame.draw.rect(surface, RED, fill_rect)
        pygame.draw.rect(surface, WHITE, outline_rect, 1)

class Boss(Enemy):
    """最终Boss类，更大更强"""
    def __init__(self, x, y, hp, name, color):
        super().__init__(x, y, hp, name, color, size=80)
        self.shoot_delay = 800  # 射击更快

    def update(self):
        # Boss移动：左右摆动并缓慢向下
        self.rect.x += math.sin(pygame.time.get_ticks() * 0.001) * 2
        self.rect.y += 0.5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def shoot(self):
        """Boss发射多发子弹，返回子弹列表"""
        bullets = []
        for offset in [-20, 0, 20]:
            bullet = Bullet(self.rect.centerx + offset, self.rect.bottom, 1)
            bullets.append(bullet)
        return bullets

class Game:
    def __init__(self):
        # 设置敌人类的全局组引用，使shoot方法能添加子弹到正确组
        Enemy.bullet_group = self.enemy_bullets = pygame.sprite.Group()
        Enemy.all_sprites_group = self.all_sprites = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.bullets = pygame.sprite.Group()       # 玩家子弹组
        self.enemies = pygame.sprite.Group()       # 敌人组
        self.enemy_bullets = pygame.sprite.Group() # 敌人子弹组

        self.level = 1
        self.score = 0
        self.game_over = False
        self.victory = False
        self.level_start_time = 0
        self.level_duration = 120000  # 120秒（毫秒）
        self.level_time_remaining = self.level_duration

        # 小Boss列表
        self.mini_boss_names = ["孙杨", "王一廷", "蒋军利", "熊作军", "郭美云"]
        self.mini_boss_index = 0
        self.boss_spawned = False
        self.current_mini_boss = None
        self.current_boss = None

        self.start_level()

    def start_level(self):
        """初始化当前关卡"""
        # 重置玩家位置
        self.player.rect.centerx = SCREEN_WIDTH // 2
        self.player.rect.bottom = SCREEN_HEIGHT - 30
        self.player.invulnerable = False  # 重置无敌状态

        # 清空所有精灵（除玩家外）
        for sprite in self.enemies:
            sprite.kill()
        for sprite in self.bullets:
            sprite.kill()
        for sprite in self.enemy_bullets:
            sprite.kill()
        self.enemies.empty()
        self.bullets.empty()
        self.enemy_bullets.empty()
        # 重新填充all_sprites（只需保留玩家，其他已被kill自动移除）
        self.all_sprites.empty()
        self.all_sprites.add(self.player)

        # 重置关卡状态
        self.mini_boss_index = 0
        self.boss_spawned = False
        self.current_mini_boss = None
        self.current_boss = None
        self.level_start_time = pygame.time.get_ticks()
        # 生成第一个小Boss
        self.spawn_mini_boss()

    def spawn_mini_boss(self):
        """生成下一个小Boss"""
        if self.mini_boss_index < len(self.mini_boss_names):
            name = self.mini_boss_names[self.mini_boss_index]
            hp = 5 + self.level * 2
            color = [RED, GREEN, BLUE, PURPLE, ORANGE][self.mini_boss_index % 5]
            x = random.randint(100, SCREEN_WIDTH - 100)
            y = 50
            enemy = Enemy(x, y, hp, name, color, size=40)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
            self.current_mini_boss = enemy
            self.mini_boss_index += 1
        else:
            # 所有小Boss已出，准备生成最终Boss
            self.spawn_final_boss()

    def spawn_final_boss(self):
        """生成当前关卡的最终Boss"""
        if not self.boss_spawned:
            self.boss_spawned = True
            if self.level == 1:
                name = "图灵"
                color = CYAN
            elif self.level == 2:
                name = "邱奇"
                color = ORANGE
            else:
                name = "冯诺依曼"
                color = PURPLE
            hp = 20 + self.level * 10
            x = SCREEN_WIDTH // 2
            y = 80
            boss = Boss(x, y, hp, name, color)
            self.enemies.add(boss)
            self.all_sprites.add(boss)
            self.current_boss = boss

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = self.player.shoot()
                    self.bullets.add(bullet)
                    self.all_sprites.add(bullet)
        return True

    def update(self):
        if self.game_over or self.victory:
            return

        # 更新时间
        now = pygame.time.get_ticks()
        elapsed = now - self.level_start_time
        self.level_time_remaining = max(0, self.level_duration - elapsed)

        # 超时判定
        if self.level_time_remaining <= 0:
            self.game_over = True
            return

        # 更新所有精灵（玩家、子弹、敌人）
        self.all_sprites.update()

        # 处理敌人射击（由Game统一控制，避免在Enemy.update中直接添加子弹）
        for enemy in self.enemies:
            if now - enemy.shoot_timer > enemy.shoot_delay:
                bullets = enemy.shoot()  # 可能返回单个子弹或列表
                if isinstance(bullets, list):
                    for b in bullets:
                        self.enemy_bullets.add(b)
                        self.all_sprites.add(b)
                else:
                    self.enemy_bullets.add(bullets)
                    self.all_sprites.add(bullets)
                enemy.shoot_timer = now
                # 随机重置延迟（仅对普通敌人，Boss使用固定延迟）
                if not isinstance(enemy, Boss):
                    enemy.shoot_delay = random.randint(1500, 3000)

        # 玩家子弹与敌人碰撞
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for enemy, bullets in hits.items():
            enemy.hp -= len(bullets)
            if enemy.hp <= 0:
                enemy.kill()
                self.score += 10
                # 如果是小Boss被击败，生成下一个
                if enemy == self.current_mini_boss:
                    self.current_mini_boss = None
                    if self.mini_boss_index < len(self.mini_boss_names):
                        self.spawn_mini_boss()
                # 如果是最终Boss被击败，通关或进入下一关
                if enemy == self.current_boss:
                    if self.level < 3:
                        self.level += 1
                        self.start_level()
                    else:
                        self.victory = True

        # 敌人子弹与玩家碰撞
        hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
        if hits:
            if self.player.hit():
                self.game_over = True

        # 玩家与敌人碰撞
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            if self.player.hit():
                self.game_over = True

    def draw(self):
        screen.fill(BLACK)

        # 绘制所有精灵
        self.all_sprites.draw(screen)

        # 绘制敌人血量条
        for enemy in self.enemies:
            enemy.draw_hp_bar(screen)

        # 绘制玩家生命
        lives_text = font.render(f"生命: {self.player.lives}", True, WHITE)
        screen.blit(lives_text, (10, 10))

        # 绘制得分
        score_text = font.render(f"得分: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 40))

        # 绘制关卡
        level_text = font.render(f"关卡: {self.level}", True, WHITE)
        screen.blit(level_text, (10, 70))

        # 绘制倒计时
        seconds = self.level_time_remaining // 1000
        time_text = font.render(f"时间: {seconds}s", True, WHITE)
        screen.blit(time_text, (10, 100))

        # 绘制当前目标
        if self.current_mini_boss:
            target_text = font.render(f"目标: {self.current_mini_boss.name}", True, YELLOW)
            screen.blit(target_text, (SCREEN_WIDTH - 200, 10))
        elif self.current_boss:
            target_text = font.render(f"目标: {self.current_boss.name}", True, YELLOW)
            screen.blit(target_text, (SCREEN_WIDTH - 200, 10))

        # 游戏结束或胜利提示
        if self.game_over:
            over_text = large_font.render("GAME OVER", True, RED)
            screen.blit(over_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 - 50))
        elif self.victory:
            victory_text = large_font.render("VICTORY!", True, GREEN)
            screen.blit(victory_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 50))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            clock.tick(FPS)
            running = self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

# 主程序入口
if __name__ == "__main__":
    game = Game()
    game.run()