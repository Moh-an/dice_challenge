import subprocess
from pathlib import Path

def ex_in(audio_path,output_path):
    """
       Extracts the instrumentals from an audio file by isolating vocals.

       Parameters:
           audio_path (str): Path to the input audio file (e.g., 'song.mp3' or 'track.wav').
           output_dir (str): Directory where the separated stems will be saved.
       """
    print(f'{audio_path} proceessing audio')
    # Construct the demucs command
    # --two-stems=vocals splits the audio into 'vocals' and 'no_vocals' (the instruments)
    command=[
        "demucs",
        "--two-stems=vocals",
        "-o", output_path,
        audio_path
    ]
    try:
        # Run the command line tool via Python subprocess
        subprocess.run(command,check=True)
        # Locate the extracted instrumental file
        file_path=Path(audio_path).stem
        # Demucs saves files under: output_dir/model_name/file_name/
        instrumental_path = Path(output_path) / "no_vocals.wav"

        print("\nSeparation Complete!")
        print(f"Instruments saved to: {instrumental_path}")
        print(f"Vocals saved to: {Path(output_path) / 'vocals.wav'}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during extraction: {e}")
    except FileNotFoundError:
        print("Error: 'demucs' command not found. Please ensure it is installed via pip.")

    # Example Usage
if __name__ == "__main__":
        # Replace with your actual file path
    my_song = 'C://Users//Mohan//Downloads//Avinash_Gupta.mp3'
    ex_in(my_song,'C/Users/Mohan/Downloads')


