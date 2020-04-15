#import bibliotek
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#wyświetlenie zawartości katalagou opinions
print(os.listdir("./opinions"))

#wczytanie id produktu, którego opinie będą analizowane
product_id = input("Podaj kod produktu: ")

opinions = pd.read_json("opinions/"+product_id+".json")
opinions = opinions.set_index("opinion_id")

opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",",".")))

#histogram częstości występowanie poszczególnej oceny 
stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
fig, ax = plt.subplots()
stars.plot.bar(color="lightskyblue")
ax.set_title("gwiazdki")
ax.set_xlabel("liczba gwiazdek")
ax.set_ylabel("liczba opinii")
plt.savefig("figures/"+product_id+"_bar.png")
plt.close()

#udział poszczególmych rekomendacji w ogólnej liczbie opinii
recommendation = opinions["recommendation"].value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label="", autopct="%1.1f%%", colors=['forestgreen', 'crimson'])
plt.savefig("figures/"+product_id+"_pie.png")
plt.close()

average_score = opinions["stars"].mean()
pros = opinions["pros"].count()
cons = opinions["cons"].count()
purchased = opinions["purchased"].sum()

print(average_score,pros,cons,purchased)

stars_purchased = pd.crosstab(opinions["stars"], opinions["purchased"])

print(stars_purchased)