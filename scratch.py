#  ## BULLET & SHARK COLLISION
#         if bullet.y - bullet.radius < shark.hitbox[1] + shark.hitbox[3] and bullet.y + bullet.radius > shark.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
#             if bullet.x + bullet.radius > shark.hitbox[0] and bullet.x - bullet.radius < shark.hitbox[0] + shark.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
#                 shark.hit()
#                 # shark2.hit()
#                 if shark.visible == True:
#                   score += 1
#                   bullets.pop(bullets.index(bullet))

#         if bullet.y - bullet.radius < shark2.hitbox[1] + shark2.hitbox[3] and bullet.y + bullet.radius > shark2.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
#             if bullet.x + bullet.radius > shark2.hitbox[0] and bullet.x - bullet.radius < shark2.hitbox[0] + shark2.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
#                 shark2.hit()
#                 # shark2.hit()
#                 if shark2.visible == True:
#                   score += 1
#                   bullets.pop(bullets.index(bullet))

# def enemyCollision(enemyObj):
#     if bullet.y - bullet.radius < enemyObj.hitbox[1] + enemyObj.hitbox[3] and bullet.y + bullet.radius > enemyObj.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
#     if bullet.x + bullet.radius > enemyObj.hitbox[0] and bullet.x - bullet.radius < enemyObj.hitbox[0] + enemyObj.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
#         enemyObj.hit()
#         # shark2.hit()
#         if enemyObj.visible == True:
#           score += 1
#           bullets.pop(bullets.index(bullet))


if octopus.hitbox[1] < shark.hitbox[1] + shark.hitbox[3] and octopus.hitbox[1] + octopus.hitbox[3] > shark.hitbox[1]:
    if octopus.hitbox[0] + octopus.hitbox[2] > shark.hitbox[0] and octopus.hitbox[0] < shark.hitbox[0] + shark.hitbox[2]:
        octopus.hit(windowSurface)
        score -= 5

def playerCollision(player, enemy, score):
    if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
            player.hit(windowSurface)
            score -= 5
