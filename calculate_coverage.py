import yaml
import numpy as np

with open("flag_arrays.yml") as fin:
        data = yaml.load(fin, Loader=yaml.FullLoader)
boxplot_array = np.array(data["BOXPLOT_ARRAY"])
eventplot_array = np.array(data["EVENTPLOT_ARRAY"])
hist_array = np.array(data["HIST_ARRAY"])
make_image_array = np.array(data["MAKE_IMAGE_ARRAY"])
spectral_helper_array = np.array(data["SPECTRAL_HELPER_ARRAY"])

print("BOXPLOT coverage: ", boxplot_array.sum()*100/len(boxplot_array), "%")
print(f"BOXPLOT uncovered flags#: {' '.join([str(i) for i, v in enumerate(boxplot_array) if not v])}")

print("\nEVENTPLOT coverage: ", eventplot_array.sum()*100/len(eventplot_array), "%")
print(f"EVENTPLOT uncovered flags#: {' '.join([str(i) for i, v in enumerate(eventplot_array) if not v])}")

print("\nHIST coverage: ", hist_array.sum()*100/len(hist_array), "%")
print(f"HIST uncovered flags#: {' '.join([str(i) for i, v in enumerate(hist_array) if not v])}")

print("\nMAKE_IMAGE coverage: ", make_image_array.sum()*100/len(make_image_array), "%")
print(f"MAKE_IMAGE uncovered flags#: {' '.join([str(i) for i, v in enumerate(make_image_array) if not v])}")

print("\nSPECTRAL_HELPER coverage: ", spectral_helper_array.sum()*100/len(spectral_helper_array), "%")
print(f"SPECTRAL_HELPER uncovered flags#: {' '.join([str(i) for i, v in enumerate(spectral_helper_array) if not v])}")

reset = input('\nClear flag_arrays.yml file? (Y/N):')
if reset == 'Y':
    data["BOXPLOT_ARRAY"] = []
    data["EVENTPLOT_ARRAY"]= []
    data["HIST_ARRAY"] = []
    data["MAKE_IMAGE_ARRAY"] = []
    data["SPECTRAL_HELPER_ARRAY"] = []
    with open("flag_arrays.yml", "w") as f:
        yaml.dump(data, f)