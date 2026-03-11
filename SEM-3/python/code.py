import os
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects

# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================
# "Editor's Note: We define our constants up front so we can tweak colors 
# and timing without hunting through the whole script."

ASSETS_DIR = "assets"
OUTPUT_FILE = "final_wedding_invite.mp4"
FONT_PATH = os.path.join(ASSETS_DIR, "gujarati_font.ttf") # Path to your .ttf file
VIDEO_SIZE = (1080, 1920) # Vertical HD format

# Colors extracted from the video
COLOR_MAROON = "#5e0e0e"
COLOR_GOLD = "#b8860b"
COLOR_TEXT_BODY = "#2e2e2e"

# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================

def create_gujarati_text(text, fontsize, color, duration, position="center"):
    """
    Creates a text clip. 
    Note: MoviePy uses ImageMagick. Ensure your ImageMagick handles UTF-8 correctly.
    """
    txt_clip = TextClip(
        text, 
        font=FONT_PATH, 
        fontsize=fontsize, 
        color=color, 
        size=(VIDEO_SIZE[0] - 100, None), # Padding
        method='caption',
        align='center'
    ).set_duration(duration).set_position(position)
    return txt_clip

def add_sparkles(clip):
    """
    Simulates the particle overlay effect.
    In a real workflow, we'd overlay a 'dust_particles.mp4' with screen blending.
    Here, we leave a placeholder for where that overlay code goes.
    """
    # If you have a sparkle video overlay:
    # sparkles = VideoFileClip(os.path.join(ASSETS_DIR, "sparkles.mp4"), has_mask=True).resize(VIDEO_SIZE).loop()
    # return CompositeVideoClip([clip, sparkles.set_duration(clip.duration)])
    return clip

# ==========================================
# 3. SCENE CONSTRUCTION
# ==========================================

def build_intro_scene():
    """ 00:00 - 0:05: Ganesha on Clouds """
    duration = 5
    
    # Background: Clouds
    bg = VideoFileClip(os.path.join(ASSETS_DIR, "cloud_bg.mp4")).resize(newsize=VIDEO_SIZE)
    bg = bg.subclip(0, duration).fadein(1)

    # Asset: Ganesha
    ganesha = (ImageClip(os.path.join(ASSETS_DIR, "ganesha.png"))
               .resize(height=400)
               .set_position(("center", 300))
               .set_duration(duration)
               .crossfadein(1))
    
    # Text: Shloka
    shloka = create_gujarati_text(
        "વક્રતુંડ મહાકાય સૂર્યકોટિ સમપ્રભ:\nનિર્વિઘ્નં કુરુ મે દેવ સર્વકાર્યેષુ સર્વદા", 
        40, COLOR_MAROON, duration, ("center", 800)
    ).crossfadein(2)

    return CompositeVideoClip([bg, ganesha, shloka]).set_duration(duration)

def build_invite_scene():
    """ 00:05 - 0:12: The Golden Frame Reveal """
    duration = 7
    
    # Background: Golden texture
    bg = ColorClip(size=VIDEO_SIZE, color=(255, 253, 208), duration=duration) # Cream color
    
    # Asset: Ornate Frame
    frame = (ImageClip(os.path.join(ASSETS_DIR, "gold_frame.png"))
             .resize(width=1000)
             .set_position("center")
             .set_duration(duration))

    # Text Content
    t1 = create_gujarati_text("સસ્નેહ નિમંત્રણ", 60, COLOR_MAROON, duration, ("center", 500))
    t2 = create_gujarati_text("વાઘેલા પરિવાર", 80, COLOR_MAROON, duration, ("center", 700))
    t3 = create_gujarati_text("આપ સૌને ભાવભર્યું નિમંત્રણ પાઠવે છે.", 40, COLOR_TEXT_BODY, duration, ("center", 900))

    return CompositeVideoClip([bg, frame, t1, t2, t3]).set_duration(duration)

def build_couple_scene():
    """ 00:12 - 0:15: Couple Photo with Transition """
    duration = 3
    
    # In the reference, this is a "liquid gold" transition.
    # In code, we simulate this with a CrossFade and a Zoom.
    
    bg = ColorClip(size=VIDEO_SIZE, color=(255, 255, 255), duration=duration)
    
    photo = (ImageClip(os.path.join(ASSETS_DIR, "couple_photo.jpg"))
             .resize(height=800)
             .set_position("center")
             .set_duration(duration)
             .crossfadein(0.5))
             
    # Add a zoom effect (Simulated by resizing over time - advanced MoviePy technique)
    # Keeping it simple for stability:
    return CompositeVideoClip([bg, photo]).set_duration(duration)

