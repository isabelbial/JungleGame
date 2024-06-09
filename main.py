import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100

    def add_item(self, item):
        self.inventory.append(item)
  
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

print('You suddenly wake up all dizzy without knowing where or when you are...')
print('Your hands touch the damp floor and you smell the wet earth that hangs in the air.')
print('You hear the distant call of birds and the rustle of leaves as a gentle breeze blows through the trees.')
print('Slowly you open your eyes and just can\'t believe what you see:')
print(' ')
print('           · · ────────  𖥸    ───────── · ·')
print('             The dense forest surrounds you')
print('           · · ────────  𖥸    ───────── · ·')
print(' ')
print('Somehow you can\'t remember your name. The only thing you have near you is a backpack.')
print(' ')
print('What do you do?')
print('  1) Investigate the backpack')
print('  2) Investigate around')

apple_eaten = False
player = Player("")

while True:
    qst1 = input('Type your answer: ')

    if qst1 == '1':
        print(' ')
        print('You open the backpack.')
        print('There\'s a shining little plate with a name written on it...')
        name = input('What name do you see? ')
        print(' ')
        print('...', name, '...???')
        print('-\'This is mine!!!\' - you scream')
        print(' ')
        player = Player(name)

        print('You start to investigate more and now have the following items in your inventory:')
        print(' ')
        print('╭─────༺ 🕷 ༻─────╮')
        player.add_item('🗡️  Dagger')
        player.add_item('🍎 Apple')
        player.add_item('📜 Old Paper')

        for item in player.inventory:
            print(item)  
    
        print('╰─────༺ 🕷 ༻─────╯')

        while True:
            print(' ')
            print('What do you want to do now?')
            print('  1) Look at the Dagger')
            if not apple_eaten:
                print('  2) Look at the Apple')
            print('  3) Read the Old Paper')
            print('  4) Look around')
            bckp_qst = input('Type your answer: ')

            if bckp_qst == '1':
                print(' ')
                print('This seems to be very sharp, it is good to be careful when handling it.')
                print('It can cause medium damage to an opponent if used with dexterity.')

            elif bckp_qst == '2' and not apple_eaten:
                print(' ')
                print('Somehow, this looks like it was freshly collected.')
                eat = input('Do you wanna eat it (Y or N)? ').upper()
                if eat == 'Y':
                    apple_eaten = True
                    player.remove_item('🍎 Apple')
                    player.health -= 20
                    print(' ')
                    print('You eat it and feel a strange sensation.')
                    print('You feel weaker and your vision blurs slightly.')
                    print(f'Health: {player.health}')

            elif bckp_qst == '3':
                print(' ')
                print('You slowly open the old paper and read the following sequence:')
                print('...1015...')
                print('It looks like a date, or maybe a code. You wonder what it means.')

            elif bckp_qst == '4':
                if apple_eaten:
                    print(' ')
                    print('You look around and see a little silhouette looking at you from behind the bush.')
                    print('The thing sees you looking at her and starts running away.')
                    print('You start to run after the mysterious thing, but slowly your vision starts to darken.')
                    print('Looks like you shouldn\'t have eaten that apple.')
                    print(' ')
                    print('...You fall on the ground...')
                    print('...')
                    print('Something hits your head and suddenly you wake up.')
                    print('You almost can\'t believe what your eyes are seeing...')
                    print('You are now being carried inside of a jail by four strong warriors.')
                    print('They take out some plants to pass and you see a huge temple.')
                    print('There\'s a beautiful waterfall near it and a lot of curious people trying to look at you.')
                    print(' ')
                    where = input('Wanna ask where you are? (Y or N)').upper()

                    if where == 'Y':
                        print(' ')
                        print('...WHERE ARE WE????.. - You scream.')
                        print('One of the warriors looks at you and answers:')
                        print(' ')
                        print(' - You don\'t know how to read? ')
                        print('He points to a huge sign, where you can read:')
                        print(' ')
                    else:
                        print(' ')
                        print('You try to look around to know where you are.')
                        print('Then you see a huge sign that says:')
                        print(' ')
                    
                    print('           · · ────────  𖥸    ───────── · ·')
                    print('                  Temple of Jumanji')
                    print('           · · ────────  𖥸    ───────── · ·')
                    print(' ')
                    print('You can\'t believe your eyes..')
                    print('This temple, hiding in the woods.. might have some secrets, for sure!')
                    print(' ')
                    print('Then the warriors throw you into a deep, dark dungeon.')
                    print('You try to look around but it\'s too dark to see anything.')
                    print(' ')
                    print('What do you want to do now?')
                    print(' 1) Try to climb out with your hands')
                    print(' 2) Write your name on the walls, so someday someone might remember you')
                    print(' 3) Try to see if there\'s any way out')
                    dungeon = input('Type your answer: ')

                    if dungeon == '1':
                        print(' ')
                        print('You try with all your power to climb out, and you are now about a meter away from the exit.')
                        print('Suddenly some kind of tarantula jumps on your hand.')
                        print('You get scared and your foot slips from the rock wall.')
                        print('The fall is high enough to break you all, but not to kill you.')
                        print('.. Sadly no one shows up to help you and you slowly die.')
                        print('... You die alone, without reaching your objectives....')
                        print('.... Maybe someone out there misses you, we don\'t know.')
                        print('                ─── ⋆⋅ ♰ ⋅⋆ ───')
                        break

                    elif dungeon == '2':
                        print(' ')
                        print('You write your name on the walls, hoping that someday someone will remember', name)
                        print('Time passes slowly in the darkness. You hear distant sounds, but nothing comes close.')
                        print('.. Eventually, your strength fades and you pass away.')
                        print('... You die alone, with your name etched in the walls....')
                        print('.... Maybe someone will find your message and remember you.')
                        print('                ─── ⋆⋅ ♰ ⋅⋆ ───')
                        break

                    elif dungeon == '3':
                        print(' ')
                        print('You fumble around in the darkness, feeling for anything that might help you escape.')
                        print('You find a loose stone and pry it out, revealing a hidden passage.')
                        print('You squeeze through the passage and find yourself in a maze of tunnels.')
                        print('With determination, you navigate the tunnels and eventually find an exit.')
                        print('You emerge into the sunlight, free at last.')
                        print('.... You have escaped the dungeon and survived....')
                        print('Your adventure continues....')
                        break

                else:
                    print(' ')
                    print('You look around and see a little silhouette looking at you from behind the bush.')
                    print('The thing sees you looking at her and starts running away.')
                    print('You hesitate for a moment, then decide to follow, your curiosity piqued.')
                    print(' ')
                    print('As you chase the silhouette through the dense forest, you can\'t help but feel that this encounter is just the beginning.')
                    print('There are many more secrets hidden within these woods, and you are determined to uncover them.')
                    print(' ')
                    print('With each step, you get closer to the unknown, ready to face whatever challenges lie ahead.')
                    print('Your adventure will continue...')
                    break

            else:
                print('Sorry, I don\'t understand.')
        break

    elif qst1 == '2':
        print('You decide to investigate around.')
        print(' ')
        print('The forest is thick and the trees tower above you, their leaves forming a dense canopy.')
        print('You hear the sound of running water nearby. It might be a river or a stream.')
        print(' ')
        print('What do you want to do?')
        print('  1) Head towards the sound of water')
        print('  2) Explore deeper into the forest')
        print('  3) Climb a tree to get a better view')

        forest_qst = input('Type your answer: ')

        if forest_qst == '1':
            print(' ')
            print('You follow the sound of water and soon come across a small, clear stream.')
            print('The water looks refreshing. You see some fish swimming around and the sunlight sparkles on the surface.')
            print('You notice something shiny in the water.')
            print(' ')
            print('What do you want to do?')
            print('  1) Drink the water')
            print('  2) Try to catch a fish')
            print('  3) Investigate the shiny object')

            water_qst = input('Type your answer: ')

            if water_qst == '1':
                print(' ')
                print('You kneel down and drink some of the water.')
                print('It tastes fresh and cool, rejuvenating you.')
                player.health += 10
                print(f'Health: {player.health}')

            elif water_qst == '2':
                print(' ')
                print('You try to catch a fish with your bare hands.')
                print('After a few attempts, you manage to catch one.')
                print('It\'s small but it might make a decent meal.')
                player.add_item('🐟 Fish')

            elif water_qst == '3':
                print(' ')
                print('You carefully reach into the water and pull out the shiny object.')
                print('It\'s a small, ornate key. You wonder what it might open.')
                player.add_item('🔑 Key')

        elif forest_qst == '2':
            print(' ')
            print('You venture deeper into the forest.')
            print('The trees become thicker and the light dimmer.')
            print('You come across a clearing with a strange, ancient stone structure in the center.')
            print('It looks like an old altar, covered in moss and vines.')
            print(' ')
            print('What do you want to do?')
            print('  1) Investigate the altar')
            print('  2) Look around the clearing')
            print('  3) Continue exploring the forest')

            altar_qst = input('Type your answer: ')

            if altar_qst == '1':
                print(' ')
                print('You approach the altar and see that it has strange carvings all over it.')
                print('There is a bowl in the center, filled with what looks like old, dried blood.')
                print('You feel a sense of unease as you study it.')
                print(' ')
                print('What do you want to do?')
                print('  1) Touch the carvings')
                print('  2) Look inside the bowl')
                print('  3) Leave the altar alone')

                carving_qst = input('Type your answer: ')

                if carving_qst == '1':
                    print(' ')
                    print('You touch the carvings and feel a strange energy course through you.')
                    print('Suddenly, the altar begins to glow and a voice echoes in your mind.')
                    print('It says, "Seek the hidden temple. The key lies within."')
                    player.add_item('✨ Energy Boost')
                    player.health += 20
                    print(f'Health: {player.health}')

                elif carving_qst == '2':
                    print(' ')
                    print('You look inside the bowl and see a glint of something metallic.')
                    print('You reach in and pull out a small, golden amulet.')
                    print('It has strange symbols on it that you can\'t decipher.')
                    player.add_item('📿 Golden Amulet')

                elif carving_qst == '3':
                    print(' ')
                    print('You decide to leave the altar alone and step back.')
                    print('The sense of unease fades and you feel a bit more at ease.')
                    print(' ')
                    print('You take a deep breath and realize that this is just the beginning of your journey.')
                    print('The mysteries of this forest are far from over, and many more challenges await.')
                    print(' ')
                    print('With a renewed sense of purpose, you gather your courage and prepare to venture further into the unknown.')
                    print('Your adventure will continue...')
                    break

            elif altar_qst == '2':
                print(' ')
                print('You look around the clearing and see several paths leading in different directions.')
                print('One path looks well-trodden, while the others are overgrown with vegetation.')
                print('You also notice some strange footprints on the ground, leading towards one of the paths.')
                print(' ')
                print('What do you want to do?')
                print('  1) Follow the well-trodden path')
                print('  2) Follow the overgrown path')
                print('  3) Follow the footprints')

                path_qst = input('Type your answer: ')

                if path_qst == '1':
                    print(' ')
                    print('You follow the well-trodden path.')
                    print('It leads you to a small village hidden deep in the forest.')
                    print('The villagers look at you curiously as you approach.')
                    print(' ')
                    print('What kind of mysteries those villagers hide?')
                    print('...Your adventure will continue...')
                    break

                elif path_qst == '2':
                    print(' ')
                    print('You follow the overgrown path and have to push through thick vegetation.')
                    print('Eventually, you come across an old, abandoned cabin.')
                    print('It looks like it hasn\'t been used in years.')
                    print(' ')
                    print('What kind of mysteries this cabin hide?')
                    print('...Your adventure will continue...')
                    break

                elif path_qst == '3':
                    print(' ')
                    print('You follow the footprints and soon hear the sound of voices.')
                    print('You hide behind a tree and see a group of people gathered around a fire.')
                    print('They seem to be discussing something important.')
                    print(' ')
                    print('What kind of secrets those people are talking about?')
                    print('...Your adventure will continue...')
                    break

        elif forest_qst == '3':
            print(' ')
            print('You find a sturdy-looking tree and begin to climb it.')
            print('From the top, you can see the forest stretching out in all directions.')
            print('In the distance, you spot what looks like the ruins of an old temple.')
            print('You also see smoke rising from what might be a village.')
            print(' ')
            print('This will be a great adventure to see...')
            print('...your adventure will continue...')
            break

    else:
        print('Sorry, I don\'t understand.')
