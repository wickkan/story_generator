"""
This is a story generator made in Python
"""

from random import choice

url = 'https://github.com/wickkan'

def story_gen():
    who = ['Peter Rabbit', 'Johnny Depp', 'Mickey Mouse', 'Hannah Montana']
    what = ['was eating a cake', 'flew to Paris', 'turned up to school late', 'crashed his car']
    when = ['last night', 'yesterday', 'a few days ago', 'just then']
    action = ['but unknowingly left their wallet at home.', 'but instantly regretted it.', 'and also flew to Berlin.', 'and unfortunately missed their dentist appointment.']
    return print('\033[93m' + choice(who) + ' ' + choice(what) + ' ' + choice(when) + ' ' + choice(action) + '\033[0m')

def print_story():
    print('----------------------------------------------------')
    story_gen()
    print(
        '*****------------------------------------------*****\n''Thanks for trying: Story Generator\n''Click the link to check out more of my projects:\n',
        url)
    print('*****------------------------------------------*****')

if __name__ == '__main__':
    print_story()
