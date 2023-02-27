define persistent.skin = 0
define TetrisWinner = 0
define LineLimit = 0
define TetrisScore = 0
define PlayerForMonika = 0


# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Moonlightphoenixgames",
        name="Learn together tetris",
        description="Adds Tetris to the Learn together submod",
        version="1.0.0"
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Play_tetris_with_Monika",
            category=["Learn","Games"],
            prompt="Tetris",
            random=False,
            pool=True,
            unlocked=True
        )
    )
label Play_tetris_with_Monika:
    python:

        boopable = False
        LineLimit = 0
        TetrisScore = 0
    if True:
                                 menu:
                                   m "Oh, so you'd like to play some Tetris, hm?"
                                   "Yes.":
                                      if True:
                                          m "Oh, good."
                                          m "Which theme would you like this time?"
                                          $ pass
                                   "No.":
                                     if True:
                                         m "I see..."
                                         m "Perhaps some other time, then."
                                         jump ch30_loop

                                 menu:
                                     "Default Theme.":
                                                  if True:
                                                      m "You don't want to give Tetris any kind of skin? That's ok."
                                                      $ persistent.skin = 1
                                     "Tetris 99 Theme.":
                                                    if True:
                                                        m "Oh? Going to experience one of the latest Tetris themes?"
                                                        m "Please don't expect too much I am still working on the code."
                                                        $ persistent.skin = 2
                                     "GameBoy Tetris Theme.":
                                                          if True:
                                                              m "Oh! Is this the classic Tetris for HandHelds? Have in mind that this is the color version"
                                                              $ persistent.skin = 3
                                     "Mega Drive Tetris Theme.":
                                                            if True:
                                                                m "Okay. It's unfortunate that you can't Blast Processing in Ren'py."
                                                                $ persistent.skin = 4
                                     "M1ND BEND3R theme.":
                                                      if True:

                                                          $ persistent.skin = 5
                                     "Custom Theme.":
                                                 if True:
                                                     call custom_tetris_checkpoint_start from _call_custom_tetris_checkpoint_start
    elif True:
          menu:
              "Default Theme.":
                            if True:
                                m "You don't want to give Tetris any kind of skin? That's ok."
                                $ persistent.skin = 1
              "Tetris 99 Theme.":
                              if True:
                                  m "Oh? Going to experience one of the latest Tetris themes?"
                                  m "Please don't expect too much I am still working on the code."
                                  $ persistent.skin = 2
              "GameBoy Tetris Theme.":
                                   if True:
                                       m "Oh! Is this the classic Tetris for HandHelds? Have in mind that this is the color version"
                                       $ persistent.skin = 3
              "Mega Drive Tetris Theme.":
                                      if True:
                                          m "Okay. It's unfortunate that you can't Blast Processing in Ren'py."
                                          $ persistent.skin = 4
              "M1ND BEND3R theme.":
                                if True:

                                    $ persistent.skin = 5
              "Custom Theme.":
                           if True:
                               call custom_tetris_checkpoint_start from _call_custom_tetris_checkpoint_start
    m "Alright [player], now I can let you select the modes you want to play."
    menu:
        "Line count":
                  if True:
                      m "It's a nice way to pass the time, really."
                      m "Just a couple doing things together..."
                      m "Ahem... Anyway let's get started."
                      menu:
                          "30":
                            if True:
                                $ LineLimit = 30
                          "50":
                            if True:
                                $ LineLimit = 50
                          "100":
                             if True:
                                 $ LineLimit = 100
                          "150":
                             if True:
                                 $ LineLimit = 150
                          "300":
                             if True:
                                 $ LineLimit = 300
                      jump tetris_difficulty
        "Score":
             if True:
                 m "Oh, some competition, eh?"
                 m "Maybe you will win me as a prize to be cherished... Forever~"
                 m "Or maybe I would win you. hehe. Either way, everyone wins!"
                 menu:
                     "20000":
                          if True:
                              $ TetrisScore = 20000
                     "50000":
                          if True:
                              $ TetrisScore = 50000
                     "100000":
                           if True:
                               $ TetrisScore = 100000
                     "200000":
                           if True:
                               $ TetrisScore = 200000
                     "300000":
                           if True:
                               $ TetrisScore = 300000
                     "500000":
                           if True:
                               $ TetrisScore = 500000
                 jump tetris_difficulty
        "CO-OP (Alpha)":
                     if True:
                         m "Oh how fun~!"
                         m "W-well if you insist [player]. It is better when we strive toward the same goal together."
                         m "Maybe it might even become an all-nighter! Ehehe..."
                         m "Ok game on dear [player]!"
                         $ AI_difficulty = "CO_OP"
                         jump tetris_rules
label custom_tetris_checkpoint_start:
    m "Oh, you'd like to try your hand on a custom Tetris build?"
    m "Well, let me give you a quick walkthrough of how it's done or do you already have it all figured out?"
    menu:
        "Try me!":
               if True:
                   m "Okay"
                   jump custom_tetris_checkpoint
        "No":
          if True:
              m "By the way, you should probably write this down somewhere..."
label custom_tetris_repeat:
     m "All those files which you will create will have to go in the folder \"game\\Submods\\Learn together\\Play Tetris with Monika\\custom_tetris\""
     m "First thing you need to know is that all images have to be in .png format and all sounds need to be in .ogg format. Ren'py will reject anything else."
     m "Let's start with the background. {b}Line Count{/b} and {b}Score{/b} have two types of background depending on difficulties."
     m "For the Easy, Medium and Hard difficulties it has to be 220 x 420 pixels image. Use the {b}background.png{/b} file from the folder \"game\\Submods\\Learn together\\Play Tetris with Monika\\images\\tetris\\tetris\" as an example..."
     m "For the same modes but in the Disadvantage, Veteran and Expert difficulties, it is the exact same procedure, but this time you have to delete the grids and name it {b}backgrund_no_grind{/b}... oh yes, and it still has to be a .png file!"
     m "The Co-op mode shares the same procedure, but this time it is 421 x 420 pixels and you name it {b}grids (coop).png{/b}. It's in the same folder again"
     m "Now we come to the blocks."
     m "Fun fact, did you know that a single block is called a Tetromino?"
     m "There are 7 pieces in Tetris which usually have diffrent colors. You could make them the same colors"
     m "But that would be kind of boring. Don't you think?"
     m "Each pieces is build from individual blocks which are number from 1 to 7."
     m "Also in newer version of Tetris. You can see where the piece will land. We refer it as {b}shadow pieces{/b} "
     m "They also need to have their own colors which are usually transparency of nomral blocks"
     m "Each of the cube need to be a .png image with size 20x20. You can use the {b}cube_1.png{/b} file from the folder \"game\\Submods\\Learn together\\Play Tetris with Monika\\images\\tetris\\tetris\" as an example..."
     m "For the T Piece you set up cube_1.png and shadow_1.png"
     m "For the S Piece you set up cube_2.png and shadow_2.png"
     m "For the Z Piece you set up cube_3.png and shadow_3.png"
     m "For the L Piece you set up cube_4.png and shadow_4.png"
     m "For the J Piece you set up cube_5.png and shadow_5.png"
     m "For the I Piece you set up cube_6.png and shadow_6.png"
     m "For the O Piece you set up cube_7.png and shadow_7.png"
     m "The last is wall of the game. For wall you set up cube_8.png. Most of the time is black for easy distinguish"
     m "For now in your custome_Tetris folder, you should have 18 files. 2 Background, 8 cube and 8 shadow png"
     m "Is everything good? If not let me know and I will reapet the step again"
     menu:
         "Yes":
            if True:
                m "Okay. Let's go to the next part"
         "No":
           if True:
               m "Let me repeat the steps again."
               jump custom_tetris_repeat
