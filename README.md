# Y13-Coursework

TODO:
- (!) Fix troll swing moving backwards when facing left
- (!) fix troll swing being above ground
- (!) rename stuff (i.e troll to skeleton, forest to swamp, files etc.)

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
- new stand and pant animations (?)
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
