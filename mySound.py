# # use winsound. can't control volume. can't use without wav
# import winsound
# def playSound():
#     winsound.PlaySound("complete.wav",winsound.SND_FILENAME)

# use playsound. can't control volume.
import playsound as ps
class mySound():
    def __init__(self):
        pass
    def playSound(self,_filepath):
        try:
            ps.playsound(_filepath)
        except:
            pass

# use audioplayer.
# from audioplayer import AudioPlayer
# class mySound():
#     def __init__(self):
#         self.sound = AudioPlayer("./complete.mp3")
#         self.sound.volume = 50
#         # pass

#     def playSound(self):
#         print("SOUND!")
#         self.sound.play(loop=False, block=True)
#         self.sound.stop()