label custom_tetris_repeat_audio:
    m "Now for the audio part..."
    m "All the audio files must have specific names, otherwise the game will reject them, so here are the names for the sounds."
    m "Keep in mind that sfx should be a very short sounds. If they will be long they will overlap. It will turn into mess"
    m "Here are the names of the sfx sounds"
    m "t-fl.ogg for a single line clear."
    m "t-2f1.ogg for a double line clear."
    m "t-3fl.ogg for a triple line clear."
    m "t-4fl.ogg for a full tetris line clear."
    m "t-drop.ogg for the hard drop sound."
    m "t-move.ogg for whenever you move the piece."
    m "t-rotate.ogg for whenever you rotate the piece."
    m "Those are were sfx sound. For the main music which will loop for the duration of game."
    m "Use \"tetris.ogg\""
    m "So in the end your custome_Tetris folder should have 26 files. 2 Background, 8 cube, 8 shadow png and 8 .ogg files"
    m "I-I hope I didn't confuse you with that explanation..."
    m "I'm not good at explaining such technicalities..."
    m "If I mess up and you still need to adjust something let me know and I will repeat the steps"
    menu:
        "Everything is fine":
                          if True:
                              m "Yay"
        "Please start from the beginning":
                                       if True:
                                           m "Okay"
                                           jump custom_tetris_repeat
        "Please start form audio files":
                                     if True:
                                         m "Okay"
                                         jump custom_tetris_repeat_audio
    call custom_tetris_checkpoint from _call_custom_tetris_checkpoint
    return
label custom_tetris_failure:
    m "[player]? It seems you need to fix some of the issues I mentioned"
    m "Perhaps I should explain all the steps again"
    call custom_tetris_repeat from _call_custom_tetris_repeat
label custom_tetris_checkpoint:
    menu:
        m "Do you have everything done?"
        "Yes." if True:
            python:
                from os import walk
                f = []
                for (dirpath, dirnames, filenames) in walk(config.basedir + "/game/Submods/Learn together/Play Tetris with Monika/custom_tetris"):
                    f.extend(filenames)
                    break
                custom_tetris = []

                for i in f:
                    if i.find(".ogg") == -1 and i.find(".mp3") == -1 and i.find(".wav") == -1 and i.find(".flac") == -1 and i.find(".png") == -1:
                        pass
                    else:
                        custom_tetris.append((i, i))
                custom_tetris.append(("", ""))

                if custom_tetris == [("", "")]:

                    m("Seems like you don't have anything in the folder right now...")

                    m("That's fine. I'll wait.")
                    renpy.jump("ch30_loop")
                custom_tetris_png_req = ["background", "background_no_grind"]
                custom_tetris_music_req = ["t-fl", "t-2fl", "t-3fl", "t-4fl", "t-drop", "t-move", "t-rotate", "tetris"]
                custom_tetris_all_ready = True
                for i in custom_tetris_png_req:
                    element = (i + ".png", i + ".png")
                    if not element in custom_tetris:
                        m("It seems there is issue with background image:" + i)
                        renpy.call("custom_tetris_failure")
                for i in custom_tetris_music_req:
                    element = (i + ".ogg", i + ".ogg")
                    if not element in custom_tetris:
                        m("It seems there is issue with audio files: " + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 9):
                    element = ("cube_" + str(i) + ".png", "cube_" + str(i) + ".png")
                    if not element in custom_tetris:
                        m("It seems there is issue with piece cube image:" + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 8):
                    element = ("shadow_" + str(i) + ".png", "shadow_" + str(i) + ".png")
                    if not element in custom_tetris:
                        m("It seems there is issue with piece shadows image:" + i)
                        renpy.call("custom_tetris_failure")
                persistent.skin = 6
        "No." if True:

            m "I see."

            m "No need to rush. Take your time."
            jump ch30_loop
    return
label tetris_difficulty:
    m "If you are not used to tetris, we can adjust the difficulty a bit. Just tell me how you wish it to be, I will not judge."
    menu:
        "Easy":
            if True:
                $ AI_difficulty = 1
                m "Oh, I see."
                m "You'd like me to go easy on you this time, eh?"
                m "I'm happy to oblige, [player]!"
        "Medium":
              if True:
                  $ AI_difficulty = 2
                  m "Oh I see~ Trying to warm up with a slight challenge eh?"
                  m "Well then. I would like to see how you do!"
                  m "It is good to test your self now and again!"
        "Hard":
            if True:
                $ AI_difficulty = 3
                m "Oh hehehe.. Really turning up the dial are you now, [player]"
                m "Well I do like it when you are a bit more daring~ It is rather inspiring."
                m "Well as they say, Let the games begin!"
                m "O-oh but don't go too hard on your self [player]... Eheheh."
        "Disadvantage":
                    if True:
                        $ AI_difficulty = 4
                        m "Mmm..."
                        m "Oh dear [player]. that seems like such a huge task to handle. Are you sure!"
                        m "Ehehehehe... Well alright if you insist~"
                        m "Prepare thy mind and body for the penultimate gamers challenge dear [player]"
        "Expert":
              if True:
                  $ AI_difficulty = 5
                  m "Oh you are in for a bumpy ride [player]..."
                  m "...but I guess you like it that way don't you..."
        "Veteran":
               if True:
                   $ AI_difficulty = 6
                   m " The highest, I see..."
                   m "I'm not even sure if I can pull this off but... let's give it a try."
