import urllib.request
import ssl

def main():



    with open('Output.txt', 'r') as reader:
        # Read and print the entire file line by line
        line = reader.readline()
        if line == 'quit':  
            print(line, end='')
            line = reader.readline()






if __name__ == '__main__':
    main()

