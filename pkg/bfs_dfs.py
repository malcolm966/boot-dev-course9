class Graph:
    def depth_first_search(self, start_vertex):
        visited = list()
        return self.depth_first_search_r(visited, start_vertex)

    def depth_first_search_r(self, visited:list, current_vertex):
        visited.append(current_vertex)
        for e in sorted(self.graph[current_vertex]):
            if e in visited:
                continue
            self.depth_first_search_r(visited, e)
        return visited
    
    
    def breadth_first_search(self, v):
        visited = list()
        to_be_visit = list()
        to_be_visit.append(v)
        while len(to_be_visit) != 0:
            cur = to_be_visit.pop(0)
            visited.append(cur)
            if cur in self.graph:
                ad_list = sorted(self.graph[cur])
                for i in ad_list:
                    if i not in to_be_visit and i not in visited:
                        to_be_visit.append(i)
        return visited
    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


run_cases = [
    (
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
        ],
        "New York",
        ["New York", "Cairo", "London", "Dubai", "Tokyo"],
    ),
]
submit_cases = run_cases + [
    (
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "New York",
        [
            "New York",
            "Buenos Aires",
            "Tokyo",
            "Cairo",
            "Kyiv",
            "San Francisco",
            "Madrid",
            "London",
            "Dubai",
        ],
    ),
]


def test(edges_to_add, starting_at, expected_visited):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        bfs = graph.depth_first_search(starting_at)
        for i, v in enumerate(bfs):
            print(f"Visiting:  {v}")
            print(f"Expected:  {expected_visited[i]}")

        if bfs == expected_visited:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
