# processing edf file format

# import numpy as np
# import mne
# edf = mne.io.read_raw_edf('your_edf_file.edf')
# header = ','.join(edf.ch_names)
# np.savetxt('your_csv_file.csv', edf.get_data().T, delimiter=',', header=header)


# adding sampling time

# import csv

# FS = 1000

# y = []
# x = []
# x.append(float(0))
# dataset = []
# sampling = 1 / FS
# with open('file.csv', 'r') as csv_file:
#     i = 0
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         y.append(float(line[1]))
#         x.append(float(x[i] + sampling))
#         dataset.append([x[i], y[i]])
#         i += 1
# with open('file_processed.csv', 'w') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     for [xval, yval] in dataset:
#         csv_writer.writerow([xval, yval])
