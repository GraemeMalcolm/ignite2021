def show_detected_objects(image, objects):
    from matplotlib import pyplot as plt
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    import os

    test_img_h, test_img_w, test_img_ch = np.array(image).shape

    # Create a figure to display the results
    fig = plt.figure(figsize=(10, 10))
    plt.axis('off')

    # Display the image with boxes around each detected object
    draw = ImageDraw.Draw(image)
    lineWidth = int(np.array(image).shape[1]/100)
    object_colors = {
        "apple": "lightgreen",
        "banana": "yellow",
        "orange": "orange"
    }
    for prediction in objects:
        color = 'white' # default for 'other' object tags
        if (prediction.probability*100) > 50:
            if prediction.tag_name in object_colors:
                color = object_colors[prediction.tag_name]
            left = prediction.bounding_box.left * test_img_w 
            top = prediction.bounding_box.top * test_img_h 
            height = prediction.bounding_box.height * test_img_h
            width =  prediction.bounding_box.width * test_img_w
            points = ((left,top), (left+width,top), (left+width,top+height), (left,top+height),(left,top))
            draw.line(points, fill=color, width=lineWidth)
            plt.annotate(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100),(left,top), backgroundcolor=color)
    plt.imshow(image)