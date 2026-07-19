from PIL import Image

def compare_images(base_path, output_path, save_path):
    base = Image.open(base_path).convert("RGB")
    output = Image.open(output_path).convert("RGB")

    # Ensure same size
    if base.size != output.size:
        raise ValueError("Images must be same size!")

    width, height = base.size
    result = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            b_pixel = base.getpixel((x, y))
            o_pixel = output.getpixel((x, y))

            if b_pixel == o_pixel:
                result.putpixel((x, y), (0, 0, 0))  # black
            elif b_pixel != (0,0,0) and o_pixel == (0,0,0):
                result.putpixel((x, y), (0, 255, 0))  # green (missing)
            elif o_pixel != (0,0,0) and b_pixel == (0,0,0):
                result.putpixel((x, y), (255, 0, 0))  # red (extra)
            else:
                result.putpixel((x, y), (255, 255, 255))  # fallback

    result.save(save_path, "TIFF")
