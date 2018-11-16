##############################################################################
# The program do not nothing special, only shows formatting dictionary
##############################################################################

A = {1: "one", 2: "two"}
B = {2: "dva", 3: "three"}


def transforms(A):  # converts dict to list in tuple
    l = []
    for i in A.items():
        l.append(i)
    print("Converting dictionary:\n{}\n\nTo tuple:\n{}\n{}\n".format(A,
                                                                     l,
                                                                     "=" * 50))


def merge(A, B):
    ax = A.copy()
    bx = B.copy()
    for key, value in bx.items():
        if key in ax:
            ax[key] = [ax[key], value]
        else:
            ax[key] = value
    print(">>> A = {}\n>>> B = {}\n>>> Merge: {}\n{}\n".format(A,
                                                               B,
                                                               ax,
                                                               "=" * 50))


transforms(A)
merge(A, B)
