from PIL import Image, ImageDraw, ImageChops
import random
import colorsys
def random_color():
    h = random.random()
    s = 1
    v = 1
    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x*255) for x in float_rgb]
    return tuple(rgb)

def interpolate(startColor, endColor, factor:float):
    recip = 1 - factor
    return (
    int(startColor[0] *recip +endColor[0] *factor),
    int(startColor[1] *recip +endColor[1] *factor),
    int(startColor[2] *recip +endColor[2] *factor))


def generate_art(path: str):
    target_size_px = 256
    scale_factor = 2
    image_size_px = target_size_px *scale_factor
    image_background_color = (0, 0, 0)
    start_color = random_color()
    end_color = random_color()
    image = Image.new("RGB", 
    size=(image_size_px , image_size_px ), color=(image_background_color))
    padding_px = 16*scale_factor
    points = []
    thickness = 0
    #Draw lines
    draw = ImageDraw.Draw(image)
    for _ in range(10):
        randompoint = (random.randint(padding_px, image_size_px-padding_px), random.randint(padding_px, image_size_px-padding_px))
        points.append(randompoint)
    #Draw bounding box
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    # draw.rectangle((min_x, min_y, max_x, max_y),outline=(230, 230,230))
    #Center image
    delta_x = min_x-(image_size_px - max_x)
    delta_y = min_y -(image_size_px- max_y)
    for i, point in enumerate(points):
        points[i]=(point[0] - delta_x//2, point[1] -delta_y//2)
    
  
    n_points = len(points)-1

    #draw points
    for i, point in enumerate(points):
        #overlay canvas
        overlay_image = Image.new("RGB", size=(image_size_px , image_size_px ), color=(image_background_color))
        overlay_draw = ImageDraw.Draw(overlay_image)
        p1 = point
        if i ==n_points:
            p2 = points[0]
        else:
            p2 = points[i-1]
        line_xy = (p1, p2)
        color_factor = i/n_points
        line_color = interpolate(startColor = start_color, endColor= end_color,factor=color_factor)
        thickness += scale_factor
        # overlay_draw.line(line_xy, fill=line_color, width=thickness)
        overlay_draw.rectangle(line_xy,fill=line_color, width=thickness)
        # overlay_draw.arc(xy=line_xy, start=min_x, end=max_y)
        image = ImageChops.add(image, overlay_image)

    image =image.resize((target_size_px, target_size_px), resample=Image.ANTIALIAS)
    image.save(path)
if __name__ == '__main__':
    for i in range(10):
        generate_art(f"test_image_{i}.png")