import os
import fastf1 as ff1
import plotly
import plotly.graph_objs as go

def setup_cache(path):
    if not os.path.exists(path):
        os.makedirs(path)

    ff1.Cache.enable_cache(path)


# Interactive plots 
def plot_data_interactive(df_list, x_col, y_col, labels):
    fig = go.Figure()

    for i, df in enumerate(df_list):
        fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col], mode='lines', name=labels[i],
                                 line=dict(color='blue' if i == 0 else 'red')))
    
    fig.update_layout(
        xaxis=dict(title=x_col),
        yaxis=dict(title=y_col),
        title=f'Comparison of {y_col} between drivers',
        legend=dict(title='Driver'),
        hovermode='x unified',
        showlegend=True,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
    )

    fig.show()

# example call 
"""
Before you call the function ensure to add distance and seconds 

fastest_yuki = yuki.pick_fastest().get_car_data().add_distance()
fastest_mag = mag.pick_fastest().get_car_data().add_distance()

fastest_mag['sec'] = fastest_mag['Time'].dt.total_seconds()
fastest_yuki['sec'] = fastest_yuki['Time'].dt.total_seconds()
fastest_yuki


plot_data_interactive([fastest_yuki, fastest_mag], 'Distance', 'RPM', ['Tsunoda', 'Magnussen'])


"""

def plot_data_interactive1(df_list, x_col, y_col, labels, circuit_info=None):
    fig = go.Figure()

    for i, df in enumerate(df_list):
        fig.add_trace(go.Scatter(x=df[x_col], y=df[y_col], mode='lines', name=labels[i],
                                  line=dict(color='blue' if i == 0 else 'red')))
        
    if circuit_info is not None:
        v_min = min(df[y_col].min() for df in df_list)
        v_max = max(df[y_col].max() for df in df_list)

        for _, corner in circuit_info.corners.iterrows():
            txt = f"{corner['Number']}{corner['Letter']}"
            fig.add_annotation(x=corner['Distance'], y=max(v_min-150, 0), text=txt,
                              showarrow=False, font=dict(size=10))

    fig.update_layout(
        xaxis=dict(title=x_col),
        yaxis=dict(title=y_col),
        title=f'Comparison of {y_col} between {labels[0] } and {labels[1]}',
        legend=dict(title='Driver'),
        hovermode='x unified',
        showlegend=True,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
    )

    fig.show()

