import flask
from flask import Flask, render_template, request, redirect, session
import pymysql
import pandas as pd 
import plotly
import plotly.express as px
import json
import plotly
import plotly.graph_objs as go
import json
#from dotenv import load_dotenv
import os

# Load environment variables from the .env file
#load_dotenv()

app = Flask(__name__)



df = pd.DataFrame({'COLUMN COURSES': ["PROGRAMMING IN PYTHON ", "APPLIED MACHINE LEARNING FROM BEGINNER TO PROFESSIONALS", "apache", "DATA SCIENCE PROFESSIONALS", 4,5,6,7,8,9,10],
                   'COURSE VIEWED': [5, 6, 7, 8, 9,10,11,12,13,14,15],
                   
                    'Assignment CHECK': [5, 6, 7, 8, 9,15,16,17,18,19,20],
                    'Assignment total': [5, 6, 7, 8, 9,15,16,17,18,19,20],
                    'Assignment New': [5, 6, 7, 8, 9,15,16,17,18,19,20],



                   'COURSE COMPLETED': ['a', 'b', 'c', 'd', 'e', "f", "g" , "h" , "i" , "j" , "k"]})


@app.route('/')
def homepage():
    # s = "<H2> Welcome to Mentorship App </H2>"
    user_email = "student@yahoo.in"  # Get email 

    ###################################################################################
    #CODE TO CREATE A LINE CHART 
    #######################################################################################

    #return render_template('form_pie_chart.html', name='form')   
    fig = go.Figure(data=[go.Line(x=["21-10-1", "21-10-4" , "21-10-6" , "21-10-10" , "21-10-13", "21-10-16"], 
    y=[10,15, 16,16,18,25])])
     
    # Create graphJSON
    #graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
     
    #  ###################Create graphJSON ##########    
    ##################################################################################

    #####################################################
    # student status bar details 
    ##########################################################

    Last_login= "23-Jan-2024"
    update_on= "1-Feb-2024"
    Bundle="Black Belt+ Program"
    Activate_date = "23-Dec-2023"
    Expiry_date = "23-Dec-2024"
    Last_men_date= "25-Jan-2024"
    topic_men = "Python"


    #######################################################




    ########################################################
    #### TABLE RENDER USING PLOTLY
    ######################################################3

    df = pd.read_csv("student_dashboard_sample.csv")
    new_col = [i for i in range(1, (df.shape[0]+1))]
    df.insert(loc=0, column='S no.', value=new_col)
    header_values = df.columns 
    cell_values = []
    for i in range(len(df.columns)): 
        cell_values.append(df.iloc[:,i].values)

    



    # Create a Plotly Figure for the table
    fig2 = go.Figure(data=[go.Table(
    
    header=dict(values=header_values, line_color='darkslategray',
    fill_color='royalblue',
    align=['left','left'],
    font=dict(color='white', size=16),
    height=40),
        
        cells=dict(values=cell_values , line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'left' , 'center'],
    font_size=12,
    height=30))
    ])

    #fig2.update_layout(
    #margin=dict(t=5, b=5,l=12, r=35)  # Left, Right, Top, Bottom margins
    #    )
        
    fig.update_layout(#title="THE STUDENT PROGRESS LINE", 
        font=dict(  # General font used for text like the title
        family="Arial, sans-serif",
        size=12,
        color="WHITE"),


    margin=dict(t=25, b=1,l=12, r=45)  # Left, Right, Top, Bottom margins
           ,plot_bgcolor='paleturquoise',  # Set the background color for the chart area
    paper_bgcolor='royalblue'  # Set the background color for the entire figure
        , width = 1430, height=410)

    # Create a Plotly Figure for the table
    fig2 = go.Figure(data=[go.Table(
        columnwidth=[10,100,50,50,50,50],
        header=dict(values=header_values, line_color='darkslategray',
    fill_color='royalblue',
    align=['left',"left",'center'],
    font=dict(color='white', size=15),
    height=40),
        
        cells=dict(values=cell_values , line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'left', 'center'],
    font_size=12,
    height=30))
    ])

    fig2.update_layout(
    margin=dict(t=5, b=5,l=12, r=35)  # Left, Right, Top, Bottom margins
        )
        
    fig.update_layout(#title="THE STUDENT PROGRESS LINE", 
        font=dict(  # General font used for text like the title
        family="Arial, sans-serif",
        size=12,
        color="WHITE"),


    margin=dict(t=25, b=1,l=12, r=45)  # Left, Right, Top, Bottom margins
           ,plot_bgcolor='paleturquoise',  # Set the background color for the chart area
    paper_bgcolor='royalblue'  # Set the background color for the entire figure
        , width = 1430, height=410)

    # Convert the figure to JSON
    graphJSON = json.dumps([fig,fig2], cls=plotly.utils.PlotlyJSONEncoder)


    ######################################################

    return render_template('index.html', user_email=user_email,tables=[df.to_html(classes='data')],
     titles=df.columns.values,graphJSON=graphJSON,
     Last_login=Last_login, update_on=update_on, Bundle=Bundle,Activate_date=Activate_date,
     Expiry_date=Expiry_date, Last_men_date=Last_men_date, topic_men=topic_men)

    #return render_template('index.html', user_email=user_email)




