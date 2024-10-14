def main():

  import pyfiglet

  text="Cipher"
  welcome=pyfiglet.figlet_format(text,font='graffiti')
  print(welcome)
  while True:
    from EncodeDecode import encoder1,decoder1
    option = input('Encode or Decode (E/D/Exit): ').lower()

    if option == 'e':
      user_input = input('Enter Input: ')
      shift = int(input('Enter shift: '))
      shift= shift%26
      name = encoder1(user_input, shift)
      print(name)
      continue
    elif option == 'd':
      user_input = input('Enter Input: ')
      shift = int(input('Enter shift: '))
      shift= shift%26
      decoded = decoder1(user_input, shift)
      print(decoded)
      continue
    else:
      print('Good Bye')
      break

main()

