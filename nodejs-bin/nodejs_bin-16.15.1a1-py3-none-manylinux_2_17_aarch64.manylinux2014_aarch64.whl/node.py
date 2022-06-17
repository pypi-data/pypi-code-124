import os, sys, subprocess
def run(args):
    return subprocess.call([
        os.path.join(os.path.dirname(__file__), "bin/node"),
        *args
    ])
def main():
    sys.exit(run(sys.argv[1:]))
if __name__ == '__main__':
    main()
