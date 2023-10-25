from vertex import vertex
from edge import edge
class graph:
    def __init__(self):
        self.nodes= [
                vertex(0, 0, 0),
                vertex(1, 1, 1),
                vertex(2, 2, 2),
                vertex(3, 3, 3),
                vertex(4, 0, 1),
                vertex(5, 1, 2),
                vertex(6, 2, 3),
                vertex(7, 3, 0),
                ]

        lines = [
                [0, 1 ,1],
                [0, 7, 4],
                [1, 7, 2],
                ]

        for k in range(0, len(lines)):
            temp_edge = []
            for i in range(0, len(self.nodes)):
                j = 0

                if self.nodes[i].getID() == lines[k][0]:
                    j = j + 1
                    temp_edge.append(self.nodes[i])
                if self.nodes[i].getID() == lines[k][1]:
                    j = j + 1
                    temp_edge.append(self.nodes[i])

                if j == 2:
                    break
            
            print(temp_edge)
            temp_edge[0].getEdges().append(edge(temp_edge[1], temp_edge[0].distanceTo(temp_edge[1])))
            temp_edge[1].getEdges().append(edge(temp_edge[0], temp_edge[1].distanceTo(temp_edge[0])))
                                            

    def get_node(self,x ,y):
        search = vertex(0, x, y)
        closest = self.nodes[0]
        distance = search.distanceTo(closest)

        for i in range(1, len(self.nodes)):
            if search.distanceTo(self.nodes[i]) < distance:
                closest = self.nodes[i]
                distance = search.distanceTo(closest)

        return closest


