# O(n) T | O(n) S


def isImportantToken(token):
    # not "" empty string( like "//") , not . , previously "/" is checked
    return len(token) > 0 and token != "."

def shortenPath(path):
    ifStartsWithSlash = path[0] == "/"

    isImportantTokens = filter(isImportantToken, path.split("/"))
    stack = []
    if ifStartsWithSlash:
        stack.append("")
    for token in isImportantTokens:
        if token == "..":
            # this means, .. is the current token and there is nothing previous to it like "../"
            # if .. is already present in stack,(we have already seen ..) then append .. like "../.."
            if len(stack)== 0 or stack[-1] == "..":
                stack.append(token)
            # incase last holded char in stack is not root directory, which we choosen to represent using "" empty string,
            # pop stack, because there is .. and there is somethign in stack other than root, which will go back by one directory

            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)


    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)

print(shortenPath( "/foo/../test/../test/../foo//bar/./baz" ))

print(shortenPath( "foo/bar/baz" ))
print(shortenPath( "/../../foo/bar/baz" ))
print(shortenPath( "../../foo/bar/baz" ))


print(shortenPath( "/../../foo/../../bar/baz" ))
print(shortenPath( "../../foo/../../bar/baz" ))

print(shortenPath( "/foo/./././bar/./baz///////////test/../../../kappa"))

print("afd;j")
print(shortenPath("../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../.."))


print(shortenPath("/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../../foo"
))


print(shortenPath("foo/bar/.."))

print(shortenPath( "./foo/bar"))

print(shortenPath("foo/../.."))
print(shortenPath("/"))