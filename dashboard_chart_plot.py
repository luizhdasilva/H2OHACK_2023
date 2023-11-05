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
                            lineWidth={st.session_state['line_width']},
                            pointSize = {0},
                            colors = {st.session_state['data_color']},
                            pointColor = {st.session_state['data_color']},
                            pointBorderWidth = {0},
                            pointBorderColor = {st.session_state['data_color']},
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
                                "background": st.session_state['bkg_color'],
                                "textColor": st.session_state['text_color'],
                                "tooltip": {
                                    "container": {
                                        "background": "#FFFFFF",
                                        "color": "#31333F",
                                    }
                                },
                                'axis':{
                                    "legend":{
                                        "text":{
                                            "fontSize": st.session_state['font_size']+2,
                                            "outlineWidth": 0,
                                            "outlineColor": "transparent"
                                            }
                                        },
                                    "ticks": {
                                        "text": {
                                            "fontSize": st.session_state['font_size'],
                                            "outlineWidth": 0,
                                            "outlineColor": "transparent"
                                        }
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
                            padding={1-st.session_state['bar_width']},
                            valueScale={ "type": 'linear' },
                            indexScale={ "type": 'band'},
                            colors=st.session_state['data_color'],
                            axisBottom = {
                                'orient': 'bottom',
                                'tickSize': st.session_state['font_size'],
                                'tickPadding': 5,
                                'tickRotation': 45,
                                'legend': st.session_state['x_label'],
                                'legendOffset': 80,
                                'legendPosition': 'middle'
                            },
                            axisLeft = {
                                'orient': 'left',
                                'tickSize': st.session_state['font_size'],
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
                                "background": st.session_state['bkg_color'],
                                "textColor": st.session_state['text_color'],
                                "tooltip": {
                                    "container": {
                                        "background": "#FFFFFF",
                                        "color": "#31333F",
                                    }
                                },
                                'axis':{
                                    'legend':{
                                        'text':{
                                            'fontSize': st.session_state['font_size']+2
                                            }
                                        },
                                    "ticks": {
                                        "text": {
                                            "fontSize": st.session_state['font_size'],
                                            "outlineWidth": 0,
                                            "outlineColor": "transparent"
                                        }
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
                            colors = {st.session_state['data_color']},
                            pointSize = {st.session_state['marker_size']},
                            pointColor = {st.session_state['data_color']},
                            pointBorderWidth = {2},
                            pointBorderColor = {st.session_state['data_color']},
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
                                "background": st.session_state['bkg_color'],
                                "textColor": st.session_state['text_color'],
                                "tooltip": {
                                    "container": {
                                        "background": "#FFFFFF",
                                        "color": "#31333F",
                                    }
                                },
                                'axis':{
                                    'legend':{
                                        'text':{
                                            'fontSize': st.session_state['font_size']+2
                                            }
                                        },
                                    "ticks": {
                                        "text": {
                                            "fontSize": st.session_state['font_size'],
                                            "outlineWidth": 0,
                                            "outlineColor": "transparent"
                                        }
                                    }
                                }
                            }
                        )