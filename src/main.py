import os
from static_generator import copy_to_dst

# code
def main():
    current_path = os.getcwd()

    static = os.path.join(current_path, 'static')
    public = os.path.join(current_path, 'public')

    print(current_path, static, public)

    copy_to_dst(static, public)

if __name__ == '__main__':
    main()
