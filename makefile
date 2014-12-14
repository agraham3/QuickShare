push: fresh pull add commit
	git push
add:
	git add . -A
commit:
	git commit
pull:
	git pull
fresh:
	find -name '*~' -exec rm '{}' \;
