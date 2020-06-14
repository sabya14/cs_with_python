# Problem statement 4.7 Cracking the coding interview


class BuildOrder:

    def __init__(self, projects):
        self.projects = list(map(lambda x: Node(x, []), projects))
        self.order = []

    def get_order(self, dependencies):
        self.initialize_dependencies(dependencies)
        self.find_order()
        return self.order

    def find_order(self):
        build_nodes = list(filter(lambda node: len(node.dependencies) == 0, self.projects))
        if len(build_nodes) == len(self.projects):
            self.order += list(map(lambda node: node.project, build_nodes))
            return
        else:
            self.remove_dependencies(build_nodes)
            self.find_order()

    def remove_dependencies(self, build_nodes):
        for build_node in build_nodes:
            for node in self.projects:
                node.remove_dependency(build_node.project)

    def initialize_dependencies(self, dependencies):
        for dependency in dependencies:
            current_node = next(node for node in self.projects if node.project == dependency[1])
            dependent_node = next(node for node in self.projects if node.project == dependency[0])
            current_node.add_dependency(dependent_node)


class Node:

    def __init__(self, project, dependencies):
        self.project = project
        self.dependencies = dependencies

    def __repr__(self):
        return self.project

    def __str__(self):
        return self.project

    def add_dependency(self, node):
        self.dependencies.append(node.project)

    def remove_dependency(self, remove_node):
        self.dependencies = list(filter(lambda node: node != remove_node, self.dependencies))
