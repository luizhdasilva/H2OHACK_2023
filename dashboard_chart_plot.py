import streamlit as st
from streamlit_elements import dashboard, elements, mui, nivo, html


# LINE CHART
def add_dashboard_line(data_x,data_y):
    
    # Transform the arrays into nivo structure
    data1 = [{"x": i, "y": j} for i, j in zip(data_x, data_y)]

    # Create the final dictionary with the transformed data
    data_dic = [{"id":st.session_state['site'],"data": data1}]

    layout = [
    dashboard.Item("chart_1", 0, 0, 5, 3),
    ]


    with elements("dashboard"):
        with mui.Paper:
            with mui.Typography:
                html.h1("Line Chart",
                    css={
                        "backgroundColor": "#808080",
                        "color":"white",
                        "borderRadius": "5px",
                        "zIndex": 'tooltip',
                        "height": "45px",
                        "&:hover": {
                            "color": "white"
                        }
                    })

        with dashboard.Grid(layout, draggableHandle=".draggable"):
            with mui.Card(key="chart_1", 
                          sx={"color": 'white', 'bgcolor': 'text.disable', 
                              "display": "flex", 'borderRadius': 2,  
                              "flexDirection": "column"}):
                    mui.CardHeader(title=st.session_state['title'], className="draggable")
                    with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                        nivo.Line(
                            data=data_dic,
                            margin={'top': 50, 'right': 90, 'bottom': 100, 'left': 60},
                            xFormat="time:%Y-%m-%d",
                            yScale = {
                                'type': 'linear',
                                'min': 'auto',
                                'max': 'auto'
                            },

                            yFormat = " >-.2f",
                            axisBottom = {
                                'tickValues': 10,
                                'orient': 'bottom',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 45,
                                'legend': st.session_state['x_label'],
                                'legendOffset': 80,
                                'legendPosition': 'middle'
                            },
                            axisLeft = {
                                'orient': 'left',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 0,
                                'legend': st.session_state['y_label'],
                                'legendOffset': -50,
                                'legendPosition': 'middle'
                            },
                            pointSize = {0},
                            colors = {'#FF0000'},
                            pointColor = {'#FF0000'},
                            pointBorderWidth = {0},
                            pointBorderColor = {'#FF0000'},
                            pointLabelYOffset = {-12},
                            useMesh = {'true'},
                            legends = [
                                {
                                    'anchor': 'bottom-right',
                                    'direction': 'column',
                                    'justify': 'false',
                                    'translateX': 50,
                                    'translateY': 0,
                                    'itemsSpacing': 0,
                                    'itemDirection': 'left-to-right',
                                    'itemWidth': 40,
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

# BAR CHART
def add_dashboard_bar(data_x,data_y):
    
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
                html.h1("Bar Chart",
                    css={
                        "backgroundColor": "#808080",
                        "color":"white",
                        "borderRadius": "5px",
                        "zIndex": 'tooltip',
                        "height": "45px",
                        "&:hover": {
                            "color": "white"
                        }
                    })

        with dashboard.Grid(layout, draggableHandle=".draggable"):
            with mui.Card(key="chart_1", 
                          sx={"color": 'white', 'bgcolor': 'text.disable', 
                              "display": "flex", 'borderRadius': 2,  
                              "flexDirection": "column"}):
                    mui.CardHeader(title=st.session_state['title'], className="draggable")
                    with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                        nivo.Bar(
                            data=data_dic,
                            margin={'top': 50, 'right': 90, 'bottom': 100, 'left': 60},
                            keys=["y"],
                            indexBy="x",
                            padding={0.6},
                            valueScale={ "type": 'linear' },
                            indexScale={ "type": 'band'},
                            colors={'#FF0000'},
                            axisBottom = {
                                'orient': 'bottom',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 45,
                                'legend': st.session_state['x_label'],
                                'legendOffset': 80,
                                'legendPosition': 'middle'
                            },
                            axisLeft = {
                                'orient': 'left',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 0,
                                'legend': st.session_state['y_label'],
                                'legendOffset': -45,
                                'legendPosition': 'middle'
                            },
                            labelTextColor={
                            "from": 'color',
                            "modifiers": [
                                [
                                    'opacity',
                                    0
                                ]
                            ]
                        },
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

# SCATTER CHART
def add_dashboard_scatter(data_x,data_y):
    
    # Transform the arrays into nivo structure
    data1 = [{"x": i, "y": j} for i, j in zip(data_x, data_y)]

    # Create the final dictionary with the transformed data
    data_dic = [{"id":st.session_state['site'],"data": data1}]

    layout = [
    dashboard.Item("chart_1", 0, 0, 5, 3),
    ]

    with elements("dashboard"):
        with mui.Paper:
            with mui.Typography:
                html.h1("Scatter Chart",
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
                    mui.CardHeader(title=st.session_state['title'], className="draggable")
                    with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                        nivo.Line(
                            data=data_dic,
                            margin={'top': 50, 'right': 90, 'bottom': 100, 'left': 60},
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
                                'tickRotation': 45,
                                'legend': st.session_state['x_label'],
                                'legendOffset': 80,
                                'legendPosition': 'middle'
                            },
                            axisLeft = {
                                'orient': 'left',
                                'tickSize': 5,
                                'tickPadding': 5,
                                'tickRotation': 0,
                                'legend': st.session_state['y_label'],
                                'legendOffset': -50,
                                'legendPosition': 'middle'
                            },
                            lineWidth={0},
                            pointSize = {10},
                            pointColor = {'#FF0000'},
                            pointBorderWidth = {2},
                            pointBorderColor = {'#FF0000'},
                            pointLabelYOffset = {-12},
                            useMesh = {'true'},
                            legends = [
                                {
                                    'anchor': 'bottom-right',
                                    'direction': 'column',
                                    'justify': 'false',
                                    'translateX': 50,
                                    'translateY': 0,
                                    'itemsSpacing': 0,
                                    'itemDirection': 'left-to-right',
                                    'itemWidth': 40,
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