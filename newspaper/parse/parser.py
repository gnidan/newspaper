import parsley

from newspaper.parse import utils

parser = parsley.makeGrammar(
    """
    word = <letter+>:ls -> utils.make_word(ls)

    sp = exactly(' ')

    mark = ',' | '.' | '"' | '!' | '?' | "'" | ':' | ';'

    chunk = mark*:ls word:w mark*:rs sp* -> utils.make_chunk(ls, w, rs)

    vspace = '\\n' | '\\r\\n' | '\\r'

    line = chunk+:chunks vspace -> utils.make_line(chunks)

    paragraph = line+:lines vspace+ -> utils.make_paragraph(lines)

    h1_sym = exactly('=')
    h1_row = h1_sym{3} h1_sym* vspace -> 1
    h2_sym = exactly('-')
    h2_row = h2_sym{3} h2_sym* vspace -> 2
    header_row = h1_row | h2_row
    header = line+:ls header_row:lvl vspace+ -> utils.make_header(ls, lvl)

    block = paragraph | header

    document = block+:blocks -> utils.make_document(blocks)

    """, {
        'utils': utils,
    }
)

