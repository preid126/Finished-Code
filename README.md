Somewhat Finished Coding Projects

This directory contains some projects that I am working either for school or just out of curiosity.
I am a physics student at the University of Victoria and working on improving my skills with coding
to better apply with physics concepts. 

Currently there are two projects, a raytracer engine and some orbital motion simulations.



Ray Tracing

Currently I am interested in optics so I decided that building a ray tracer would let me improve in that area. Currently it is rather basic although I was able to include non-spherical 3d shapes as well as create videos as light or objects move. I want to eventually expand this project with the orbital motion to simulate light emmited from a body like a sun orbitting some planet. The engine is also quite slow so I am looking into ways to speed up the process. Currently refraction is not taken into account, but this is also something I would like to build to. 

Numpy and OpenCV are the only libraries that are needed to run the RayTracer although when I implment the orbit it is likely that sympy will also be required. 

Currently to run the simiulation there is the option to produce a single frame .png file or to produce an .mpf video file. I have not created a new file to switch between the two yet, but it is very much a work in progress. main() defines the objects and light sources which then get added to a scene that is used with the rendering engine to produce the final product. The colours of the objects and light is defined using a normalized rgb vector. 

I used two main sources to build this project. First is Arun Ravindran's youtube series to introduce a lot of the concepts and issues that arise with ray tracing. The channel can be found at https://www.youtube.com/@arunrocks. This series was very helpful for providing the frame work to constuct the raytracer. The second resource is rossant/raytracing.py for the implementation of a plane within the simulation. 

