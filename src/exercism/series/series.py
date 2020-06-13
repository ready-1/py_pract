def slices(series, length):
    if len(series) < length:
        raise ValueError('String is shorter than series length')
    if length < 1:
        raise ValueError('Length is less than 1')
    reps = len(series) - length + 1
    return [series[i:i + length] for i in range(0, reps)]
