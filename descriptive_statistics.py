import numpy as np
import csv
import pandas as pd


with open(".../asd_data.csv", "r") as csv_file:
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


no_males_with_autism, no_males_without_autism = get_num_of_samples_out_of_autism(male, autism, "1")
print(f"no of males with autism: {no_males_with_autism}")
print(f"no males without autism: {no_males_without_autism}")
no_public_with_autism, no_public_without_autism = get_num_of_samples_out_of_autism(public, autism, "1")
print(f"no public without autism: {no_public_without_autism}")
print(f"no public with autism: {no_public_with_autism}")

no_private_with_autism, no_private_without_autism = get_num_of_samples_out_of_autism(private, autism, "1")
print(f"no private without autism: {no_private_without_autism}")
print(f"no private with autism: {no_private_with_autism}")

no_publicprivate_with_autism, no_publicprivate_without_autism = get_num_of_samples_out_of_autism(publicprivate, autism,
                                                                                                 "1")
print(f"no publicprivate without autism: {no_publicprivate_without_autism}")
print(f"no publicprivate with autism: {no_publicprivate_with_autism}")

no_hmissing_with_autism, no_hmissing_without_autism = get_num_of_samples_out_of_autism(hmissing, autism, "1")
print(f"no hmissing without autismn: {no_hmissing_without_autism}")
print(f"no hmissing with autism: {no_hmissing_with_autism}")

no_municipals_with_autism, no_municipals_without_autism = get_num_of_samples_out_of_autism(municipals, autism, "1")
print(f" no municipals without autism: {no_municipals_without_autism}")
print(f"no municipals autism: {no_municipals_with_autism}")

no_municipalml_with_autism, no_municipalml_without_autism = get_num_of_samples_out_of_autism(municipalml, autism, "1")
print(f"no municpalml without autism: {no_municipalml_without_autism}")
print(f"no municpalml with autism: {no_municipalml_with_autism}")

no_municipalmet_with_autism, no_municipalmet_without_autism = get_num_of_samples_out_of_autism(municipalmet, autism,
                                                                                               "1")
print(f"no municpalmet without autism: {no_municipalmet_without_autism}")
print(f"no municpalmet with autism: {no_municipalmet_with_autism}")

no_african_with_autism, no_african_without_autism = get_num_of_samples_out_of_autism(african, autism, "1")
print(f"no african without autism: {no_african_without_autism}")
print(f"no african with autism: {no_african_with_autism}")

no_asian_with_autism, no_asian_without_autism = get_num_of_samples_out_of_autism(asian, autism, "1")
print(f"no asian without autism: {no_asian_without_autism}")
print(f"no asian with autism: {no_asian_with_autism}")

no_caucasian_with_autism, no_caucasian_without_autism = get_num_of_samples_out_of_autism(caucasian, autism, "1")
print(f"no caucasian without autism: {no_caucasian_without_autism}")
print(f"no caucasian with autism: {no_caucasian_with_autism}")

no_indigenous_with_autism, no_indigenous_without_autism = get_num_of_samples_out_of_autism(indigenous, autism, "1")
print(f"no indigenous without autism: {no_indigenous_without_autism}")
print(f"no indigenous with autism: {no_indigenous_with_autism}")

no_mixed_with_autism, no_mixed_without_autism = get_num_of_samples_out_of_autism(mixed, autism, "1")
print(f"no mixed without autism: {no_mixed_without_autism}")
print(f"no mixed with autism: {no_mixed_with_autism}")

no_rmissing_with_autism, no_rmissing_without_autism = get_num_of_samples_out_of_autism(rmissing, autism, "1")
print(f"no rmissing without autism: {no_rmissing_without_autism}")
print(f"no rmissing with autism: {no_rmissing_with_autism}")

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

no_fever_with_autism, no_fever_without_autism = get_num_of_samples_out_of_autism(fever, autism, "1")
print(f"no fever without autism: {no_fever_without_autism}")
print(f"no fever with autism: {no_fever_with_autism}")

