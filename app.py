
from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

server = app.server


app.layout = html.Div(
    children =[
        html.H1(children ="Betsy's Data Drag Race"),
        html.P(
            children= (
                "As a new fan to the show RuPaul's Drag Race, I recently learned about the massive community supporting the show."

                "There is so much data online for every episode of the show! As a computer science major and data science minor,"
                "I was so intrested in what I could do with this data. This Dash app shows my progress as I practice my Dash, pandas, and plotly skills in an attemp to slay the house down with some cool graphs!"
            ),
        ),
        '''
        dcc.Graph(figure=age_plot),
        dcc.Graph(figure=hometown),
        dcc.Graph(figure=lipsync),
        dcc.Graph(figure= outcomes)
        '''

    ]
)


if __name__ == '__main__':
    app.run(debug=True)
