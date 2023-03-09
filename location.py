import numpy as np
import csv

with open("../asd_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    data = []
    for row in csv_reader:
        data.append(row)

data_without_columns = data[1:]


data_processing = np.array(data_without_columns)
data_processing.shape


columns = data[0]
print(len(columns))
print(columns)
print(columns[8])

ages = data_processing[:, 2]
male = data_processing[:, 8]
dead = data_processing[:, 1]
public = data_processing[:, 9]
private = data_processing[:, 10]
publicprivate = data_processing[:, 11]
hmissing = data_processing[:, 12]
municipals = data_processing[:, 13]
municipalml = data_processing[:, 14]
municipalmet = data_processing[:, 15]
african = data_processing[:, 16]
asian = data_processing[:, 17]
caucasian = data_processing[:, 18]
indigenous = data_processing[:, 19]
mixed = data_processing[:, 20]
rmissing = data_processing[:, 21]
centerwest = data_processing[:, 22]
north = data_processing[:, 23]
northeast = data_processing[:, 24]
south = data_processing[:, 25]
southeast = data_processing[:, 26]
fever = data_processing[:, 27]
cough = data_processing[:, 28]
sorethroat = data_processing[:, 29]
dyspnea = data_processing[:, 30]
spo2 = data_processing[:, 31]
resp = data_processing[:, 32]
diarrhea = data_processing[:, 33]
vomit = data_processing[:, 34]
abdpain = data_processing[:, 35]
fatigue = data_processing[:, 36]
anosmia = data_processing[:, 37]
ageusia = data_processing[:, 38]
headache = data_processing[:, 39]
nausea = data_processing[:, 40]
nasal = data_processing[:, 41]
cardio = data_processing[:, 42]
asthma = data_processing[:, 43]
immuno = data_processing[:, 44]
liver = data_processing[:, 45]
neuro = data_processing[:, 46]
renal = data_processing[:, 47]
down = data_processing[:, 48]
diabe = data_processing[:, 49]
obesity = data_processing[:, 50]
pulmonary = data_processing[:, 51]
hiv = data_processing[:, 52]
cancer = data_processing[:, 53]
hypothyroid = data_processing[:, 54]
autism = data_processing[:, 55]
vacflu = data_processing[:, 56]
antiviral = data_processing[:, 57]
icu = data_processing[:, 58]
vaccovid = data_processing[:, 59]
ventinv = data_processing[:, 60]
ventnoninv = data_processing[:, 61]
psychserv = data_processing[:, 62]


def get_num_of_samples(samples, value_of_interest):
    num_of_samples = 0
    for sample in samples:
        if sample == value_of_interest:
            num_of_samples += 1
    return num_of_samples


print(f"number of samples autism: {get_num_of_samples(autism,  1)}")
print(f"Number of samples male : {get_num_of_samples(male, 1)} ")


def get_num_of_samples_out_of_autism(samples, sample_autism_value, value_of_interest):
    num_of_samples_with_autism = 0
    num_of_samples_without_autism = 0
    for i, sample in enumerate(samples):
        if sample == value_of_interest:
            if sample_autism_value[i] == "1":
                num_of_samples_with_autism += 1
            else:
                num_of_samples_without_autism += 1
    return num_of_samples_with_autism, num_of_samples_without_autism


no_centerwest_with_autism, no_centerwest_without_autism = get_num_of_samples_out_of_autism(centerwest, autism, "1")
print(f"no centerwest without autism: {no_centerwest_without_autism}")
print(f"no centerwest with autism: {no_centerwest_with_autism}")

no_north_with_autism, no_north_without_autism = get_num_of_samples_out_of_autism(north, autism, "1")
print(f"no north without autism: {no_north_without_autism}")
print(f"no north with autism: {no_north_with_autism}")

no_northeast_with_autism, no_northeast_without_autism = get_num_of_samples_out_of_autism(northeast, autism, "1")
print(f"no northeast without autism: {no_northeast_without_autism}")
print(f"no northeast with autism: {no_northeast_with_autism}")

no_south_with_autism, no_south_without_autism = get_num_of_samples_out_of_autism(south, autism, "1")
print(f"no south without autism: {no_south_without_autism}")
print(f"no south with autism: {no_south_with_autism}")

no_southeast_with_autism, no_southeast_without_autism = get_num_of_samples_out_of_autism(southeast, autism, "1")
print(f"no southeast without autism: {no_southeast_without_autism}")
print(f"no southeast with autism: {no_southeast_with_autism}")
