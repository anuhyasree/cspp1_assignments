'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def print_dictionary(dictionary):
    """function"""
    keys = list(dictionary.keys())
    keys.sort()
    for key in keys:
        print(key,"-",dictionary[key])

def sub(temp):
    string_val = " "
    for _ in range(temp):
        string_val = string_val + "#"
    return string_val
def frequency_graph(dictionary):
    for keys in dictionary:
        temp = dictionary[keys]
        dictionary[keys] = sub(temp)
    print_dictionary(dictionary)

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
