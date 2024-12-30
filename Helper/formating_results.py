def format_home_results(home_results):
    names = []
    animeid = []
    epnum = []
    for i in home_results:
        names.append(i.get('name'))
        animeidep = (i.get('Id-Epnum'))
        animeidep = animeidep.split('-')
        ids = animeidep[:-2]
        animeid.append('-'.join(ids))
        epnum.append(animeidep[-1])
    return (names, animeid, epnum)

def format_download_results(download_results):
    qualitys = list(download_results)
    links = []
    for i in qualitys:
        links.append(download_results.get(i))
    result = ''
    for i in range(len(links)):
        result = f'{result}[{qualitys[i]}]({links[i]})\n'

    return result

def manga_chapter_html(name, list_of_links):
    x = '''<div class="who_cares" style="background-color:black">'''
    for i in list_of_links:
        x = f'''{x}
    <div class="pages">
      <img src="{i}" style="width:100%"><br>
      <br>
    </div>
        '''
    with open(f"{name}.html", "w") as f:
        f.write(x)
