def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        positional_arguments = []
        named_arguments = {}
        for arg in args:
            positional_arguments.append(convert_md_to_txt(arg))
        for key, value in kwargs.items():
            named_arguments[key] = convert_md_to_txt(value)
        return func(*positional_arguments, **named_arguments)

    return wrapper

def convert_md_to_txt(doc):
    lines = doc.split("\n")
    rendered_lines = []
    for line in lines:
        rendered_lines.append(line.lstrip("#").lstrip())
    return "\n".join(rendered_lines)

@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""

@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""