label tetris_rules:
    if persistent.tetris_first:
      m "Allow me to explain the controls..."
      m "You can use arrows to move your pieces. Hitting UP will rotate your piece, hitting DOWN will speed up your drop."
      m "Hitting SPACE will drop the piece instantaneously."
      m "Q key will put the piece into hold, but you can't double hold the same piece..."
      m "...While the E key will use the piece which you are holding."
      $ persistent.tetris_first = False
    menu:
        m "Would you like some Tetris music while we play?"
        "Yes" if True:
            if AI_difficulty != "CO_OP":
                m "Let the best Tetris player win."

                m "Game on, [player]!"

                m "Let's enjoy our time together trying to get the highest score!"




            if persistent.skin == 1:
                $ play_song("<loop 36.79>/Submods/Learn together/Play Tetris with Monika/music/tetris.ogg")
            elif persistent.skin == 2:
                $ play_song("<loop 0.80>/Submods/Learn together/Play Tetris with Monika/music/tetris_99.ogg")
            elif persistent.skin == 3:
                $ play_song("<loop 19.30>/Submods/Learn together/Play Tetris with Monika/music/tetris_gb.ogg")
            elif persistent.skin == 4:
                $ play_song("<loop 0>/Submods/Learn together/Play Tetris with Monika/music/tetris_gmd.ogg")
            elif persistent.skin == 5:
                $ play_song("<loop 0>/Submods/Learn together/Play Tetris with Monika/music/tetris_m1nd_bend3r.ogg")
            elif persistent.skin == 6:
                $ play_song("<loop 0>/Submods/Learn together/Play Tetris with Monika/custom_tetris/tetris.ogg")
        "No" if True:
            if AI_difficulty != "CO_OP":
                m "Let the best Tetris player win."

                m "Game on, [player]!"
            elif True:
                m "Let's enjoy our time together trying to get the highest score!"




    call screen startTetris(AI_difficulty)
label tetris_over:




            $ play_song(persistent.current_track)
            m "O-oh my!! Oh that was quite a little thrill~"
            m "I had enjoyment just being in that moment with you [player]. Even though I may have strived for a higher score."

            m "Really though, it is indeed the moment shared together and the heart that counts!"
            m "Hehehe... Though I will admit part of me does want to try again and see if I score higher."

            m "Either way I believe we both put our best effort!"
            menu:
                m "So [player], do you want to try again? Us together one more time?"
                "Yes" if True:
                    menu:
                        m "Would you like the same music as our last game?"
                        "Yes" if True:
                             if persistent.skin == 1:
                                 $ play_song("<loop 36.79>/Submods/Learn together/Play Tetris with Monika/music/tetris.ogg")
                             elif persistent.skin == 2:
                                   $ play_song("<loop 0.80>/Submods/Learn together/Play Tetris with Monika/music/tetris_99.ogg")
                             elif persistent.skin == 3:
                                   $ play_song("<loop 19.30>/Submods/Learn together/Play Tetris with Monika/music/tetris_gb.ogg")
                             elif persistent.skin == 4:
                                   $ play_song("<loop 0>/Submods/Learn together/Play Tetris with Monika/music/tetris_gmd.ogg")
                             elif persistent.skin == 5:
                                   $ play_song("<loop 0>/Submods/Learn together/Play Tetris with Monika/music/tetris_m1nd_bend3r.ogg")
                             elif persistent.skin == 6:
                                   $ play_song("<loop 0>/Submods/Learn together/Play Tetris with Monika/custom_tetris/tetris.ogg")

                             call screen startTetris(AI_difficulty)
                        "No":
                          if True:
                              call screen startTetris(AI_difficulty)

                "No":
                  if True:

                      m "I really enjoy playing with you. Let's do this again sometime soon."
                      $ play_song(persistent.current_track)
                      jump ch30_loop

screen startTetris(AI_difficulty):
    if AI_difficulty != "CO_OP":
        fixed:
            area (150, 120, 600, 1100)
            if AI_difficulty < 4:
                default tetris_player = tetris(0)
            else:
                default tetris_player = tetris(-1)
            add tetris_player

        fixed:
            area (900, 120, 600, 1100)
            default tetris_Monika = tetris(AI_difficulty)
            add tetris_Monika
    else:
        fixed:
            area (50, 120, 600, 1100)
            default tetris_Co_OP = Co_OP_tetris()
            add tetris_Co_OP
