# Video cutter
from moviepy.editor import VideoFileClip

# Cherche la video
clip = VideoFileClip("vid.mp4")

# Coupe la video avec le temps de début et le temps de fin (en secondes)
video_cliped = clip.subclip(10, 40)

# On peut également choisir des temps spécifiques à la video comme "fin de la video"
video_cliped_2 = clip.subclip(40, clip.end)

# Sauvegarde le clip
video_cliped.write_videofile("clip.mp4")
video_cliped_2.write_videofile("clip2.mp4")
