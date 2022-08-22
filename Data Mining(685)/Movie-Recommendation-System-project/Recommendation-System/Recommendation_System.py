import pandas as pd
import numpy as np
import math

movies = pd.read_csv('bollywood_full_1950-2019.csv')
movies = movies[['title_x','imdb_id','genres','imdb_rating','imdb_votes','summary','actors','year_of_release']]

actors = {}
for m in np.array(movies[['actors','title_x','imdb_rating','imdb_votes']]):
    cast = str(m[0])[:-1].split('|') if not (str(m[0]) == 'nan') else ['unnamed']
    title = m[1].split(' (')[0]
    try :
        rating = float(m[2]) if not (str(m[2]) == 'nan') else 0.0
    except:
        rating = 0.0    
    
    try :
        votes = int(m[3])
    except:
        votes = 0
        
    for person in cast:
        if person in actors:
            details = actors[person]    
            details[title.title()] = [rating,votes]
            details = dict(sorted(details.items(),key=lambda e:e[1][0]*math.log10(e[1][1]+1),reverse=True))
        else:
            details = {}
            details[title.title()] = [rating,votes]
        actors[person] = details
        
actors.pop('unnamed')
actors = dict(sorted(actors.items()))


genres = {}
for m in np.array(movies[['genres','title_x','imdb_rating','imdb_votes']]):
    gens = m[0].split('|')
    title = m[1].split(' (')[0]
    
    try :
        rating = float(m[2]) if not (str(m[2]) == 'nan') else 0.0
    except:
        rating = 0.0
    
    try :
        votes = int(m[3])
    except:
        votes = 0
        
    for gen in gens:
        if gen in genres:
            details = genres[gen]    
            details[title.title()] = [rating,votes]
            details = dict(sorted(details.items(),key=lambda e:e[1][0]*math.log10(e[1][1]+1),reverse=True))
        else:
            details = {}
            details[title.title()] = [rating,votes]
        genres[gen] = details
        
genres.pop('\\N')
genres = dict(sorted(genres.items()))


def getRecommendation(query):
    print('___________________________________________________________________','\n')
    if query.strip() == 'random':
        movie_r = np.array(movies['title_x'])
        for i in range(0,25):
            rand_num = np.random.randint(0,501)
            print(movie_r[rand_num])
    
    elif query.strip() == 'genres list':
        list_g = list(genres.keys())
        for g in list_g:
            print(g)
            
    elif query.strip() == 'actors list':
        list_a = list(actors.keys())
        strl = ''
        c = 0
        for a in list_a:
            c+=1
            strl += f'{a:24} '
            if (c%7) == 0:
                strl += '\n'
        print(strl)
    
    else:

        q_type = query.split(':')[0].strip()
        if q_type == 'genre':
            q_name = query.split(':')[1].strip().title()
            if(q_name in genres):
                movie_r = list(genres[q_name].keys())
                for i in range(0,min(25,len(movie_r))):
                    rand_num = np.random.randint(0,501)
                    if len(movie_r) < 501:
                        rand_num = i
                    print(movie_r[rand_num])
            else:
                print('Genre Not Found.Type Genres List in Query to know avilable Genres.')
            
        elif q_type == 'actor':
            q_name = query.split(':')[1].strip()
            if q_name.title() in actors:
                movie_r = list(actors[q_name.title()].keys())
                for i in range(0,min(25,len(movie_r))):
                    rand_num = np.random.randint(0,501)
                    if len(movie_r) < 501:
                        rand_num = i
                    print(movie_r[rand_num])   
            else:
                print('Actor Not Found.Type Actors List in Query to know available Actors.')
        else :
            print('Unrecogonised Query')
            

print("Recommendation System is Running. Enter Query. Refer 'README.txt' to know how to write query.")             
while(True):
    
    inp = input("Query - ")
    if inp.lower() == 'quit':
        break;
    else:
        getRecommendation(inp.lower())
        print('___________________________________________________________________','\n')
print('Thanks for using the Recommendation System.')
