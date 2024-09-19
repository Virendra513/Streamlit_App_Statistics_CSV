import streamlit as st
import pandas as pd


st.title(' Let us Find About your Data')
st.subheader('Upload CSV file here')

with st.sidebar:

    st.caption("You need to upload your csv file and find out statistics (mean, median, mode, variance, standard deviation) about your data..")
    st.title('Data requirement')
    with st.expander('Data format'):
        st.markdown('-utf-8')
        st.markdown('-seprated by coma')
        st.markdown(' -delimited by "."')
        st.markdown('-first row -header')
    st.divider()
    st.caption("<p style= 'text-align: center'>Developed by Virendra S</p>", unsafe_allow_html=True)

# if st.button("Let's get started"):
#     uploaded_data=st.file_uploader('choose a File',type='csv')

if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False}

def clicked(button):
    st.session_state.clicked[button] = True

st.button("Let's get started", on_click = clicked, args = [1])

if st.session_state.clicked[1]:
    uploaded_file = st.file_uploader("Choose a file", type='csv')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.header('Uploaded data sample')
        st.write(df.head())
        n_column=df.shape[1]
        stats=[]
        for i in range(n_column):
            first_column = df.iloc[:, i]
            mean_value = first_column.mean()
            median_value = first_column.median()
            mode_value = first_column.mode()[0]
            variance_value=first_column.var()
            std_deviation_value=first_column.std()
            column_name=df.columns[i]
            stats.append({
                'Column': column_name,
                'Mean': mean_value,
                'Median': median_value,
                'Mode': mode_value,
                'Variance':variance_value,
                'Standard Deviation':std_deviation_value

            })
        stats_df=pd.DataFrame(stats)
        stats_df.index = stats_df.index + 1
        st.header("Statistics")
        st.dataframe(stats_df, width=800)

        st.header('Line Plots')

        # Alternative approach with Plotly for more control over legends
        import plotly.graph_objects as go
        
        fig = go.Figure()
        for column in df.columns:
            fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))
        
        fig.update_layout(title='Line Plots of All Features',
                          xaxis_title='Index',
                          yaxis_title='Values',
                          legend_title='Columns')
        
        st.plotly_chart(fig, use_container_width=True)

            # st.write(f'Mean value of {df.columns[i]}: {mean_value}')
            # st.write(f'Median value of {df.columns[i]}: {median_value}')
            # st.write(f'Mode value of {df.columns[i]}: {mode_value}')