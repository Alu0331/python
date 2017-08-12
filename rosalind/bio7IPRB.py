from sys import argv

# Get the populations.
d, h, r = map(float, input().strip().split())

# How many are there, total?
t = d + h + r

# How probable is it that we pick two dominants?
# Or a dominant and a hetero? Or a dominant and a recessive?
dd = d/t * (d-1)/(t-1)
dh = d/t * h/(t-1) + h/t * d/(t-1)
dr = d/t * r/(t-1) + r/t * d/(t-1)

# How probable is it that we pick two heteros?
# How about a hetero and a recessive?
hh = h/t * (h-1)/(t-1)
hr = h/t * r/(t-1) + r/t * h/(t-1)

# The pairings without a dominant result in a dominant less often.
total = dd+dh+dr + hh*0.75 + hr*0.5

print(total)