init python:

    import pygame
    class tetris(renpy.Displayable):
        def __init__(self, AI):
            renpy.Displayable.__init__(self)
            if AI == -1:
                self.put_shadow = 0
                self.AI = AI + 1
            else:
                self.put_shadow = 1
                self.AI = AI
            self.movesAI = []
            self.PIXEL_SIZE = 20
            self.piece_list = [0,1,2,3,4,5,6]
            random.shuffle(self.piece_list)
            self.tetris_shapes = [
                [[1, 1, 1],
                 [0, 1, 0]],

                [[0, 2, 2],
                 [2, 2, 0]],

                [[3, 3, 0],
                 [0, 3, 3]],

                [[4, 0, 0],
                 [4, 4, 4]],

                [[0, 0, 5],
                 [5, 5, 5]],

                [[6, 6, 6, 6]],

                [[7, 7],
                 [7, 7]]
            ]

            self.stage = [[9,9,9,9,9,9,9,9,9,9,9,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,9],
                         [9,9,9,9,9,9,9,9,9,9,9,9]]

            if persistent.skin == 1:

                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound2line = "sfx/t-2fl.ogg"
                self.sound3line = "sfx/t-3fl.ogg"
                self.sound4line = "sfx/t-4fl.ogg"

            elif persistent.skin == 2:

                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(99).ogg"
                self.soundline = "sfx/t-fl(99).ogg"
                self.soundldrop = "sfx/t-fl-drop(99).ogg"
                self.soundmove = "sfx/t-move(99).ogg"
                self.soundrotate = "sfx/t-rotate(99).ogg"
                self.sound2line = "sfx/t-2fl(99).ogg"
                self.sound3line = "sfx/t-3fl(99).ogg"
                self.sound4line = "sfx/t-4fl(99).ogg"

            elif persistent.skin == 3:

                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound2line = "sfx/t-2fl.ogg"
                self.sound3line = "sfx/t-3fl.ogg"
                self.sound4line = "sfx/t-4fl.ogg"

            elif persistent.skin == 4:


                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(g).ogg"
                self.soundline = "sfx/t-fl(g).ogg"
                self.soundldrop = "sfx/t-fl-drop(g).ogg"
                self.soundmove = "sfx/t-move(g).ogg"
                self.soundrotate = "sfx/t-rotate(g).ogg"
                self.sound2line = "sfx/t-2fl(g).ogg"
                self.sound3line = "sfx/t-3fl(g).ogg"
                self.sound4line = "sfx/t-4fl(g).ogg"

            elif persistent.skin == 5:


                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(mb).ogg"
                self.soundline = "sfx/t-fl(mb).ogg"
                self.soundldrop = "sfx/t-fl-drop(mb).ogg"
                self.soundmove = "sfx/t-move(mb).ogg"
                self.soundrotate = "sfx/t-rotate(mb).ogg"
                self.sound2line = "sfx/t-2fl(mb).ogg"
                self.sound3line = "sfx/t-3fl(mb).ogg"
                self.sound4line = "sfx/t-4fl(mb).ogg"

            elif persistent.skin == 6:


                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika//custom_tetris/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-drop.ogg"
                self.soundline = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-fl.ogg"
                self.soundldrop = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-fl-drop.ogg"
                self.soundmove = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-move.ogg"
                self.soundrotate = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-rotate.ogg"
                self.sound2line = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-2fl.ogg"
                self.sound3line = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-3fl.ogg"
                self.sound4line = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-4fl.ogg"


            class current_shape:
                shape = ""
                shape_number = ""
                shape_hold = ""
                new_shape_number = self.piece_list[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.60 - 2
            self.was_it_hold = False
            self.temp_position = 3
            self.current_shape = current_shape()
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape = True
            self.game_over = False
            self.winner = None
            self.Monika_Face = 0



        def addShapeToStage(self, current_x, current_y):
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column

        def render(self, width, height, st, at):
            global PlayerForMonika

            def winner(win):
                global TetrisWinner
                if win == 0:
                    if self.AI == 0:
                        TetrisWinner = 0
                    else:
                        TetrisWinner = 1
                else:
                    if self.AI == 0:
                        TetrisWinner = 1
                    else:
                        TetrisWinner = 0

            for idc in range(4, 8):
                if self.stage[1][idc] != 0:
                    self.game_over = True
                    winner(1)

            if TetrisScore !=0:
                if self.score >= TetrisScore:
                    self.game_over = True
                    winner(0)

            elif LineLimit !=0:
                if self.allLines >= LineLimit:
                    self.game_over = True
                    winner(0)

            if self.game_over:
                import pygame
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            renpy.jump("tetris_over")



            def lines():
                numberOfFullLines = 0

                prevLine = False
                for idr in range(1, 21):
                    fullLine = True
                    for idc in range(1, 11):
                        if self.stage[idr][idc] == 0:
                            fullLine = False
                            break
                    if fullLine:
                        numberOfFullLines += 1
                        renpy.sound.play(self.soundline)
                        for idc in range(1, 11):
                            self.stage[idr][idc] = 0
                        if prevLine != fullLine:
                            for i in range(0, idr-1):
                                for idc in range(1, 11):
                                    self.stage[idr-i][idc] = self.stage[idr-i-1][idc]
                                    self.stage[idr-i-1][idc] = 0
                                    fullLine = False
                    prevLine = fullLine


                self.allLines += numberOfFullLines
                if numberOfFullLines == 1:
                    self.score += 100 * self.level
                elif numberOfFullLines == 2:
                    self.score += 300 * self.level
                    renpy.sound.play(self.sound2line)
                elif numberOfFullLines == 3:
                    self.score += 500 * self.level
                    renpy.sound.play(self.sound3line)
                elif numberOfFullLines == 4:
                    self.score += 800 * self.level
                    renpy.sound.play(self.sound4line)
                self.level =  int(self.allLines/10)+1

            r = renpy.Render(width, height)
            if persistent.skin == 1:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/background.png"), width, height, st, at)

            elif persistent.skin == 2:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/background.png"), width, height, st, at)

            elif persistent.skin == 3:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/background.png"), width, height, st, at)

            elif persistent.skin == 4:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/background.png"), width, height, st, at)

            elif persistent.skin == 5:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/background.png"), width, height, st, at)

            elif persistent.skin == 6:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/background.png"), width, height, st, at)
            r.blit(background, (0, 0))
            lines()
            if self.new_shape:
                self.was_it_hold = False
                self.current_shape.x = 5
                self.current_shape.y = 1
                self.current_shape.shape = self.current_shape.next_shape
                self.current_shape.shape_number = self.current_shape.new_shape_number
                self.piece_list.pop(0)
                if len(self.piece_list) == 0:
                    self.piece_list = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list)
                self.current_shape.new_shape_number = self.piece_list[0]
                self.current_shape.next_shape = self.tetris_shapes[self.current_shape.new_shape_number]
                self.new_shape = False
                self.temp_position = 1
                if self.AI != 0:
                    temp_AI = True
                    for idc in range(1, 11):
                        if self.stage[2][idc] != 0:
                            temp_AI = False
                    if temp_AI:
                        self.movesAI = self.Monika_AI()

            if self.oldst is None:
                self.oldst = st
            if self.level > 19:
                speed_Y = 18
            else:
                speed_Y = self.level
            if self.AI == 1:
                if self.current_shape.y >= 9:
                    self.current_shape.speed = 0.30
            elif self.AI == 2:
                if self.current_shape.y >= 5:
                    self.current_shape.speed = 0.15
            elif self.AI == 3:
                if self.current_shape.y >= 2.5:
                    self.current_shape.speed = 0.075
            elif self.AI == 4:
                self.current_shape.speed = 0.0375 - 13
            elif self.AI == 5:
                self.current_shape.speed = 0.01875 - 26
            elif self.AI == 6:
                self.current_shape.speed = 0.009375 - 39

            if self.temp_position == self.current_shape.y:
                if len(self.movesAI) != 0:
                    if self.movesAI[0] == "r":
                        self.rotateClockWiseAI()
                    else:
                        self.current_shape.x += int(self.movesAI[0])
                    del self.movesAI[0]
                    self.temp_position += 1

            dtime = st - self.oldst
            self.oldst = st
            temp_can_go_down = True
            if self.current_shape.move_time <= 0:

                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y + 1 + idr][self.current_shape.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape.move_time = self.current_shape.speed
                    self.current_shape.y += 1
                else:
                    self.new_shape = True
                    self.addShapeToStage(self.current_shape.x, self.current_shape.y)
            else:
                self.current_shape.move_time -= dtime

            def draw_shape(sx, sy, current_shape,shadow):
                for idr, row in enumerate(current_shape):
                    for idc, column in enumerate(row):
                        if column == 1:
                            shape = renpy.render(self.color_1, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_1, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 2:
                            shape = renpy.render(self.color_2, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_2, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 3:
                            shape = renpy.render(self.color_3, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_3, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 4:
                            shape = renpy.render(self.color_4, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_4, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 5:
                            shape = renpy.render(self.color_5, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_5, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 6:
                            shape = renpy.render(self.color_6, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_6, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 9:
                            shape = renpy.render(self.color_9, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))

            b = "Lines - %(s)d " % {"s":self.allLines }
            c = "Level - %(s)d " % {"s":self.level}
            d = "Next:"

            f = Text(b)
            g = Text(c)
            h = Text(d)

            text_allLines_render = renpy.render(f, width, height, st, at)
            text_level_render = renpy.render(g, width, height, st, at)
            text_next_render = renpy.render(h, width, height, st, at)


            if self.AI == 0:
                r.blit(text_allLines_render, (-120, -100))
                r.blit(text_level_render, (-120, -50))
                r.blit(text_next_render, (-120, -10))
                draw_shape(-100, 40, self.current_shape.next_shape,0)
                i = "Hold:"
                j = Text(i)
                text_hold_render = renpy.render(j, width, height, st, at)
                r.blit(text_hold_render, (-120, 100))
                draw_shape(-100, 160, self.current_shape.shape_hold,0)
                if LineLimit != 0:
                    i = "Line to Victory - %(s)d " % {"s":LineLimit}
                    j = Text(i)
                    text_line = renpy.render(j, width, height, st, at)
                    r.blit(text_line, (420, -100))
                    PlayerForMonika = self.allLines
                elif TetrisScore != 0:
                    a = "Score - %(s)d " % {"s":self.score }
                    e = Text(a)
                    text_score_render = renpy.render(e, width, height, st, at)
                    r.blit(text_score_render, (30, -100))
                    PlayerForMonika = self.score
            else:
                if LineLimit != 0 and (self.allLines > LineLimit/4 or PlayerForMonika > LineLimit/4):
                    if self.Monika_Face <> 1 and self.allLines > PlayerForMonika:

                        self.Monika_Face = 1
                        renpy.restart_interaction()
                    elif self.Monika_Face <> 2 and self.allLines < PlayerForMonika:

                        self.Monika_Face = 2
                        renpy.restart_interaction()
                elif TetrisScore != 0 and (self.score > TetrisScore/8 or PlayerForMonika > TetrisScore/8):
                    if self.Monika_Face <> 1 and self.score > PlayerForMonika:

                        self.Monika_Face = 1
                        renpy.restart_interaction()
                    elif self.Monika_Face <> 2 and self.score < PlayerForMonika:

                        self.Monika_Face = 2
                        renpy.restart_interaction()

                r.blit(text_allLines_render, (250, -100))
                r.blit(text_level_render, (250, -50))
                r.blit(text_next_render, (250, -10))
                if TetrisScore != 0:
                    a = "Score - %(s)d " % {"s":self.score }
                    e = Text(a)
                    text_score_render = renpy.render(e, width, height, st, at)
                    r.blit(text_score_render, (30, -100))
                draw_shape(280, 40, self.current_shape.next_shape,0)

            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape.x*self.PIXEL_SIZE, self.current_shape.y*self.PIXEL_SIZE, self.current_shape.shape,1)

            renpy.redraw(self, 0)
            return r


        def rotateClockWise(self, mat):
            tempShape = mat
            tempRow = tempShape
            tempX = self.current_shape.x
            tempY = self.current_shape.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            lenRow = len(mat)
            lenCol = len(mat[0])


            if lenRow == 4:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape.y+=1
                if self.stage[self.current_shape.y][self.current_shape.x-1] == 0:
                    self.current_shape.x-=1
                for idc, row in enumerate(tempRow[0]):
                    if self.stage[self.current_shape.y][self.current_shape.x+idc] != 0:
                        ifRotation = False
                        break

            elif lenRow == 1:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape.y-=1
                self.current_shape.x+=1
                for idr, row in enumerate(tempRow):
                    if self.stage[self.current_shape.y+idr][self.current_shape.x] != 0:
                        ifRotation = False
                        break




            elif lenRow == 2 and lenCol != 2:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y+idr][self.current_shape.x+idc] != 0:
                                ifRotation = False
                                break



            elif lenRow == 3:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                if self.stage[self.current_shape.y][self.current_shape.x+len(tempRow[0])-1] != 0:
                    self.current_shape.x-=1
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y+idr][self.current_shape.x+idc] != 0:
                                ifRotation = False
                                break
            elif lenRow == 2 and lenCol == 2:
                ifRotation = True

            if ifRotation == False:
                tempRow = tempShape
                self.current_shape.x = tempX
                self.current_shape.y = tempY
            return tempRow


        def find_bottom(self):
            temp_y = 0
            for idr in range(self.current_shape.y+len(self.current_shape.shape)-1, 22):
                for idc, column in enumerate(self.current_shape.shape[0]):
                    if self.stage[idr][self.current_shape.x + idc ] != 0:
                        temp_y = idr-len(self.current_shape.shape)
                        break
                if temp_y != 0:
                    break
            for position in range(0, 4):
                temp_fit = True
                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[temp_y+idr][self.current_shape.x + idc] != 0:
                                temp_fit = False
                                break
                if temp_fit:
                    temp_y += 1
                else:
                    temp_y -= 1
                    break
            return temp_y

        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if self.level > 19:
                self.current_shape.speed = 0.40 - 0.03 * 18
            else:
                self.current_shape.speed = 0.40 - 0.03 * (self.level - 1)
            if ev.type == pygame.KEYDOWN and self.AI == 0:
                if ev.key == pygame.K_UP:
                    self.current_shape.shape = self.rotateClockWise(self.current_shape.shape)
                elif ev.key == pygame.K_LEFT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape.x -= 1
                elif ev.key == pygame.K_RIGHT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x + 1 + idc ] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape.x += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape.speed = 0.002
                elif ev.key == pygame.K_SPACE:
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape.x, self.find_bottom())
                    self.new_shape = True
                elif ev.key == pygame.K_q and self.current_shape.shape_hold == "" and self.was_it_hold ==False:
                    self.current_shape.shape_hold = self.current_shape.shape
                    self.new_shape = True
                elif ev.key == pygame.K_e and self.current_shape.shape_hold != "":
                    self.current_shape.next_shape = self.current_shape.shape
                    self.current_shape.shape = self.current_shape.shape_hold
                    self.current_shape.shape_hold = ""
                    self.current_shape.x = 5
                    self.current_shape.y = 1
                    self.was_it_hold = True

        def rotateClockWiseAI(self):
            lenRow = len(self.current_shape.shape)
            lenCol = len(self.current_shape.shape[0])
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0,column)
            del self.current_shape.shape
            self.current_shape.shape = tempRow



        def Monika_AI(self):
            def calculateScoreForMove():
                height = 0
                lines = 0
                holes = 0
                temp_col_height = [None] * 10
                bumpiness = 0

                for idr in range(20, 0, -1):
                    temp_clear_line = True
                    for idc in range(1, 11):
                        if self.stage[idr][idc] == 0:
                            temp_clear_line = False
                            break
                    if temp_clear_line:
                        lines += 1

                for idc in range(1, 11):
                    temp_col_height[idc-1] = 0
                    temp_holes = 0
                    for idr in range(20, 0, -1):
                        if self.stage[idr][idc] != 0:
                            holes += temp_holes
                            temp_holes = 0
                        else:
                            temp_holes += 1
                        if self.stage[idr][idc] != 0:
                            temp_col_height[idc-1] = 21-idr
                for i in range(0, 9):
                    height += temp_col_height[i]
                    bumpiness += abs(temp_col_height[i] - temp_col_height[i+1])
                height += temp_col_height[9]
                score = (-0.510066 * height) + (0.760666 * lines) - (0.35663 * holes) - (0.184483 * bumpiness)
                return score

            def shapeRotation(shape):
                if shape == 6:
                    return 2
                elif shape == 0 or shape == 3 or shape == 4:
                    return 5
                elif shape == 1 or shape == 2 or shape == 5:
                    return 3


            def bestMove():
                import copy
                moves = []
                best_score = -100
                temp_shape = copy.deepcopy(self.current_shape.shape)
                temp_rotation = shapeRotation(self.current_shape.shape_number)


                temp_stage = copy.deepcopy(self.stage)
                for rot in range(1, temp_rotation):
                    temp_len = len(self.current_shape.shape[0])-1
                    for idc in range(1, 11-temp_len):
                        del self.stage
                        self.stage = copy.deepcopy(temp_stage)
                        temp_break = False
                        for idr in range(1, 22):
                            for idcShape in range(0, len(self.current_shape.shape[0])):
                                if self.current_shape.shape[len(self.current_shape.shape)-1][idcShape] != 0:
                                    if self.stage[idr][idc+idcShape] != 0:
                                        temp_idr = idr
                                        temp_break = True
                                        break
                            if temp_break:
                                break
                        for idr in range(0, 21):
                            temp_free = True
                            temp_idr -= 1
                            for idrShape, row in enumerate(self.current_shape.shape):
                                for idcShape, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[temp_idr+(idrShape-(len(self.current_shape.shape)-1))][idc+idcShape] != 0:
                                            temp_free = False
                            if temp_free:
                                self.addShapeToStage(idc, temp_idr-(len(self.current_shape.shape)-1))
                                temp_score = calculateScoreForMove()
                                if temp_score > best_score:
                                    best_score = temp_score
                                    moves = [idc-5, rot]
                                break
                    self.rotateClockWiseAI()
                self.stage = copy.deepcopy(temp_stage)
                del temp_stage
                self.current_shape.shape = copy.deepcopy(temp_shape)
                del temp_shape

                temp_moves = []
                for i in range(0, moves[1]-1):
                    temp_moves.append("r")
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        temp_moves.append("1")
                else:
                    for i in range(moves[0], 0):
                        temp_moves.append("-1")
                return temp_moves
            return bestMove()



    class Co_OP_tetris(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.movesAI = []
            self.PIXEL_SIZE = 20
            self.piece_list_player = [0,1,2,3,4,5,6]
            self.piece_list_Monika = [0,1,2,3,4,5,6]
            random.shuffle(self.piece_list_player)
            random.shuffle(self.piece_list_Monika)
            self.tetris_shapes = [
                [[1, 1, 1],
                 [0, 1, 0]],

                [[0, 2, 2],
                 [2, 2, 0]],

                [[3, 3, 0],
                 [0, 3, 3]],

                [[4, 0, 0],
                 [4, 4, 4]],

                [[0, 0, 5],
                 [5, 5, 5]],

                [[6, 6, 6, 6]],

                [[7, 7],
                 [7, 7]]
            ]

            self.stage = [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                         [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]]

            if persistent.skin == 1:

                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound4line = "sfx/t-4fl.ogg"


            elif persistent.skin == 2:

                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(99).ogg"
                self.soundline = "sfx/t-fl(99).ogg"
                self.soundldrop = "sfx/t-fl-drop(99).ogg"
                self.soundmove = "sfx/t-move(99).ogg"
                self.soundrotate = "sfx/t-rotate(99).ogg"
                self.sound2line = "sfx/t-2fl(99).ogg"
                self.sound3line = "sfx/t-3fl(99).ogg"
                self.sound4line = "sfx/t-4fl(99).ogg"


            elif persistent.skin == 3:

                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound4line = "sfx/t-4fl.ogg"


            elif persistent.skin == 4:


                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(g).ogg"
                self.soundline = "sfx/t-fl(g).ogg"
                self.soundldrop = "sfx/t-fl-drop(g).ogg"
                self.soundmove = "sfx/t-move(g).ogg"
                self.soundrotate = "sfx/t-rotate(g).ogg"
                self.sound4line = "sfx/t-4fl(g).ogg"

            elif persistent.skin == 5:


                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(mb).ogg"
                self.soundline = "sfx/t-fl(mb).ogg"
                self.soundldrop = "sfx/t-fl-drop(mb).ogg"
                self.soundmove = "sfx/t-move(mb).ogg"
                self.soundrotate = "sfx/t-rotate(mb).ogg"
                self.sound2line = "sfx/t-2fl(mb).ogg"
                self.sound3line = "sfx/t-3fl(mb).ogg"
                self.sound4line = "sfx/t-4fl(mb).ogg"

            elif persistent.skin == 6:


                self.color_1 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_1.png")
                self.color_2 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_2.png")
                self.color_3 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_3.png")
                self.color_4 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_4.png")
                self.color_5 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_5.png")
                self.color_6 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_6.png")
                self.color_7 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_7.png")
                self.color_9 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/cube_8.png")

                self.shadow_color_1 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_1.png")
                self.shadow_color_2 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_2.png")
                self.shadow_color_3 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_3.png")
                self.shadow_color_4 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_4.png")
                self.shadow_color_5 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_5.png")
                self.shadow_color_6 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_6.png")
                self.shadow_color_7 = Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-drop.ogg"
                self.soundline = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-fl.ogg"
                self.soundldrop = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-fl-drop.ogg"
                self.soundmove = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-move.ogg"
                self.soundrotate = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-rotate.ogg"
                self.sound2line = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-2fl.ogg"
                self.sound3line = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-3fl.ogg"
                self.sound4line = "Submods/Learn together/Play Tetris with Monika/custom_tetris/t-4fl.ogg"


            class current_shape_player:
                shape = ""
                shape_number = ""
                new_shape_number = self.piece_list_player[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.40

            class current_shape_Monika:
                shape = ""
                shape_number = ""
                new_shape_number = self.piece_list_Monika[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.40

            self.temp_position = 3
            self.current_shape_player = current_shape_player()
            self.current_shape_Monika = current_shape_Monika ()
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape_player = True
            self.new_shape_Monika = True
            self.game_over = False
            self.winner = None



        def addShapeToStage(self, current_shape, current_x, current_y):
            for idr, row in enumerate(current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column

        def render(self, width, height, st, at):

            global TetrisWinner

            for idc in range(4, 16):
                if self.stage[1][idc] != 0:
                    self.game_over = True

            if self.game_over:
                if self.score > persistent.best_co_op_tetris_score:
                    persistent.best_co_op_tetris_score = self.score
                    TetrisWinner = 2
                else:
                    TetrisWinner = 3
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            renpy.jump("tetris_over")



            def lines():
                numberOfFullLines = 0

                prevLine = False
                for idr in range(1, 21):
                    fullLine = True
                    for idc in range(1, 21):
                        if self.stage[idr][idc] == 0:
                            fullLine = False
                            break
                    if fullLine:
                        numberOfFullLines += 1
                        renpy.sound.play(self.soundline)
                        for idc in range(1, 21):
                            self.stage[idr][idc] = 0
                        if prevLine != fullLine:
                            for i in range(0, idr-1):
                                for idc in range(1, 21):
                                    self.stage[idr-i][idc] = self.stage[idr-i-1][idc]
                                    self.stage[idr-i-1][idc] = 0
                                    fullLine = False
                    prevLine = fullLine


                self.allLines += numberOfFullLines
                if numberOfFullLines == 1:
                    self.score += 100 * self.level
                elif numberOfFullLines == 2:
                    self.score += 300 * self.level
                elif numberOfFullLines == 3:
                    self.score += 500 * self.level
                elif numberOfFullLines == 4:
                    self.score += 800 * self.level
                    renpy.sound.play(self.sound4line)
                self.level =  int(self.allLines/10)+1

            r = renpy.Render(width, height)

            if persistent.skin == 1:
                background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 2:
                background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_99/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 3:
                background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gb/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 4:
                background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_gmd/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 5:
                background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/images/tetris/tetris_mb/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 6:
                background = renpy.render(Image("Submods/Learn together/Play Tetris with Monika/custom_tetris/background_co_op.png"), width, height, st, at)

            r.blit(background, (0, 0))
            lines()


            if self.new_shape_player:
                self.current_shape_player.x = 5
                self.current_shape_player.y = 1
                self.current_shape_player.shape = self.current_shape_player.next_shape
                self.current_shape_player.shape_number = self.current_shape_player.new_shape_number
                self.piece_list_player.pop(0)
                if len(self.piece_list_player) == 0:
                    self.piece_list_player = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list_player)
                self.current_shape_player.new_shape_number = self.piece_list_player[0]
                self.current_shape_player.next_shape = self.tetris_shapes[self.current_shape_player.new_shape_number]
                self.new_shape_player = False


            if self.new_shape_Monika:
                self.current_shape_Monika.x = 15
                self.current_shape_Monika.y = 1
                self.current_shape_Monika.shape = self.current_shape_Monika.next_shape
                self.current_shape_Monika.shape_number = self.current_shape_Monika.new_shape_number
                self.piece_list_Monika.pop(0)
                if len(self.piece_list_Monika) == 0:
                    self.piece_list_Monika = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list_Monika)
                self.current_shape_Monika.new_shape_number = self.piece_list_Monika[0]
                self.current_shape_Monika.next_shape = self.tetris_shapes[self.current_shape_Monika.new_shape_number]
                self.new_shape_Monika = False
                self.temp_position = 1
                temp_AI = True
                for idc in range(1, 21):
                    if self.stage[2][idc] != 0:
                        temp_AI = False
                if temp_AI:
                    self.movesAI = self.Monika_AI()

            if self.oldst is None:
                self.oldst = st

            if self.current_shape_Monika.y >= 4:
                self.current_shape_Monika.speed = 0.4 - 0.03 * (self.level - 1)

            if self.temp_position == self.current_shape_Monika.y:
                for i in range(0, 3):
                    if len(self.movesAI) != 0:
                        if self.movesAI[0] == "r":
                            self.rotateClockWiseAI()
                        else:
                            self.current_shape_Monika.x += int(self.movesAI[0])
                        del self.movesAI[0]
                self.temp_position += 1

            dtime = st - self.oldst
            self.oldst = st
            temp_can_go_down = True


            if self.current_shape_player.move_time <= 0:

                for idr, row in enumerate(self.current_shape_player.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y + 1 + idr][self.current_shape_player.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape_player.move_time = self.current_shape_player.speed
                    self.current_shape_player.y += 1
                else:
                    self.new_shape_player = True
                    self.addShapeToStage(self.current_shape_player, self.current_shape_player.x, self.current_shape_player.y)
            else:
                self.current_shape_player.move_time -= dtime


            if self.current_shape_Monika.move_time <= 0:

                for idr, row in enumerate(self.current_shape_Monika.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_Monika.y + 1 + idr][self.current_shape_Monika.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape_Monika.move_time = self.current_shape_Monika.speed
                    self.current_shape_Monika.y += 1
                else:
                    self.new_shape_Monika = True
                    self.addShapeToStage(self.current_shape_Monika, self.current_shape_Monika.x, self.current_shape_Monika.y)
            else:
                self.current_shape_Monika.move_time -= dtime

            def draw_shape(sx, sy, current_shape,shadow):
                for idr, row in enumerate(current_shape):
                    for idc, column in enumerate(row):
                        if column == 1:
                            shape = renpy.render(self.color_1, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_1, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 2:
                            shape = renpy.render(self.color_2, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_2, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 3:
                            shape = renpy.render(self.color_3, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_3, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 4:
                            shape = renpy.render(self.color_4, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_4, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 5:
                            shape = renpy.render(self.color_5, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_5, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 6:
                            shape = renpy.render(self.color_6, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_6, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 9:
                            shape = renpy.render(self.color_9, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))

            a = "Score - %(s)d " % {"s":self.score }
            b = "Lines - %(s)d " % {"s":self.allLines }
            c = "Level - %(s)d " % {"s":self.level}
            d = "Next player:"
            i = "Best Score - %(s)d " % {"s":persistent.best_co_op_tetris_score }
            k = "Next Monika:"

            e = Text(a)
            f = Text(b)
            g = Text(c)
            h = Text(d)
            j = Text(i)
            l = Text(k)

            text_allLines_render = renpy.render(f, width, height, st, at)
            text_level_render = renpy.render(g, width, height, st, at)
            text_next_player_render = renpy.render(h, width, height, st, at)
            text_next_Monika_render = renpy.render(l, width, height, st, at)

            text_score_render = renpy.render(e, width, height, st, at)
            r.blit(text_score_render, (5, -50))

            text_score_render = renpy.render(j, width, height, st, at)
            r.blit(text_score_render, (5, -100))
            r.blit(text_allLines_render, (250, -100))
            r.blit(text_level_render, (250, -50))

            r.blit(text_next_player_render, (5, 450))
            draw_shape(25, 500, self.current_shape_player.next_shape,0)

            r.blit(text_next_Monika_render, (250, 450))
            draw_shape(275, 500, self.current_shape_Monika.next_shape,0)

            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape_player.x*self.PIXEL_SIZE, self.current_shape_player.y*self.PIXEL_SIZE, self.current_shape_player.shape,1)
            draw_shape(self.current_shape_Monika.x*self.PIXEL_SIZE, self.current_shape_Monika.y*self.PIXEL_SIZE, self.current_shape_Monika.shape,0)

            renpy.redraw(self, 0)
            return r


        def rotateClockWise(self, mat):
            tempShape = mat
            tempRow = tempShape
            tempX = self.current_shape_player.x
            tempY = self.current_shape_player.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            lenRow = len(mat)
            lenCol = len(mat[0])


            if lenRow == 4:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape_player.y+=1
                if self.stage[self.current_shape_player.y][self.current_shape_player.x-1] == 0:
                    self.current_shape_player.x-=1
                for idc, row in enumerate(tempRow[0]):
                    if self.stage[self.current_shape_player.y][self.current_shape_player.x+idc] != 0:
                        ifRotation = False
                        break

            elif lenRow == 1:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape_player.y-=1
                self.current_shape_player.x+=1
                for idr, row in enumerate(tempRow):
                    if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x] != 0:
                        ifRotation = False
                        break




            elif lenRow == 2 and lenCol != 2:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x+idc] != 0:
                                ifRotation = False
                                break



            elif lenRow == 3:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                if self.stage[self.current_shape_player.y][self.current_shape_player.x+len(tempRow[0])-1] != 0:
                    self.current_shape_player.x-=1
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x+idc] != 0:
                                ifRotation = False
                                break
            elif lenRow == 2 and lenCol == 2:
                ifRotation = True

            if ifRotation == False:
                tempRow = tempShape
                self.current_shape_player.x = tempX
                self.current_shape_player.y = tempY
            return tempRow

        def find_bottom(self):
            temp_y = 0
            for idr in range(self.current_shape_player.y, 22):
                for idc, column in enumerate(self.current_shape_player.shape[0]):
                    if self.stage[idr][self.current_shape_player.x + idc ] != 0:
                        temp_y = idr-len(self.current_shape_player.shape)
                        break
                if temp_y != 0:
                    break
            for position in range(0, 4):
                temp_fit = True
                for idr, row in enumerate(self.current_shape_player.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[temp_y+idr][self.current_shape_player.x + idc] != 0:
                                temp_fit = False
                                break
                if temp_fit:
                    temp_y += 1
                else:
                    temp_y -= 1
                    break
            return temp_y

        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if self.level > 19:
                self.current_shape.speed = 0.40 - 0.03 * 18
            else:
                self.current_shape_player.speed = 0.40 - 0.03 * (self.level - 1)
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.current_shape_player.shape = self.rotateClockWise(self.current_shape_player.shape)
                elif ev.key == pygame.K_LEFT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape_player.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape_player.y + idr][self.current_shape_player.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape_player.x -= 1
                elif ev.key == pygame.K_RIGHT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape_player.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape_player.y + idr][self.current_shape_player.x + 1 + idc ] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape_player.x += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape_player.speed = 0.002
                elif ev.key == pygame.K_SPACE:
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape_player, self.current_shape_player.x, self.find_bottom())
                    self.new_shape_player = True

        def rotateClockWiseAI(self):
            lenRow = len(self.current_shape_Monika.shape)
            lenCol = len(self.current_shape_Monika.shape[0])
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(self.current_shape_Monika.shape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0,column)
            del self.current_shape_Monika.shape
            self.current_shape_Monika.shape = tempRow



        def Monika_AI(self):
            def calculateScoreForMove():
                height = 0
                lines = 0
                holes = 0
                temp_col_height = [None] * 20
                bumpiness = 0

                for idr in range(20, 0, -1):
                    temp_clear_line = True
                    for idc in range(1, 21):
                        if self.stage[idr][idc] == 0:
                            temp_clear_line = False
                            break
                    if temp_clear_line:
                        lines += 1

                for idc in range(1, 21):
                    temp_col_height[idc-1] = 0
                    temp_holes = 0
                    for idr in range(20, 0, -1):
                        if self.stage[idr][idc] != 0:
                            holes += temp_holes
                            temp_holes = 0
                        else:
                            temp_holes += 1
                        if self.stage[idr][idc] != 0:
                            temp_col_height[idc-1] = 21-idr
                for i in range(0, 19):
                    height += temp_col_height[i]
                    bumpiness += abs(temp_col_height[i] - temp_col_height[i+1])
                height += temp_col_height[19]
                score = (-0.510066 * height) + (0.760666 * lines) - (0.35663 * holes) - (0.184483 * bumpiness)
                return score

            def shapeRotation(shape):
                if shape == 6:
                    return 2
                elif shape == 0 or shape == 3 or shape == 4:
                    return 5
                elif shape == 1 or shape == 2 or shape == 5:
                    return 3


            def bestMove():
                import copy
                moves = [0,1]
                best_score = -100
                temp_shape = copy.deepcopy(self.current_shape_Monika.shape)
                temp_rotation = shapeRotation(self.current_shape_Monika.shape_number)


                temp_stage = copy.deepcopy(self.stage)
                for rot in range(1, temp_rotation):
                    temp_len = len(self.current_shape_Monika.shape[0])-1
                    for idc in range(1, 21-temp_len):
                        del self.stage
                        self.stage = copy.deepcopy(temp_stage)
                        temp_break = False
                        for idr in range(1, 22):
                            for idcShape in range(0, len(self.current_shape_Monika.shape[0])):
                                if self.current_shape_Monika.shape[len(self.current_shape_Monika.shape)-1][idcShape] != 0:
                                    if self.stage[idr][idc+idcShape] != 0:
                                        temp_idr = idr
                                        temp_break = True
                                        break
                            if temp_break:
                                break
                        for idr in range(0, 21):
                            temp_free = True
                            temp_idr -= 1
                            for idrShape, row in enumerate(self.current_shape_Monika.shape):
                                for idcShape, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[temp_idr+(idrShape-(len(self.current_shape_Monika.shape)-1))][idc+idcShape] != 0:
                                            temp_free = False
                            if temp_free:
                                self.addShapeToStage(self.current_shape_Monika, idc, temp_idr-(len(self.current_shape_Monika.shape)-1))
                                temp_score = calculateScoreForMove()
                                if temp_score > best_score:
                                    best_score = temp_score
                                    moves = [idc-15, rot]
                                break
                    self.rotateClockWiseAI()
                self.stage = copy.deepcopy(temp_stage)
                del temp_stage
                self.current_shape_Monika.shape = copy.deepcopy(temp_shape)
                del temp_shape

                temp_moves = []
                for i in range(0, moves[1]-1):
                    temp_moves.append("r")
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        temp_moves.append("1")
                else:
                    for i in range(moves[0], 0):
                        temp_moves.append("-1")
                return temp_moves

            return bestMove()


