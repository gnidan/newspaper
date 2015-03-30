import parsley

from newspaper.ast import node

def flatten_lines(lines):
    return [line.nodes for line in lines]

parser = parsley.makeGrammar(
    """
    word = <letter+>:ls -> node.Word(ls)

    wordws = word:word exactly(' ')* -> word

    vspace = '\\n' | '\\r\\n' | '\\r'

    line = wordws+:text vspace -> node.Text(text)

    paragraph = line+:lines vspace+ -> node.Text([node for line in lines for node in line.nodes])

    """, {'node': node})

