import essentia
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

    print pool
    return (pool['bpm'], pool['ticks'], pool['confidence'], pool['estimates'], pool['bpmIntervals'])
