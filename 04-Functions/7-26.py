def f(text):
    result = ""
    for i in range(len(text)):
        result += text[i]
        if i < len(text) - 1:
            result += "-"
    return result

print(f("Univesity"))