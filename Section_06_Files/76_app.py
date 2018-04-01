# import file_operations
from utils.file_operations import save_to_file, read_file


if __name__ == '__main__':
    # file_operations.save_to_file('Rolf','76_data.txt')
    save_to_file('Rolf', '76_data.txt')

    print(read_file('76_data.txt'))