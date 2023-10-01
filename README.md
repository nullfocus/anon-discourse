# anon-discourse

A wholly-independent webapp which allows a group to spin up an anonymous chat group and invite others.

## Todo

### immediate functionality
[ ] Host and route to shared channels
[ ] Devise persisted data structure for chat, send chat to new entrees

### housekeeping
[ ] Get rid of page() function and use templates

### larger efforts
[x] Leverage "prod ready" server, like nginx, gunicorn, etc
[ ] Integrate crypto, perhaps include "password" to encrypt/decrypt chat contents
[ ] Improve configurations by leveraging .env file and python dotenv library
[ ] Introduce testing library, refactor code to be more testable (DI, IoC, etc)
[ ] Extensive logging