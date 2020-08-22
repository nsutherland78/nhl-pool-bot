#!/usr/bin/python3
'''
This program was written to make random selections in the NHL playoff pool.
'''
import yaml
import random
#  ArgumentParser passes variables directly into the app
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(
        description='Auto generates hockey picks based on data provided.'
    )
    parser.add_argument(
        'datafile',
        type=str,
        help='Tells program which data file to generate the picks from.'
    )
    parser.add_argument(
        'picksfile',
        type=str,
        help='Tells program which file to output the picks from.'
    )
    parser.add_argument(
        '-p',
        '--picktype',
        type=int,
        choices=[1, 2, 3, 4],
        help='Selects which type of pick to perform, 1st to 4th round, and Stanley Cup Winner, if not specified, it will pick all.'
    )
    return parser.parse_args()


ARGS = create_parser()


def importdata(datafile):
    print("Importing data from yaml file provided...")
    with open('{}'.format(datafile), 'r') as df:
        data = yaml.load(df, Loader=yaml.FullLoader)
    print("Import complete.")
    return data


def make_picks(data, picktype):
    print("Making random pick selections...")
    if picktype == 1:
        # CREATE PICKS STRUCTURE
        picks = {'firstround':{'east':{'match1':'','match2':'','match3':'', 'match4':''},'west':{'match1':'','match2':'','match3':'', 'match4':''}}, 'stanleycupwinner':''}
        # EASTERN CONFERENCE PICKS
        picks['firstround']['east']['match1'] = random.choice(data['firstround']['east']['match1']) + ' ' + str(random.randint(4, 7))
        picks['firstround']['east']['match2'] = random.choice(data['firstround']['east']['match2']) + ' ' + str(random.randint(4, 7))
        picks['firstround']['east']['match3'] = random.choice(data['firstround']['east']['match3']) + ' ' + str(random.randint(4, 7))
        picks['firstround']['east']['match4'] = random.choice(data['firstround']['east']['match4']) + ' ' + str(random.randint(4, 7))
        # WESTERN CONFERENCE PICK
        picks['firstround']['west']['match1'] = random.choice(data['firstround']['west']['match1']) + ' ' + str(random.randint(4, 7))
        picks['firstround']['west']['match2'] = random.choice(data['firstround']['west']['match2']) + ' ' + str(random.randint(4, 7))
        picks['firstround']['west']['match3'] = random.choice(data['firstround']['west']['match3']) + ' ' + str(random.randint(4, 7))
        picks['firstround']['west']['match4'] = random.choice(data['firstround']['west']['match4']) + ' ' + str(random.randint(4, 7))
        sclist = []
        for pick in picks['firstround']['east']:
            sclist.append(picks['firstround']['east']['{}'.format(pick)])
        for pick in picks['firstround']['west']:
            sclist.append(picks['firstround']['west']['{}'.format(pick)])
        scoutput = random.choice(sclist)
        scwinner = scoutput.split(' ')
        picks['stanleycupwinner'] = scwinner[0]
    elif picktype == 2:
        # CREATE PICKS STRUCTURE
        picks = {'secondround':{'east':{'match1':'','match2':''},'west':{'match1':'','match2':''}}}
        # EASTERN CONFERENCE PICKS
        picks['secondround']['east']['match1'] = random.choice(data['secondround']['east']['match1']) + ' ' + str(random.randint(4, 7))
        picks['secondround']['east']['match2'] = random.choice(data['secondround']['east']['match2']) + ' ' + str(random.randint(4, 7))
        # WESTERN CONFERENCE PICKS
        picks['secondround']['west']['match1'] = random.choice(data['secondround']['west']['match1']) + ' ' + str(random.randint(4, 7))
        picks['secondround']['west']['match2'] = random.choice(data['secondround']['west']['match2']) + ' ' + str(random.randint(4, 7)) 
    elif picktype == 3:
        # CREATE PICKS STRUCTURE
        picks = {'thirdround':{'east':{'match1':''},'west':{'match1':''}}}
        # EASTERN CONFERENCE PICKS
        picks['thirdround']['east']['match1'] = random.choice(data['thirdround']['east']['match1']) + ' ' + str(random.randint(4, 7))
        # WESTERN CONFERENCE PICKS
        picks['thirdround']['west']['match1'] = random.choice(data['thirdround']['west']['match1']) + ' ' + str(random.randint(4, 7))
    elif picktype == 4:
        # CREATE PICKS STRUCTURE
        picks = {'fourthround':''}
        # FINAL PICK
        picks['fourthround'] = random.choice(data['fourthround']) + ' ' + str(random.randint(4, 7))
    else:
        print("No legitimate picktype was provided.  How did you get here?")
    return picks


def exportdata(picks, picksfile):
    print("Beginning export of data to picks.yaml...")
    with open('{}'.format(picksfile), 'w') as pf:
        yaml.dump(picks, pf)
    print("Export to {} file complete.".format(picksfile))


def main():
    datafile = ARGS.datafile
    picksfile = ARGS.picksfile
    picktype = ARGS.picktype
    data = importdata(datafile)
    picks = make_picks(data, picktype)
    exportdata(picks, picksfile)


if __name__ == '__main__':
    main()
