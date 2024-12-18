def words(_content):
    return (_content.split())

def character_count(_content):
    _content_lowered = _content.lower()
    _content_char_count = {}
    
    for char in _content_lowered:
        if char not in _content_char_count: 
            _content_char_count[char] = 0
        _content_char_count[char] = _content_char_count[char] + 1

    return _content_char_count

def convert_dict_to_list_of_dicts(_dict):
    _return_list = []
    for key,value in _dict.items():
        _return_list.append({'name': key,  'count': value})

    return _return_list

def sort_on(_dict):
    return _dict['count']


def print_character_count_report(_char_counts):
    _char_counts.sort(reverse=True, key=sort_on)
    
    for char in _char_counts:
        name = char['name']
        count = char['count']
        if  char['name'].isalpha():
            print(f"The '{name}' character was found {count} times")



if __name__ == '__main__':
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()

    assert file_contents is not None, "Could not load the book"

    w = words(file_contents)
    print(len(w))

    c = character_count(file_contents)

    l = convert_dict_to_list_of_dicts(c)

    print_character_count_report(l)
