import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Worldstar Sales Report')

# Provided data
data = {
    'date': ['19/05/2020', '03/08/2020', '15/10/2020', '16/10/2020', '20/10/2020', '27/11/2020', '30/11/2020', '04/01/2020', '08/02/2021', '21/03/2021', '04/04/2021', '04/05/2021', '12/09/2021', '23/09/2021', '27/09/2021', '27/09/2021', '15/10/2021', '25/10/2021', '28/10/2021', '15/11/2021', '18/11/2021', '28/11/2021', '29/11/2021', '21/11/2021', '01/12/2021', '10/01/2022', '25/01/2022', '03/02/2022', '27/04/2022', '21/06/2022', '24/06/2022', '22/09/2022', '30/01/2023', '07/03/2023', '11/07/2023', '08/01/2023', '18/08/2023', '28/08/2023', '03/10/2023', '25/10/2023'],
    'sales': [283500, 10640000, 259600, 532000, 154530, 384000, 119800, 13300, 128000, 128000, 135000, 39500, 39500, 39500, 580000, 39500, 145000, 35500, 234000, 38500, 48100, 39500, 2303750, 414600, 39500, 562400, 133000, 469950, 150000, 270800, 84360, 1302985, 13400, 130500, 36000, 35000, 45600, 36300, 322440, 148888]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Create a table according to year
yearly_table = df.groupby(df['date'].dt.year)['sales'].sum().reset_index()
print("Yearly Table:")
print(yearly_table)

# Create a table according to month
monthly_table = df.groupby(df['date'].dt.to_period('M'))['sales'].sum().reset_index()
print("\nMonthly Table:")
print(monthly_table)

# ## Year selection
# year_list = df.year.unique()
# year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
# year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
# reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
# reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# Display DataFrame
df.date = df.date.astype('string')
st.dataframe(df)
# df_editor = st.data_editor(df, height=212, use_container_width=True,
#                             column_config={"date": st.column_config.TextColumn("Date")},
#                             column_config={"sales": st.column_config.TextColumn("Sales")},
#                             num_rows="dynamic")

# Convert 'Month' column to datetime
monthly_table.date = monthly_table.date.astype('string')
yearly_table.date = yearly_table.date.astype('string')

st.subheader('Sales by Year')
# Create chart
year_chart = alt.Chart(yearly_table).mark_bar().encode(
    x=alt.X('date', title='Year'),
    y=alt.Y('sales', title='Sales'),
    tooltip=['date', 'sales']
).properties(
    width=700,
    height=400
)

# Display chart
st.altair_chart(year_chart, use_container_width=True)

st.subheader('Sales by Month')

# # Create chart
# month_chart = alt.Chart(df).mark_line().encode(
#     x=alt.X('date:T', title='Month'),
#     y=alt.Y('sales:Q', title='Sales ($)'),
#     tooltip=['date:T', 'sales:Q']
# ).properties(
#     width=700,
#     height=400
# ).interactive()

# # Display chart
# st.altair_chart(month_chart, use_container_width=True)

# Display chart
chart = alt.Chart(monthly_table).mark_line().encode(
            x=alt.X('date:N', title='Date'),
            y=alt.Y('sales:Q', title='Sales')
            ).properties(height=320)
st.altair_chart(chart, use_container_width=True)
