"""Sort dictionary keys based on value"""
# key arg in sorted is a function that will be called on all the
# elements before comparison, thus this returns the keys of freq in sorted order
freq = {'t': 1, 'r': 1, 'e': 2}
sorted_keys = sorted(freq, key=freq.get, reverse=True)  # max to min