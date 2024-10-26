from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio_on_silence(input_file, output_folder, silence_thresh=-30, min_silence_len=2000, keep_silence=100):
    # Load audio file
    audio = AudioSegment.from_file(input_file, format="wav")

    # Split audio based on silence
    segments = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
        keep_silence=keep_silence
    )

    # Export segments and print their lengths
    for i, segment in enumerate(segments):
        segment.export(f"{output_folder}/segment_{i}.wav", format="wav")
        
        # Calculate and print segment duration in seconds
        segment_duration = len(segment) / 1000.0  # Convert milliseconds to seconds
        print(f"Segment {i}: Duration = {segment_duration:.2f} seconds")

if __name__ == "__main__":
    input_file = "C:\\Users\\Nidhi\\Downloads\\3.wav"
    output_folder = "C:\\Users\\Nidhi\\downloads\\outputfolder1"

    split_audio_on_silence(input_file, output_folder)
