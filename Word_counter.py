file = open("text.txt", encoding = "latin-1")
list_words = file.read().split()
word_counts = {}

for word in list_words:
    if word in word_counts.keys():
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

file.close()

def top10(L):
    L_ordered = sorted(L, reverse = True)
    return L_ordered[:10]

file = open("PnP.txt", encoding = "latin-1")
list_words = file.read().split()
freq = {}

for word in list_words:
    if word in freq.keys():
        freq[word] += 1
    else:
        freq[word] = 1

inv_freq = {}
for key in freq.keys():
    if freq[key] in inv_freq.keys():
        inv_freq[freq[key]].append(key)
    else:
        inv_freq[freq[key]] = [key]

# Alternate version:
sorted_inv_freq = sorted(inv_freq.keys())
top10_words_count = sorted_inv_freq[-1 : -11 : -1]
top10_words_freq = {}
for count in top10_words_count:
    top10_words_freq[count] = inv_freq[count]
print(top10_words_freq)

file.close()
