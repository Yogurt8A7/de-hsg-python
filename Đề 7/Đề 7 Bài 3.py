S = input("Nhập xâu S: ")
longest_words = []
word_count = 0
for word in S.split():
    word_count+=1
len_word = max(S.split(), key = len)
longest_words.append(len_word)
for w in S.split(): longest_words.append(w) if len(w) == len(len_word) and w not in longest_words else None
ch_ct = 0
for char in len_word: ch_ct +=1
print("Xâu có",word_count,"từ")
print(f"Từ dài nhất có {ch_ct} kí tự")
print("Các từ dài nhất là:", " ".join(longest_words))