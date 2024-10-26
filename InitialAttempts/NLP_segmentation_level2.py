import numpy as np
import librosa
import librosa.display
from pydub import AudioSegment
import os
import soundfile as sf
import matplotlib.pyplot as plt

def split_audio_into_segments(audio_file_path, output_folder):
    audio = AudioSegment.from_file(audio_file_path, format="wav")
    
    
    y, sample_rate = librosa.core.load(audio_file_path, sr=None, mono=True)

    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    segments = librosa.effects.split(y, top_db=20)
    segment_count = len(segments)
    
    for i, (start, end) in enumerate(segments):
        segment = y[start:end]
        
        # Export segment directly to the output folder
        output_file_path = os.path.join(output_folder, f"segment_{i}.wav")
        sf.write(output_file_path, segment, sample_rate)
        
        # Calculate and print segment duration in seconds
        segment_duration = (end - start) / sample_rate
        print(f"Segment {i}: Duration = {segment_duration:.2f} seconds")
                
    return segment_count

def plot_audio_with_marks(y, sample_rate, segments):
    plt.figure(figsize=(15, 5))
    librosa.display.waveshow(y, sr=sample_rate, alpha=0.5)
    
    
    for start, end in segments:
        plt.axvline(start, color='r', linestyle='--')
        plt.axvline(end, color='r', linestyle='--')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Original Audio with Segmentation Marks')
    plt.show()

if __name__ == "__main__":
    audio_file_path = "C:\\Users\\Nidhi\\Downloads\\outputfolder1\\segment_1.wav"
    output_folder = "C:\\Users\\Nidhi\\Downloads\\output_segments"
    
    y, sample_rate = librosa.load(audio_file_path, sr=16000, mono=True)
    
    segments = []
    for start, end in librosa.effects.split(y, top_db=20):
        segments.append((start/sample_rate, end/sample_rate))  
    
    plot_audio_with_marks(y, sample_rate, segments)
    
    segment_count = split_audio_into_segments(audio_file_path, output_folder)
    print(f"{segment_count} segments saved to {output_folder}")
