import mysignals as sigs


_mean =0.0

def calc_mean(sig_src_arr):
    global _mean
    for x in range(len(sig_src_arr)):
        _mean += sig_src_arr[x]
    _mean = _mean/len(sig_src_arr)
    return _mean
    
print(calc_mean(sigs.InputSignal_1kHz_15kHz))
