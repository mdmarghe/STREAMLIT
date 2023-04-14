import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

st.title("IRIS DATASET")
st.header("a summary of Iris Species")
dataset_path='https://frenzy86.s3.eu-west-2.amazonaws.com/fav/iris.data'

iris = pd.read_csv(dataset_path, header=None)


iris.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
st.write(iris)

st.text("vediamo se il db è eterogeneo in base alla classe")
st.dataframe(iris.groupby('class').count())
st.text("il db è eterogeneo")
fig=sns.pairplot(iris,hue='class', height=3, aspect=1)
st.pyplot(fig)
st.text("gia da qui evinciamo che possiamo creare gia un cluster a priori")

from pandas.plotting import parallel_coordinates

plt.figure(figsize=(13,10))
fig2=parallel_coordinates(iris, "class",colormap='cool')

st.pyplot(fig2)

