import pandas as pd
import plotly.express as px
import streamlit as st
import time

#setting page configurations


st.set_page_config ( page_title = "SUPERMARKET SALES",             #title of dashboard page
                     page_icon = ":chart_with_upwards_trend:",     #setting up favicon
                     layout = "wide"                               #wide becoz i want to use full screen (by default it is center)
)

#st.title("DASHBOARD")

@st.cache                                                        #streamlit cache mechanism to avoid calculating same values again and again
def get_data_from_excel():
    df = pd.read_excel(
        io = 'supermkt_sales.xlsx',       #file_name
        engine = 'openpyxl',
        sheet_name = 'Sales',             #excel sheet_name
        skiprows = 3,                     #no. of rows to skip
        usecols = 'B:R',                  #cols to use
        nrows = 1000,                     #number of rows to use
    )
    
    df["hour"] = pd.to_datetime(df["Time"], format = "%H:%M:%S").dt.hour                    #adding 'hour' column to df
    return df
df= get_data_from_excel()                                        #obtaining required data from excel file and storing it in the cache

#st.dataframe(df)  #printing dataframe on the page 

# configuring sidebar

st.sidebar.header("Filer:")

city = st.sidebar.multiselect(            #for multiple selection in a drop down
    "Select city:",                       #label
    options = df["City"].unique(),        #unique cities as option
    default = df["City"].unique()         #all unique cities picked up by default
)

prod_line = st.sidebar.multiselect(           
    "Select product line:",                       
    options = df["Product_line"].unique(),       
    default = df["Product_line"].unique()
    
)

gender = st.sidebar.multiselect(           
    "Select gender:",                       
    options = df["Gender"].unique(),       
    default = df["Gender"].unique()        
)

cust_type = st.sidebar.multiselect(           
    "Select customer type:",                       
    options = df["Customer_type"].unique(),       
    default = df["Customer_type"].unique()        
)

pay = st.sidebar.multiselect(           
    "Select payment method:",                       
    options = df["Payment"].unique(),       
    default = df["Payment"].unique()        
)

df_select = df.query(                            #querying columns of rows for checking the conditions to be satisfied and selecting those valid rows
    "City == @city  & Product_line == @prod_line & Gender == @gender & Customer_type == @cust_type & Payment == @pay"
)



#mainpage KPI

st.title(":chart_with_upwards_trend:DASHBOARD : SUPERMARKET SALES")                                              #title of page
st.text("This is a dashboard created for the purpose of analysing and visualizing sales data of a supermarket")  #inserting some text

  
st.markdown("##")        #adding new paragraph

#KPI'S

avg_rating = round(df_select["Rating"].mean(),1)              #round mean of rating to 1 decimal
star_rating = ":star:" * int(round(avg_rating, 0))            #printing stars which signify how good is rating

total_sales = int(df_select["Total"].sum())                   #returns float which is typecasted to int
total_unit = int(df_select["Quantity"].sum())
avg_sales_perunit = round(total_sales/total_unit,3)

left_col, right_col = st.columns(2)                           #creating two columns
with left_col:
    st.subheader("Total Sales Revenue:")
    st.subheader(f"US ${total_sales:,}")                      #fstring used to concatenate total sales number with US dollars and comma used as a separator
with right_col:
    st.subheader("Average Sales Revenue per unit quantity:")
    st.subheader(f"US ${avg_sales_perunit}")

st.markdown("---")                                         #paragraph end

st.markdown("##")                                          #new paragraph start


if st.button("Click this button to calculate total products bought and rating"):           #inserting a button
    with st.empty():
        for seconds in range(4):
            st.subheader(f":hourglass_flowing_sand:{3-seconds} seconds")          #setting up timer
            time.sleep(1)
        st.subheader(f"Total products bought: {total_unit} units")                #text to print after timer ends
    st.subheader("Average Rating:")
    st.subheader(f"{avg_rating} {star_rating}")
    if avg_rating>6:
        st.balloons()                                                              #adding some visuals
        st.success("Yay ! customer rating not bad")
st.markdown("---")                                            #paragraph end



