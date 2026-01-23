mkdir -p ./wczesniej_niz_4_mies
find ~ -type f -mtime +120 -exec cp {} ./wczesniej_niz_4_mies \;
