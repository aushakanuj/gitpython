def hanoi(n, source, auxilary, destination):

    if n == 1:
        print("Plate 1 from %s to %s" % (source, destination))
        return

    hanoi(n - 1, source, destination, auxilary)

    print("Plate %s from %s to %s" % (n, source, destination))

    hanoi(n - 1, auxilary, source, destination)

