# MSHack-Hackathon-Management-Platform
Hackathon Management Platform



## Topic
IncubateIND needs to build a Campus Ambassador Program for our representatives in colleges/ institutes across India so we can build the robots ecosystem.

## Proposed Features
1. Amabassador Task Tracking System
	1. Application forms with location from Map-my-India api
	2. Assign tasks or goals to ambassadors
	3. Track the progress of the assign tasks
2. Discussion Channels
	1. To discuss about topics and form groups
3. Chat
	1. To get help in ongoing hackathons
4. Admin panel
	1. Stats
	2. Hackathon page generator


## Quick Start
1. `python3 -m venv kratos`
2. `source kratos/bin/activate`
3. `pip install -r requirements.txt`
4. `cd src && ./kratos/settings/local.sample.env`
5. `python manage.py migrate`
6. `sudo python manage.py runserver 0.0.0.0:80`