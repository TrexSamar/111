from calendar import c
from numpy import std
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math_score"], show_hist = False)
#fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean of population: ", mean)
print("Standard deviation of population: ", std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean of sample: ", mean)
print("Standard deviation of sample: ", std_deviation)



fsds, fsde = mean - std_deviation, mean + std_deviation
ssds, ssde = mean - (2*std_deviation), mean + (2* std_deviation)
tsds, tsde = mean - (3*std_deviation), mean + (3* std_deviation)

#pltotting tha graph with traces

fig = ff.create_distplot([mean_list], ["Math_score"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean "))
fig.add_trace(go.Scatter(x = [fsds, fsds], y = [0, 0.17], mode = "lines", name = "std_dev_1_start"))
fig.add_trace(go.Scatter(x = [fsde, fsde], y = [0, 0.17], mode = "lines", name = "std_dev_1_end"))

fig.add_trace(go.Scatter(x = [ssds, ssds], y = [0, 0.17], mode = "lines", name = "std_dev_2_start"))
fig.add_trace(go.Scatter(x = [ssde, ssde], y = [0, 0.17], mode = "lines", name = "std_dev_2_end"))

fig.add_trace(go.Scatter(x = [tsds, tsds], y = [0, 0.17], mode = "lines", name = "std_dev_3_start"))
fig.add_trace(go.Scatter(x = [tsde, tsde], y = [0, 0.17], mode = "lines", name = "std_dev_3_end"))

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)

print("mean_of_sample1", mean_of_sample1)
fig.add_trace(go.Scatter(x = [mean_of_sample1, mean_of_sample1], y = [0, 0.17], mode = "lines", name = "mean of students who got fun sheets"))

fig.show()


z =  (mean_of_sample1 - mean) / std_deviation
print(z)
