# anon-discourse   

A webapp which hosts anonymous chat groups.

## Setup

- prerequisit of docker and docker-compose installed
- clone locally
- run `make run`
- browse to [localhost:5000](http://localhost:5000) or [your ip]:5000

## Todo


### mvp functionality
- [x] Host and route to shared channels
- [x] Devise persisted data structure for chat, send chat to new entrees
- [x] Format chat-box-like

### housekeeping
- [x] Linter! 
- [ ] Tests!
- [ ] Improved logging
- [ ] Get rid of page() function and use templates for 404 and error handling

### larger efforts
- [x] Leverage "prod ready" server, like nginx, gunicorn, etc
- [ ] Identify approach for including SSL cert 
- [ ] Integrate crypto, perhaps include "password" to encrypt/decrypt chat contents
- [ ] Improve configurations by leveraging .env file and python dotenv library
- [ ] Introduce testing library, refactor code to be more testable (DI, IoC, etc)