def build_names_scene():
    """ 00:15 - 0:28: Chi. Sagar weds Chi. Kavita """
    duration = 13
    
    bg = ColorClip(size=VIDEO_SIZE, color=(255, 253, 208), duration=duration)
    frame = (ImageClip(os.path.join(ASSETS_DIR, "floral_border.png"))
             .resize(VIDEO_SIZE)
             .set_duration(duration))
    
    # Groom Name
    groom = create_gujarati_text("ચિ. સાગર", 90, COLOR_MAROON, duration, ("center", 500))
    # Weds Icon or Text
    weds = create_gujarati_text("સંગે", 50, COLOR_GOLD, duration, ("center", 700))
    # Bride Name
    bride = create_gujarati_text("ચિ. કવિતા", 90, COLOR_MAROON, duration, ("center", 900))

    return CompositeVideoClip([bg, frame, groom, weds, bride]).set_duration(duration)

def build_events_scene():
    """ 00:29 - 0:40: Mangalya Prasango (Events) """
    duration = 11
    
    bg = ColorClip(size=VIDEO_SIZE, color=(255, 253, 208), duration=duration)
    frame = ImageClip(os.path.join(ASSETS_DIR, "gold_frame.png")).resize(width=1000).set_position("center").set_duration(duration)
    
    header = create_gujarati_text(":: માંગલ્ય પ્રસંગો ::", 70, COLOR_MAROON, duration, ("center", 400))
    
    # Event 1
    evt1_title = create_gujarati_text(":: મંડપ મુહૂર્ત ::", 50, COLOR_MAROON, duration, ("center", 600))
    evt1_date = create_gujarati_text("તા. ૨૫-૧૨-૨૦૨૫, ગુરુવાર", 40, COLOR_TEXT_BODY, duration, ("center", 680))
    
    # Event 2
    evt2_title = create_gujarati_text(":: જાન પ્રસ્થાન ::", 50, COLOR_MAROON, duration, ("center", 900))
    evt2_date = create_gujarati_text("સવારે ૯:૦૦ કલાકે", 40, COLOR_TEXT_BODY, duration, ("center", 980))

    return CompositeVideoClip([bg, frame, header, evt1_title, evt1_date, evt2_title, evt2_date]).set_duration(duration)

def build_outro_scene():
    """ 00:40 - End: Venue and Final RSVP """
    duration = 10
    
    bg = ColorClip(size=VIDEO_SIZE, color=(255, 253, 208), duration=duration)
    
    title = create_gujarati_text(":: અવસરનું આંગણું ::", 60, COLOR_MAROON, duration, ("center", 400))
    venue = create_gujarati_text("શ્રી રામજીભાઈ વાઘેલાનું નિવાસ સ્થાન,\nઅમદાવાદ.", 40, COLOR_TEXT_BODY, duration, ("center", 600))
    
    invite_msg = create_gujarati_text("લી. વાઘેલા પરિવાર", 70, COLOR_GOLD, duration, ("center", 1200))

    return CompositeVideoClip([bg, title, venue, invite_msg]).set_duration(duration)

# ==========================================
# 4. MAIN ASSEMBLY LINE
# ==========================================

def assemble_video():
    print("🎬 Starting Video Assembly...")
    
    # 1. Generate Scenes
    clip1 = build_intro_scene()
    clip2 = build_invite_scene()
    clip3 = build_couple_scene()
    clip4 = build_names_scene()
    clip5 = build_events_scene()
    clip6 = build_outro_scene()
    
    # 2. Stitch them together
    # We use fadein/fadeout for smooth transitions between scenes
    final_video = concatenate_videoclips([
        clip1.fadeout(1),
        clip2.fadein(1).fadeout(1),
        clip3.fadein(1).fadeout(1),
        clip4.fadein(1).fadeout(1),
        clip5.fadein(1).fadeout(1),
        clip6.fadein(1)
    ], method="compose") # 'compose' handles fading overlapping well
    
    # 3. Add Music
    if os.path.exists(os.path.join(ASSETS_DIR, "audio.mp3")):
        print("🎵 Adding Music...")
        audio = AudioFileClip(os.path.join(ASSETS_DIR, "audio.mp3"))
        # Loop audio if it's shorter than video, or cut if longer
        if audio.duration < final_video.duration:
            audio = audio_loop(audio, duration=final_video.duration)
        else:
            audio = audio.subclip(0, final_video.duration)
        final_video = final_video.set_audio(audio)
    else:
        print("⚠️ Warning: No audio.mp3 found in assets folder.")

    # 4. Render
    print("🚀 Rendering Final Video... (This may take a while)")
    final_video.write_videofile(
        OUTPUT_FILE, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac",
        threads=4
    )
    print(f"✅ Video saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    # Ensure assets directory exists
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
        print(f"📁 Created '{ASSETS_DIR}' folder. Please place your images/video/font there!")
    else:
        assemble_video()