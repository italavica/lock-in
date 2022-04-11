from matplotlib.pyplot import plot, legend, show, grid, figure, savefig, title

import csv
with open(r'C:\Users\ezxiaav\Documents\Lock-in Spectrometer\sine_wave.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        print(row)

# figure(figsize=(10,5))
# plot(t,PS1_filtered_3, 'g', linewidth=1.75,label='PS1')
# plot(loc_PS1_3/fs,PS1_filtered_3[loc_PS1_3], 'r*', linewidth=1.75)
# plot(t,PS2_filtered_3, 'b', linewidth=1.75,label='PS2')
# plot(loc_PS2_3/fs,PS2_filtered_3[loc_PS2_3], 'r*', linewidth=1.75)
# legend()
# title("Peaks PS1 and PS2")
# grid(True)
# show()