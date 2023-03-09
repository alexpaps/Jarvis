#English Song List
def EnglishSongs():
    import pygame
    import time
    from mutagen.mp3 import MP3
    import speech_recognition as sr
    import sys

    # function to play the current song
    def play_current_song():
        global current_song_index
        global audio_files
        while current_song_index < len(audio_files):
            # load and play the current song        
            pygame.mixer.music.load(audio_files[current_song_index])
            pygame.mixer.music.play()
                          
            current_song_index += 1
            
            length = mutagen_length(audio_files[current_song_index-1])

            # Set the target time
            start_time = time.time()
            #target_time = time.time() + length

            while time.time() - start_time  < length:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    StInput = r.recognize_google(audio)
                except:
                    continue

                k = 0
                #Exit the program
                if StInput.find("exit")!=-1 :#or StInput.find("stop")!=-1  :
                    if k == -1:
                        sys.exit()
                    else:
                        k = 1
                        break
                #Next Song
                elif StInput.find("next song")!=-1:
                    play_next_song()
                #Pause the Song
                elif StInput.find("pause")!=-1 or StInput.find("pose")!=-1 or StInput.find("stop the music")!=-1 or StInput.find("stop")!=-1:
                    stop_time = time.time()
                    pause_current_song()
                #Resume the song
                elif StInput.find("resume")!=-1 or StInput.find("start")!=-1:
                    resume_time = time.time()
                    start_time = start_time + (resume_time - stop_time)
                    resume_current_song()
                #Replay the song    
                elif StInput.find("replay")!=-1:
                    replay_current_song()
                #Play the previus song
                elif StInput.find("previous song") != -1:
                    play_previous_song()
                #Play a specific song from the song list
                elif StInput.find("play") != -1:
                    k = -1
                    name = StInput.strip("play")
                    name = (name.lower()).strip()
                    print(name)
                    play_specific_song(name)
            if k ==1:
                break

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

    def mutagen_length(path):
        try:
            audio = MP3(path)
            length = audio.info.length
            return length
        except:
            return None

    # function to play the next song
    def play_next_song():
        global current_song_index
        
        print(current_song_index)

        # if the current song index exceeds the number of songs, set it back to 0
        if current_song_index >= len(audio_files):
            current_song_index = 0

        # play the next song
        play_current_song()

    # function to pause the current song
    def pause_current_song():
        pygame.mixer.music.pause()

    # function to resume the current song
    def resume_current_song():
        pygame.mixer.music.unpause()

    # function to replay the current song
    def replay_current_song():
        global current_song_index
        current_song_index -= 1
        pygame.mixer.music.rewind()
        play_current_song()

    # function to play the previous song
    def play_previous_song():
        global current_song_index
        current_song_index -= 2
        pygame.mixer.music.rewind()
        play_current_song()

    # play a specific song from the song list
    def play_specific_song(name):
        global current_song_index
        global audio_files

        for audio_file_index in range(len(audio_files)):
            audio = audio_files[audio_file_index].lower()
            print(audio)
            if audio.find(name) != -1:
                current_song_index = audio_file_index
                print(current_song_index)
                break
        play_current_song()

    pygame.init()

    # set the mixer frequency and size
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    # create a list of audio file names
    global audio_files
    audio_files = ["People You Know.mp3","LA VIDA ES UNA(from PUSS IN BOOTS).mp3", "Radioactive.mp3", "Coldplay.mp3","Clocks.mp3","I Aint Worried.mp3","Maybe My Soulmate Died.mp3","Pepas.mp3","Bones.mp3","Grenade.mp3","The Lazy Song.mp3","Hurt.mp3","Start Again.mp3"]

    # set the current song index to 0
    global current_song_index
    current_song_index = 0
        
    # start playing the first song
    play_current_song()

    # quit pygame
    pygame.quit()

