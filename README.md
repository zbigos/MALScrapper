# MALScrapper
Qick and dirty python script for scraping character drawings from my anime list.

This script will download anime arts from MAL and place them into a catalog tree.

# Usage
  -d to download all arts from every single anime article on MAL
  -dra=<num> to download specified number of arts from different anime articles
  -drs=<num> to download all arts from specified number of different anime articles
  
  -b to store every picture in /pictures catalog, named pic<number>.jpeg
  -bm, same as b, but also creates a .json file with description for every picture (anime name, voice actor, etc.)
  -ss to store every picture in /pictures/<anime_name> catalog, named <anime_name>_<number>.jpeg
  -ssn to store every picture in /pictures/<anime_name> catalog, named <anime_name>_<character_name>.jpeg
