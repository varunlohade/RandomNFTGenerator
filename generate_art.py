from PIL import Image, ImageDraw
import random
def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def interpolate(startColor, endColor, factor:float):
    recip = 1 - factor
    return (
    int(startColor[0] *recip +endColor[0] *factor),
    int(startColor[1] *recip +endColor[1] *factor),
    int(startColor[2] *recip +endColor[2] *factor))


def generate_art():
    image_size_px = 128
    image_background_color = (255, 255, 255)
    start_color = random_color()
    end_color = random_color()
    image = Image.new("RGB", 
    size=(image_size_px , image_size_px ), color=(image_background_color))
    padding_px = 12
    points = []
    thickness = 0
    #Draw lines
    draw = ImageDraw.Draw(image)
    for _ in range(10):
        randompoint = (random.randint(padding_px, image_size_px-padding_px), random.randint(padding_px, image_size_px-padding_px))
        points.append(randompoint)

    n_points = len(points)-1
    
    for i, point in enumerate(points):
        p1 = point
        if i ==n_points:
            p2 = points[0]
        else:
            p2 = points[i+1]
        line_xy = (p1, p2)
        color_factor = i/n_points
        line_color = interpolate(startColor = start_color, endColor= end_color,factor=color_factor)
        thickness += 1
        draw.line(line_xy, fill=line_color, width=thickness)
    image.save(f"test_image{i}.png")
if __name__ == '__main__':
    generate_art()