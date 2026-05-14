echo "" > build/output.lc2
find . -name "*.lc3" -exec echo {} >> build/output.lc3 ';'
lc3as build/output.lc3