no_cough_with_autism, no_cough_without_autism = get_num_of_samples_out_of_autism(cough, autism, "1")
print(f"no cough without autism: {no_cough_without_autism}")
print(f"no cough with autism: {no_cough_with_autism}")

no_sorethroat_with_autism, no_sorethroat_without_autism = get_num_of_samples_out_of_autism(sorethroat, autism, "1")
print(f"no sorethroat without autism: {no_sorethroat_without_autism}")
print(f"no sorethroat with autism: {no_sorethroat_with_autism}")

no_dyspnea_with_autism, no_dyspnea_without_autism = get_num_of_samples_out_of_autism(dyspnea, autism, "1")
print(f"no dyspnea without autism: {no_dyspnea_without_autism}")
print(f"no dyspnea with autism: {no_dyspnea_with_autism}")

no_spo2_with_autism, no_spo2_without_autism = get_num_of_samples_out_of_autism(spo2, autism, "1")
print(f"no spo2 without autism: {no_spo2_without_autism}")
print(f"no spo2 with autism: {no_spo2_with_autism}")

no_resp_with_autism, no_resp_without_autism = get_num_of_samples_out_of_autism(resp, autism, "1")
print(f"no resp without autism: {no_resp_without_autism}")
print(f"no resp with autism: {no_resp_with_autism}")

no_diarrhea_with_autism, no_diarrhea_without_autism = get_num_of_samples_out_of_autism(diarrhea, autism, "1")
print(f"no diarrhea without autism: {no_diarrhea_without_autism}")
print(f"no diarrhea with autism: {no_diarrhea_with_autism}")

no_vomit_with_autism, no_vomit_without_autism = get_num_of_samples_out_of_autism(vomit, autism, "1")
print(f"no vomit without autism: {no_vomit_without_autism}")
print(f"no vomit with autism: {no_vomit_with_autism}")

no_abdpain_with_autism, no_abdpain_without_autism = get_num_of_samples_out_of_autism(abdpain, autism, "1")
print(f"no abdpain without autism: {no_abdpain_without_autism}")
print(f"no abdpain with autism: {no_abdpain_with_autism}")

no_fatigue_with_autism, no_fatigue_without_autism = get_num_of_samples_out_of_autism(fatigue, autism, "1")
print(f"no fatigue without autism: {no_fatigue_without_autism}")
print(f"no fatigue with autism: {no_fatigue_with_autism}")

no_dead_with_autism, no_dead_without_autism = get_num_of_samples_out_of_autism(dead, autism, "1")
print(f"no dead without autism: {no_dead_without_autism}")
print(f"no dead with autism: {no_dead_with_autism}")

no_anosmia_with_autism, no_anosmia_without_autism = get_num_of_samples_out_of_autism(anosmia, autism, "1")
print(f"no anosmia without autism: {no_anosmia_without_autism}")
print(f"no anosmia with autism: {no_anosmia_with_autism}")

no_ageusia_with_autism, no_ageusia_without_autism = get_num_of_samples_out_of_autism(ageusia, autism, "1")
print(f"no ageusia without autism: {no_ageusia_without_autism}")
print(f"no ageusia with autism: {no_ageusia_with_autism}")

no_headache_with_autism, no_headache_without_autism = get_num_of_samples_out_of_autism(headache, autism, "1")
print(f"no headache without autism: {no_headache_without_autism}")
print(f"no headache with autism: {no_headache_with_autism}")

no_nausea_with_autism, no_nausea_without_autism = get_num_of_samples_out_of_autism(nausea, autism, "1")
print(f"no nausea without autism: {no_nausea_without_autism}")
print(f"no nausea with autism: {no_nausea_with_autism}")

no_nasal_with_autism, no_nasal_without_autism = get_num_of_samples_out_of_autism(nasal, autism, "1")
print(f"no nasal without autism: {no_nasal_without_autism}")
print(f"no nasal with autism: {no_nasal_with_autism}")

