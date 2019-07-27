import wget
import re
import argparse




def download():
    baselink = 'http://www.diag.uniroma1.it/~deluca/rob1_en/'

    links = []
    regex = re.compile('(?<=href=")(.*?)(?=.pdf*)')
    with open('exam_links', 'r') as file_link:
        for line in file_link:
            res = regex.split(line)
            for el in res:
                if el.startswith('Written'):
                    links.append(el+'.pdf')

    for link in links:
        try:
            wget.download(baselink + link)
        except Exception as e:
            print(e, 'on file: ', link)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='From the html source of a web page, inserting the initial (usually: http:\\\\ ) and final (usually the file extension) letters of the various file links, it will download (with wget) every file from the links found')
    parser.add_argument('-f','--file_path', help='the file path in which is stored the html of the page')
    parser.add_argument('-s', '--starting_string', help='the string which the link should end with')
    parser.add_argument('-e', '--ending_string', help='the string which the link should end with')

    args = parser.parse_args()

    download()