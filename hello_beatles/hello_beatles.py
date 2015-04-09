import fileinput


def main():
    for line in fileinput.input():
        print 'Hello, {name}!'.format(name=line.rstrip())


if __name__ == '__main__':
    main()
