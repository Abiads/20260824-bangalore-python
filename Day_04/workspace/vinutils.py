def line():
    print('-'*80)


def dir1(obj):
    return [at for at in dir(obj) if not at.startswith("_")]