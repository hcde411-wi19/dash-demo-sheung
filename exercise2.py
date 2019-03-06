# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# Exercise 2. Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

#This visualization shows shows the percentage of adults (men and women) who say they use a specified social media platform
# from survey data conducted in the United States.
#Source: http://www.pewinternet.org/2018/03/01/social-media-use-2018-appendix-a-detailed-table/

#static datas
social_media_in_order = ['Facebook', 'Youtube', 'Pinterest', 'Instagram', 'Snapchat', 'Twitter']
men_percentages = [62, 75, 16, 30, 23, 23]
women_percentages = [74, 72, 41, 39, 31, 24]
total_percentages = [68, 73, 29, 35, 24]

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Exercise #2:Gender-use of Different Social Media Platforms'),

    # a div to put a short description
    html.Div(children='''
        This is a Dash application that shows the percentage of adults (women and men) who use specified social media platform. The data 
        if from a survey conducted in the United States (http://www.pewinternet.org/2018/03/01/social-media-use-2018-appendix-a-detailed-table/). 
    '''),
 # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                {'x': social_media_in_order , 'y': men_percentages, 'type': 'bar', 'name': 'Men'},
                {'x': social_media_in_order , 'y': women_percentages, 'type': 'bar', 'name': 'Female'},
                {'x': social_media_in_order , 'y': total_percentages, 'type': 'bar', 'name': 'Total'},
            ],
            # configure the layout of the visualization --
            'layout': {
                'title': 'Percentage use of Different Social Media Platforms By Gender'
            }
        }
    )
])
if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



