import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="EEG Brainwave Analysis", layout="wide")


st.title(" EEG Brainwave Analysis Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/EEG_data.csv")
    return df


df = load_data()


brainwaves = [
    "Delta",
    "Theta",
    "Alpha1",
    "Alpha2",
    "Beta1",
    "Beta2",
    "Gamma1",
    "Gamma2",
]


st.sidebar.header(" Filters")

selected_wave = st.sidebar.selectbox("Select Brainwave", brainwaves)

if "predefinedlabel" in df.columns:
    selected_label = st.sidebar.selectbox(
        "Select Label", df["predefinedlabel"].unique()
    )
    filtered_df = df[df["predefinedlabel"] == selected_label]
else:
    filtered_df = df


st.subheader(" Key Metrics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Average Attention", int(filtered_df["Attention"].mean()))

with col2:
    st.metric("Average Meditation", int(filtered_df["Mediation"].mean()))

st.subheader(" Dataset Preview")
st.dataframe(filtered_df.head(50))


st.subheader(f" {selected_wave} Distribution")

fig1, ax1 = plt.subplots()
sns.histplot(filtered_df[selected_wave], kde=True, ax=ax1)
st.pyplot(fig1)

st.subheader(" Brainwave Comparison")

fig2, ax2 = plt.subplots()
filtered_df[brainwaves].mean().plot(kind="bar", ax=ax2)
ax2.set_title("Average Brainwave Activity")
st.pyplot(fig2)


st.subheader(" Attention vs Meditation")

fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["Attention"], filtered_df["Mediation"])
ax3.set_xlabel("Attention")
ax3.set_ylabel("Meditation")
st.pyplot(fig3)


if "predefinedlabel" in df.columns:
    st.subheader(" Label Distribution")
    st.bar_chart(df["predefinedlabel"].value_counts())


st.subheader(" Brainwave Correlation")

fig4, ax4 = plt.subplots()
sns.heatmap(filtered_df[brainwaves].corr(), cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

st.subheader(" Dominant Brainwave")

avg_wave = filtered_df[brainwaves].mean()
dominant = avg_wave.idxmax()

st.success(f" Dominant Brainwave: {dominant}")

st.subheader(" Top 3 Brainwaves")

top3 = avg_wave.sort_values(ascending=False).head(3)
st.write(top3)


st.subheader(" Insights")

st.write(" Different brainwaves represent different mental states.")
st.write(" Alpha waves indicate relaxation and calmness.")
st.write(" Beta waves indicate active thinking and focus.")
st.write(" Theta waves relate to deep relaxation or drowsiness.")
st.write(" Attention and Meditation values show cognitive state variations.")
st.write(" Correlation between waves shows brain activity patterns.")


st.markdown("---")
st.write("Developed by Simhadri Kondapally ")
