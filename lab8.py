from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    encoded_img = img.copy()
    img = Image.open(image_path)
    img = img.convert('RGB')  # Convert image to RGB mode


    width, height = img.size
    message_length = len(message)

    encoded = False
    if message_length * 3 <= width * height:  # Проверяем, может ли сообщение поместиться в изображение
        encoded = True
        message += "###"  # Добавляем разделитель, чтобы отметить конец сообщения

        data_index = 0
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))

                # Кодируем ASCII-значение каждого символа в значения пикселей (R, G, B)
                if data_index < len(message):
                    ascii_value = ord(message[data_index])
                    encoded_img.putpixel((x, y), (r // 2 * 2 + ascii_value % 2,
                                                   g // 2 * 2 + (ascii_value // 2) % 2,
                                                   b // 2 * 2 + (ascii_value // 4) % 2))
                    data_index += 1

                if data_index >= len(message):
                    break
            if data_index >= len(message):
                break

    encoded_img.save("encoded_image.png")
    return encoded

# Пример использования:
message_to_hide = "Привет, это секретное сообщение!"
image_path = "C:\\Users\\Admin\\Desktop\\пит\\крылья.png"
# Кодирование сообщения в изображение
encoded = encode_image(image_path, message_to_hide)
if encoded:
    print("Сообщение успешно закодировано в изображение.")
else:
    print("Сообщение слишком длинное для кодирования в изображение.")
