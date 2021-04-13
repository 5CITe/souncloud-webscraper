
#to edit browser in real time
from selenium import webdriver
#to parse requests
import requests
import bs4
import os

top_url="https://soundcloud.com/charts/top"
hot_url="https://soundcloud.com/charts/new"
song_search_url="https://soundcloud.com/search/sounds?q="
artist_search_url="https://soundcloud.com/search/people?q="

d1=webdriver.Chrome("C:/Users/archh/Downloads/chromedriver")
d1.get("https://soundcloud.com")
print (">>>>>>>>>>>>> MY SCRAPER <<<<<<<<<<<<<")
print ("Enter the number of the option you wish to choose: ")

while True:
  
  print("1. Top 50")
  print("2. New and Hot 50")
  print("3. search for a song")
  print("4. search for an artist")
  print("0. Exit")
  print()
  print("->",end=" ")
  choice=int(input())

  if choice == 0:
    d1.quit()
    break

  if choice == 3:
    name=input("Enter name of song: ").strip()
    "%20".join(name.split())
    d1.get(song_search_url+name)
    continue

  if choice == 4:
    name=input("Enter name of artist: ").strip()
    "%20".join(name.split())
    d1.get(artist_search_url+name)
    continue

  if choice == 1:
    req=requests.get(top_url)
    #print(req.text)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    genres=soup.select('a[href*="genre"]')[2:]
    genre_links=[]
    #print(genres)
    
    for count,genre in enumerate(genres):
      print(f"{count} : {genre.text}")
      genre_links.append(genre.get("href"))
    
    
    print()
    choice2=input("Enter which genre you would like to see: (x to go back) ")
  
    if choice2 =='x':
      continue
    else:
      choice2=int(choice2)
    
    url="http://soundcloud.com"+genre_links[choice2]
    req=requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    #print(request.text)
    tracks=soup.select('h2 a') 
      
    track_links=[]
    track_names=[]
  
    count=1
    index=1
    for track in tracks:
      if count%2!=0:
        track_links.append(track.get("href"))
        track_names.append(track.text)
        print(f"{index} : {track.text}")
        print()
        index=index+1
      count=count+1
    #print(track_links)
        # song selection loop
      
    while True:
      choice3 = input(">>> Your choice (x to re-select genre): ")
      print()

      if choice3 == 'x': 
        break
      else: 
        choice3 = int(choice3)-1

      print("Now playing: " + track_names[choice3])
      print(track_links[choice3])

      d1.get("http://soundcloud.com" + track_links[choice3])

  if choice == 2:
    req=requests.get(hot_url)
    print(req.text)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    tracks=soup.select('h2 a') 
      
    track_links=[]
    track_names=[]
  
    count=1
    index=1
    for track in tracks:
      if count%2!=0:
        track_links.append(track.get("href"))
        track_names.append(track.text)
        print(f"{index} : {track.text}")
        print()
        index=index+1
      count=count+1
    #print(track_links)
        # song selection loop
      
    while True:
      choice3 = input(">>> Your choice (x to re-select genre): ")
      print()

      if choice3 == 'x': 
        break
      else: 
        choice3 = int(choice3)-1

      print("Now playing: " + track_names[choice3])
      print(track_links[choice3])

      d1.get("http://soundcloud.com" + track_links[choice3])


  
    

print()
print("exited")

  