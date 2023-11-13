from MiniCParser import parser

def read_input() :
  result = ''

  while True :
    data = input('Mini-C> ').strip()

    if data :      
      result += data + ' '
    else :
      break
      
  return result.strip()

# Main

while True :
  data = read_input()

  if data == 'exit;' :
    break

  if not data :
    continue

  try :
    tree = parser.parse(data)

  except Exception as e :
    print(e.args[0])
    continue

  print(tree)