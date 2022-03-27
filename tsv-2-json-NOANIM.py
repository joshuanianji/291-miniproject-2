import json
import time

def starting_text():
    '''
    fancy starting text
    '''
    texts = [
        ' ::::::::   ::::::::    :::        ::::    ::::  :::::::::   ::::::::  ',
        ':+:    :+: :+:    :+: :+:+:        +:+:+: :+:+:+ :+:    :+: :+:    :+: ',
        '      +:+  +:+    +:+   +:+        +:+ +:+:+ +:+ +:+    +:+       +:+  ',
        '    +#+     +#++:++#+   +#+        +#+  +:+  +#+ +#++:++#+      +#+    ',
        '  +#+             +#+   +#+        +#+       +#+ +#+          +#+      ',
        ' #+#       #+#    #+#   #+#        #+#       #+# #+#         #+#       ',
        '##########  ########  #######      ###       ### ###        ########## '
    ]

    for text in texts:
            print(text)
    
    time.sleep(0.075) 
    print('Welcome to TSV2JSON!')

    time.sleep(0.075) 
    print('Made by ' + 'Vedant' + ', ' + 'Kailash' + ' and ' + 'Joshua' + '.')

    # Boot screen

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0        

    # pointer for travelling the loading string
    i = 0

    print('\n')
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.025) 
        print ("\033[A                             \033[A")
        print('Booting up...' + animation[anicount])
        anicount = (anicount + 1) % 4
        counttime = counttime + 1



def tsv2json(input_file,output_file):

    print('\n' + 'Converting ' + input_file + ' to ' + output_file + '...' )

    arr = []
    file = open(input_file, 'r')
    a = file.readline()

    # The first line consist of headings of the record 
    # so we will store it in an array and move to 
    # next line in input_file.
    titles = [t.strip() for t in a.split('\t')]

    # find length of file
    pos = file.tell()
    file_length = len(file.readlines())
    file.seek(pos)

    for line in file:
        d = {}
        for t, f in zip(titles, line.split('\t')):

            # Convert each row into dictionary with keys as titles
            NestTitles = ['primaryProfession', 'knownForTitles', 'genres', 'characters']
            if t in NestTitles:
                if t == 'primaryProfession' or t == 'knownForTitles' or t == 'genres':
                    #temp = f.strip().split('\n')[0].split(',')
                    temp = f.strip(' \n').split(',')
                if t == 'characters':
                   # temp = f.strip().split('\n')[0].strip(' "[]').split(',')
                    temp = f.strip('\n "[]').split(',')
                if temp[0] == '\\N':
                    temp = None
                d[t] = temp

            else:
                temp = f.strip()
                if temp == '\\N':
                    temp = None
                d[t] = temp

        # we will use strip to remove '\n'.
        arr.append(d)

    # we will append all the individual dictionaires into list 
    # and dump into file.

    print('Writing data to ' + output_file + '...')
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(json.dumps(arr, indent=4))
    print('Done!')

def main():
    starting_text()
    #saving the names of the files to be converted in list 
    fileNames = ['name.basics', 'title.basics', 'title.ratings', 'title.principals']
    for name in fileNames:
        input_filename = name + '.tsv'
        output_filename = name + '.json'
        tsv2json(input_filename,output_filename)



#calling the function

if __name__ == '__main__':
    main()