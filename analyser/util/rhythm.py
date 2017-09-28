#encoding:utf-8
import essentia
import json
import variables
import os
from essentia.streaming import *
from multiprocessing import Process, Manager

def rhythm_extractor(filename):
    manager = Manager()
    result = manager.list()
    filename = os.path.join(variables.UPLOAD_FOLDER, filename)
    p = Process(target=__rhythm_extractor_process, args=(filename, result,))
    p.start()
    p.join()
    # 这里的实现不是很好，问题是python2里的manager.dict()有bug，无法共享内存，所以用list.append代替，再取第0个元素
    return result[0]

def __rhythm_extractor_process(filename, result):
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
    result.append({'bpm': pool['bpm'], 'ticks': list(pool['ticks']), 'confidence': pool['confidence'],
              'estimates': list(pool['estimates']), 'bpmIntervals': list(pool['bpmIntervals'])})
    pool.clear()
