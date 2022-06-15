import moviepy.editor as mp
import speech_recognition as sr
import os


def video_2_audio(video_file_path, audio_file_name='converted.tmp.wav'):
    clip = mp.VideoFileClip("videos/"+video_file_path)

    #if clip.duration > 600:  # 600s max video duration to process
    #    raise "ERROR : cannot process a video with more than 10min length !"

    clip.audio.write_audiofile(audio_file_name)


def audio_2_speech(audio_file_path):
    r = sr.Recognizer()
    audio = sr.AudioFile(audio_file_path)
    with audio as source:
        audio_file = r.record(source)

    return r.recognize_google(audio_file)


def video_2_speech(video_file_path):
    default_output_wav_filename = 'converted.tmp.wav'
    video_2_audio(video_file_path)
    result = audio_2_speech(default_output_wav_filename)
    # Remove the generated audio file
    os.remove(default_output_wav_filename)
    return result
