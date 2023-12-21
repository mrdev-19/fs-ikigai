from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, output_image_path, texts, positions, font_size=30, font_color=(0, 0, 0), font_path=None):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)

    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.truetype("Gaegu.ttf", font_size)
    except IOError:
        font = ImageFont.truetype("Gaegu.ttf", font_size)
    
    for text, position in zip(texts, positions):
        draw.text(position, text, font=font, fill="#4B4649")
    image.save(output_image_path)

def pic_write(responses_from_user):
    input_image_path = "ikigai.jpeg"
    output_image_path = "ikigai_with_text.jpeg"
    #we can add the text we want to add here
    texts_to_add=responses_from_user
    #positions fo the texts def image size is 1080 x 1080
    custom_font_path = "Gaegu-Bold.ttf"
    texts_to_add[0]=texts_to_add[0]+"'s"
    W, H = 1080, 1080
    msg = texts_to_add[0]
    im = Image.new("RGBA", (W, H), "yellow")
    draw = ImageDraw.Draw(im)
    font_size=30
    font = ImageFont.truetype(custom_font_path, font_size)
# Use textbbox instead of textsize
    bbox = draw.textbbox((0, 0), msg, font=font)
    w, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    positions = [(((W-w)/2)-20,505),(480,180),(170,500),(480,800),(750,500),(350,430),(610,430),(350,630),(610,630)]
    #if we have another font we can use this
    add_text_to_image(input_image_path, output_image_path, texts_to_add, positions, font_size, font_path=custom_font_path)
    #we can change the text size , font , and positions as needed 
