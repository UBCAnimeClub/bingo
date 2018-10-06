#!/usr/bin/env python

import random, sys

# check for the right # of args
if len(sys.argv) != 4:
    print "USAGE: " + sys.argv[0], " [file of terms] [output file] [# of cards]"
    print "Example: " + sys.argv[0] + " bingo_terms.txt bingo.html 20"
    sys.exit(1)

# read in the bingo terms
with open(sys.argv[1], 'r') as in_file:
    terms = [line.strip() for line in in_file.readlines()]
    terms = filter(lambda x: x != "", terms)

# XHTML4 Strict, y'all!
head = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
        "<html lang=\"en\">\n<head>\n"
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Bingo Cards</title>\n"
        "<style type=\"text/css\">\n"
        "\tbody { font-size: 12px; }\n"
        "\ttable { margin: 40px auto; border-spacing: 2px; }\n"
        "\t.newpage { page-break-after:always; }\n"
        "\ttr { height: 60px; }\n"
        "\ttd { text-align: center; border: thin black solid; padding: 10px; width: 60px; }\n"
        "</style>\n</head>\n<body>\n")

# Generates an HTML table representation of the bingo card for terms
def generate_table(terms):
    ts = terms[:12] + ["FREE SPACE"] + terms[12:24]
    res = "<table>\n"
    for i, term in enumerate(ts):
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

def page_break():
    return "<table class=\"newpage\">\n"

with open(sys.argv[2], 'w') as out_file:
    out_file.write(head)
    cards = int(sys.argv[3])
    for i in range(1, cards + 1):
        random.shuffle(terms)
        out_file.write(generate_table(terms))

        if i % 2 == 0:
            out_file.write(page_break())

    out_file.write("</body></html>")
