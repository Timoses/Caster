
CV_PKGS=castervoice casterplugin

lint:
	flake8 $(CV_PKGS)
	pylint --rcfile=setup.cfg $(CV_PKGS)
