# Y13-Coursework

TODO:
- (!) rename stuff (i.e troll to skeleton, forest to swamp, files etc.)
- (!) make game quit when you press quit game in leaderboard

- rework newScore: make textbox a new object with an 'active' attribute. remove explicit text input for newScore from graphicsBackend
- move block into knight entity class, in case some future player classes cant block (e.g mage)
- downscale troll healthBar text
- fix glitchy player swing
- fix glitchy troll attack anims
- stop troll from continuously walking to make space, even if it hits a wall
- add troll appear and die animations
- properly animate 1 frame animations e.g drop, jump, knockback..
- add jump/drop attack
- new hit detection, using two text files per frame:
  - have a file with co-ords for each frame for a box (over the attacker's sword) where a hit is detected
  - have a file with co-ords for each frame for a box (over the receiving entity) where a hit could land
  - EITHER of these would make block management much either, because I could just move/remove the recieving hitbox
  - If i change the way blocking works like this, i will have to remove the way it's currently handled (with armour boosting)
- split stamina bar into different colours at the points where the player has enough stamina to execute the different attacks
- random item spawns
-> food, potions, boosters
- (?) add more enemies
- (?) add more enemy types
- (?) add more player types
- make it easier to start with -> troll damage
- add experience
- level up troll after a random number of kills
- display "troll mutation!" etc
- display level above troll
- Randomly choose whether to block a player attack or not
- Add difficulty setting -> e.g increase base troll difficulty, FPS, number of trolls, number of kills per troll kill
- store separate leaderboards for each difficulty
