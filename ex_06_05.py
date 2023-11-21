str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
piece = str[ipos+2:]
x = float(piece)
print(x)