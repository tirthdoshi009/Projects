import argparse
import sys

def ccwc(filename, count_bytes=False, count_lines=False, count_words=False, count_characters=False):
    try:
        if filename:
            with open(filename, 'rb') as file:
                content = file.read()
        else:
            content = sys.stdin.buffer.read()
        
        if not any([count_bytes, count_lines, count_words, count_characters]) :
            byte_count = len(content)
            number_of_words = len(content.split())
            numberOfLines = content.count(b'\n')
            char_count = len(content.decode('utf-8'))
            print(f"{byte_count : 8} {number_of_words : 8} {numberOfLines : 8} {char_count : 8}")
        if count_bytes:
            byte_count = len(content)
            print(f"{byte_count} {filename}")
        if count_words:
            number_of_words = 0
            lines = content.split()
            for word in lines:
                if not word.isdigit() :
                    number_of_words += 1
            print("The number of words is:", number_of_words)
        if count_lines:
            
            numberOfLines = content.count(b'\n')
            print("The number of lines in the file is: ", numberOfLines)
        if count_characters:
            totalCharacters = len(content.decode('utf-8'))
            print("The number of characters in the file is: ", totalCharacters)
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ccwc - Count bytes in a file")
    parser.add_argument('-c', action='store_true', help="cCount bytes in a file")
    parser.add_argument('-l', action = 'store_true', help="Get number of lines in a file")
    parser.add_argument('-w', action='store_true', help="Get the number of words in a file")
    parser.add_argument('-m', action='store_true', help=" Get number of characters in a file")
    parser.add_argument('filename', nargs = '?', type=str, default='', help="Name of the file")
    
    args = parser.parse_args()
    
    if not args.c and not args.l and not args.w and not args.m:
        ccwc(args.filename, args.c, args.l, args.w, args.m)
    else:
        ccwc(args.filename, args.c, args.l, args.w, args.m)