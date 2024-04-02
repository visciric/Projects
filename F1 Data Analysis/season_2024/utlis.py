import os
import fastf1 as ff1
import plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt

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


def plot_race_results(session,session_name, figsize=(12, 5), dpi=300):
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    # Plot driver positions
    for drv in session.drivers:
        drv_laps = session.laps.pick_driver(drv)
        abb = drv_laps['Driver'].iloc[0]
        color = ff1.plotting.driver_color(abb)

        ax.plot(drv_laps['LapNumber'], drv_laps['Position'],
                label=abb, color=color)
    
    # Add starting positions on the left side of the plot
    for drv in session.drivers:
        drv_laps = session.laps.pick_driver(drv)
        abb = drv_laps['Driver'].iloc[0]
        starting_position = int(drv_laps['Position'].iloc[0])
        ax.text(0.8, drv_laps['Position'].iloc[0], f"P{starting_position}: {abb} ", color='w', ha='right')
    
    # Add final positions and places gained on the right side of the plot
    for drv in session.drivers:
        drv_laps = session.laps.pick_driver(drv)
        abb = drv_laps['Driver'].iloc[0]
        final_position = drv_laps['Position'].iloc[-1]
        starting_position = int(drv_laps['Position'].iloc[0])
        places_gained = int(starting_position - final_position)
        places_text =  f"({'+' if places_gained > 0 else '' if places_gained == 0 else '-'}{abs(places_gained)})"
        ax.text(57, final_position, f"P{starting_position}:{abb} {places_text}", color='w', ha='left') 

    # Add annotation for track position on the left side
    ax.annotate('Track Position', xy=(-0.11, 0.4), xycoords='axes fraction', fontsize=14, color='w', rotation=90)

    ax.set_ylim([20.5, 0.5])
    ax.set_yticks([])
    ax.set_xlabel('Lap Number', fontsize=14)
    ax.set_xlim([1, 57])
    plt.title(f'2024 {session_name} Grand Prix', font='Arial', fontweight='bold', fontsize=24)
    plt.tight_layout()
    plt.show()

# # Example usage
# plot_race_results(session, 'Bahrain')



import pandas as pd

def calculate_lap_metrics(laps_df):
    """
    Sorts drivers by position for each lap, calculates the delta times to the driver in front and behind,
    and calculates the gap to the leader.

    Parameters:
    - laps_df: DataFrame containing lap data. Must include 'LapNumber', 'Driver', 'LapTime', and 'Position'.

    Returns:
    - DataFrame with additional 'DeltaTimeToFront', 'DeltaTimeToBehind', and 'GapToLeader' columns representing
      the time differences and gap to the leader for each lap.
    """
    # Ensure laps are sorted by LapNumber and Position for consistent calculations
    laps_df = laps_df.sort_values(by=['LapNumber', 'Position'])

    # Initialize columns for the delta times and cumulative time
    laps_df['DeltaTimeToFront'] = pd.NA
    laps_df['DeltaTimeToBehind'] = pd.NA
    laps_df['CumulativeTime'] = laps_df.groupby('Driver')['LapTime'].cumsum()
    laps_df['GapToLeader'] = pd.NA

    # Iterate over each lap in the race
    for lap in laps_df['LapNumber'].unique():
        lap_data = laps_df[laps_df['LapNumber'] == lap]

        # Leader's cumulative time for the gap calculation
        leader_time = lap_data.iloc[0]['CumulativeTime']

        # Calculate the delta times and gap to the leader
        for i in range(len(lap_data)):
            if i > 0:  # Skip the first row (leader) for delta time calculations
                current_driver_time = lap_data.iloc[i]['LapTime'].total_seconds()
                front_driver_time = lap_data.iloc[i - 1]['LapTime'].total_seconds()
                delta_time_to_front = current_driver_time - front_driver_time
                laps_df.loc[lap_data.iloc[i].name, 'DeltaTimeToFront'] = delta_time_to_front

                # Calculate and assign the delta time to the driver behind if not the last driver
                if i < len(lap_data) - 1:
                    behind_driver_time = lap_data.iloc[i + 1]['LapTime'].total_seconds()
                    delta_time_to_behind = behind_driver_time - current_driver_time
                    laps_df.loc[lap_data.iloc[i].name, 'DeltaTimeToBehind'] = delta_time_to_behind

            # Gap to the leader calculation for all drivers
            laps_df.loc[lap_data.iloc[i].name, 'GapToLeader'] = lap_data.iloc[i]['CumulativeTime'] - leader_time

    # Replace pd.NA with appropriate representations
    laps_df['GapToLeader'].fillna(pd.Timedelta(seconds=0), inplace=True)

    return laps_df
