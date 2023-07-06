from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='en', target='french').translate(englishText)
    print(frenchText)
    return frenchText

englishToFrench('This is a test')
