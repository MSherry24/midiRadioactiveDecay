import pyglet

window = pyglet.window.Window()
# label = pyglet.text.Label('Hello, world', 
#                           font_name='Times New Roman', 
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')

# points = pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,('v2i', (10, 15, 30, 35)),('c3B', (0, 0, 255, 0, 255, 0)))


@window.event
def on_draw():
    # window.clear()
    # points.draw()
    # label.draw()
	for i in range(50):
	    for j in range(50):
	        color = int(2.56 * (i + j))
	        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
	            ('v2i', (i, j)),
	            ('c3B', (color, color, color))
	        )


pyglet.app.run()
