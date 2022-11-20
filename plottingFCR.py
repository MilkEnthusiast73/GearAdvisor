from communicate_with_database import*

def update_plot(fileName, currentGear, currentSpeed, currentFCR):
    graph = json_to_dict(fileName)
    if str(currentGear) not in graph:
        graph[str(currentGear)] = {}
    graph[str(currentGear)][str(currentSpeed)] = currentFCR
    dict_to_json(graph,fileName)