st.markdown("##")                                             #paragraph start

st.header("Analysing sales revenue pattern using bar charts")

fig_prodsales = df_select.groupby(by=["Product_line"]).sum()[["Total"]].sort_values(by="Total")     #creating data for product_line vs total
#st.write(fig_prodsales)
bar_prod=px.bar( fig_prodsales, x="Total", y= fig_prodsales.index, orientation="h",                 #horizontal bar plot for product_line vs total
        title="<b> Sales revenue by Product line</b>",
            hover_data=["Total", fig_prodsales.index], color="Total", height=400,
            width=1000,
            color_discrete_sequence=["#0083B8"]*len(fig_prodsales),                             
           # template = "plotly_white"
        )
#st.plotly_chart(bar_prod)

fig_hrsales = df_select.groupby(by=["hour"]).sum()[["Total"]]                                       #creating data for hour vs total
#st.write(fig_hrsales)
bar_hr=px.bar( fig_hrsales, x="Total", y= fig_hrsales.index, orientation="h",                       #horizontal bar plot for hour vs total
        title="<b> Sales revenue by hour</b>",
            hover_data=["Total", fig_hrsales.index], color="Total", height=400,
            width=1000,
            color_discrete_sequence=["#0083B8"]*len(fig_hrsales),
           # template = "plotly_white"
        )
#st.plotly_chart(bar_hr)

left_col, right_col = st.columns(2)                                                        #creating 2 columns
with left_col:
    st.subheader ("Product line vs sales revenue data:")
    st.write(fig_prodsales)                                                                 #printing product_line vs total data
    st.text(' ') 
    st.text(' ')
    st.text(' ')
    st.text(' ')
    st.text(' ')
    st.text(' ')
    st.plotly_chart(bar_prod,use_container_width = True)                                    #printing product_line vs total bar plot
with right_col:
    st.subheader ("hour vs sales revenue data:")
    st.write(fig_hrsales)                                                                   #printing hour vs total data
    st.plotly_chart(bar_hr,use_container_width = True)                                      #printing hour vs total bar plot

fig_citysales = df_select.groupby(by=["City"]).sum()[["Total"]].sort_values(by="Total")           #city vs total data

bar_city=px.bar( fig_citysales, x="Total", y= fig_citysales.index, orientation="h",               #horizontal bar plot for city vs total
        title="<b> Sales revenue by city</b>",
            hover_data=["Total", fig_citysales.index], color="Total", height=400,
            width=1000,
            color_discrete_sequence=["#0083B8"]*len(fig_citysales),
           # template = "plotly_white"
        )

fig_gendersales = df_select.groupby(by=["Gender"]).sum()[["Total"]].sort_values(by="Total")       #gender vs total data

bar_gender=px.bar( fig_gendersales, x="Total", y= fig_gendersales.index, orientation="h",         #horizontal bar plot for gender vs total
        title="<b> Sales revenue by gender</b>",
            hover_data=["Total", fig_gendersales.index], color="Total", height=400,
            width=1000,
            color_discrete_sequence=["#0083B8"]*len(fig_gendersales),
           # template = "plotly_white"
        )

with left_col:
    st.subheader ("City vs sales revenue data:")
    st.write(fig_citysales)                                                                    #printing city vs total data
    st.plotly_chart(bar_city,use_container_width = True)                                       #printing city vs total bar plot
with right_col:
    st.subheader ("Gender vs sales revenue data:")
    st.text(' ')
    st.write(fig_gendersales)                                                                  #printing gender vs total data
    st.plotly_chart(bar_gender,use_container_width = True)                                     #printing gender vs total bar plot

fig_custsales = df_select.groupby(by=["Customer_type"]).sum()[["Total"]].sort_values(by="Total")    #customer type vs total data

bar_cust=px.bar( fig_custsales, x="Total", y= fig_custsales.index, orientation="h",                #horizontal bar plot for customer type vs total data
        title="<b> Sales revenue by customer type</b>",
            hover_data=["Total", fig_custsales.index], color="Total", height=400,
            width=1000,
            color_discrete_sequence=["#0083B8"]*len(fig_custsales),
           # template = "plotly_white"
        )

