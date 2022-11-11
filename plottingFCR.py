def create_plot_dictionary(gearCount):

    graph = {}

    for gear in range(1, gearCount):
        graph[gear] = {}

        for speed in range(0,160):
            graph[gear][speed] = None
    
    return graph


def update_plot(plot, currentGear, currentSpeed, currentFCR):
    plot[currentGear][currentSpeed] = currentFCR
    return plot