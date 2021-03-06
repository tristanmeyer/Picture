"""
picture.py
Author: Tristan Meyer
Credit: None


Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xFDF200, 1.0)
darkgreen= Color(0x00A61B,1.0)
line = LineStyle(2, black)
lineyellow = LineStyle(2, yellow)
sky = RectangleAsset(2000,2000,line,blue)
Sprite(sky, (-50,-50))
triangle = PolygonAsset([(0,0),(300,-400),(600,0)], line, green)
Sprite(triangle, (100, 50))
longtriangle = PolygonAsset([(0,0),(400,-350),(800,0)], line, green)
Sprite(longtriangle, (250, 100))
bigtriangle = PolygonAsset([(0,0),(275,-300),(750,0)], line, green)
Sprite(bigtriangle, (250, 150))
hugetriangle= bigtriangle = PolygonAsset([(0,0),(500,-500),(900,0)], line, green)
Sprite(hugetriangle, (450, -50))
bigtriangle = PolygonAsset([(0,0),(275,-300),(750,0)], line, green)
Sprite(bigtriangle, (-150, 150))
sun = CircleAsset(75,line,yellow)
Sprite(sun, (150,0))
hill = EllipseAsset(1200,250,line,darkgreen)
Sprite(hill, (-500,400))
eye = CircleAsset(10,line,black)
Sprite(eye, (185,40))
eye = CircleAsset(10,line,black)
Sprite(eye, (240,40))
smile = EllipseAsset(40,25,line, black)
Sprite(smile, (185, 70))
smile = EllipseAsset(40,25,lineyellow,yellow)
Sprite(smile, (185,60))
myapp = App()
myapp.run()


# add your code here /\  /\  /\


myapp = App()
myapp.run()
