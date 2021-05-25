'''
Doesn't make any sense
'''




from PyPDF2 import PdfFileReader
from pprint import pprint
import PyPDF2

def walk(obj, fnt, emb):
    '''
    If there is a key called 'BaseFont', that is a font that is used in the document.
    If there is a key called 'FontName' and another key in the same dictionary object
    that is called 'FontFilex' (where x is null, 2, or 3), then that fontname is 
    embedded.
    
    We create and add to two sets, fnt = fonts used and emb = fonts embedded.
    '''
    if not hasattr(obj, 'keys'):
        return None, None
    fontkeys = set(['/FontFile', '/FontFile2', '/FontFile3'])
    if '/BaseFont' in obj:
        fnt.add(obj['/BaseFont'])
    if '/FontName' in obj:
        if [x for x in fontkeys if x in obj]:# test to see if there is FontFile
            emb.add(obj['/FontName'])

    for k in obj.keys():
        walk(obj[k], fnt, emb)

    return obj[k], fnt, emb# return the sets for each page

if __name__ == '__main__':
    fname = 'input.pdf'
    pdf = PdfFileReader(fname)
    fonts = set()
    embedded = set()
    for page in pdf.pages:
        obj = page.getObject()
        # updated via this answer:
        # https://stackoverflow.com/questions/60876103/use-pypdf2-to-detect-non-embedded-fonts-in-pdf-file-generated-by-google-docs/60895334#60895334 
        # in order to handle lists inside objects. Thanks misingnoglic !
        # untested code since I don't have such a PDF to play with.
        if type(obj) == PyPDF2.generic.ArrayObject:  # You can also do ducktyping here
            for i in obj:
                if hasattr(i, 'keys'):
                    obj, f, e = walk(i, fonts, embedded_fonts)
                    print(obj, f, e)
                    fonts = fonts.union(f)
                    embedded = embedded.union(e)
        else:
            obj, f, e = walk(obj['/Resources'], fonts, embedded)
            print(obj, f, e)
            fonts = fonts.union(f)
            embedded = embedded.union(e)

    unembedded = fonts - embedded
    print ('Font List')
    pprint(sorted(list(fonts)))
    if unembedded:
        print ('\nUnembedded Fonts')
        pprint(unembedded)