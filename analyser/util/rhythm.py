import essentia
import json
from essentia.streaming import *

def rhythm_extractor(filename):
    pool = essentia.Pool()

    loader = MonoLoader(filename=filename)
    bt = RhythmExtractor2013()
    loader.audio >> bt.signal
    bt.bpm >> (pool, 'bpm')
    bt.ticks >> (pool, 'ticks')
    bt.confidence >> (pool, 'confidence')
    bt.estimates >> (pool, 'estimates')
    bt.bpmIntervals >> (pool, 'bpmIntervals')
    essentia.run(loader)

    result = {'bpm' : pool['bpm'], 'ticks' : list(pool['ticks']), 'confidence' : pool['confidence'], 'estimates' : list(pool['estimates']), 'bpmIntervals' : list(pool['bpmIntervals'])}
    print result

    return result
