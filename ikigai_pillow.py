from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, output_image_path, texts, positions, font_size=30, font_color=(0, 0, 0), font_path=None):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)

    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.truetype("arial.ttf", font_size)
    
    for text, position in zip(texts, positions):
        draw.text(position, text, font=font, fill=font_color)
    image.save(output_image_path)

def chatgpt_model(responses):
    #we use the responses to genrate the 4 values for putting in our pic
    return responses

def pic_write(responses_from_user):
    input_image_path = "ikigai.jpeg"
    output_image_path = "ikigai_with_text.jpeg"
    #we can add the text we want to add here
    texts_to_add=chatgpt_model(responses_from_user)
    #positions fo the texts def image size is 640 x 640
    positions = [(190, 210), (400, 210), (190, 410), (400, 410)]
    font_size = 20
    #if we have another font we can use this
    custom_font_path = "Arial.ttf"
    add_text_to_image(input_image_path, output_image_path, texts_to_add, positions, font_size, font_path=custom_font_path)
    #we can change the text size , font , and positions as needed 
