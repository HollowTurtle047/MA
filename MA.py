
import zmq, sys

CARDS = ['1','2','3','4','5','6','7','8','9','B']

def main():
    welcome()
    selectSC()
    
def selectSC():
    strIn = valid_input(['0','1','Q'], '0-Server 1-Client Q-Quit:')
    if strIn == '0':
        # server
        print('server')
        server()
    elif strIn == '1':
        # client
        print('client')
        client()
    elif strIn == 'Q':
        print('Quit')

def server():
    context = zmq.Context(1)
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    cards = CARDS
    score = 0
    
    while True:
        if not cards:
            break
        
        myCard = valid_input(cards,\
            '\r\ncards:\r\n[' + '] ['.join(cards) + ']')
        cards.remove(myCard) # use the card
        print('Wating opponent')
        oppoCard = socket.recv_string() # wating message
        score = compare(myCard, oppoCard, score)
        socket.send_string(myCard) # send my card
        
    oppoScore = socket.recv_string()
    socket.send_string(str(score))
    compare_score(score, int(oppoScore))

def client():
    context = zmq.Context(2)
    socket = context.socket(zmq.REQ)
    address = input('Please input server IP address:\r\n')
    socket.connect('tcp://' + address + ':5555')
    cards = CARDS
    score = 0
    
    while True:
        if not cards:
            break
        
        myCard = valid_input(cards, \
            '\r\ncards:\r\n[' + '] ['.join(cards) + ']')
        cards.remove(myCard)  # use the card
        socket.send_string(myCard)
        print('Wating opponent')
        oppoCard = socket.recv_string() # wating message
        score = compare(myCard, oppoCard, score)
        
    socket.send_string(str(score))
    oppoScore = socket.recv_string()
    compare_score(score, int(oppoScore))
    
def valid_input(valid_list, mesg):
    # TODO flush buffer
    while True:
        inputStr = input(mesg + '\r\n').upper()
        if inputStr in valid_list:
            return inputStr
        print('Invalid input')
        
def compare(card, oppoCard, score):
    if card == oppoCard:
        score += 1
        string = 'same'
    elif oppoCard == 'B':
        score += 1
        string = 'your hourse is boomshagalaga'
    elif card == 'B':
        score += 1
        string = 'you exploded the hourse'
    elif card < oppoCard:
        string = 'loss'
    elif card > oppoCard:
        score += 2
        string = 'win'
    else:
        exit()
    print('{} vs {}, {}, your score: {}'.format(card, oppoCard, string, score))
    return score

def compare_score(score, oppoScore):
    print('Your score is {}, your opponent score is {}. '.format(score, oppoScore), end='')
    if score == oppoScore:
        print('Draw!')
    elif score < oppoScore:
        print('You loss!')
    elif score > oppoScore:
        print('Congratulation, you win!')
    print('Thank you for playing the game!')

def welcome():
    print('='*30)
    print('-'*30)
    print(r'''Welcome to Zha MA! (\_/) 
                 ,((((^`\
                ((((  (6 \ 
              ,((((( ,    \
            ,(((((  /"._  ,`,
           ,((((   /    `-.-' ''')
    print('='*30)
    
if __name__ == '__main__':
    main()


