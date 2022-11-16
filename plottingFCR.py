from communicate_with_database import*
# def create_plot_dictionary(gearCount):

#     graph = {}

#     for gear in range(1, gearCount):
#         graph[gear] = {}

#         for speed in range(0,160):
#             graph[gear][speed] = None
    
#     return graph

# print(create_plot_dictionary(6))

def update_plot(fileName, currentGear, currentSpeed, currentFCR):
    graph = json_to_dict(fileName)
    graph[str(currentGear)][str(currentSpeed)] = currentFCR
    dict_to_json(graph,fileName)