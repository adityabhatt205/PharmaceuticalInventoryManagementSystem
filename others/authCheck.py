authorized = {"root": "root", "guest": "123456"}


def authCheck(L):
    if (L[0] in authorized) and (authorized[L[0]] == L[1]):
        return True
    return False


#
# correct = ["root", "root"]
# incorrect = ["guest", "not root"]
#
# print(authCheck(correct), authCheck(incorrect), sep="\n")
