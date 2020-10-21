[![Documentation Status](https://readthedocs.org/projects/pypuregym/badge/?version=latest)](https://pypuregym.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.com/j-muller/pypuregym.svg?branch=master)](https://travis-ci.com/j-muller/pypuregym) [![codecov](https://codecov.io/gh/j-muller/pypuregym/branch/master/graph/badge.svg)](https://codecov.io/gh/j-muller/pypuregym)

pypuregym
=================

A Python library to interact with Pure Fitness/Pure Yoga APIs.
This library helps you to get the schedule of a Pure studio and book classes.
Currently, the following Pure locations are supported:

* Hong Kong
* Singapore
* Shanghai

## Installation

```
$ pip install pypuregym
```

## CLI usage

```
$ pypuregym --help
Interact with Pure Fitness/Yoga service.

Usage:
  pypuregym location <gym-type> <region-id>
  pypuregym schedule <region-id> <location-id> <date>
  pypuregym book <region-id> <class-id> <username> <password> [--wait-until <wait>] [--retry <retry>]

Options:
  <gym-type>                  Can be "fitness" or "yoga".
  <region-id>                 Can be "HK", "CN" or "SG".
  <location-id>               ID of the studio (given with the "location" command).
  <date>                      Date to get the schedule for.
  <class-id>                  Class ID to book.
  <username>                  Your Pure username/email.
  <password>                  Your Pure password.
  --wait-until <wait>         When booking a class, wait until the specified date time before booking.
  --retry <retry>             Number of time to retry when booking the class.
```

#### Get Pure locations

```
$ pypuregym location fitness hk
╒══════╤═════════════════╤══════════════════════════════╤══════════════╕
│   ID │ Code            │ Name                         │ District     │
╞══════╪═════════════════╪══════════════════════════════╪══════════════╡
│    4 │ LTP             │ Lee Theatre                  │ Causeway Bay │
├──────┼─────────────────┼──────────────────────────────┼──────────────┤
│    6 │ LPF             │ Langham Place                │ Mongkok      │
├──────┼─────────────────┼──────────────────────────────┼──────────────┤
│    8 │ KIN             │ Kinwick Centre               │ Central      │
╘══════╧═════════════════╧══════════════════════════════╧══════════════╛
```

#### Get Pure schedule

```
$ pypuregym schedule hk 4 2020-01-01
╒═══════╤═════════════════════╤═══════════╤══════════════╤════════════╕
│    ID │ Class Name          │ Teacher   │ Start Time   │ End Time   │
╞═══════╪═════════════════════╪═══════════╪══════════════╪════════════╡
│ 71647 │ BODYATTACK™         │ John D.   │ 10:00:00     │ 11:00:00   │
├───────┼─────────────────────┼───────────┼──────────────┼────────────┤
│ 71648 │ RPM™                │ John D.   │ 11:15:00     │ 12:05:00   │
├───────┼─────────────────────┼───────────┼──────────────┼────────────┤
│ 71649 │ BODYPUMP™           │ Jane F.   │ 11:15:00     │ 12:15:00   │
├───────┼─────────────────────┼───────────┼──────────────┼────────────┤
│ 71650 │ ABS, BUTTS & THIGHS │ Jane F.   │ 12:30:00     │ 13:30:00   │
╘═══════╧═════════════════════╧═══════════╧══════════════╧════════════╛
```

#### Book a class

```
$ pypuregym book hk 155188 $PURE_USERNAME $PURE_PASSWORD
```

## Documentation

You can read the documentation here.
This project has been tested under Python 3.6+