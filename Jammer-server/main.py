from src.audio2midi import audio2midi

if __name__ == '__main__':
    audio2midi.run('/Users/vladikravtsov/Jammer/Jammer-server/src/audio-files/10_second_short_music.wav',
                   '/Users/vladikravtsov/Jammer/Jammer-server/src/midi-files/110_second_short_music.midi')
    print('Kaki Gadol')
