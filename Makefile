start:
	@docker-compose up -d --build --remove-orphans
	#@python3 server/manage.py runserver 0.0.0.0:8000
stop:
	@docker-compose down -v
logs:
	@docker-compose logs --tail=100 -f

make spiderrun:


# Shell colors.
RED=\033[0;31m
LIGHT_RED=\033[1;31m
GREEN=\033[0;32m
LIGHT_GREEN=\033[1;32m
ORANGE=\033[0;33m
YELLOW=\033[1;33m
BLUE=\033[0;34m
LIGHT_BLUE=\033[1;34m
PURPLE=\033[0;35m
LIGHT_PURPLE=\033[1;35m
CYAN=\033[0;36m
LIGHT_CYAN=\033[1;36m
NC=\033[0m