fig_paysales = df_select.groupby(by=["Payment"]).sum()[["Total"]].sort_values(by="Total")       #payment mode vs total data

bar_pay=px.bar( fig_paysales, x="Total", y= fig_paysales.index, orientation="h",                #horizontal bar plot for payment mode vs total data
        title="<b> Sales revenue by mode of payment</b>",
            hover_data=["Total", fig_paysales.index], color="Total", height=400,
            width=1000,
            color_discrete_sequence=["#0083B8"]*len(fig_paysales),
           # template = "plotly_white"
        )

with left_col:
    st.subheader ("Customer type vs sales revenue data:")
    st.write(fig_custsales)                                                                    #printing customer type vs total data
    st.plotly_chart(bar_cust,use_container_width = True)                                       #printing customer type vs total bar plot
with right_col:
    st.subheader ("Payement mode vs sales rervenue data:")
    st.write(' ')
    st.write(fig_paysales)                                                                     #printing payment mode vs total data
    st.plotly_chart(bar_pay,use_container_width = True)                                        #printing payment mode vs total bar plot

    
st.markdown("##")                                                                                #paragraph end

st.header("Analysing sales pattern (quantity of units purchased):")

#unit quantity purchased by cities, product_line, gender, payment mode, customer type, hour

fig_prodq = df_select.groupby(by=["Product_line"]).sum()[["Quantity"]]                          #product_line vs quantity data
pie_prod = px.pie(fig_prodq, values = "Quantity", names = fig_prodq.index,title="<b> Sales quantity by prodct line</b>")    #pie chart for product_line vs quantity
#st.plotly_chart(pie_prod)

fig_cityq = df_select.groupby(by=["City"]).sum()[["Quantity"]]                                   #city vs quantity data
pie_city = px.pie(fig_cityq, values = "Quantity", names = fig_cityq.index,title="<b> Sales quantity by city</b>")           #pie chart for city vs quantity
#st.plotly_chart(pie_city)

left_col, right_col = st.columns(2)                                                           #creating 2 columns
with left_col:
    st.subheader ("Product line vs sales data:")
    st.write(fig_prodq)                                                                     #printing product_line vs quantity data
    st.plotly_chart(pie_prod,use_container_width = True)                                    #printing product_line vs quantity pie chart
with right_col:
    st.subheader ("city vs sales data:")
    st.write(fig_cityq)                                                                     #printing city vs quantity data
    st.write(' ')
    st.write(' ')                                                                           #printing some empty lines just for formatting and aligning things
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.plotly_chart(pie_city,use_container_width = True)                                    #printing city vs quantity pie chart

st.subheader("hour vs sales data:")
fig_hrq = df_select.groupby(by=["hour"]).sum()[["Quantity"]]                                #hour vs quantity data

heatmap_hr = px.density_heatmap(fig_hrq, x = "Quantity", y = fig_hrq.index,nbinsx=10, nbinsy=5, color_continuous_scale="Viridis",title="<b> Sales quantity by hour</b>")
                                                                                           #heatmap for hour vs quantity
left_col, right_col = st.columns(2)
with left_col:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(fig_hrq)                                                                        #printing hour vs quantity data
with right_col:
    st.plotly_chart(heatmap_hr,use_container_width = True)                                   #printing hour vs quantity heatmap



hist_pay = px.histogram(df_select, x = "Payment" ,title="<b> Customer vs payment mode</b>")               #histogram for payment vs quantity
hist_gender = px.histogram(df_select, x = "Gender" ,title="<b> Customer vs gender</b>")                   #histogram for gender vs quantity
left_col, right_col = st.columns(2)                                                                       #2 columns
with left_col:
    st.subheader("Mode of payment vs sales data:")
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.plotly_chart(hist_pay,use_container_width = True)                                                   #printing histgram for payment vs quantity
with right_col:
    st.subheader("Gender vs sales data:")
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.plotly_chart(hist_gender,use_container_width = True)                                                 #printing histogram for gender vs quantity

