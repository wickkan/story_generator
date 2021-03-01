"""
This is a story generator made in Python
"""

from random import choice

def story_gen():
    who = ['Peter Rabbit', 'Johnny Depp', 'Mickey Mouse', 'Hannah Montana']
    what = ['was eating a cake', 'flew to Paris', 'turned up to school late', 'crashed his car']
    when = ['last night', 'yesterday', 'a few days ago', 'just then']
    action = ['but unknowingly left their wallet at home.', 'but instantly regretted it.', 'and also flew to Berlin.', 'and unfortunately missed their dentist appointment.']
    return print(choice(who) + ' ' + choice(what) + ' ' + choice(when) + ' ' + choice(action))

def print_story():
    print('---------------------------')
    story_gen()
    print('---------------------------')

if __name__ == '__main__':
    print_story()
