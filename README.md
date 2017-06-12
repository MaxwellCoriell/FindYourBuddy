# Find Your Buddy

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A lost pet utility where users can post about lost and found pets in their area. Currently, only the Greater Nashville Area will be available.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)   
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## About
Hey, y'all, this website is not only the cummulation of what I have learned at [Nashville Software School](https://github.com/nashville-software-school), but also a long-term project that's eventually going to be a live mobile app (hpefully on one or more app stores).

As I was beginning the brainstorming phase of what I wanted to do for my backend capstone, one of my friends called me and asked for my help in finding her dog that had gotten out of her fenced-in backyard. She said she had posted on multiple platforms to help with the cause, but it did not seem fruitful.

I then did some research (I googled) and found that there really aren't many good resources for helping owners find their lost pets. Thus, Find Your Buddy was born.

As the owner of an escape artist cat, I am well aware of the stress and anxiety that comes from losing your best friend, and Find Your Buddy(FYB) is designed to help with that.

In it's infancy, FYB will be a basic CRUD posting app where users can post about their lost pet, or about a pet they have found that the owner may not know is lost yet. Over time, new features will expand the project to include notifications and other cool things.
Follow our progress on [Twitter]()



### Prerequisites
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django:
```
pip install django
```


## Installation

This will be hosted, but if you want to have it local, (to play around with or work on, or whatever) do this stuff:

```
git clone https://github.com/maxwellcoriell/BackendCapstone.git
cd BackEndCapstone
```
Setting up the database:

```
python migrate_backend.sh
```
Run project in browser:

```
python manage.py runserver
```



## Usage
[UNDER CONSTRUCTION]


## Contribute
1. Fork it!
2. Create your feature branch:
```git checkout -b <YourInititals-WhatNewFeatureDoes>```
3. Commit your changes:
```git commit -m 'Add some feature, or whatever'```
4. Push to the branch:
```git push origin <YourInititals-WhatNewFeatureDoes>```
5. Submit a pull request :D

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Credits

Build Contributors:
  * [Max Baldridge](https://github.com/MaxwellCoriell)

## License
[MIT © 2017 Max Baldridge](./LICENSE)