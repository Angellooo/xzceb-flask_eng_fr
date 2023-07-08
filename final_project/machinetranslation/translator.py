''' Script to translate English to Fremch and reverse '''

import deep_translator

def english_to_french(english_to_text):
    ''' Function to translate English to French '''
    french_to_text = deep_translator.MyMemoryTranslator(
        source='en-US', target='fr-FR').translate(english_to_text)
    return french_to_text

def french_to_english(french_to_text):
    ''' Function to translate French to English '''
    english_to_text = deep_translator.MyMemoryTranslator(
        source='fr-FR', target='en-US').translate(french_to_text)
    return english_to_text
