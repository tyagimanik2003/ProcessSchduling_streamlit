import streamlit as st
import matplotlib.pyplot as plt

# Function to create the Gantt chart
def create_gantt_chart(processes):
    sorted_processes = sorted(processes, key=lambda x: (x[1], x[2]))

    fig, ax = plt.subplots()
    ax.set_ylim(0, len(sorted_processes))
    start_times = [0] * len(sorted_processes)
    end_times = [0] * len(sorted_processes)

    current_time = 0
    for i, (process, arrival_time, burst_time) in enumerate(sorted_processes):
        if arrival_time > current_time:
            current_time = arrival_time
        start_times[i] = current_time
        end_times[i] = current_time + burst_time
        current_time += burst_time

    total_timeline = max(end_times)
    ax.set_xlim(0, total_timeline)
    ax.set_yticks(range(len(sorted_processes)))
    ax.set_yticklabels(process for process, _, _ in sorted_processes)

    for i, (process, _, burst) in enumerate(sorted_processes):
        ax.barh(i, end_times[i] - start_times[i], left=start_times[i], height=0.5, align='center', alpha=0.8)
        ax.text(start_times[i] + (end_times[i] - start_times[i]) / 2, i, str(end_times[i] - start_times[i]), ha='center', va='center')

    ax.set_title("FCFS Gantt Chart")
    ax.set_xlabel("Time")

    return fig

# Streamlit app
def main():
    st.title("FCFS Scheduling Gantt Chart")

    # Input form
    st.header("Input Process Details")
    num_processes = st.number_input("Number of Processes", min_value=1, step=1, value=3)

    # Process details input
    processes = []
    for i in range(num_processes):
        process_name = st.text_input(f"Process {i+1} Name", f"P{i+1}")
        arrival_time = st.number_input(f"Process {i+1} Arrival Time", min_value=0, step=1, value=0)
        burst_time = st.number_input(f"Process {i+1} Burst Time", min_value=1, step=1, value=1)
        processes.append((process_name, arrival_time, burst_time))

    # Generate Gantt chart button
    if st.button("Generate Gantt Chart"):
        fig = create_gantt_chart(processes)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
