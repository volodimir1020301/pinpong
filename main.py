import pygame
pygame.init()

game_state = {
    "platsorms": {
        "0": 600 // 2 - 50,
        "1": 600 // 2 - 50,
    },
    "ball": {
        "x": 800 // 2,
        "y": 600 // 2,
    },
    "scores": [0 , 0]
}

window = pygame.display.set_mode([800, 600])
fps = pygame.time.Clock()
PLATFORM_H = 100
PLATFORM_SPEED = 5

font_main = pygame.font.Font(None, 32)
while 1 == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    plat1 = pygame.Rect(20, game_state["platsorms"]["0"],20, PLATFORM_H)
    plat2 = pygame.Rect(760, game_state["platsorms"]["1"],20, PLATFORM_H)
    window.fill([123, 123, 123])
    pygame.draw.rect(window, [255, 0, 0],plat1)
    pygame.draw.rect(window, [255, 0, 0],plat2)
    pygame.draw.circle(window, [255, 0, 0], [game_state["ball"]["x"], game_state["ball"]["y"]], 10)
    score_text = font_main.render(f"{game_state['scores'][0]} : {game_state['scores'][1]}", True, (255, 255, 255))
    window.blit(score_text, (800 // 2 - 25, 20))
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game_state["platsorms"]["0"] -= PLATFORM_SPEED
    if keys[pygame.K_s]:
        game_state["platsorms"]["0"] += PLATFORM_SPEED
    if keys[pygame.K_UP]:
        game_state["platsorms"]["1"] -= PLATFORM_SPEED
    if keys[pygame.K_DOWN]:
        game_state["platsorms"]["1"] += PLATFORM_SPEED
    fps.tick(60)