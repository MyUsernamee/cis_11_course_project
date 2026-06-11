""" Simple LC3 assembler preprocessor to add some extra directives.
I got really tired of writing out pushes and pops, and clearing registers or moving values, so I made this."""

from argparse import ArgumentParser
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryFile
from tree_sitter_lc3asm import language
from tree_sitter import *

LANGUAGE = Language(language())

subsitutions = {
        ".PUSH": """
ADD R6, R6, #-1
STR R7, R6, #0
ADD R6, R6, #-1
STR R1, R6, #0
ADD R6, R6, #-1
STR R2, R6, #0
ADD R6, R6, #-1
STR R3, R6, #0 
ADD R6, R6, #-1
STR R4, R6, #0 
ADD R6, R6, #-1
STR R5, R6, #0 ; Save R1-R5, R7 to stack""",
        ".POP": """LDR R7, R6, #5
LDR R1, R6, #4
LDR R2, R6, #3
LDR R3, R6, #2
LDR R4, R6, #1
LDR R5, R6, #0
ADD R6, R6, #6""",
}

def do_directives(src: bytes):
    parser = Parser(LANGUAGE)
    c = QueryCursor(Query(LANGUAGE, "(directive) @d"))
    tree = parser.parse(src)
    captures = c.captures(tree.root_node)

    while len(captures['d']) > 0:
        text = ""
        while not text in subsitutions and len(captures['d']) > 0:
            node = captures["d"].pop()
            text = node.text.decode().upper()
        if len(captures['d']) == 0 and not text in subsitutions:
            return src
        src = src[:node.start_byte] + subsitutions[text].encode() + src[node.end_byte:]
        tree = parser.parse(src)
        tree.print_dot_graph(open('./test.dot', 'w'))
        captures = c.captures(tree.root_node)

    return src

def main():
    parser = ArgumentParser("lc3preprocess")

    _ = parser.add_argument("filenames", nargs="+")
    args = parser.parse_args()

    for file in args.filenames:
        path = Path(file)
        src = open(path, "r").read().encode()
        new_path = path.with_suffix(".post.lc3")
        new_src = do_directives(src)
        open(new_path, "w").write(new_src.decode())
        subprocess.call(["lc3as", new_path])

if __name__ == "__main__":
    main()

