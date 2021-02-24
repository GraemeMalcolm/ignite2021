def show_action(intent, entities):
    import matplotlib.pyplot as plt
    from PIL import Image
    import os

    action = 'unknown'
    device = 'none'
    if intent in ['switch_on', 'switch_off']:
            # Check for entities
            if len(entities) > 0:
                # Check for a device entity
                if 'device' in entities:
                    # ML entities are strings, get the first one
                    device = entities['device'][0][0]
                    action = intent + '_' +  device
    print('Intent: {}'.format(intent))
    print('Device: {}'.format (device))
    img_name = action + '.jpg'
    img = Image.open(os.path.join("data", "luis" ,img_name))
    plt.axis('off')
    plt. imshow(img)

def show_action_from_speech(intent, entities):
    import matplotlib.pyplot as plt
    from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioConfig
    from PIL import Image
    from dotenv import load_dotenv
    import json
    import os

    action = 'unknown'
    device = 'none'
    if intent in ['switch_on', 'switch_off']:
        # Check for entities
        if len(entities) > 0:
            # Check for a device entity
                # Get the first entity (if any)
                if entities[0]["type"] == 'device':
                    device = entities[0]["entity"]
                    action = intent + '_' +  device
        load_dotenv()
        cog_key = os.getenv('SPEECH_KEY')
        cog_location = os.getenv('SPEECH_REGION')
        response_text = "OK, I'll {} the {}!".format(intent, device).replace("_", " ")
        speech_config = SpeechConfig(cog_key, cog_location)
        speech_synthesizer = SpeechSynthesizer(speech_config)
        result = speech_synthesizer.speak_text(response_text)

    img_name = action + '.jpg'
    img = Image.open(os.path.join("data", "luis" ,img_name))
    plt.axis('off')
    plt. imshow(img)

