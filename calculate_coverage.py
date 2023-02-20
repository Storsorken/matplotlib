import yaml
import numpy as np

with open("flag_arrays.yml") as fin:
        data = yaml.load(fin, Loader=yaml.FullLoader)
boxplot_array = np.array(data["BOXPLOT_ARRAY"])
eventplot_array = np.array(data["EVENTPLOT_ARRAY"])
hist_array = np.array(data["HIST_ARRAY"])
make_image_array = np.array(data["MAKE_IMAGE_ARRAY"])
spectral_helper_array = np.array(data["SPECTRAL_HELPER_ARRAY"])
errorbar_array = np.array(data["ERRORBAR_ARRAY"])

print("BOXPLOT coverage: ", boxplot_array.sum()*100/len(boxplot_array), "%")
print("EVENTPLOT coverage: ", eventplot_array.sum()*100/len(eventplot_array), "%")
print("HIST coverage: ", hist_array.sum()*100/len(hist_array), "%")
print("MAKE_IMAGE coverage: ", make_image_array.sum()*100/len(make_image_array), "%")
print("SPECTRAL_HELPER coverage: ", spectral_helper_array.sum()*100/len(spectral_helper_array), "%")
print("ERRORBAR coverage: ", errorbar_array.sum()*100/len(errorbar_array), "%")

reset = input('\nClear flag_arrays.yml file? (Y/N):')
if reset == 'Y':
    data["BOXPLOT_ARRAY"] = []
    data["EVENTPLOT_ARRAY"]= []
    data["HIST_ARRAY"] = []
    data["MAKE_IMAGE_ARRAY"] = []
    data["SPECTRAL_HELPER_ARRAY"] = []
    data["ERRORBAR_ARRAY"] = []
    with open("flag_arrays.yml", "w") as f:
        yaml.dump(data, f)