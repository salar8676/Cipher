alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encoder1(user_input , shift):

  encoder = ''

  for i in user_input:
    index = alpha.index(i)
    new_index = index + shift
    encoder = encoder + alpha[new_index]

  return encoder

def decoder1(encoder, shift):

  decoder = ''

  for i in encoder:
    index = alpha.index(i)
    new_index = index - shift
    decoder = decoder + alpha[new_index]

  print(decoder) 