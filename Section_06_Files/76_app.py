from utils.common.file_operations import save_to_file, read_file
from utils.find import find_in


if __name__ == '__main__':
    save_to_file('Rolf', '76_data.txt')

    print(read_file('76_data.txt'))