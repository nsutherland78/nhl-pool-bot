# nhl-pool-bot
Performs random selections in NHL playoff pools.

## Requirements

You will need a functioning install of python 3, as well as pyyaml.

## Install

Simply clone the repo to your preferred directory:

```
https://github.com/nsutherland78/nhl-pool-bot.git
```

## Usage

To use the nhl-pool-bot, you must first update the data.yaml file. Then run the tool.

You can look at the syntax the tool is expecting by using the help argument "-h".

```
⇒  ./nhl-pool-bot.py -h
usage: nhl-pool-bot.py [-h] [-p {1,2,3,4}] datafile picksfile

Auto generates hockey picks based on data provided.

positional arguments:
  datafile              Tells program which data file to generate the picks from.
  picksfile             Tells program which file to output the picks from.

optional arguments:
  -h, --help            show this help message and exit
  -p {1,2,3,4}, --picktype {1,2,3,4}
                        Selects which type of pick to perform, 1st to 4th round, and Stanley Cup Winner, if not specified, it will pick all.
```

For first round picks + stanley cup winner choice:
```
./nhl-pool-bot.py data/playoffs-data-2020.yaml picks/playoffs-firstround-2020.yaml -p 1
```

For second round picks:
```
./nhl-pool-bot.py data/playoffs-data-2020.yaml picks/playoffs-secondround-2020.yaml -p 2
```

For third round picks:
```
./nhl-pool-bot.py data/playoffs-data-2020.yaml picks/playoffs-secondround-2020.yaml -p 3
```

For fourth and final round picks:
```
./nhl-pool-bot.py data/playoffs-data-2020.yaml picks/playoffs-secondround-2020.yaml -p 4
```

## Contributors
Nathan Sutherland (nathan.sutherland@gmail.com)