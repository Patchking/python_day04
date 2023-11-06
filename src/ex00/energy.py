
def fix_wiring(cables, sockets, plugs):
    return [f"plug {cable} into {socket} using {plug}" if plug is not None else f"weld {cable} to {socket} without plug" 
            for cable, socket, plug in zip(
                filter(lambda x: isinstance(x, str), cables),
                filter(lambda x: isinstance(x, str), sockets),
                sorted(plugs, key=lambda a: not isinstance(a, str))
                )
            ]

def main():
    print("\\" * 10, "test1", "\\" * 10)
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    print("\\" * 10, "test2", "\\" * 10)
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    print("\\" * 25)

if __name__ == "__main__":
    main()