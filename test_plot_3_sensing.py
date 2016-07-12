import matplotlib.pyplot as plt

index = range(0,10)

random = [1.171278, 2.045942, 2.183006, 1.567254, 1.061972, 1.353644, 2.138906, 1.521760, 2.568738, 1.150876]

myopic = [1.430192, 2.237792, 2.209822, 1.715322, 1.494330, 1.676150, 2.287710, 2.001180, 2.578390, 1.386496]

whittle = [1.398468, 2.199054, 2.200054, 1.654064, 1.391816, 1.639626, 2.221868, 1.870272, 2.576396, 1.316618]

asyncQ = [1.200376, 2.049434, 2.181354, 1.586540, 1.285996, 1.374568, 2.152630, 1.778206, 2.569286, 1.224272]

lz_same = [0.8824744807201103, 0.8475264084865345, 0.8439186264546377, 0.9719334584930805, 0.6995345646028724, 0.87562895790943, 0.8205386126603762, 0.7701701343141177, 0.5937514275238382, 0.8914802338383675]


random_distinct = [1.414802, 1.361716, 1.367178, 1.587614, 1.823710, 1.665240, 1.496756, 1.469092, 1.410450, 1.183566]

whittle_distinct = [2.176666, 1.816336, 1.990938, 2.032402, 2.368728, 2.306860, 1.934146, 2.057038, 1.938204, 1.931010]

asyncQ_distinct = [1.991844, 1.730484, 1.710680, 1.858022, 2.216416, 2.157140, 1.771692, 1.934214, 1.736686, 1.777632]

lz_distinct = [0.647131, 0.834870, 0.744238, 0.823963, 0.776086, 0.657251, 0.810457, 0.733422, 0.748655, 0.616782]


plt.plot(index, random, 'm-o',  index, myopic, 'b-s', index, whittle, 'g-^', index, asyncQ, 'r-*')

plt.ylabel('average reward')
plt.ylabel('index')
plt.title('6 identical markov channel, 3 sensing')

plt.legend(['random', 'myopic', 'whittleIdx', 'Q-learning'], loc='upper center')



plt.show()