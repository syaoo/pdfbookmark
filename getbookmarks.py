from PyPDF2 import PdfFileReader as reader
def getbookmark(fullfile):
    pdffile = reader(fullfile)
    outlins = pdffile.getOutlines()
    content = []
    for bm in outlins:
        if type(bm) == list:
            for sub in bm:
                thistitl = sub.title
                thispage = pdffile.getDestinationPageNumber(sub)
                content.append((thistitl,thispage))
        else:
            thistitl = bm.title
            thispage = pdffile.getDestinationPageNumber(bm)
            content.append((thistitl,thispage))
    return content

lis = getbookmark('/home/astro/tianti.pdf')
# lis = getbookmark('./天文地球.pdf')
f = open('./contents1.txt','w')
for s in lis:
    f.write('{}@{}\n'.format(s[0],s[1]))
f.close()