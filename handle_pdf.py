# coding:utf-8
# 添加PDF书签
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import configparser
import sys
import codecs
# reload(sys)
# sys.setdefaultencoding('utf-8')

def main():
    # 从配置文件中读取配置信息
    cf = configparser.ConfigParser()
    cf.readfp(codecs.open('./info.conf','r','utf-8'))
    # cf.read('./info.conf')
    print('a:{0}'.format(cf.sections))
    pdf_path = cf.get('info','pdf_path')
    bookmark_file_path = cf.get('info','bookmark_file_path')
    page_offset = cf.getint('info','page_offset')
    new_pdf_file_name = cf.get('info','new_pdf_file_name')

    pdf_handler = MyPDFHandler(pdf_path,mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt(bookmark_file_path,page_offset = page_offset)
    pdf_handler.save2file(new_pdf_file_name)

if __name__ == '__main__':
    main()