@app.route('/mentor')
def mentorhome():
    # s = "<H2> Welcome to Mentorship App </H2>"
    user_email = "mentor@yahoo.in"  # Get email 

    ###################################################################################
    #CODE TO CREATE A LINE CHART 
    #######################################################################################

    #return render_template('form_pie_chart.html', name='form')   
    fig = go.Figure(data=[go.Line(x=["21-10-1", "21-10-4" , "21-10-6" , "21-10-10" , "21-10-13", "21-10-16"], 
    y=[10,15, 16,16,18,25])])
     
    # Create graphJSON
    #graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
     
    #  ###################Create graphJSON ##########    
    ##################################################################################

    #####################################################
    # student status bar details 
    ##########################################################
    tmt = 20
    Last_login= "23-Jan-2024"
    update_on= "1-Feb-2024"
    ttt = 12
    tus= 9 
    Last_men_date= "25-Jan-2024"
    topic_men = "Python"


    #######################################################




    ########################################################
    #### TABLE RENDER USING PLOTLY
    ######################################################3

    header_values = ["Date", "Amount", "User" , "Course" , "activation Date" , 
    "Expiry Date", "Percentage" , "Personal Details" , "Flag"]
    cell_values = [
        ["2023-01-01", "2023-01-02", "2023-01-03" , "2023-01-01", "2023-01-02", "2023-01-03",
        "2023-01-01", "2023-01-02", "2023-01-03" , "2023-01-01", "2023-01-02", "2023-01-03","2023-01-03","2023-01-03"],  # Dates
        [100, 250, 180, 100,200,170,100,200,300,400,500,5000,500,600],  # Amounts
        ["Alice", "Bob", "Charlie", "Jax" , "Ariel", "dulo","Alice", "Bob", "Charlie", "Jax" , "Ariel", "dulo"]  # Users
        ,["A" , "B" , "C", "D" ,"E" , "F" , "G","A" , "B" , "C", "D" ,"E" , "F" , "G" ]
        ,["2023-01-01", "2023-01-02", "2023-01-03","2023-01-01", "2023-01-02", "2023-01-03","2023-01-03","2023-01-03",
        "2023-01-01", "2023-01-02", "2023-01-03" , "2023-01-01", "2023-01-02", "2023-01-03"],
        ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-01", "2023-01-02", "2023-01-03",
        "2023-01-01", "2023-01-02", "2023-01-03" , "2023-01-01", "2023-01-02", "2023-01-03","2023-01-03","2023-01-03"], 
        [100, 100,304,132,91,921,80,100,100,100, 100,304,132,91], 
        [1,2,3,4,5,6,1,2,3,4,5,6,6,6],
        [0,1,1,1,0,0,0,0,1,1,1,0,1,1]
    ]

    # Create a Plotly Figure for the table
    fig2 = go.Figure(data=[go.Table(
        header=dict(values=header_values, line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40),
        
        cells=dict(values=cell_values , line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30))
    ])

    fig2.update_layout(
    margin=dict(t=5, b=5,l=12, r=12)  # Left, Right, Top, Bottom margins
        )
        
    fig.update_layout(#title="THE STUDENT PROGRESS LINE", 
        font=dict(  # General font used for text like the title
        family="Arial, sans-serif",
        size=12,
        color="WHITE"),


    margin=dict(t=25, b=1,l=12, r=45)  # Left, Right, Top, Bottom margins
           ,plot_bgcolor='paleturquoise',  # Set the background color for the chart area
    paper_bgcolor='royalblue'  # Set the background color for the entire figure
        , width = 1430, height=410)

    # Convert the figure to JSON
    graphJSON = json.dumps([fig,fig2], cls=plotly.utils.PlotlyJSONEncoder)


    ######################################################

    return render_template('index_mentor.html', user_email=user_email,tables=[df.to_html(classes='data')],
     titles=df.columns.values,graphJSON=graphJSON, tmt = tmt, tus = tus ,
     Last_login=Last_login, update_on=update_on, ttt= ttt ,
     Last_men_date=Last_men_date, topic_men=topic_men)







# if __name__ == '__main__':
#     app.run(debug=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


