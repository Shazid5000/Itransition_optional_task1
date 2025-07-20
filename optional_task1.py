# optional_task1.py
# Python → JavaScript → Python Quine

def escape_js_multiline_string(s):
    return s.replace('\\', '\\\\').replace('`', '\\`')

def main():
    python_src = '''# optional_task1.py
# Python → JavaScript → Python Quine

def escape_js_multiline_string(s):
    return s.replace('\\\\', '\\\\\\\\').replace('`', '\\\\`')

def main():
    python_src = %r
    js_template = %r
    with open("output.js", "w", encoding="utf-8") as f:
        js_code = js_template %% escape_js_multiline_string(python_src %% (repr(python_src), repr(js_template)))
        f.write(js_code)

if __name__ == "__main__":
    main()'''

    js_template = '''// output.js
const code = `%s`;
console.log(code);'''

    with open("output.js", "w", encoding="utf-8") as f:
        js_code = js_template % escape_js_multiline_string(python_src % (repr(python_src), repr(js_template)))
        f.write(js_code)

if __name__ == "__main__":
    main()