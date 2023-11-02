import streamlit as st
from streamlit_elements import dashboard, elements, mui, nivo, html


def add_dashboard_line(data_x,data_y):
    
    layout = [
        dashboard.Item("chart_1", 0, 0, 5, 3),
    ]
    
    # Transform the arrays into nivo structure
    data1 = [{"x": i, "y": j} for i, j in zip(data_x, data_y)]

    # Create the final dictionary with the transformed data
    data_dic = [{"id":st.session_state['characteristic'],"data": data1}]

    layout = [
    dashboard.Item("chart_1", 0, 0, 5, 3),
    ]


    with elements("dashboard"):
        with mui.Paper:
            with mui.Typography:
                html.h1("Streamlit-elements",
                    css={
                        "backgroundColor": "#000000",
                        "color":"white",
                        "borderRadius": "5px",
                        "zIndex": 'tooltip',
                        "height": "45px",
                        "&:hover": {
                            "color": "gray"
                        }
                    })

        with dashboard.Grid(layout, draggableHandle=".draggable"):
            with mui.Card(key="chart_1", 
                          sx={"color": 'white', 'bgcolor': 'text.disable', 
                              "display": "flex", 'borderRadius': 2,  
                              "flexDirection": "column"}):
                    mui.CardHeader(title=st.session_state['site'], className="draggable")
                    with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                        nivo.Line(
                            data=data_dic,
                            margin={'top': 50, 'right': 110, 'bottom': 100, 'left': 60},
                            yScale = {
                                'type': 'linear',
                                'min': 'auto',
                                'max': 'auto'
                            },

                            yFormat = " >-.2f",
                            axisBottom = {
                                'tickValues': 5,
                                'orient': 'bottom',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 90,
                                'legend': st.session_state['x'],
                                'legendOffset': 36,
                                'legendPosition': 'middle'
                            },
                            axisLeft = {
                                'orient': 'left',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 0,
                                'legend': st.session_state['y'],
                                'legendOffset': -40,
                                'legendPosition': 'middle'
                            },
                            pointSize = {10},
                            pointColor = {'theme': 'background'},
                            pointBorderWidth = {2},
                            pointBorderColor = {
                            'from': 'serieColor'},
                            pointLabelYOffset = {-12},
                            useMesh = {'true'},
                            legends = [
                                {
                                    'anchor': 'bottom-right',
                                    'direction': 'column',
                                    'justify': 'false',
                                    'translateX': 100,
                                    'translateY': 0,
                                    'itemsSpacing': 0,
                                    'itemDirection': 'left-to-right',
                                    'itemWidth': 80,
                                    'itemHeight': 20,
                                    'itemOpacity': 0.75,
                                    'symbolSize': 12,
                                    'symbolShape': 'circle',
                                    'symbolBorderColor': 'rgba(0, 0, 0, .5)',
                                    'effects': [
                                        {
                                            'on': 'hover',
                                            'style': {
                                                'itemBackground': 'rgba(0, 0, 0, .03)',
                                                'itemOpacity': 1
                                            }
                                        }
                                    ]
                                }
                            ],
                            theme={
                                "background": "#000000",
                                "textColor": "white",
                                "tooltip": {
                                    "container": {
                                        "background": "#FFFFFF",
                                        "color": "#31333F",
                                    }
                                }
                            }
                        )

def add_dashboard_bar(data_x,data_y):
    
    layout = [
        dashboard.Item("chart_1", 0, 0, 5, 3),
    ]
    
    # Transform the arrays into nivo structure
    data1 = [{"x": i, "y": j} for i, j in zip(data_x, data_y)]

    # Create the final dictionary with the transformed data
    data_dic = data1

    layout = [
    dashboard.Item("chart_1", 0, 0, 5, 3),
    ]


    with elements("dashboard"):
        with mui.Paper:
            with mui.Typography:
                html.h1("Charts",
                    css={
                        "backgroundColor": "#808080",
                        "color":"white",
                        "borderRadius": "5px",
                        "zIndex": 'tooltip',
                        "height": "45px",
                        "&:hover": {
                            "color": "gray"
                        }
                    })

        with dashboard.Grid(layout, draggableHandle=".draggable"):
            with mui.Card(key="chart_1", 
                          sx={"color": 'white', 'bgcolor': 'text.disable', 
                              "display": "flex", 'borderRadius': 2,  
                              "flexDirection": "column"}):
                    mui.CardHeader(title=st.session_state['site'], className="draggable")
                    with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                        nivo.Bar(
                            data=data_dic,
                            margin={'top': 50, 'right': 110, 'bottom': 100, 'left': 60},
                            keys=["y"],
                            indexBy="x",
                            padding={0.6},
                            valueScale={ "type": 'linear' },
                            colors="#2a7ef0",
                            axisBottom = {
                                'orient': 'bottom',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 90,
                                'legend': st.session_state['x'],
                                'legendOffset': 36,
                                'legendPosition': 'middle'
                            },
                            axisLeft = {
                                'orient': 'left',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 0,
                                'legend': st.session_state['y'],
                                'legendOffset': -40,
                                'legendPosition': 'middle'
                            },
                            theme={
                                "background": "#808080",
                                "textColor": "white",
                                "tooltip": {
                                    "container": {
                                        "background": "#000000",
                                        "color": "#808080",
                                    }
                                }
                            }
                        )
