import essentia
import json
from essentia.streaming import *

def rhythm_extractor(filename):
    pool = essentia.Pool()

    loader = AudioLoader(filename=filename)
    mixer = MonoMixer()
    bt = RhythmExtractor2013()
    loader.audio >> mixer.audio
    loader.numberChannels >> mixer.numberChannels
    loader.sampleRate >> None
    loader.md5 >> None
    loader.bit_rate >> None
    loader.codec >> None
    mixer.audio >> bt.signal
    bt.bpm >> (pool, 'bpm')
    bt.ticks >> (pool, 'ticks')
    bt.confidence >> (pool, 'confidence')
    bt.estimates >> (pool, 'estimates')
    bt.bpmIntervals >> (pool, 'bpmIntervals')
    essentia.run(loader)

    result = {'bpm' : pool['bpm'], 'ticks' : list(pool['ticks']), 'confidence' : pool['confidence'], 'estimates' : list(pool['estimates']), 'bpmIntervals' : list(pool['bpmIntervals'])}
    print result

    return result
