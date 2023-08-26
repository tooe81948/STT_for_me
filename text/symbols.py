'''
Defines the set of symbols used in text input to the model.
'''

_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijklmnoprstuvwyzʃʧʦɯɹəɥ⁼ʰ`→↓↑ ๆไำพะัีรนยบลฟหกดเ้่าสวงผปแอิืทมใฝฦฬฒ?์ฺฮฉ.ซศษ๋็ฌโฏฆฤ๐ฎฑธํ๊ณฯญฐภถุูึคตจขช๙๘๗๖๕๔๓๒๑)'



# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")
