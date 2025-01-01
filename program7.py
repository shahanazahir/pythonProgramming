def length(words):
  return max(len(word)for word in words)
word_list=input("enter a list at words separated by spaces:").split()
print("length of the largest word:",length(word_list))