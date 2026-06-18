def process_tfile():
    with open(input('File name to open: '), 'r') as fp:
        text = fp.read()
        
        if len(text.strip()) == 0:
            raise ValueError('Empty file')

        all_words = text.split()
        print(f"Total words: {len(all_words)}")

        # print all words that have a length of at least 3 chars
        for word in all_words:
            if len(word) >= 3:
                print(word)



