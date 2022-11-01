import eel

eel.init('web', allowed_extensions=['.*'])

eel.start('templates/index.html', port=0, jinja_templates='templates', size=(1200, 800))