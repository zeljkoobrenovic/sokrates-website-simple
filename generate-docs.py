import json
import datetime

data = json.load(open('data/projects.json'))
date_string = datetime.date.today().strftime('%Y-%m-%d')

with open('docs/index.html', 'w') as html_file:
    template = open('templates/index.html').read()
    html_file.write(template
                    .replace('${import style.css}', open('templates/fragments/style.css').read())
                    .replace('${import home.html}', open('templates/fragments/home.html').read())
                    .replace('${import examples.html}', open('templates/fragments/examples.html').read())
                    .replace('${import install.html}', open('templates/fragments/install.html').read())
                    .replace('${import articles.html}', open('templates/fragments/articles.html').read())
                    .replace('${import config.html}', open('templates/fragments/config.html').read())
                    .replace('${import features.html}', open('templates/fragments/features.html').read())
                    .replace('${data}', json.dumps(data)))

