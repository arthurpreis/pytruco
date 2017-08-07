def parse_player_input():
        s = input()
        valid_inputs = ['1', '2', '3', 't', 'y', 'n', 'f', 'T', 'Y', 'N', 'F']
        if s in valid_inputs:
            print('valid input')
        else:
            print('invalid input')

while True:
    parse_player_input()