no_cardio_with_autism, no_cardio_without_autism = get_num_of_samples_out_of_autism(cardio, autism, "1")
print(f"no cardio without autism: {no_cardio_without_autism}")
print(f"no cardio with autism: {no_cardio_with_autism}")

no_asthma_with_autism, no_asthma_without_autism = get_num_of_samples_out_of_autism(asthma, autism, "1")
print(f"no asthma without autism: {no_asthma_without_autism}")
print(f"no asthma with autism: {no_asthma_with_autism}")

no_immuno_with_autism, no_immuno_without_autism = get_num_of_samples_out_of_autism(immuno, autism, "1")
print(f"no immuno without autism: {no_immuno_without_autism}")
print(f"no immuno with autism: {no_immuno_with_autism}")

no_liver_with_autism, no_liver_without_autism = get_num_of_samples_out_of_autism(liver, autism, "1")
print(f"no liver without autism: {no_liver_without_autism}")
print(f"no liver with autism: {no_liver_with_autism}")

no_neuro_with_autism, no_neuro_without_autism = get_num_of_samples_out_of_autism(neuro, autism, "1")
print(f"no neuro without autism: {no_neuro_without_autism}")
print(f"no neuro with autism: {no_neuro_with_autism}")

no_renal_with_autism, no_renal_without_autism = get_num_of_samples_out_of_autism(renal, autism, "1")
print(f"no renal without autism: {no_renal_without_autism}")
print(f"no renal with autism: {no_renal_with_autism}")

no_down_with_autism, no_down_without_autism = get_num_of_samples_out_of_autism(down, autism, "1")
print(f"no down without autism: {no_down_without_autism}")
print(f"no down with autism: {no_down_with_autism}")

no_diabe_with_autism, no_diabe_without_autism = get_num_of_samples_out_of_autism(diabe, autism, "1")
print(f"no diabe without autism: {no_diabe_without_autism}")
print(f"no diabe with autism: {no_diabe_with_autism}")

no_obesity_with_autism, no_obesity_without_autism = get_num_of_samples_out_of_autism(obesity, autism, "1")
print(f"no obesity without autism: {no_obesity_without_autism}")
print(f"no obesity with autism: {no_obesity_with_autism}")

no_pulmonary_with_autism, no_pulmonary_without_autism = get_num_of_samples_out_of_autism(pulmonary, autism, "1")
print(f"no pulmonary without autism: {no_pulmonary_without_autism}")
print(f"no pulmonary with autism: {no_pulmonary_with_autism}")

no_hiv_with_autism, no_hiv_without_autism = get_num_of_samples_out_of_autism(hiv, autism, "1")
print(f"no hiv without autism: {no_hiv_without_autism}")
print(f"no hiv with autism: {no_hiv_with_autism}")

no_cancer_with_autism, no_cancer_without_autism = get_num_of_samples_out_of_autism(cancer, autism, "1")
print(f"no cancer without autism: {no_cancer_without_autism}")
print(f"no cancer with autism: {no_cancer_with_autism}")

no_hypothyroid_with_autism, no_hypothyroid_without_autism = get_num_of_samples_out_of_autism(hypothyroid, autism, "1")
print(f"no hypothyroid without autism: {no_hypothyroid_without_autism}")
print(f"no hypothyroid with autism: {no_hypothyroid_with_autism}")

no_vacflu_with_autism, no_vacflu_without_autism = get_num_of_samples_out_of_autism(vacflu, autism, "1")
print(f"no vacflu without autism: {no_vacflu_without_autism}")
print(f"no vacflu with autism: {no_vacflu_with_autism}")

no_antiviral_with_autism, no_antiviral_without_autism = get_num_of_samples_out_of_autism(antiviral, autism, "1")
print(f"no antiviral without autism: {no_antiviral_without_autism}")
print(f"no antiviral with autism: {no_antiviral_with_autism}")

