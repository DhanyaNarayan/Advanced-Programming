
import sys

def word_count_dict(filename):

  word_count = {} 
  input_file = open(filename, encoding='utf-8')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  
  return word_count


def print_words(filename):
  
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print(word, word_count[word])


def get_count(word_count_tuple):
  
  return word_count_tuple[1]


def print_top(filename):
  
  word_count = word_count_dict(filename)

  
  items = sorted(word_count.items(), key=get_count, reverse=True)

  
  for item in items[:20]:
    print(item[0], item[1])


def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
