# think this is done


class Scene:

    def __init__(self, camera, objects = None, lights = None, width = 800, height = 600):
        self.camera = camera
        self.objects = objects if objects is not None else []
        self.lights = lights if objects is not None else []
        self.width = width
        self.height = height

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self,obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def add_light(self, light):
        self.lights.append(light)

    def remove_light(self, light):
        if light in self.lights:
            self.lights.remove(light)

    def update_scene(self, d_t):
        for obj in self.objects:
            if hasattr(obj, 'center_velocity'):
                obj.center += obj.center_velocity * d_t

        for light in self.lights:
            if hasattr(light, 'velocity'):
                light.position += light.velocity * d_t
