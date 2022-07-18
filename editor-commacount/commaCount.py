def countCommas(text):
    try:
        processText = text
        if ("?text=" in text):
            processText=text.split('=',1)
        if (len(processText)<1):
            return -1
        commas = processText.count(',')
        return commas
    except:
        return -1
