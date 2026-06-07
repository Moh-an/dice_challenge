# import moviepy.editor
from moviepy import ImageClip, concatenate_videoclips, TextClip, AudioFileClip, CompositeVideoClip
from moviepy import *
from moviepy.video.fx import FadeIn, FadeOut, Resize

# Load your images - replace with your file paths
images = [
    ImageClip("temple_1.jpeg").with_duration(4),
    ImageClip("priests_aarti.jpeg").with_duration(4),
    ImageClip("bhasma_aarti.jpeg").with_duration(4)
]

# Add effects and transitions
clips = []
for img in images:
    clip = (img
            .resized(width=1080)
            .with_effects([FadeIn(0.5), FadeOut(0.5)])
            .resized(lambda t: 1 + 0.02*t))  # slow zoom
    clips.append(clip)

video = concatenate_videoclips(clips, method="compose")

# Add text overlay
txt = TextClip(
    text="Om Namah Shivaya\nMahakaleshwar Jyotirlinga",
    font_size=70,
    color='white',
    # font='Arial-Bold',
    stroke_color='gold',
    stroke_width=2
)
txt = txt.with_position('center').with_duration(video.duration)

# Add background audio - replace with your chant file
# audio = AudioFileClip("om_namah_shivaya.mp3").with_volume_scaled(0.8)
# video = video.with_audio(audio).with_duration(audio.duration)

# Add the text on top
final = CompositeVideoClip([video, txt])

# Export
final.write_videofile("mahakaleshwar_aarti.mp4", fps=24, codec='libx264')