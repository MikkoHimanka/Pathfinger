from utils.mathTools import distance


class AStar:
    def get_path(self, start_node, end_node):
        start_node.distance = 0

        queue = []
        visited_points = []

        queue.append((0, start_node))

        while len(queue) > 0:
            node = queue.pop()[1]

            if not node.visited:
                visited_points.append(node.origin)
                node.visited = True

            if node == end_node:
                break

            for neighbor in node.connections:
                new_distance = (
                    node.distance + distance(node.origin, neighbor.origin)
                )
                if new_distance >= neighbor.distance:
                    continue
                neighbor.distance = new_distance
                neighbor.previous_node = node

                neighbour_to_goal = distance(neighbor.origin, end_node.origin)
                queue.append((neighbour_to_goal, neighbor))

            queue.sort(key=lambda item: item[0], reverse=True)

        resulting_path = []
        current = end_node

        try:
            while current.previous_node:
                resulting_path.append(current.origin)
                current = current.previous_node
        except AttributeError:
            pass

        if len(resulting_path) > 0:
            resulting_path.append(current.origin)

        resulting_path.reverse()

        return [resulting_path, visited_points]
