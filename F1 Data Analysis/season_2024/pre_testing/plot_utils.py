import matplotlib.pyplot as plt 


def plot_data(df_list, x_col, y_col, labels):
    fig, axs = plt.subplots(figsize=(12, 5), dpi=300)
    
    for i, df in enumerate(df_list):
        axs.plot(df[x_col], df[y_col], color='blue' if i == 0 else 'red', label=labels[i])
    
    # Assuming circuit_info is available
    v_min = min(df[y_col].min() for df in df_list)
    v_max = max(df[y_col].max() for df in df_list)
    axs.vlines(x=circuit_info.corners['Distance'], ymin=max(v_min-100, 7), ymax=v_max+10,
               linestyles='dotted', colors='grey')

    for _, corner in circuit_info.corners.iterrows():
        txt = f"{corner['Number']}{corner['Letter']}"
        axs.text(corner['Distance'], max(v_min-150, 0), txt,
                 va='center_baseline', ha='center', size='small')
    
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Comparison of {y_col} between drivers')
    axs.set_xlim(left=0)
    axs.legend()
    plt.show()
    
# how to call the function 

# import sys
# sys.path.append(r'C:\Users\ricca\OneDrive - ZHAW\Desktop\Personal_Projects\Formula1\season_2024\pre_testing')  # Add the directory containing plot_utils.py to the Python path

# from plot_utils import plot_data