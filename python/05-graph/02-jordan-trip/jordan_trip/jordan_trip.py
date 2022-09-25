def jordan_trip(graph, city_arr):
    node_list = graph.get_nodes()
    node_dict = {}
    weight = 0
    for node in node_list:
        node_dict[node.value] = node
    for index in range(len(city_arr) - 1):
        first_city = city_arr[index]
        second_city = city_arr[index + 1]
        first_node = node_dict[first_city]
        second_node = node_dict[second_city]
        first_city_neighbors = graph.get_neighbors(first_node)
        linked = False
        for edge in first_city_neighbors:
            if edge.vertex == second_node:
                weight += edge.weight
                linked = True
        if not linked:
            return None
    return weight