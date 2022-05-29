class GameObject:
        def __init__(self, transform, components = []):
                components.append(transform)
                self.components = components

        def AddComponent(self, component):
                self.components.append(component)

        def RemoveComponent(self, component):
                self.components.remove(component)