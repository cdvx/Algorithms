"""simple challenge"""

__author__ = 'cdvx'

def count_change(money,coins):
    ways = [1]+[0]*money

    for coin in coins:
        for i in range(coin, money+1):
            ways[i]+=ways[i-coin]
    return ways[money]

print(count_change(7,[1,2,3]))


mapper = {
  '-':'T', '--':'M', '---':'O', '--.':'G', '-.':'N', '-..': 'D', '-.-':'K','.':'E',
  '..':'I', '...':'S','..-':'U', '.-':'A', '.--':'W', '.-.':'R', '?':['E','T'], '?.':['I', 'N'], '.?':['I','A'], '?-?':['R', 'W', 'G', 'O'],'?-':['A', 'M'], '-?':['N','M'], '..?':['S', 'U'], '--?':['G', 'O'], '.-?':['R', 'W'], '-.?':['D', 'K'], '?.?':['D', 'K', 'S', 'U'], '.??':['S','U','R','W'], '-??':['D','K','G','O'], '?..':['S', 'D'],'?--':['W', 'O'], '?-.':['R','G'],'?.-':['U','K'], '??.':['S','R','D','G'],'??-':['U','W','K','O'], '.?.':['S','R'], '.?-':['U','W'], '-?.':['D','G'], '-?-':['K','O'],'??':['I','A','N','M'],
'???':['S', 'U', 'R', 'W', 'D', 'K', 'G', 'O']
}

def possibilities(word):
  letters = word.split()
  w = []

  for i in letters:
    
    x = mapper.get(i)
    if isinstance(x, list):
      w.extend(x)
    else:
      w.append(x)
  return w


