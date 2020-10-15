names = ['Ruturaj', 'Ruturaj mind', 'Ruturaj Efficiency']
values = [1, 10, 100]

plt.figure(figsize=(15, 7))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Ruturaj NON volatiles')
plt.show()
