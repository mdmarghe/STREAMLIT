

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import streamlit as st

st.title("Lezione Matplotlib")
st.text("iniziamo con importare le varie librerie")
code='''import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
'''
st.code(code, language='python')
st.subheader("metodo scatter")

x=rand(100)
y=rand(100)

fig=plt.scatter(x,y)
st.pyplot(fig,)




