# :octopus: **OctoGun: Delivery Service** :octopus: | 
You are a gunslinger octopus whose job is to deliver packages. You must successfully navigate the seafloor, evading all sharks and eels to collect and deliver packages to your customers.

  <img src="assets/screenshot.png" alt="OctoGun Delivery Service Screen Shot" width="800px">

## To-do List:

- [] octo & squid => end game
- [] fix bug: octo still shooting when not visible 
- [] deploy as a [Stand Alone App](https://stackoverflow.com/questions/10527678/how-to-send-my-game-made-with-pygame-to-others)
- [x] render octo & octo moving()
- [x] octo has projectiles
- [x] add enemy shark: has health bar, is moving correct direction
- [x] add packages: 1. create package class, 2. render 
- [x] fix bug on shark collision
- [x] add more sharks
- [x] background music
- [x] octo health render, decrease when touching shark
- [x] octo & package collision logic
- [x] score bug
- [x] restart & game over screens
- [x] add package score when octo collides
- [x] SFX
- [x] bug on loading screen
- [x] octo & squid collision
- [x] randomize squid position & velocity
- [x] bug on `x` close button & game over screen, pinpointed to `self.playing` & `self.running` vars
- [x] render G.O. screen on player kill

## Proof of Concept:
- :white_check_mark: Render octopus with game controls
- :white_check_mark: Detect collisions and have feedback in the game
- :white_check_mark: Game success & game over scenario

**Tech Personal Goals:**
- Know how to manage state, controls, & collision using the PyGame physics engine
- Use scenes if possible
- Use open-source sprites if possible or create one. Use static images for now.

**Creativity Goals**
- Make sure to tie in Octopus-related themes:
  - 8 lives
  - 8 packages to return
- Produce some images, possibly a sprite sheet

## Game Controls (thus far)
- **ESC** quit game
- **SPACEBAR** shoot ink bullets
- **UP** move octopus up
- **DOWN** move octopus down
- **LEFT** move octopus left
- **RIGHT** move octopus right

## Concept Art

<img src="assets/delivery.png" alt="Octopus Delivery Service" width="800px">

## How to get started?

### Step 1: Set-up environment
My environment is already optimized for MacOS and VS Code. Here's how I got started: 

- Check to see if you have Python already installed via command `Python3 --version`
- If it returns something like `Python 3.7.0` then you're good. You can update your current version if you like. 
- Run `which python` to check that the path is something like `/usr/local/bin/python`
- If you don't have Python installed a.k.a. nothing returned or there was an error when you typed in `Python3 --version` then you can enter `brew install python3`

### Step 2: Optimize environment
Install extensions on VS Code. This is mainly:

- Python
- Python Extension (by Don Jayamanne)
- Code Runner (run a script file via CTRL + ALT + N)
- Pylinter 

### Step 3: Study Python Fundamentals (Optional)
- Follow along this awesome free book by **Allen D. Downey** [Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython2/html/index.html)

### Step 4: Open the game
1. Clone this repo:
* [OctoGun Repo](https://github.com/thinkful-ei26/octo-delivery-service.git) or `git clone https://github.com/thinkful-ei26/octo-delivery-service.git`
2. Open a new terminal shell and then `cd` into a directory that you want to clone the repo in
3. Finally, enter the command `python3 main.py` and you will see a blue window prompting you to press any key. 
4. Game controls are:
- **Arrow keys** to move
- **ESC** to quit the game
- **Spacebar** to shoot

**Note:** I apologize if the graphics look like a 5-year old drew it. I drew most of the assets using MS paint. :joy: I also used [BFXR](https://www.bfxr.net/) for the sound effects. The background music is from an open source website [OrangeFreeSounds](http://www.orangefreesounds.com/category/music/background-music/).