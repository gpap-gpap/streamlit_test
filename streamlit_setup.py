mantis_dark_theme = {
'background_dark'       : '#333333',
'background_light'      : '#777777', 
'highlight'             : '#ff8000',
'text'                  : '#d9d9d9',
'mantis_green'          : '#005500',
'mantis_light_green'    : '#00aa00',
'mantis_white'          : '#aabbee',
}

# set up colors for menu

# set up streamlit theme
file = open("./config.toml", "r+")
file.seek(0)
file.truncate()
file.write('[theme]') 
file.write('\n primaryColor = "' + mantis_dark_theme['highlight']+'"')
file.write('\n backgroundColor = "' + mantis_dark_theme['background_dark']+'"') 
file.write('\n secondaryBackgroundColor = "' + mantis_dark_theme['background_light']+'"') 
file.write('\n textColor = "' + mantis_dark_theme['text']+'"') 
file.write('\n font = "sans serif"') 
file.close() 

def remove_1_char(str):
    return str[1:]
# set up colors for matplotlib
file = open("./test.mplstyle", "r+")
file.seek(0)
file.truncate()
file.write('\n #-----colours-----')
file.write('\naxes.facecolor : ' + remove_1_char(mantis_dark_theme['background_light']))
file.write('\naxes.edgecolor : ' + remove_1_char(mantis_dark_theme['text']))
file.write('\nxtick.color : ' + remove_1_char(mantis_dark_theme['text']))
file.write('\nytick.color : ' + remove_1_char(mantis_dark_theme['text']))
file.write('\nfigure.facecolor : ' + remove_1_char(mantis_dark_theme['background_dark']))
file.write('\nfigure.edgecolor : ' + remove_1_char(mantis_dark_theme['background_dark']))
file.write('\nsavefig.facecolor : ' + remove_1_char(mantis_dark_theme['background_dark']))
file.write('\nsavefig.edgecolor : ' + remove_1_char(mantis_dark_theme['background_dark']))
file.write('\ntext.color : ' + remove_1_char(mantis_dark_theme['background_light']))
file.write('\npatch.edgecolor : ' + remove_1_char(mantis_dark_theme['mantis_light_green']))
file.write('\nfont.family: sans serif \nfont.weight: bold\nfont.size: 12')
file.write("\naxes.prop_cycle: \
    cycler(color = ['d7191c', 'fdae61', 'ffffbf', 'a6d96a', '1a9641']) \
        # ['a50026','d73027','f46d43','fdae61','fee08b','d9ef8b','a6d96a','66bd63','1a9850','006837'])\
        # + cycler(linestyle=['-', '--', ':', '-.','-', '--', ':', '-.','-', '--'])\
        # + cycler(lw=[1, 2, 2, 2, 1, 2, 2, 2, 1, 2]\
        )")
file.write('\n\n#-----geometry-----')
# file.write('\naxes.set_anchor : (0.,0.)')
file.close() 
