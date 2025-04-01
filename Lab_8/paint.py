import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    shapes = []  # List to store drawn shapes
    drawing_shape = None  # None, 'rectangle', 'circle', 'eraser'
    shape_start = None
    shape_end = None
    mouse_held = False
    erasing = False
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    drawing_shape = 'circle'
                elif event.key == pygame.K_v:
                    drawing_shape = 'rectangle'
                elif event.key == pygame.K_e:
                    drawing_shape = 'eraser'
                elif event.key == pygame.K_p:
                    drawing_shape = None  # Pen mode
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_held = True
                    if drawing_shape == 'eraser':
                        erasing = True
                    elif drawing_shape:
                        shape_start = event.pos
                    else:
                        radius = min(200, radius + 1)
                elif event.button == 3:  # Right click
                    radius = max(1, radius - 1)
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_held = False
                    erasing = False
                    if drawing_shape and shape_start:
                        shape_end = event.pos
                        shapes.append((drawing_shape, shape_start, shape_end, mode))
                        shape_start = None
                        shape_end = None
                
            if event.type == pygame.MOUSEMOTION:
                if mouse_held:
                    if drawing_shape == 'eraser':
                        points.append((event.pos, 'eraser'))
                    elif drawing_shape and shape_start:
                        shape_end = event.pos
                    elif not drawing_shape:
                        position = event.pos
                        points.append((position, mode))
                        points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # Draw all points
        i = 0
        while i < len(points) - 1:
            if points[i][1] == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), points[i][0], 20)
            else:
                drawLineBetween(screen, i, points[i][0], points[i + 1][0], radius, points[i][1])
            i += 1
        
        # Draw all stored shapes
        for shape, start, end, shape_color in shapes:
            drawShape(screen, shape, start, end, shape_color)
        
        # Preview shape while drawing
        if shape_start and shape_end:
            drawShape(screen, drawing_shape, shape_start, shape_end, mode, preview=True)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawShape(screen, shape, start, end, color_mode, preview=False):
    color_dict = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    color = color_dict.get(color_mode, (255, 255, 255))
    if preview:
        color = (200, 200, 200)  # Gray preview color
    
    if shape == 'rectangle':
        x1, y1 = start
        x2, y2 = end
        pygame.draw.rect(screen, color, pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2 if preview else 0)
    elif shape == 'circle':
        x1, y1 = start
        x2, y2 = end
        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start, radius, 2 if preview else 0)
    elif shape == 'eraser':
        pygame.draw.circle(screen, (0, 0, 0), start, 20)

main()