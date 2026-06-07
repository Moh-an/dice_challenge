import os
import sys
import subprocess
from pydub import AudioSegment


def auto_setup_ffmpeg():
    """Automatically downloads and hooks up FFmpeg for Python without Windows PATH setup."""
    try:
        # Check if ffmpeg-downloader can find its local binary
        import ffdl
        # Dynamically locate the bin directory where ffdl installs ffmpeg
        ffdl_bin = os.path.join(os.path.dirname(ffdl.__file__), "bin")

        # Append it to the running script's environment PATH
        if ffdl_bin not in os.environ["PATH"]:
            os.environ["PATH"] += os.pathsep + ffdl_bin

        # Point pydub directly to it
        AudioSegment.converter = os.path.join(ffdl_bin, "ffmpeg.exe")
        AudioSegment.ffprobe = os.path.join(ffdl_bin, "ffprobe.exe")
    except ImportError:
        # If not installed yet, download it immediately via command line
        print("Downloading integrated audio codecs... please wait.")
        subprocess.run([sys.executable, "-m", "ffdl", "install"], check=True)


def extract_instruments_pure_python(input_path, output_path):
    """Extracts instruments by canceling out center-panned vocals."""
    print("Initializing local audio engines...")
    auto_setup_ffmpeg()

    print(f"Loading: {os.path.basename(input_path)}")
    # Load the stereo audio file
    sound = AudioSegment.from_file(input_path)

    # Split the stereo file into separate Left and Right channels
    left, right = sound.split_to_mono()

    print("Isolating instrument frequencies...")
    # Invert the phase of the right channel
    inverted_right = right.invert_phase()

    # Combined Left + Inverted Right cancels out center-panned sounds (Vocals)
    # leaving mostly the stereo-widened instruments behind
    instruments = left.overlay(inverted_right)

    # Export the file back to your downloads folder
    print(f"Saving instrumental to: {output_path}")
    instruments.export(output_path, format="mp3")
    print("Done!")


if __name__ == "__main__":
    target_song = r"C:\Users\Mohan\Downloads\Avinash_Gupta.mp3"
    output_song = r"C:\Users\Mohan\Downloads\Avinash_Gupta_Instruments.mp3"

    if os.path.exists(target_song):
        extract_instruments_pure_python(target_song, output_song)
    else:
        print(f"Error: Can't find file at {target_song}")
