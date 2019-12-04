from PyPDF2 import PdfFileReader as reader
def getbookmark(fullfile:str, outfile:str=None):
    '''
    提取PDF文件中的bookmarks，存储到content元组列表中
    :param fullfile：PDF文件路径字符串
    :param outfile：可选参数，将提取的PDF书签输出outfile指定路径
    : return: list
    '''
    pdffile = reader(fullfile)
    outlins = pdffile.getOutlines()
    content = []
    for bm in outlins:
        if type(bm) == list:
            for sub in bm:
                thistitl = sub.title
                thispage = pdffile.getDestinationPageNumber(sub)
                content.append(('\t'+thistitl,thispage))
                # if bm.index(sub) == 0:
                #     content.append(('\t'+thistitl,thispage))
                # else:
                #     content.append((thistitl,thispage))
        else:
            thistitl = bm.title
            thispage = pdffile.getDestinationPageNumber(bm)
            content.append((thistitl,thispage))
    # outfile存在则将bookmarks存储到outfie中
    if outfile != None:
        f = open(outfile,'w')
        for s in content:
            f.write('{}@{}\n'.format(s[0],s[1]))
        f.close()
    return content

# lis = getbookmark('/home/astro/tianti.pdf','./files/tt')
lis = getbookmark('/home/astro/物理学中的数学方法-李政道.pdf','./files/tt.txt')
for t,n in lis:
    print(t,n)
