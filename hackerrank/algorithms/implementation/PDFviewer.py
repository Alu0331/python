'''Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
 The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples.
 With no arguments, it returns an empty iterator. '''
h = list(map(int, input().strip().split(' ')))
word = input().strip()
h_max = 0
zipped = (zip("abcdefghijklmnopqrstuvwxyz", h))
dict = {key: value for (key, value) in zipped}
for i in word:
    if dict[i] > h_max:
        h_max = dict[i]
print(h_max * len(word))