no_icu_with_autism, no_icu_without_autism = get_num_of_samples_out_of_autism(icu, autism, "1")
print(f"no icu without autism: {no_icu_without_autism}")
print(f"no icu with autism: {no_icu_with_autism}")

no_vaccovid_with_autism, no_vaccovid_without_autism = get_num_of_samples_out_of_autism(vaccovid, autism, "1")
print(f"no vaccovid without autism: {no_vaccovid_without_autism}")
print(f"no vaccovid with autism: {no_vaccovid_with_autism}")

no_ventinv_with_autism, no_ventinv_without_autism = get_num_of_samples_out_of_autism(ventinv, autism, "1")
print(f"no ventinv without autism: {no_ventinv_without_autism}")
print(f"no ventinv with autism: {no_ventinv_with_autism}")

no_ventnoninv_with_autism, no_ventnoninv_without_autism = get_num_of_samples_out_of_autism(ventnoninv, autism, "1")
print(f"no ventnoninv without autism: {no_ventnoninv_without_autism}")
print(f"no ventnoninv with autism: {no_ventnoninv_with_autism}")

no_psychserv_with_autism, no_psychserv_without_autism = get_num_of_samples_out_of_autism(psychserv, autism, "TRUE")
print(f"no psychserv without autism: {no_psychserv_without_autism}")
print(f"no psychserv with autism: {no_psychserv_with_autism}")



num_of_autis = 0
for a in autism:
  if a=="1":
    num_of_autis+=1

print(f"num of autis: {num_of_autis}")


age_validated_is_autis = []
age_validated_is_non_autis= []
num_ages_missing_is_autis = 0
num_ages_missing_is_non_autis = 0

for i, age in enumerate(ages):
  if autism[i] == "1":
    if age == "NA":
      num_ages_missing_is_autis+= 1
    else:
      age_validated_is_autis.append(age)
  if autism[i] == "0":
    if age == "NA":
      num_ages_missing_is_non_autis +=1
    else:
      age_validated_is_non_autis.append(age)

print(f"num ages missing is autis: {num_ages_missing_is_autis}")
print(f"num ages missing non autis: {num_ages_missing_is_non_autis}")


num_of_patients = 1230298
num_of_non_autis = num_of_patients - num_of_autis

print(f"percentage of missing age non autis: {num_ages_missing_is_non_autis / num_of_non_autis*100}")


float_values = [float(i) for i in age_validated_is_autis]
sorted_age_validated_is_autis = np.sort(float_values)
index = int(len(sorted_age_validated_is_autis)/2 -0.5)

print(f"sorted age validated is autis: {sorted_age_validated_is_autis[index]}")
print(f"median float values is autis: {np.median(float_values)}")

Q1 = np.median(sorted_age_validated_is_autis[:index])
Q2 = np.median(sorted_age_validated_is_autis[index:])

IQR = Q2 - Q1
print(f"IQR is autis: {IQR}")

float_values = [float(i) for i in age_validated_is_non_autis]
sorted_age_validated_non_autis = np.sort(float_values)
index = int(len(age_validated_is_non_autis)/2 -0.5)

print(f"sorted age validated non autis: {sorted_age_validated_non_autis[index]}")
print(f"median float values non autis: {np.median(float_values)}")

Q1 = np.median(sorted_age_validated_non_autis[:index])
Q2 = np.median(sorted_age_validated_non_autis[index:])

IQR = Q2 - Q1
print(f"IQR non autis: {IQR}")


# percentages
percentage_dead_with_aut = (no_dead_with_autism/num_of_autis)*100
print(f"percentage of dead autistic patients of all autistic patients: {percentage_dead_with_aut}")

percentage_dead_without_aut = (no_dead_without_autism/num_of_non_autis)*100
print(f"percentage of dead non-autistic patients of all non-autistic patients: {percentage_dead_without_aut}")



# Load the dataset from CSV file into a pandas DataFrame
df = pd.read_csv('../asd_data.csv')
