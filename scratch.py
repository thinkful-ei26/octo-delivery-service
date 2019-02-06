 ## BULLET & SHARK COLLISION
        if bullet.y - bullet.radius < shark.hitbox[1] + shark.hitbox[3] and bullet.y + bullet.radius > shark.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
            if bullet.x + bullet.radius > shark.hitbox[0] and bullet.x - bullet.radius < shark.hitbox[0] + shark.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
                shark.hit()
                # shark2.hit()
                if shark.visible == True:
                  score += 1
                  bullets.pop(bullets.index(bullet))

        if bullet.y - bullet.radius < shark2.hitbox[1] + shark2.hitbox[3] and bullet.y + bullet.radius > shark2.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
            if bullet.x + bullet.radius > shark2.hitbox[0] and bullet.x - bullet.radius < shark2.hitbox[0] + shark2.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
                shark2.hit()
                # shark2.hit()
                if shark2.visible == True:
                  score += 1
                  bullets.pop(bullets.index(bullet))

def enemyCollision(enemyObj):
    if bullet.y - bullet.radius < enemyObj.hitbox[1] + enemyObj.hitbox[3] and bullet.y + bullet.radius > enemyObj.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
    if bullet.x + bullet.radius > enemyObj.hitbox[0] and bullet.x - bullet.radius < enemyObj.hitbox[0] + enemyObj.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
        enemyObj.hit()
        # shark2.hit()
        if enemyObj.visible == True:
          score += 1
          bullets.pop(bullets.index(bullet))