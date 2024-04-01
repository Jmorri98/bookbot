def main():
    book_pathway = "books/frankenstein.txt"
    text = get_book_text(book_pathway)
    word_count = len(get_book_text(book_pathway).split())
    character_count = convert_to_list(book_character_count(book_pathway))
    character_count.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_pathway} --- \n{word_count} words found in the document")
    for x in character_count:
        print(f"The character '{x["letter"]}' was found {x["count"]} times")
    

    

def get_book_text(pathway):
    with open(pathway) as f:
        return f.read()

def book_word_count(pathway):
    book_list = get_book_text(pathway).split()
    return len(book_list)

def book_character_count(pathway):
    letter_dictionary ={
        'a':0,'b':0,'c':0,'d':0,'e':0,
        'f':0,'g':0,'h':0,'i':0,'j':0,
        'k':0,'l':0,'m':0,'n':0,'o':0,
        'p':0,'q':0,'r':0,'s':0,'t':0,
        'u':0,'v':0,'w':0,'x':0,'y':0,
        'z':0,
    }
    book_string = get_book_text(pathway).lower()
    for x in book_string:
        if x.isalpha():
            letter_dictionary[x] += 1
    return letter_dictionary

def sort_on(dict):
    return dict["count"]

def convert_to_list(dict):
    new_list = []
    for x in dict:
        new_list.append({"letter":x, "count": dict[x]})
    return new_list


main()