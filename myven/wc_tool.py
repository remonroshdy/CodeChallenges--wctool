
import sys
import argparse
import optparse
def read_file(file_path= None):
    if file_path:
        # Try to open and read the file specified by file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
    else:
        # Read from standard input if no file path is provided
        return sys.stdin.read()
    





def count_lines(content):
    num_lines = content.splitlines()
    #num_lines = content.split('\n')
    return len(num_lines)


def count_words(content):
    # Split the content into words based on whitespace
    words = content.split()
    return len(words)

def count_characters(content):
    # Count the number of characters in the content
    return len(content)

def count_byte(content):
    num_bytes = len(content.encode('utf-8'))
    return num_bytes

def main():
    # Set up argument parsing object 
    parser = argparse.ArgumentParser(description="Count lines, words, and characters in a file.")
    
    
# added Mutually  exclusive group and kept it here for learning but later i removed it... 
    # optional argument are defined by  having - , -- and the flag  action= 'store_true'
    # Define mutually exclusive group for options, as i only allow one argument a time , short command 1 dash -l 
    # 2 dashes infront of a word full command  --lines ,   action = 'store_true'  to create a flag = true  
    """
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--lines', action='store_true', help="Count the number of lines")
    group.add_argument('-w', '--words', action='store_true', help="Count the number of words")
    group.add_argument('-m', '--characters', action='store_true', help="Count the number of characters")
    group.add_argument('-c','--bytes',action='store_true', help='count number of bytes ')
    """

    parser.add_argument('-l', '--lines', action='store_true', help="Count the number of lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count the number of words")
    parser.add_argument('-m', '--characters', action='store_true', help="Count the number of characters")
    parser.add_argument('-c', '--bytes', action='store_true', help="Count the number of bytes")


    # add positional argument  the file to the object are defined without dashes and no flags , 
    # postion argument is the last command when parsed since i .add_argument('file ', ... ) is the last line here added to object 
     # Defined without dashes, identified by its position, and is required.
    parser.add_argument('file', nargs='?', type=str, help="Path to the file to analyze")
    
    # parse The parse_args() method reads the command-line arguments, 
    # matches them against the arguments defined in the ArgumentParser object which is obj attribute
    # and stores the results.

    args = parser.parse_args()

    file_path = args.file
    file_content = read_file(file_path)
    
    if file_content is not None:
        if args.lines:
            num_lines = count_lines(file_content)
            print(f"Number of lines: {num_lines}")
        if args.words:
            num_words = count_words(file_content)
            print(f"Number of words: {num_words}")
        if args.characters:
            num_characters = count_characters(file_content)
            print(f"Number of characters: {num_characters}")

        if args.bytes:
            num_bytes = count_byte(file_content)
            print(f"Number of Bytes:",{num_bytes})

        if not (args.lines or args.words or args.characters or args.bytes):
            # Default case: count lines, words, and characters
            num_bytes = count_byte(file_content)
            num_lines = count_lines(file_content)
            num_words = count_words(file_content)
            print(f"Number of Bytes: {num_bytes}")
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")

if __name__ == "__main__":
    main()