#Greek Song List
def GreekSongs():
    import pygame
    import time
    from mutagen.mp3 import MP3
    import speech_recognition as sr
    import sys

    # function to play the current song
    def play_current_song():
        global current_song_index
        global audio_files
        while current_song_index < len(audio_files):
            # load and play the current song        
            pygame.mixer.music.load(audio_files[current_song_index])
            pygame.mixer.music.play()
                    
            current_song_index += 1
            
            length = mutagen_length(audio_files[current_song_index-1])

            # Set the target time
            target_time = time.time() + length
            while time.time() < target_time:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    StInput = r.recognize_google(audio)
                except:
                    continue

                #Exit the program
                if StInput.find("exit")!=-1 :#or StInput.find("stop")!=-1  :
                    sys.exit()
                #Next Song
                elif StInput.find("next song")!=-1:
                    play_next_song()
                #Pause the Song
                elif StInput.find("pause")!=-1 or StInput.find("pose")!=-1 or StInput.find("stop the music")!=-1 or StInput.find("stop")!=-1:
                    pause_current_song()
                #Resume the song
                elif StInput.find("resume")!=-1 or StInput.find("start")!=-1:
                    resume_current_song()
                #Replay the song    
                elif StInput.find("replay")!=-1:
                    replay_current_song()
                #Play the previus song
                elif StInput.find("previous song") != -1:
                    play_previous_song()
                #Play a specific song from the song list
                elif StInput.find("play") != -1:
                    name = StInput.strip("play")
                    name = (name.lower()).strip()
                    print(name)
                    play_specific_song(name)

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

    def mutagen_length(path):
        try:
            audio = MP3(path)
            length = audio.info.length
            return length
        except:
            return None

    # function to play the next song
    def play_next_song():
        global current_song_index
        
        print(current_song_index)

        # if the current song index exceeds the number of songs, set it back to 0
        if current_song_index >= len(audio_files):
            current_song_index = 0

        # play the next song
        play_current_song()

    # function to pause the current song
    def pause_current_song():
        pygame.mixer.music.pause()

    # function to resume the current song
    def resume_current_song():
        pygame.mixer.music.unpause()

    # function to replay the current song
    def replay_current_song():
        global current_song_index
        current_song_index -= 1
        pygame.mixer.music.rewind()
        play_current_song()

    # function to play the previous song
    def play_previous_song():
        global current_song_index
        current_song_index -= 2
        pygame.mixer.music.rewind()
        play_current_song()

    # play a specific song from the song list
    def play_specific_song(name):
        global current_song_index
        global audio_files

        for audio_file_index in range(len(audio_files)):
            audio = audio_files[audio_file_index].lower()
            print(audio)
            if audio.find(name) != -1:
                current_song_index = audio_file_index
                print(current_song_index)
                break
        play_current_song()

    pygame.init()

    # set the mixer frequency and size
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    # create a list of audio file names
    global audio_files
    audio_files = ["Pame Havai.mp3",]

    # set the current song index to 0
    global current_song_index
    current_song_index = 0
        
    # start playing the first song
    play_current_song()

    # quit pygame
    pygame.quit()



#Army Song - Visino.mp3 
def Christooulos():
    import pygame
    import time
    from mutagen.mp3 import MP3
    import speech_recognition as sr
    import sys

    # function to play the current song
    def play_current_song():
        global current_song_index
        global audio_files
        while current_song_index < len(audio_files):
            # load and play the current song        
            pygame.mixer.music.load(audio_files[current_song_index])
            pygame.mixer.music.play()

            current_song_index += 1
            
            length = mutagen_length(audio_files[current_song_index-1])

            # Set the target time
            start_time = time.time()
            #target_time = time.time() + length

            while time.time() - start_time  < length:

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    StInput = r.recognize_google(audio)
                except:
                    continue

                k = 0
                #Exit the program
                if StInput.find("exit")!=-1 :#or StInput.find("stop")!=-1  :
                    if k == -1:
                        sys.exit()
                    else:
                        k = 1
                        break
                #Pause the Song
                elif StInput.find("pause")!=-1 or StInput.find("pose")!=-1 or StInput.find("stop the music")!=-1 or StInput.find("stop")!=-1:
                    stop_time = time.time()
                    pause_current_song()
                #Resume the song
                elif StInput.find("resume")!=-1 or StInput.find("start")!=-1:
                    resume_time = time.time()
                    start_time = start_time + (resume_time - stop_time)
                    resume_current_song()
                #Replay the song    
                elif StInput.find("replay")!=-1:
                    replay_current_song()
            if k ==1:
                break

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

    def mutagen_length(path):
        try:
            audio = MP3(path)
            length = audio.info.length
            return length
        except:
            return None

    # function to pause the current song
    def pause_current_song():
        pygame.mixer.music.pause()

    # function to resume the current song
    def resume_current_song():
        pygame.mixer.music.unpause()

    # function to replay the current song
    def replay_current_song():
        global current_song_index
        current_song_index -= 1
        pygame.mixer.music.rewind()
        play_current_song()

    pygame.init()

    # set the mixer frequency and size
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

    # create a list of audio file names
    global audio_files
    audio_files = ["Visino.mp3"]
    # set the current song index to 0
    global current_song_index
    current_song_index = 0
        
    # start playing the first song
    play_current_song()

    # quit pygame
    pygame.quit()