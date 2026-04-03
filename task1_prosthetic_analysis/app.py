import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="EMG Signal Analysis", layout="wide")


st.title(" Prosthetic EMG Signal Analysis Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/EMG_data.csv")
    return df


df = load_data()


channel_cols = [col for col in df.columns if "channel" in col]


st.sidebar.header(" Controls")

selected_channel = st.sidebar.selectbox("Select Channel", channel_cols)

if "label" in df.columns:
    selected_label = st.sidebar.selectbox("Select Label", df["label"].unique())
    filtered_df = df[df["label"] == selected_label]
else:
    filtered_df = df


st.subheader(" Dataset Preview")
st.dataframe(filtered_df.head(100))


st.subheader(f" {selected_channel} Signal Over Time")

fig1, ax1 = plt.subplots()
ax1.plot(filtered_df["time"], filtered_df[selected_channel])
ax1.set_xlabel("Time")
ax1.set_ylabel("Signal Strength")
ax1.set_title(f"{selected_channel} vs Time")
st.pyplot(fig1)


st.subheader(" Signal Distribution")

fig2, ax2 = plt.subplots()
sns.histplot(filtered_df[selected_channel], kde=True, ax=ax2)
ax2.set_title("Signal Distribution")
st.pyplot(fig2)


st.subheader(" Multi-Channel Comparison")

fig3, ax3 = plt.subplots()

for ch in channel_cols[:4]:
    ax3.plot(filtered_df["time"], filtered_df[ch], label=ch)

ax3.legend()
ax3.set_title("Multiple Channels Comparison")
st.pyplot(fig3)


st.subheader(" Channel Correlation")

fig4, ax4 = plt.subplots()
sns.heatmap(df[channel_cols].corr(), cmap="coolwarm", annot=False, ax=ax4)
ax4.set_title("Channel Correlation Heatmap")
st.pyplot(fig4)


st.subheader(" Peak Signal Detection")

signal = filtered_df[selected_channel]

threshold = signal.mean() + 2 * signal.std()
peaks = signal[signal > threshold]

st.write(f" Detected Peaks: {len(peaks)}")

fig5, ax5 = plt.subplots()
ax5.plot(filtered_df["time"], signal, label="Signal")
ax5.scatter(filtered_df.loc[peaks.index, "time"], peaks, color="red", label="Peaks")
ax5.legend()
ax5.set_title("Peak Detection")
st.pyplot(fig5)


st.subheader(" Signal Strength (RMS)")

rms = np.sqrt(np.mean(signal**2))
st.write(f" RMS Value: {rms:.6f}")


st.subheader(" Insights")

st.write(" EMG signals show time-varying muscle activation patterns.")
st.write(" High amplitude spikes indicate strong muscle contractions.")
st.write(" RMS value represents overall muscle effort level.")
st.write(" Channel correlation suggests coordinated muscle activity across sensors.")
st.write(" Different labels correspond to distinct movement patterns.")


st.markdown("---")
st.write("Developed by Simhadri Kondapally ")
